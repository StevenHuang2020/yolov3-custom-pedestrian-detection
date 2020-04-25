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

## trainPennFudan
Darknet config files for training.

## Detection effect 
<br/>
<img src="res/pd.png" width="320" height="240">
<img src="res/pd_detect.png" width="320" height="240">
<img src="res/pd2.png" width="320" height="240">
<img src="res/pd2_detect.png" width="320" height="240">
