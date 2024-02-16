#Code block 1: Listing_6_19
!unzip '/content/drive/MyDrive/PPE/ppe.zip'

#Code block 2: Listing_6_20
!git clone https://github.com/WongKinYiu/yolov7.git /content/drive/MyDrive/PPE/yolov7

#Code block 3: Listing_6_21
%%shell
cd /content/drive/MyDrive/PPE/yolov7
python train.py \
--epochs 10  \
--workers 8 \
--device 0 \
--batch-size 16 \
--data /content/safety-Helmet-Reflective-Jacket/data.yaml \
--img 640 640 \
--cfg cfg/training/yolov7.yaml \
--weights '' \
--name yolov7-ppe \
--hyp data/hyp.scratch.p5.yaml

#Code block 4: Listing_6_22
%%shell
cd /content/drive/MyDrive/PPE/yolov7
python \
-m torch.distributed.launch \
--nproc_per_node 4 \
--master_port 9527 \
train.py \
--epochs 100  \
--workers 8 \
--device 0,1,23 \
--sync-bn \
--batch-size 16 \
--data /content/safety-Helmet-Reflective-Jacket/data.yaml \
--img 640 640 \
--cfg cfg/training/yolov7.yaml \
--weights '' \
--name yolov7-ppe \
--hyp data/hyp.scratch.p5.yaml

#Code block 5: Listing_6_23
%load_ext tensorboard
%tensorboard --logdir /content/drive/MyDrive/PPE/yolov7/runs/train
