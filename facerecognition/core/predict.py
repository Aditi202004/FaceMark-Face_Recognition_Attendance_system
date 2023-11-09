def predict(img_list, className):
    import joblib
    import numpy as np
    import insightface
    # import mxnet as mx
    from insightface.app import FaceAnalysis
    import cv2
    from django.conf import settings
    import os
    from sklearn.metrics.pairwise import cosine_similarity

    directory = os.path.join(settings.BASE_DIR, 'static','classes.pkl')
    try:
        if os.path.exists(directory) and os.path.getsize(directory) > 0:
            _classes = joblib.load(directory)
        else:
            _classes = {}
            _classes[className] = [[],[]]
    except Exception as e:
        print(f"Error loading/pickling classes: {e}")
    train_embeddings = _classes[className][0]
    labels = _classes[className][1]

    model = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    model.prepare(ctx_id=0, det_size=(640,640))
    final_idx = set()
    for img in img_list:
        faces = model.get(img)
        test_embeddings = []
        for face in faces: 
            test_embeddings.append(face.embedding)
        for i, student in enumerate(test_embeddings):
            max = -99999999999999999999999999999999999999
            idx_pro = 0
            for idx, face in enumerate(train_embeddings):
                # Assuming you have two sets of embeddings (embedding1 and embedding2)
                embedding1 = np.array(student)  # Replace with your actual embeddings
                embedding2 = np.array(face)  # Replace with your actual embeddings

                # Reshape the embeddings to be 2D arrays with a single row
                embedding1 = embedding1.reshape(1, -1)
                embedding2 = embedding2.reshape(1, -1)

                # Calculate the cosine similarity between the two embeddings
                cosine_sim = cosine_similarity(embedding1, embedding2)
                if cosine_sim > max:
                    max = cosine_sim
                    idx_pro = idx
            final_idx.add(idx_pro)

    roll = []
    for idx in final_idx:
        roll.append(labels[idx])

    return roll