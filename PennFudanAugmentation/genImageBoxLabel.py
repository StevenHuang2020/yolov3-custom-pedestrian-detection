#python3 steve
#10/04/2020 Penn-Fudan dataset generate box label from raw label

#yolo annotation fmt
#<object-class> <xCenter> <yCenter> <width> <height>
#<object-class> <(Xmin+Xmax)*0.5/width> <(Ymin+Ymax)*0.5/height> <(Xmax-Xmin)/width> <(Ymax-Ymin)/height>
#1 0.716797 0.395833 0.216406 0.147222
#0 0.687109 0.379167 0.255469 0.158333
#1 0.420312 0.395833 0.140625 0.166667

import sys
import re
import cv2
from modules.folder.folder_file import pathsFiles,createPath,getFileName,getFmtFile
from modules.folder.folder_file import deleteFile,deleteFolder

def listFile(path,fmt=''):
	for i in pathsFiles(path,fmt):
		yield i 

def parseCoordinate(line):
    #(160, 182) - (302, 431)
    pattern = re.compile(r'\d+')   #search numbers
    res = pattern.findall(line)
    #print('res=', res)
    res = list(map(int, res))
    #print('resC=', res)
    return res

def writeToDst(file,content):
    with open(file,'a',newline='\n') as dstF:
        dstF.write(content)
        
def getFileCoordinates(fileAnnot):
    coordinates = []
    with open(fileAnnot,'r') as srcF:
        for i in srcF.readlines():
            if i.find("Bounding box for object") == 0:
                i = i[i.find(':')+1:-1]
                Xmin,Ymin,Xmax,Ymax = parseCoordinate(i)
                coordinates.append((Xmin,Ymin,Xmax,Ymax))
    return coordinates
       
def loadImg(file,mode=cv2.IMREAD_COLOR):
    #mode = cv2.IMREAD_COLOR cv2.IMREAD_GRAYSCALE cv2.IMREAD_UNCHANGED
    return cv2.imread(file,mode)

def getImgHW(img):
    return img.shape[0],img.shape[1]

def getImgAnnotFile(annotPath,file):
    fAnnot = getFileName(file)
    return annotPath + '\\'+ fAnnot[:fAnnot.rfind('.')]+'.txt'
        
def writeToAnnotFile(H,W,file,coordinates):
    for i in coordinates:
            #print(i,'H,W=',H,W)
            Xmin,Ymin,Xmax,Ymax = i
            x,y,w,h = (Xmin+Xmax)/2, (Ymin+Ymax)/2, Xmax-Xmin, Ymax-Ymin
            dstLine = '0 '+ str(x/W) + ' ' + str(y/H) + ' ' + str(w/W) + ' ' + str(h/H)
            writeToDst(file,dstLine + '\n') 
            
def writeCordToAnnotFile(file,coordinates):
    for i in coordinates:
            #print(i)
            Xmin,Ymin,Xmax,Ymax = i
            dstLine = '0 '+ str(Xmin) + ' ' + str(Ymin) + ' ' + str(Xmax) + ' ' + str(Ymax)
            writeToDst(file,dstLine + '\n') 
           
def generateImageLabel(imgPath,annotPath,dst):
    deleteFolder(dst)
    createPath(dst)
    for i in listFile(imgPath,'png'):
        H,W = getImgHW(loadImg(i))
        #print(H,W)
        fAnnot = getImgAnnotFile(annotPath,i)
        fAnnotName = getFileName(fAnnot)
        dstFile = dst+ '\\' +  fAnnotName
        print('fAnnot=', fAnnot)
        #print('dstFile=', dstFile)
        
        deleteFile(dstFile)
        coordinates = getFileCoordinates(fAnnot)
        writeToAnnotFile(H,W,dstFile,coordinates)
    
def main():
    annotPath = r'.\res\PennFudanPed\Annotation'
    imgPath = r'.\res\PennFudanPed\PNGImages'
    dst = r'.\res\PennFudanPed\Label'
    if len(sys.argv)==2:
        imgPath = sys.argv[1]
    elif len(sys.argv)==3:
        imgPath = sys.argv[1]
        dst = sys.argv[2]
    print('imagePath=',imgPath)
    print('dst=',dst)
        
    generateImageLabel(imgPath,annotPath,dst)
    '''
    deleteFolder(dst)
    createPath(dst)
    for i in listFile(imgPath,'png'):
        H,W = getImgHW(loadImg(i))
        #print(H,W)
        fAnnot = getImgAnnotFile(annotPath,i)
        fAnnotName = getFileName(fAnnot)
        dstFile = dst+ '\\' +  fAnnotName
        print('fAnnot=', fAnnot)
        print('dstFile=', dstFile)
        
        deleteFile(dstFile)
        
        coordinates = getFileCoordinates(fAnnot)
        writeToAnnotFile(H,W,dstFile,coordinates)
    '''
    
if __name__=='__main__':
    main()
    