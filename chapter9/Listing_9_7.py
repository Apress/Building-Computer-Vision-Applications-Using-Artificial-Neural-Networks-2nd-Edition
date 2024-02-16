%%shell
python /content/models/research/object_detection/model_main_tf2.py \
--model_dir=/content/computer_vision/surface_defect_detection_model \
--pipeline_config_path=/content/computer_vision/pre-trained-model/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/pipeline.config \
--checkpoint_dir=/content/computer_vision/ surface_defect_detection_model
