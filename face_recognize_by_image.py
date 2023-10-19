import os
import face_recognition


def encoding_image(foldername, filename) :
    try:

        # Pastikan file yang dibaca adalah image file
        if not filename.endswith((".jpg", ".png", ".jpeg")):
            raise Exception("file is not an image file")

        image_path = os.path.join(foldername, filename)
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)

        # Pastikan hanya ada satu wajah dalam gambar
        if len(face_locations) != 1:
            raise Exception("image must be contains exatcly one face")
        
        face_encoding = face_recognition.face_encodings(image, face_locations)[0]
        return face_encoding
    
    except Exception as e:
        return e

def get_faces_encode(image_folder):
    try:
        faces = []

        for filename in os.listdir(image_folder):
    
            face_encoding = encoding_image(image_folder, filename)
            faces.append(face_encoding)
        
        return faces
    
    except Exception as e:
        return e

def compare_face(faces_encode, image_folder):
    try:

        image_file = ""
        for filename in os.listdir(image_folder):
            image_file = filename
        
        if image_file == "" :
            raise Exception("image file is not found")
        
        face_encoding = encoding_image(image_folder, image_file)
        matches = face_recognition.compare_faces(faces_encode, face_encoding)
        accuracy = sum(matches) / len(matches)

        is_matching = False
        if accuracy > 0.8 :
            is_matching = True

        response = {"is_matching" : is_matching, "accuracy" : accuracy}

        return response
    
    except Exception as e:
        return e

