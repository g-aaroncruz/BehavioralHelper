import os
import random
from pydub import AudioSegment
from pydub.playback import  play
recordings_folder = r"/home/aaron/Downloads/BR"
files = os.listdir(recordings_folder)
random.shuffle(files)
for file in files:
    recording_to_play = os.path.join(recordings_folder, file)
    audio = AudioSegment.from_file(recording_to_play, format='m4a')
    play(audio)
    print ("press 'c' to continue to next question...")
    user_in= ""
    while (user_in != 'c'):
        user_in= input()
