%%shell
export PYTHONPATH=$PYTHONPATH:/content/models/research
export PYTHONPATH=$PYTHONPATH:/content/models/research/slim
cd /content/models/research
PIPELINE_CONFIG_PATH=/content/computer_vision/pre-trained-model/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/pipeline.config
MODEL_DIR=/content/computer_vision/surface_defect_detection_model/
NUM_TRAIN_STEPS=100000
SAMPLE_1_OF_N_EVAL_EXAMPLES=1
python object_detection/model_main_tf2.py \
--pipeline_config_path=${PIPELINE_CONFIG_PATH} \
--model_dir=${MODEL_DIR} \
--num_train_steps=${NUM_TRAIN_STEPS} \
--sample_1_of_n_eval_examples=${SAMPLE_1_OF_N_EVAL_EXAMPLES} \
--alsologtostderr
