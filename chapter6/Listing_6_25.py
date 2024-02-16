%%shell
cd /content/drive/MyDrive/PPE/yolov7
python detect.py \
--project /content/detection \
--weights /content/drive/MyDrive/PPE/yolov7/runs/train/yolov7-ppe3/weights/best.pt \
--conf 0.25 \
--img-size 640 \
--source /content/construction-site.mp4
