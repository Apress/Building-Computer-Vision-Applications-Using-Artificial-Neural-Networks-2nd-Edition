#Code block 1: Listing_6_27
!pip install onnx-tf tensorflow-probability

#Code block 2: Listing_6_28
%%shell
onnx-tf convert \
-i /content/drive/MyDrive/PPE/yolov7/runs/train/yolov7-ppe3/weights/best.onnx \
-o yolov7-tf

#Code block 3: Listing_6_29
import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model('/content/yolov7-tf/')
tflite_model = converter.convert()

with open('/content/tflite/yolov7-tiny.tflite', 'wb') as f:
  f.write(tflite_model)
