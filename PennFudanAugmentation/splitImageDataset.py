#python3 steve
#12/04/2020 image dataset split
import sys
from modules.folder.folder_file import createPath,getFileName,pathsFilesList
from modules.folder.folder_file import deleteFolder,copyFile

def getImgAnnotFile(annotPath,file):
    fAnnot = getFileName(file)
    return annotPath + '\\'+ fAnnot[:fAnnot.rfind('.')]+'.txt'

def train_test_split(srcPath,label,dstTrainPath,dstTestPath,dstTrainLabels,dstTestLabels,test_size=0.3):
    files = pathsFilesList(srcPath,filter='png')
    total = len(files)
    trainLen = int(total*(1-test_size))
    print('trainLen,testLen=',total,trainLen,total-trainLen)
    for i,f in enumerate(files):
        fileName = getFileName(f)
        fAnnot = getImgAnnotFile(label,f)
        print('fAnnot=',fAnnot)
        if i<trainLen:
            copyFile(f,dstTrainPath + '\\' + fileName)
            copyFile(fAnnot,dstTrainLabels + '\\')
        else:
            copyFile(f,dstTestPath + '\\' + fileName)
            copyFile(fAnnot,dstTestLabels + '\\')

def main():    
    dstTrainPath = r'.\res\PennFudanPed\train_PNGImages'
    dstTestPath = r'.\res\PennFudanPed\test_PNGImages'
    dstTrainLabels =  r'.\res\PennFudanPed\labels\train_PNGImages'
    dstTestLabels =  r'.\res\PennFudanPed\labels\test_PNGImages'
    
    deleteFolder(dstTrainPath)
    createPath(dstTrainPath)
    deleteFolder(dstTestPath)
    createPath(dstTestPath)
    deleteFolder(dstTrainLabels)
    createPath(dstTrainLabels)
    deleteFolder(dstTestLabels)
    createPath(dstTestLabels)
    
    imgPathList=[]
    imgPathList.append((r'.\res\PennFudanPed\PNGImages',r'.\res\PennFudanPed\Label'))
    imgPathList.append((r'.\res\PennFudanPed\NewImagesClip',r'.\res\PennFudanPed\NewImagesClipLabel'))
    imgPathList.append((r'.\res\PennFudanPed\NewImagesScale',r'.\res\PennFudanPed\NewImagesScaleLabel'))
    
    for i in imgPathList:
        imgPath = i[0]
        label = i[1]
        train_test_split(imgPath,label,dstTrainPath,dstTestPath,dstTrainLabels,dstTestLabels,test_size=0.2)
    
    # imgPath = r'.\res\PennFudanPed\NewImagesClip'
    # label = r'.\res\PennFudanPed\NewImagesClipLabel'
    # train_test_split(imgPath,label,dstTrainPath,dstTestPath,dstTrainLabels,dstTestLabels,test_size=testSize)
    
    # imgPath = r'.\res\PennFudanPed\NewImagesScale'
    # label = r'.\res\PennFudanPed\NewImagesScaleLabel'
    # train_test_split(imgPath,label,dstTrainPath,dstTestPath,dstTrainLabels,dstTestLabels,test_size=testSize)
    
    
if __name__=='__main__':
    main()
    