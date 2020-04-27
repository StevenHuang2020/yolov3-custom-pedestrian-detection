# Yolov3-custom-pedestrian-detection

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

## Detection effect 
<br/>
<img src="res/pd.png" width="320" height="240">
<img src="res/pd_detect.png" width="320" height="240">
<img src="res/pd2.png" width="320" height="240">
<img src="res/pd2_detect.png" width="320" height="240">

![Last update](https://img.shields.io/endpoint?color=blue&style=flat-square&url=https%3A%2F%2Fraw.githubusercontent.com%2Falext234%2Fcoronavirus-stats%2Fmaster%2Fdata%2Flast_update.json)


![GitHub watchers](https://img.shields.io/github/downloads/StevenHuang2020/WebSpider/total)
![GitHub watchers](https://img.shields.io/github/watchers/StevenHuang2020/WebSpider?label=Watch)
![GitHub stars](https://img.shields.io/github/stars/StevenHuang2020/WebSpider?style=social)
