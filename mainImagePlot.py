#python3
#Steven 11/03/2020 image plot modoule

import matplotlib.pyplot as plt
from common import getRowAndColumn

def plotImagList(imgList,nameList,gray=False):
    nImg = len(imgList)
    nRow,nColumn = getRowAndColumn(nImg)
    
    for n in range(nImg):
        img = imgList[n]
        ax = plt.subplot(nRow, nColumn, n + 1)
        ax.title.set_text(nameList[n])
        if gray:
            plt.imshow(img,cmap="gray")
        else:
            plt.imshow(img)

    #plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    #file = r'./res/obama.jpg'#'./res/Lenna.png' #
    #img = ImageBase(file,mode=cv2.IMREAD_GRAYSCALE) # IMREAD_GRAYSCALE IMREAD_COLOR
    #print(img.infoImg())
    #showimage(img.binaryImage(thresHMin=50,thresHMax=150))
    pass

if __name__=='__main__':
    main()
