# yolov3-custom-pedestrian-detection

## PennFudanAugmentation
Reference: https://www.cis.upenn.edu/~jshi/ped_html/
The data set contains only 170 samples, so we argument the data set 
by scaling or cropping each image.
1)genImageBoxLabel
Convert the original annotation to yolov3 label format
2)splitImageDataset
Split images and labels file to train and test set.
3)testLabel
Rectangle image from yolov3 labels format to validate the labels data.
4)main
Main function to argument the image set by scaling and cropping method.

## trainPennFudan
Darknet config files for training.
