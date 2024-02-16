import tensorflow as tf, numpy as np, pandas as pd
import matplotlib.pyplot as plt
# Load MNIST data using built-in datasets download function
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data(path="/content/data/mnist.npz")

#Noramalize the pixel values by deviding each pixel by 255
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the 4-layer neural network (MLP)
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(60, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model and set optimizer,loss function and metrics
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Finally, train or fit the model
trained_model = model.fit(x_train, y_train, validation_split=0.3, epochs=100)

# Visualize loss  and accuracy history
plt.plot(trained_model.history['loss'], 'r--')
plt.plot(trained_model.history['accuracy'], 'b-')
plt.legend(['Training Loss', 'Training Accuracy'])
plt.xlabel('Epoch')
plt.ylabel('Percent')
plt.show();

# Evaluate the result using the test set.\
evalResult = model.evaluate(x_test,  y_test, verbose=1)
print("Evaluation", evalResult)
predicted = model.predict(x_test)
predicted_df = pd.DataFrame(predicted)
print("Probabilities of all classes predicted from the model:")
print(predicted_df)
print("Predicted class based on the highest probability:")
predicted_df.idxmax(axis=1)

print("===Confusion Matrix==")
confusion = tf.math.confusion_matrix(y_test, np.argmax(predicted, axis=1), num_classes=10)
tf.print(confusion)
tensor_values = confusion.numpy()
confusion_df = pd.DataFrame(tensor_values)
print(confusion_df)
