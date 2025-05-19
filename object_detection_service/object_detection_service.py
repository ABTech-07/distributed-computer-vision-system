from flask import Flask, jsonify, request
import cv2
import numpy as np

app = Flask(__name__)

# Load the pre-trained Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

@app.route('/detect_faces', methods=['POST'])
def detect_faces():
    try:
        # Get the image from the request
        file = request.files['image']
        
        # Check if the file is empty
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        # Read the image and check if it was read correctly
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            return jsonify({'error': 'Failed to load image'}), 400

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Create a response
        response = {'faces': []}
        for (x, y, w, h) in faces:
            # Convert np.int32 to int before adding to response
            response['faces'].append({
                'x': int(x), 
                'y': int(y), 
                'width': int(w), 
                'height': int(h)
            })

        return jsonify(response)
    
    except Exception as e:
        # Return a 500 error with the exception details
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
