import sys
import subprocess
import os
from pydub import AudioSegment
from mutagen.mp4 import MP4, MP4Cover
from mutagen.id3 import ID3, APIC, error
from mutagen.id3 import ID3NoHeaderError
from io import BytesIO
original = sys.argv[1]
original_path = sys.argv[2]

new_audio_name = original.replace(".m4a", ".mp3")
audio = AudioSegment.from_file(original_path, format="m4a")

tags = MP4(original_path)
artwork = "noArt.mp3"

if 'covr' in tags:
    artwork = tags['covr'][0]

audio.export(os.path.dirname(__file__)+"\\SoundConvStorage\\"+new_audio_name, format="mp3")


new_tags = ID3(os.path.dirname(__file__)+"\\SoundConvStorage\\"+new_audio_name)

#new_tags = ID3()
new_tags.add(
    APIC(
        encoding=3,
        mime='image/png',
        type=3,
        desc=u'Cover',
        data=artwork
    )
)
new_tags.save()
