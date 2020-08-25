# import the libraries
import os
import face_recognition


def image_compare():
    # make a list of all the available images
    images = os.listdir('images')

    # load your image
    image_to_be_matched = face_recognition.load_image_file('photo.jpg')

    # encoded the loaded image into a feature vector
    image_to_be_matched_encoded = face_recognition.face_encodings(
        image_to_be_matched)[0]

    # iterate over each image
    try:
        for image in images:
            # load the image
            current_image = face_recognition.load_image_file("images/" + image)
            # encode the loaded image into a feature vector
            current_image_encoded = face_recognition.face_encodings(current_image)[0]
            # match your image with the image and check if it matches
            result = face_recognition.compare_faces(
                [image_to_be_matched_encoded], current_image_encoded)
            # check if it was a match
            if result[0] == True:
                return True
    except:
        return False
