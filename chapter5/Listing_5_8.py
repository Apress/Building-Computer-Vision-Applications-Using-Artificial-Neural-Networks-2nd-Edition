import numpy as np, pandas as pd
import tensorflow as tf
import os

model_path = "/content/models/pneumiacnn"
input_dir = "/content/chest_xray/val"
classes = ["NORMAL", "PNEUMONIA"]
image_dimensions = [1024, 1024]
# Load the trained model, including its weights and the optimizer
model = tf.saved_model.load(model_path)

# Predict the class of the input image from the loaded model
for file in os.listdir(input_dir):
  image_dir = os.path.join(input_dir, file)
  if os.path.isdir(image_dir):
    for img in os.listdir(image_dir):
      image_path = os.path.join(image_dir, img)
      image = tf.io.read_file(image_path)
      image = tf.io.decode_image(image, channels=3)
      image = tf.image.resize(image, image_dimensions)
      image = image / 255.0  # Normalize pixel values between 0 and 1
      image = tf.expand_dims(image, axis=0)  # Add batch dimension
      predicted = model(image)
      max_probability = np.max(predicted)
      max_index = np.argmax(predicted)
      print("Image:", image_path, " Predicted", classes[max_index], " Actual:", file, " Probability: ", max_probability)
