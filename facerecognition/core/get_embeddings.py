def get_embeddings(className, img, roll):
    import joblib
    import numpy as np
    import insightface
    # import mxnet as mx
    from insightface.app import FaceAnalysis
    import cv2
    from django.conf import settings
    import os

    directory = os.path.join(settings.BASE_DIR, 'static','classes.pkl')
    try:
        if os.path.exists(directory) and os.path.getsize(directory) > 0:
            _classes = joblib.load(directory)
        else:
            _classes = {}
            _classes[className] = [[],[]]
    except Exception as e:
        print(f"Error loading/pickling classes: {e}")
    embeddings = _classes[className][0]
    labels = _classes[className][1]

    def get_padding(image):
        original_image = cv2.resize(image, (50,50))
        padding = 120
        height, width, channels = original_image.shape
        new_height = height + 2 * padding
        new_width = width + 2 * padding
        padded_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)
        padded_image[padding:padding+height, padding:padding+width, :] = original_image
        return padded_image
    
    padded_face = get_padding(img)

    model = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    model.prepare(ctx_id=0, det_size=(640,640))
    face = model.get(padded_face)

    embeddings.append(face[0].embedding)
    labels.append(roll)

    _classes[className][0] = embeddings
    _classes[className][1] = labels
    print(embeddings,labels)
    joblib.dump(_classes, directory)

