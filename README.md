# yolov3-custom-pedestrian-detection

## PennFudanAugmentation
Darknet yolo: https://pjreddie.com/darknet/yolo/
<br/>
Dataset: https://www.cis.upenn.edu/~jshi/ped_html/ 
<br/>
The data set contains only 170 samples, so we argument the data set 
by scaling or cropping each image.
<br/>
1)genImageBoxLabel<br/>
Convert the original annotation to yolov3 label format.
<br/>
2)splitImageDataset<br/>
Split images and labels file to train and test set.
<br/>
3)testLabel<br/>
Rectangle image from yolov3 labels format to validate the labels data.
<br/>
4)main<br/>
Main function to argument the image set by scaling and cropping method.

## trainPennFudan
Darknet config files for training.
