# Yolov3-custom-pedestrian-detection [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) ![Python Version](https://img.shields.io/badge/python-v3.6-blue)

## 📝 Table of Contents
- [PennFudanAugmentation](#PennFudanAugmentation)
- [trainPennFudan](#trainPennFudan)
- [DetectionEffect](#DetectionEffect)


## PennFudanAugmentation
Darknet yolo: https://pjreddie.com/darknet/yolo/
<br/>
Dataset: https://www.cis.upenn.edu/~jshi/ped_html/ 
<br/>
The data set contains only 170 samples, so we argument the data set 
by scaling or cropping each image.
<br/>
1)genImageBoxLabel: Convert the original annotation to yolov3 label format.
<br/>
2)splitImageDataset: Split images and labels file to train and test set.
<br/>
3)testLabel: Rectangle image from yolov3 labels format to validate the labels data.
<br/>
4)main: Main function to argument the image set by scaling and cropping method.

<br/>
Dataset description before augmentation(170 sample images).
<br/>
<img src="res/dataset.png" width="320" height="240">
<br/>
Dataset description after augmentation(5270 sample images).
<br/>
<img src="res/datasetAug.png" width="320" height="240">

## trainPennFudan
Darknet config files for training.

## DetectionEffect 
<br/>
<img src="res/pd.png" width="320" height="240">
<img src="res/pd_detect.png" width="320" height="240">
<img src="res/pd2.png" width="320" height="240">
<img src="res/pd2_detect.png" width="320" height="240">

