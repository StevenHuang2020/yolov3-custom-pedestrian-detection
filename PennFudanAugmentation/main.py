#python3 steve
#10/04/2020 Penn-Fudan dataset augmentation
#resizing and cropping
import sys
import cv2
import numpy as np 
from modules.folder.folder_file import pathsFiles,createPath,getFileName,getFmtFile,getRootFile,deleteFile
from genImageBoxLabel import getFileCoordinates,writeToAnnotFile,writeCordToAnnotFile
from genImageBoxLabel import loadImg,getImgHW,listFile,getImgAnnotFile,generateImageLabel

def writeImg(img,filePath):
    cv2.imwrite(filePath,img)
    
def clipImg(img,startPt,stopPt):
    return img[startPt[1]:stopPt[1], startPt[0]:stopPt[0]]

def clipImgCoordinate(img,clipCoordinate,coordinates):
    clipImg = img[clipCoordinate[1]:clipCoordinate[3], clipCoordinate[0]:clipCoordinate[2]]
    
    newCoordinates=[]
    for cod in coordinates:
        Xmin,Ymin,Xmax,Ymax = cod
        newCoordinates.append((Xmin-clipCoordinate[0],Ymin-clipCoordinate[1],Xmax-clipCoordinate[0],Ymax-clipCoordinate[1]))
    return clipImg,newCoordinates

    return clipImg

def rectangleImg(img,startPt,stopPt):
    color = (0, 0, 255) 
    thickness=2
    image = cv2.rectangle(img, startPt, stopPt, color, thickness) 
    return image
 
def resizeImg(img,ratio,coordinates):
    #print(ratio.shape)
    ratio = float(ratio)
    h,w = img.shape[0],img.shape[1]
    reH,reW = round(h*ratio), round(w*ratio)
    #print('raw=',ratio,reH,reW,round(265.4),round(img.shape[0]*2))
    #return cv2.resize(img, (int(h*ratio), int(w*ratio)), interpolation=cv2.INTER_CUBIC) #INTER_LANCZOS4
    rimg = cv2.resize(img, (reW,reH), interpolation=cv2.INTER_CUBIC) #INTER_CUBIC INTER_NEAREST INTER_LINEAR INTER_AREA
    
    newCoordinates=[]
    for cod in coordinates:
        Xmin,Ymin,Xmax,Ymax = cod
        newCoordinates.append((round(Xmin*ratio),round(Ymin*ratio),round(Xmax*ratio),round(Ymax*ratio)))
    return rimg,newCoordinates

def generateByScaling(imgPath,annotPath,dstPath,dstBoundingBoxPath,dstLabelPath,N=20):
     for i in listFile(imgPath):
        imgFile = getFileName(i)
        fAnnot = getImgAnnotFile(annotPath,i)
        img = loadImg(i)
        H,W = getImgHW(img)
        print(i,fAnnot,H,W)
        coordinates = getFileCoordinates(fAnnot)   
        
        #start generate new images
        ratios = np.linspace(0.5,2,N)    
        for ratio in ratios:     
            rImg,newCoordinates = resizeImg(img,ratio,coordinates)
            #print(i,'ratio=',ratio,'src=',coordinates,'dst=',newCoordinates)
            
            newImgFile = imgFile[:imgFile.rfind('.')] + '_scale_' + str(ratio)
            writeImg(rImg,dstPath + '\\' + newImgFile + '.png')
            
            #newFileCoord = dstPath + '\\' + newImgFile + '.txt'
            #writeCordToAnnotFile(newFileCoord, newCoordinates)
            boundingImg = rImg.copy()
            for i in newCoordinates:
                boundingImg = rectangleImg(boundingImg,(i[0],i[1]),(i[2],i[3]))
            writeImg(boundingImg, dstBoundingBoxPath + '\\' + newImgFile + '.png')
            
            newImgAnnotFile = dstLabelPath + '\\' + newImgFile + '.txt'
            writeToAnnotFile(boundingImg.shape[0],boundingImg.shape[1],newImgAnnotFile,newCoordinates)
    
