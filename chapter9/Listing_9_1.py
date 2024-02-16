# Code block 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Code block 2: uncompress NEU data
 %%shell
ls /content/drive/'My Drive'/NEU-DET.zip
unzip /content/drive/'My Drive'/NEU-DET.zip

!pip install numpy==1.23
!apt install -y protobuf-compiler
!pip install pillow==9.5

%%shell
git clone --depth 1 https://github.com/tensorflow/models.git
cd models/research/
protoc object_detection/protos/*.proto --python_out=.
cd /content
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make
cp -r pycocotools /content/models/research
cd
cd /content/models/research/
cp object_detection/packages/tf2/setup.py .
python -m pip install .
