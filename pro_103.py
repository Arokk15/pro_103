import os
import shutil

import time

path_a="/Users/aro/Downloads/"
c_pat="/Users/aro/Desktop/class project/PRO-C100/110/"
a_path="Users/aro/"

list_files=os.listdir(path_a)

file_exe=[]

z=0

pic=[".tif",".tiff",".jpg",".jpeg",".gif",".png",".bmp",".eps",".raw",".cr2",".nef",".orf",".sr2"]
video=[".mp4",".avi",".mov",".wmv",".flv",".mkv"]
docm=[".docx",".pdf"]
compress=[".rar",".zip","7z",".tar"]
app=[".exe"]




def pice():
    for i in pic:
        for j in list_files:
            
            root,ext=os.path.splitext(j)
            if i == ext:
                if os.path.exists(c_pat+"images/"+j):
                    print("as")
                    shutil.move(path_a+j,c_pat+"images/"+root+str(z)+i)
                    
                else:
                    a=path_a+j
                    b=c_pat+"images"
                    print("the image is moving.......")
                    shutil.move(a,b)
def movie():
    for i in video:
        for j in list_files:
            root,ext=os.path.splitext(j)
            if i == ext:
                if os.path.exists(c_pat+"videos/"+j):
                    print("as")
                    shutil.move(path_a+j,c_pat+"videos/"+root+str(z)+i)
                else:
                    a=path_a+j
                    b=c_pat+"videos"
                    print("the videos is moving.......")
                    shutil.move(a,b)
def document():
    for i in docm:
        for j in list_files:
            root,ext=os.path.splitext(j)
            if i == ext:
                if os.path.exists(c_pat+"document/"+j):
                    print("as")
                    shutil.move(path_a+j,c_pat+"document/"+root+str(z)+i)
                else:
                    a=path_a+j
                    b=c_pat+"document"
                    print("the document is moving.......")
                    shutil.move(a,b)
def appl():
    for i in app:
        for j in list_files:
            root,ext=os.path.splitext(j)
            if i == ext:
                if os.path.exists(c_pat+"application/"+j):
                    print("as")
                    shutil.move(path_a+j,c_pat+"application/"+root+str(z)+i)
                else:
                    a=path_a+j
                    b=c_pat+"application"
                    print("the application is moving.......")
                    shutil.move(a,b)
def cf():
    for i in compress:
        for j in list_files:
            root,ext=os.path.splitext(j)
            if i == ext:
                if os.path.exists(c_pat+"compressed file/"+j):
                    print("as")
                    shutil.move(path_a+j,c_pat+"compressed file/"+root+str(z)+i)
                else:
                    a=path_a+j
                    b=c_pat+"compressed file"
                    print("the compressed file is moving.......")
                    shutil.move(a,b)


while True:
    list_files=os.listdir(path_a)
    z=z+1
    
    if os.path.exists(c_pat+"videos")!=True:
        os.mkdir(c_pat+"videos")
        
    if os.path.exists(c_pat+"images")!=True:
        os.mkdir(c_pat+"images")

    if os.path.exists(c_pat+"document")!=True:
        os.mkdir(c_pat+"document")



    if os.path.exists(c_pat+"compressed file")!=True:
        os.mkdir(c_pat+"compressed file")

    if os.path.exists(c_pat+"application")!=True:
        os.mkdir(c_pat+"application")
    pice()
    movie()
    cf()
    appl()
    document()
    print("refresh times ......",z)
    time.sleep(1)
    os.system('cls')
    
    
