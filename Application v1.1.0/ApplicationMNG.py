import time #Used to make program wait
import os #Used to manage things within the operating system
import sys # ^
from pygame import mixer #Used to play audio
import subprocess #Used to run other python files
import random #Used to generate random lists
import mutagen #Used tp access audio file metadata
from mutagen.mp3 import MP3 # ^ Same as above
from mutagen.wave import WAVE # ^ Same as above
from pathlib import Path #Used to manage file paths (mostly file extensions)
import threading #Used to run multiple threads at once (Play audio while running app)
import asyncio
import playMNG
mixer.init()
self_path = os.path.abspath(sys.argv[0])
os.chdir(os.path.dirname(self_path))
SONG_PATH = None
os.system('cls')
class applicationManager():
    def __init__(self, app):
        self.all_playlists = os.listdir(os.path.dirname(__file__)+'\\pList')
        self.currently_playing = "\\No song playing"
        self.stop_playing = True;
        self.play_count = 0
        self.app = app
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
        self.play_count += 1
        self.app.updateTitle()
        mixer.music.load(song)
        mixer.music.play()
        try:
            time.sleep(song_length)
        except asyncio.CancelledError:
            self.stop_playing = True;

    def shuffle(self, plist):
        shuffledList = self.listPlaylists(plist)
        random.shuffle(shuffledList)
        keep_playing = playMNG.playMNG(self.play_count)
        song_counter = 0
        for song in shuffledList:
            if keep_playing.get_val() != self.play_count:
                break
            else:
                keep_playing.set_val(keep_playing.get_val()+1)

                self.currently_playing = song
                self.playMusic(song)

    def shuffleLoop(self, plist):
        shuffledList = self.listPlaylistls(plist)
        random.shuffle(shuffledList)
        keep_playing = playMNG.playMNG(self.play_count)
        song_counter = 0
        for song in shuffledList:
            if song_counter == len(shuffledList)-1:
                song_counter += 1
                self.playMusic(song)
                self.shuffleLoop(plist)
            elif keep_playing.get_val() != self.play_count:
                break
            else:
                keep_playing.set_val(keep_playing.get_val()+1)
                self.currently_playing = song
                song_counter += 1
                self.playMusic(song)

    def play(self, plist):
        playlist = self.listPlaylists(plist)
        keep_playing = playMNG.playMNG(self.play_count)
        song_counter = 0
        for song in playlist:
            if song_counter == len(playlist)-1:
                song_counter += 1
                self.currently_playing = song
                self.playMusic(song)
                self.play(plist)
            elif keep_playing.get_val() != self.play_count:
                break
            else:
                keep_playing.set_val(keep_playing.get_val()+1)
                self.currently_playing = song
                
                self.playMusic(song)
    def add(self, path, plist):
        pathToAdd = path
        playlists = os.listdir(os.path.dirname(__file__)+'\\pList')
        if(int(plist) >= len(playlists)):
            pass
        else:
            subprocess.run(['python', 'DataMNG.py', pathToAdd, playlists[plist]])
    def create_plist(self, name):
        newFile = name
        try:
            with open(os.path.dirname(__file__)+"\\pList\\"+newFile+".bin", 'w') as file:
                file.write("")
        except:
            return -1
    def getCurrentlyPlaying(self):
        return self.currently_playing
    def pause(self):
        mixer.music.pause()
    def unpause(self):
        mixer.music.unpause()
if __name__ == "__main__":
    print("MusicPy Application Manager")