#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

from modules.folder.folder_file import *
from modules.file.file import *

def parseArgv():
	print("python file:",sys.argv[0])
	for i in range(1, len(sys.argv)):
		print("param:", i, sys.argv[i])

def infoImg(img,str='image:'):
    return(str,'shape:',img.shape,'size:',img.size,'dims=',img.ndim,'dtype:',img.dtype)
	
def main():
	parseArgv()
	#path = r'.\res\PennFudanPed\PNGImages'
	pathList = []
	
	if 1:
 		pathList.append(r'.\res\PennFudanPed\PNGImages')
	else:
		pathList.append(r'.\res\PennFudanPed\trainEx\test_PNGImages')
		pathList.append(r'.\res\PennFudanPed\trainEx\train_PNGImages')
	
	shapes = np.empty((0,3), int)
	for pathImg in pathList:
		for i in pathsFiles(pathImg,'png'):
			#print(i)
			img = cv2.imread(i)
			#print(infoImg(img,i))
			#print(i,img.shape)
			shapes = np.vstack((shapes, np.array(img.shape)))

	print(shapes.shape)
	print(shapes[0])
	print('statistic height:',np.min(shapes[:,0]),np.max(shapes[:,0]),np.mean(shapes[:,0]))
	print('statistic weight:',np.min(shapes[:,1]),np.max(shapes[:,1]),np.mean(shapes[:,1]))
	#print(np.min(shapes[:,2]))
 
	#plotData(shapes)
	scatterData(shapes)
 
def scatterData(data):
    ax = plt.subplot(1,1,1)
    ax.scatter(data[:,1],data[:,0])
    ax.set_xlabel("weight")
    ax.set_ylabel("height")
    plt.show()
    
def plotData(data):
    #plt.suptitle('Penn-Fudan Database')
	ax = plt.subplot(2,2,1)	
	l = 'height range'
	plot(data[:,0],ax,label=l)
	ax = plt.subplot(2,2,2)
	plotHist(data[:,0],ax,label=l)
	
	l = 'weight range'
	ax = plt.subplot(2,2,3)
	plot(data[:,1],ax,label=l)
	ax = plt.subplot(2,2,4)
	plotHist(data[:,1],ax,label=l)
	plt.show()

def plot(x,ax,label='weight Range'):
	ax.plot(x,label=label,color='k')
	ax.legend()
 
def plotHist(x,ax,label='weight Range'):
	num_bins = 8
	ax.hist(x, num_bins,alpha=0.5,rwidth=0.9,label=label,color='k')
	ax.legend()  
     
if __name__=="__main__":
	main()
   
	