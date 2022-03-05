import os
import face_recognition

os.system('cls')

# Load the jpg files into numpy arrays

img1 = face_recognition.load_image_file("assets/images/img8.jpg")
img2 = face_recognition.load_image_file("assets/images/img9.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
img1_face_encoding = face_recognition.face_encodings(img1)[0]
img2_face_encoding = face_recognition.face_encodings(img2)[0]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces([img1_face_encoding], img2_face_encoding)

print(results)