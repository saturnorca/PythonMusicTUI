import sys
import subprocess
import os
from pydub import AudioSegment

original = sys.argv[1]
original_path = sys.argv[2]
new_audio_name = original.replace(".m4a", ".mp3")
audio = AudioSegment.from_file(original_path, format="m4a")

audio.export(os.path.dirname(__file__)+"\\SoundConvStorage\\"+new_audio_name, format="mp3")
