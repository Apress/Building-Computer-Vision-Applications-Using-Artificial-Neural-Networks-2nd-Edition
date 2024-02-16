%%shell
export PYTHONPATH=$PYTHONPATH:/content/models/research
export PYTHONPATH=$PYTHONPATH:/content/models/research/slim
cd /content/models/research
python /content/models/research/object_detection/exporter_main_v2.py --input_type image_tensor --pipeline_config_path /content/computer_vision/pre-trained-model/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/pipeline.config --trained_checkpoint_dir /content/computer_vision/surface_defect_detection_model --output_directory /content/computer_vision/surface_defect_detection_model/final_model