def augmentationByScaling(basePath,imgPath,annotPath,genNumPerRawImg=20):
    dstPath = basePath + 'NewImagesScale'
    dstBoundingBoxPath = basePath + 'NewImagesScaleBounding'
    dstLabelPath = basePath + 'NewImagesScaleLabel'
    
    createPath(dstPath)
    createPath(dstBoundingBoxPath)
    createPath(dstLabelPath)
    generateByScaling(imgPath,annotPath,dstPath,dstBoundingBoxPath,dstLabelPath,genNumPerRawImg)

def getBoundaryCoordinate(coordinates):
    x_min,y_min,x_max,y_max = coordinates[0]
    for i in coordinates:
        Xmin,Ymin,Xmax,Ymax = i
        if x_min > Xmin:
            x_min = Xmin
        if y_min > Ymin:
            y_min = Ymin
        if x_max < Xmax:
            x_max = Xmax
        if y_max < Ymax:
            y_max = Ymax
    return x_min,y_min,x_max,y_max
        
def generateByClipping(imgPath,annotPath,dstPath,dstBoundingBoxPath,dstLabelPath,N=10):
    for i in listFile(imgPath):
        imgFile = getFileName(i)
        fAnnot = getImgAnnotFile(annotPath,i)
        img = loadImg(i)
        H,W = getImgHW(img)
        #print(fAnnot,H,W)
        coordinates = getFileCoordinates(fAnnot)
        boundCoordinate = getBoundaryCoordinate(coordinates)
        print(i,H,W,coordinates,boundCoordinate)
        
        clipXmin = np.random.randint(boundCoordinate[0], size=N)
        clipYmin = np.random.randint(boundCoordinate[1], size=N)
        clipXmax = np.random.randint(W-boundCoordinate[2], size=N)
        clipYmax = np.random.randint(H-boundCoordinate[3], size=N)
        
        for Xmin,YMin,Xmax,Ymax in zip(clipXmin,clipYmin,clipXmax,clipYmax):
            clipCoordinate = (Xmin,YMin,Xmax+boundCoordinate[2],Ymax+boundCoordinate[3])
            clipImg,newCoordinates = clipImgCoordinate(img.copy(),clipCoordinate,coordinates)
            #print(coordinates,clipCoordinate,newCoordinates,'NewH=',clipImg.shape[0],'NewW=',clipImg.shape[1])
            clipImgName = imgFile[:imgFile.rfind('.')]+'_'+str(clipCoordinate[0])+'_'+str(clipCoordinate[1])+'_'+str(clipCoordinate[2])+'_'+str(clipCoordinate[3])
            #print(clipImgName)
            writeImg(clipImg,dstPath + '\\' + clipImgName + '.png')
            
            writeToAnnotFile(clipImg.shape[0],clipImg.shape[1],dstLabelPath+ '\\' + clipImgName + '.txt',newCoordinates)

            boundingImg = clipImg.copy()
            for i in newCoordinates:
                boundingImg = rectangleImg(boundingImg,(i[0],i[1]),(i[2],i[3]))
            writeImg(boundingImg,dstBoundingBoxPath + '\\' + clipImgName + '.png')
    
def augmentationByClipping(basePath,imgPath,annotPath,genNumPerRawImg=10):
    dstPath = basePath + 'NewImagesClip'
    dstBoundingBoxPath = basePath + 'NewImagesClipBounding'
    dstLabelPath = basePath + 'NewImagesClipLabel'
    
    createPath(dstPath)
    createPath(dstBoundingBoxPath)
    createPath(dstLabelPath)

    generateByClipping(imgPath,annotPath,dstPath,dstBoundingBoxPath,dstLabelPath,genNumPerRawImg)
           

def main():
    base = r'.\res\PennFudanPed\\'
    annotPath = base + 'Annotation'
    imgPath = base + 'PNGImages'
    dstLabelPath = base + 'Label'
    
    generateImageLabel(imgPath,annotPath,dstLabelPath)
    augmentationByScaling(base,imgPath,annotPath,genNumPerRawImg=10)
    augmentationByClipping(base,imgPath,annotPath,genNumPerRawImg=20)
           
if __name__ == '__main__':
    main()