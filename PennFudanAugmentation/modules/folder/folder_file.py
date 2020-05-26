#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import os
import shutil

def createPath(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        
def deleteFile(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def deleteFolder(file_path):
    if os.path.exists(file_path):
        #shutil.rmtree(file_path)
        for lists in os.listdir(file_path):
            f = os.path.join(file_path, lists)
            if os.path.isfile(f):
                os.remove(f)
    
def folderListFiles(path):
    return [lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))]

def folderListFolders(path):
    return [lists for lists in os.listdir(path) if os.path.isdir(os.path.join(path, lists))]
   
def curPathFiles(dir): #return cur path files
    for f in os.listdir(dir):
        yield f
        
def pathsPaths(dir):#return all include subfolder files
    for dirpath, dirnames, filenames in os.walk(dir):
        #print(dirpath)
        yield dirpath
    
def pathsFiles0(dir): #return all include subfolder paths    
    for dirpath, dirnames, filenames in os.walk(dir):
        #print ('Directory', dirpath)
        for filename in filenames:
            #print(dirpath+filename)
            yield dirpath+filenames
            
def pathsFiles(dir,filter=''): #"cpp h txt jpg"
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

def pathsFilesList(dir,filter=''): #"cpp h txt jpg"
    files=[]
    
    fmts = filter.split()
    if fmts:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                #print(filename,getFmtFile(filename),getExtFile(getFmtFile(filename)))
                if getExtFile(getFmtFile(filename)) in fmts:
                    files.append(dirpath+'\\'+filename)
    else:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                files.append(dirpath+'\\'+filename)
    return files
                 
def nameFiles(dir,filter=''): #"cpp h txt jpg"
    fmts = filter.split()    
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            fmt = getExtFile(getFmtFile(filename))
            if fmts:
                if fmt in fmts:
                    yield filename
            else:
                yield filename
				
def getExtFile(file):
    return file[file.rfind('.')+1:]

def getFmtFile(path):
    #/home/User/Desktop/file.txt    /home/User/Desktop/file     .txt
    root_ext = os.path.splitext(path) 
    return root_ext[1]

def getRootFile(path):
    #/home/User/Desktop/file.txt    /home/User/Desktop/file     .txt
    root_ext = os.path.splitext(path) 
    return root_ext[0]

def getFileName(path):  
    #'/home/user/Desktop/file.txt'   '/home/user/Desktop/'   'file.txt'
    #head_tail = os.path.split(path)
    #return head_tail[1]
    
    #'/home/User/Documents/file.txt' file.txt
    return os.path.basename(path)

def moveFile(src,dst):
    shutil.move(src,dst)
    
def copyFile(src,dst):
    shutil.copy2(src,dst) #shutil.copy(src,dst)