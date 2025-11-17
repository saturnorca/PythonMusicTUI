import time #Used to make program wait
import os #Used to manage things within the operating system
import sys # ^
from pygame import mixer #Used to play audio
import subprocess #Used to run other python files
import random #Used to generate random lists
import mutagen #Used tp access audio file metadata
from mutagen.mp3 import MP3 # ^
from mutagen.wave import WAVE # ^
from pathlib import Path #Used to manage file paths (mostly file extensions)
import threading

mixer.init()
self_path = os.path.abspath(sys.argv[0])
os.chdir(os.path.dirname(self_path))
SONG_PATH = None
os.system('cls')

class applicationManager():
    def __init__(self):
        self.all_playlists = os.listdir(os.path.dirname(__file__)+'\\pList')
        self.currently_playing = "No song playing"
    def removeNewLine(self, list):
        counter = 0
        for item in list:
            list[counter] = item.replace("\n", "")
            counter += 1
    def listPlaylists(self, plist):
        playlists = os.listdir(os.path.dirname(__file__)+'\\pList')
        incCount = 0
        for item in playlists:
            incCount += 1
        plistChoice = plist
        try:
            plistchoice = int(plistChoice)
        except:
            plistchoice = 0
            return ''
        with open(os.path.dirname(__file__)+"\\pList\\"+playlists[int(plistChoice)], 'r') as data:
            temp_SONG_LIST = data.readlines()
        self.removeNewLine(temp_SONG_LIST)
        return temp_SONG_LIST
    def playMusic(self, song):

        Song = MP3(song)
        song_info = Song.info
        song_length = song_info.length
        mixer.music.load(song)
        mixer.music.play()
        time.sleep(song_length)
    def shuffle(self, plist):
        shuffledList = self.listPlaylists(plist)
        random.shuffle(shuffledList)

        for song in shuffledList:
            self.currently_playing = song
            self.playMusic(song)

    def shuffleLoop(self, plist):
        shuffledList = self.listPlaylists(plist)
        random.shuffle(shuffledList)

        for song in shuffledList:
            self.currently_playing = song
            self.playMusic(song)

    def play(self, plist):
        playlist = self.listPlaylists(plist)
        for song in playlist:
            self.currently_playing = song
            self.playMusic(song)
    def add(self, path, plist):
        pathToAdd = path
        playlists = os.listdir(os.path.dirname(__file__)+'\\pList')
        if(int(plist) >= len(playlists)):
            pass
        else:
            subprocess.run(['python', 'DataMNG.py', pathToAdd, playlists[plist]])
    def create(self, name):
        newFile = name
        try:
            with open(os.path.dirname(__file__)+"\\pList\\"+newFile+".bin", 'w') as file:
                file.write("")
        except:
            return -1
    def getCurrentlyPlaying(self):
        return self.currently_playing
