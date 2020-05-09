#python3 steven
import cv2
import argparse
import numpy as np
import os

#----------------------------------------------
#usgae: python .\yolo_opencvPath.py -c ./darknet-master/trainPennFudan/PF_yolov3-tiny.cfg --weights ./darknet-master/trainPennFudan/backupTiny/PF_yolov3-tiny_60000.weights --classes ./darknet-master/trainPennFudan/images/PennFudan.names -s ./darknet-master/video -d .\darknet-master\video\yolo
#----------------------------------------------
from yolo_opencv import detectionImg

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
                
def createPath(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        
def getFileName(path):  
    return os.path.basename(path)
    
def cmd_line():
    # handle command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-c', '--config', required=True, help = 'path to yolo config file')
    ap.add_argument('-w', '--weights', required=True, help = 'path to yolo pre-trained weights')
    ap.add_argument('-cl', '--classes', required=True, help = 'path to text file containing class names')
    ap.add_argument('-s', '--src', required=True, help = 'path to input image')
    ap.add_argument('-d', '--dst', required=True, help = 'path to save image')
    return ap.parse_args()

def main():
    args = cmd_line()
    src = args.src
    dst = args.dst
    
    classes = None
    with open(args.classes, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    #colors = np.random.uniform(0, 255, size=(len(classes), 3))
    colors = [200,0,0]

    net = cv2.dnn.readNet(args.weights, args.config)
    
    createPath(dst)
    print(src,dst)
    for i in pathsFiles(src,'png'): #png
        fileName = getFileName(i)
        #image = detectionImg(cv2.imread(i),net,classes,colors)
        dstFile = args.dst + '\\' + fileName
        print(i,fileName,dstFile)
        cv2.imwrite(dstFile, detectionImg(cv2.imread(i),net,classes,colors))

if __name__ == '__main__':
    main()
