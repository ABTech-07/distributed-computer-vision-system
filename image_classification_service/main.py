from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image
import io

app = FastAPI()

# Example route for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the Image Classification Service!"}

# Route for image classification
@app.post("/predict/")
async def predict_image(file: bytes):
    # Load model (adjust the model path based on your setup)
    model = tf.keras.applications.MobileNetV2(weights='imagenet')

    # Convert the image bytes into a format that can be used for prediction
    image = Image.open(io.BytesIO(file))
    image = image.resize((224, 224))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    
    # Preprocess the image for MobileNetV2
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

    # Get prediction
    predictions = model.predict(image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]

    # Return the predictions
    return {"predictions": [{"label": label, "score": score} for (_, label, score) in decoded_predictions]}
