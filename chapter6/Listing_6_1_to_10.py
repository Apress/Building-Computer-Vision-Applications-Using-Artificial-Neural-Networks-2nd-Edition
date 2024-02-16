#Code block 1: Listing_6_1
!pip install numpy==1.23
!pip install pillow==9.5
!apt install -y protobuf-compiler

#Code block 2: Listing_6_2
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

#Code block 3: Listing_6_3

%%shell
cd models/research/
python object_detection/builders/model_builder_tf2_test.py

#Code block 4: Listing_6_4
%%shell
mkdir -p computer_vision/petdata
cd computer_vision/petdata
wget http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
wget http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz
tar -xvf annotations.tar.gz
tar -xvf images.tar.gz

#Code block 5: Listing_6_5
%%shell
mkdir -p /content/computer_vision/petdata/tfrecords
cd /content/models/research
python object_detection/dataset_tools/create_pet_tf_record.py \
--label_map_path=object_detection/data/pet_label_map.pbtxt \
--data_dir=/content/computer_vision/petdata \
--output_dir=/content/computer_vision/petdata/tfrecords


#Code block 6: Listing_6_6
%%shell
cd computer_vision
mkdir pre-trained-model
cd pre-trained-model
wget http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz
tar -xvf ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz

#Code block 7: Listing_6_7
%%shell
export PYTHONPATH=$PYTHONPATH:/content/models/research
export PYTHONPATH=$PYTHONPATH:/content/models/research/slim
cd /content/models/research
PIPELINE_CONFIG_PATH=/content/computer_vision/pre-trained-model/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/pipeline.config
MODEL_DIR=/content/computer_vision/pet_detection_model/
NUM_TRAIN_STEPS=100
SAMPLE_1_OF_N_EVAL_EXAMPLES=1
python object_detection/model_main_tf2.py \
--pipeline_config_path=${PIPELINE_CONFIG_PATH} \
--model_dir=${MODEL_DIR} \
--num_train_steps=${NUM_TRAIN_STEPS} \
--sample_1_of_n_eval_examples=${SAMPLE_1_OF_N_EVAL_EXAMPLES} \
--alsologtostderr

#Code block 8: Listing_6_8
%%shell
python /content/models/research/object_detection/model_main_tf2.py \
--model_dir=/content/computer_vision/pet_detection_model \
--pipeline_config_path=/content/computer_vision/pre-trained-model/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/pipeline.config \
--checkpoint_dir=/content/computer_vision/pet_detection_model

#Code block 9: Listing_6_9
%load_ext tensorboard
%tensorboard --logdir /content/computer_vision/pet_detection_model

#Code block 10: Listing_6_10
%%shell
export PYTHONPATH=$PYTHONPATH:/content/models/research
export PYTHONPATH=$PYTHONPATH:/content/models/research/slim
cd /content/models/research
python /content/models/research/object_detection/exporter_main_v2.py --input_type image_tensor --pipeline_config_path /content/computer_vision/pre-trained-model/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/pipeline.config --trained_checkpoint_dir /content/computer_vision/pet_detection_model --output_directory /content/computer_vision/pet_detection_model/final_model
