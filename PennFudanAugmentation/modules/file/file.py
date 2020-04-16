#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import os


def OpenTest():
	f = open("data.txt","r")
	f.close()
	
def OpenFile(file,mode="rb",encoding="utf-8"):
	return open(file,mode) 
	
def GetFileLines(file): #content
    f = OpenFile(file)
    nlines = f.readlines()
    CloseFile(f)
    return nlines;
    
def CloseFile(f):
	f.close();

def ClearFile(f): #"r+" "rb+"  "w" "wb" "wb+"
	f.truncate()
	
def WriteToFile(f,str):
	f.write(str)
	
def DeleteFile(file):
	if os.path.exists(file):
		os.remove(file)
	
def copyFile(sourceFile,targetFile):
	srcF = OpenFile(sourceFile,'rb')
	dstF = OpenFile(targetFile,'wb')
	dstF.write(srcF.read())
	CloseFile(srcF)
	CloseFile(dstF)
	
def getFileLinesNum(file):
    lines = GetFileLines(file)
    #lines = [x.decode('UTF8') for x in lines]
    return lines,len(lines)
    

		
	