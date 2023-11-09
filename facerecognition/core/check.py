import os

def get_list(path):
    list = os.listdir(path)
    return(list)

# print(os.walk('facerecognition/static/images/220001065'))
# print(os.scandir('facerecognition/static/images/220001065'))