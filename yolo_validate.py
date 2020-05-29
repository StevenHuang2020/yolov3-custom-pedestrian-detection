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
    ap.add_argument('-c', '--config', required=False,
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

def compareWithDifferWeights(weightsPath,config,images,classes,colors):
    weightFiles = []
    weightFiles.append(weightsPath + '/' + 'PF_yolov3-tiny_500.weights')
    weightFiles.append(weightsPath + '/' + 'PF_yolov3-tiny_10000.weights')
    #weightFiles.append(weightsPath + '/' + 'PF_yolov3-tiny_20000.weights')
    weightFiles.append(weightsPath + '/' + 'PF_yolov3-tiny_30000.weights')
    weightFiles.append(weightsPath + '/' + 'PF_yolov3-tiny_170000.weights')
    
    imgList=[]
    nameList=[]
    for image in images:
        for i in range(4):
            weights = weightFiles[i]
            net = cv2.dnn.readNet(weights, config)
            detectImg = detectionImg(image.copy(),net,classes,colors)
        
            imgList.append(detectImg)
            
            name = weights[weights.rfind('_')+1 : weights.rfind('.')]
            nameList.append('epoch='+name)  #weights[weights.rfind('/')+1 : ]
    plotImagList(imgList,nameList,showticks=False)
   
def compareWithDifferImages(weights,config,images,classes,colors):
    imgList=[]
    nameList=[]
    for image in images:
        net = cv2.dnn.readNet(weights, config)
        detectImg = detectionImg(image.copy(),net,classes,colors)
    
        imgList.append(changeBgr2Rbg(detectImg))
        
        name = weights[weights.rfind('_')+1 : weights.rfind('.')]
        #nameList.append('epoch='+name)  #weights[weights.rfind('/')+1 : ]
        nameList.append('')
    plotImagList(imgList,nameList,showticks=False)
    
def compare2(config,classes,colors):
    #weights = weightsPath + '/' + 'PF_yolov3-tiny.backup'
    #weights = weightsPath + '/' + 'PF_yolov3-tiny_170000.weights'
    #weights = r'./darknet-master/trainPennFudanEx2/' + 'PF_yolov3-tiny_170000.weights'
    weights = 'PF_yolov3-tiny_Final.weights'
    images=[]
    # images.append(cv2.imread('2.jpg'))
    # images.append(cv2.imread('3.jpg'))
    # images.append(cv2.imread('7.jpg'))
    # images.append(cv2.imread('4.jpg'))
    
    images.append(cv2.imread('pd7.png'))
    images.append(cv2.imread('pd4.png'))
    images.append(cv2.imread('pd5.png'))
    images.append(cv2.imread('pd6.png'))
    
    compareWithDifferImages(weights,config,images,classes,colors)
    
def compare1(config,classes,colors):
    #image = changeBgr2Rbg(cv2.imread(args.image))
    #weightsPath = r'./darknet-master/trainPennFudanEx'
    weightsPath = r'../darknet-master/trainPennFudan/backupTiny'
    images=[]
    images.append(changeBgr2Rbg(cv2.imread('pd.png')))
    images.append(changeBgr2Rbg(cv2.imread('pd2.png')))
    compareWithDifferWeights(weightsPath,config,images,classes,colors)
    
def compare3(config,classes,colors):
    images=[]
    #images.append(cv2.imread('2.jpg'))
    images.append(cv2.imread('3.jpg'))
    images.append(cv2.imread('7.jpg'))
    
    weights1 = r'PF_yolov3-tiny_Final.weights'
    weightsEx = 'PF_yolov3-tiny_150000.weights'#r'PF_yolov3-tiny_FinalEx.weights'
    imgList=[]
    nameList=[]
    
    net = cv2.dnn.readNet(weights1, config)
    netEx = cv2.dnn.readNet(weightsEx, config)
    for image in images:        
        detectImg = detectionImg(image.copy(),net,classes,colors)
        imgList.append(changeBgr2Rbg(detectImg))
        
        #name = weights[weights.rfind('_')+1 : weights.rfind('.')]
        #nameList.append('epoch='+name)  #weights[weights.rfind('/')+1 : ]
        nameList.append('')
        
        detectImg = detectionImg(image.copy(),netEx,classes,colors)
        imgList.append(changeBgr2Rbg(detectImg))
        nameList.append('')
        
        
    plotImagList(imgList,nameList,showticks=False)
    
def main():
    args = cmd_line()
    #image = cv2.imread(args.image)
    #net = cv2.dnn.readNet(args.weights, args.config)
    #colors = np.random.uniform(0, 255, size=(len(classes), 3))
    colors = [200,0,0]
    classes = ['pedestrain']    
    config =  r'PF_yolov3-tiny.cfg'
    
    #compare1(config,classes,colors)
    #compare2(config,classes,colors)
    compare3(config,classes,colors)
    
if __name__ == '__main__':
    main()
