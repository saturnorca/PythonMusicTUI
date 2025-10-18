import sys
import subprocess
import os
import pathlib
from pydub import AudioSegment


PATH = sys.argv[1]
plist = sys.argv[2]
plistPATH = os.path.dirname(__file__)+"\\pList\\"+plist
if(PATH[-1] == "\\"):
   PATH = PATH[:-1]
#print(PATH)
fileList = os.listdir(PATH)
for file in fileList:
    
    if(pathlib.Path(file).suffix == ".mp3" or pathlib.Path(file).suffix == ".wav"):
        #print(file)
        with open(plistPATH, 'a') as data:
            data.write(PATH+"\\"+file+"\n")
    elif(pathlib.Path(file).suffix == ''):
        subfolder_list = os.listdir(PATH+"\\"+file)
        for subfile in subfolder_list:
            if(pathlib.Path(subfile).suffix == '.mp3' or pathlib.Path(file).suffix == '.wav'):
                #print(subfile)
                with open(plistPATH, 'a') as data:
                    data.write(PATH+"\\"+file+"\\"+subfile+"\n")
            elif(pathlib.Path(subfile).suffix == '.m4a'):
                #print(subfile)
                subprocess.run(['python', 'DataConv.py', subfile, PATH+"\\"+file+"\\"+subfile])
                with open(plistPATH, 'a') as data:
                    newFile = subfile.replace(".m4a", ".mp3")
                    data.write(os.path.dirname(__file__)+"\\SoundConvStorage\\"+newFile+"\n")
    elif(pathlib.Path(file).suffix == '.m4a'):
        #print(file)
        subprocess.run(['python', 'DataConv.py', file, PATH+"\\"+file])
        with open(plistPATH, 'a') as data:
            newFile = file.replace(".m4a", ".mp3")
            data.write(os.path.dirname(__file__)+"\\SoundConvStorage\\"+newFile+"\n")
            