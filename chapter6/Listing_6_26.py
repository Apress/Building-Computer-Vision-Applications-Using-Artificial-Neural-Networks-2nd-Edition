%%shell
cd /content/drive/MyDrive/PPE/yolov7
python export.py \
--weights /content/drive/MyDrive/PPE/yolov7/runs/train/yolov7-ppe3/weights/best.pt \
--grid --end2end --simplify \
--topk-all 100 --iou-thres 0.65 \
--conf-thres 0.35 \
--img-size 640 640 --max-wh 640
