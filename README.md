# FaceMark: Face Recognition-Based Attendance System

## Introduction

FaceMark simplifies classroom attendance management using facial recognition. Designed to enhance efficiency, it offers features such as real-time attendance capture and straightforward photo uploads.

## Team Members
- Misha Jain
- Aditi Wekhande
- Sai Sanjana Reddy Algubelly

## Procedure

Our approach involves:
1. **Dataset Formatting:**
    - Photos labeled with the last four digits of roll numbers.
    - Transformed into rectangles, resized, and computed facial embeddings.

2. **Training Model:**
    - Facial recognition model trained on a diverse dataset, creating "train_embeddings" for identification.

3. **Real-time Attendance Capture:**
    - Group photos captured during class.
    - Faces identified, resized uniformly, and embeddings extracted.

4. **Recognition Process:**
    - Detected faces compared with "train_embeddings" using cosine similarity, resulting in associated roll numbers.

## Code Explanation

 ### get_embeddings
  - Obtains facial embeddings for a class, image, and roll number.
  - Utilizes the InsightFace library for deep learning facial analysis.
 
 ### predict
  - Predicts roll numbers for students in a list of images for a specified class.
  - Utilizes pre-trained embeddings and cosine similarity for facial recognition.
 
## How to Run the Code
  
 #### 1. Clone the repository:
  - git clone https://github.com/Aditi202004/FaceMark-Face_Recognition_Attendance_system.git
  - cd FaceMark-Face_Recognition_Attendance_system

 #### 2. Install dependencies:
  - pip install -r requirements.txt

 #### 2. Change your Current Directory:
  - cd facerecognition

 #### 3. Run the code:
  - python manage.py runserver

   
## Metrics

Achieved an accuracy rate of ~98-99% in predicting roll numbers.

## Acknowledgments

 - We are grateful to the [InsightFace Library](https://github.com/deepinsight/insightface) for providing essential functionalities for facial analysis.

## Documentation
For more detailed information and documentation, please visit [our documentation site](https://drive.google.com/file/d/1jNqSTrCi3ptIsSJYmodz61FPyA6tJzWB/view?usp=sharing).
 
## Project Structure

The project is organized as follows:

 - `/src`: contains the source code files.
 - `/static`: Includes CSS, JS, and images for the project's user interface.
