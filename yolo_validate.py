#python3 steven

#----------------------------------------------
#usgae: python yolo_opencv.py -i dog.jpg -c yolov3.cfg --weights ./yolov3.weights  -cl yolov3.txt
#----------------------------------------------
import os
import cv2
import argparse
import numpy as np
from yolo_opencv import detectionImg
from mainImagePlot import plotImagList

def cmd_line():
    # handle command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required=True,
                    help = 'path to input image')
    ap.add_argument('-c', '--config', required=True,
                    help = 'path to yolo config file')
    ap.add_argument('-w', '--weights', required=False,
                    help = 'path to yolo pre-trained weights')
    ap.add_argument('-cl', '--classes', required=False,
                    help = 'path to text file containing class names')
    return ap.parse_args()

def pathsFiles(dir,filter=''): #"cpp h txt jpg"
    def getExtFile(file):
        return file[file.find('.')+1:]
    def getFmtFile(path):
        #/home/User/Desktop/file.txt    /home/User/Desktop/file     .txt
        root_ext = os.path.splitext(path) 
        return root_ext[1]

    fmts = filter.split()    
    if fmts:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                if getExtFile(getFmtFile(filename)) in fmts:
                    yield dirpath+'\\'+filename
    else:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                yield dirpath+'\\'+filename
  
def changeBgr2Rbg(img): #input color img
    b,g,r = cv2.split(img)       # get b,g,r
    img = cv2.merge([r,g,b])
    return img

def main():
    args = cmd_line()
    #image = cv2.imread(args.image)
    #net = cv2.dnn.readNet(args.weights, args.config)
    #colors = np.random.uniform(0, 255, size=(len(classes), 3))
    colors = [200,0,0]
    classes = ['pedestrain']
    
    #img = r'./res/3.jpg'
    #weightsPath = r'./darknet-master/trainPennFudanEx'
    weightsPath = r'./darknet-master/trainPennFudan/backupTiny'
    config =  r'./darknet-master/trainPennFudan/PF_yolov3-tiny.cfg'
    
    weightFiles = []
    # for i in pathsFiles(weightsPath,'weights'):
    #     print(i)
    #     weightFiles.append(i)
    weightFiles.append(weightsPath + '/' + 'PF_yolov3-tiny_500.weights')
    weightFiles.append(weightsPath + '/' + 'PF_yolov3-tiny_900.weights')
    weightFiles.append(weightsPath + '/' + 'PF_yolov3-tiny_10000.weights')
    weightFiles.append(weightsPath + '/' + 'PF_yolov3-tiny_20000.weights')
    
        
    image = changeBgr2Rbg(cv2.imread(args.image))
    
    imgList=[]
    nameList=[]
    for i in range(4):
        weights = weightFiles[i]
        net = cv2.dnn.readNet(weights, config)
        detectImg = detectionImg(image.copy(),net,classes,colors)
       
        imgList.append(detectImg)
        nameList.append(weights[weights.rfind('/')+1 : ])
    
    plotImagList(imgList,nameList)
    
if __name__ == '__main__':
    main()
