from flask import Flask, jsonify, request
import face_recognize_by_image
import numpy as np
import json

app = Flask(__name__)

@app.route('/faces/encode', methods=["POST"])
def get_faces():
    try:
        request_body = request.get_json()
        image_folder = request_body.get("image_folder")
        faces = face_recognize_by_image.get_faces_encode(image_folder)
        return jsonify({"face_encode": encode_faces_to_string(faces)})
    except Exception as e:
        return jsonify({"error": str(e)}),500


@app.route('/faces/compare', methods=["POST"])
def compare_faces():
    try:
        request_body = request.get_json()
        face_encode = request_body.get("face_encode")
        image_folder = request_body.get("image_folder")
        respon = face_recognize_by_image.compare_face(decode_faces_from_string(face_encode), image_folder)
        return jsonify({"data": respon})
    except Exception as e:
        return jsonify({"error": str(e)}),500



# Fungsi untuk mengonversi faces ke dalam format string
def encode_faces_to_string(faces):
    faces_as_list = [face.tolist() for face in faces]
    faces_as_json = json.dumps(faces_as_list)
    return faces_as_json

# Fungsi untuk mengembalikan faces dari format string
def decode_faces_from_string(encoded_faces):
    faces_as_list = json.loads(encoded_faces)
    faces = [np.array(face) for face in faces_as_list]
    return faces
