import sounddevice as SoundDevice
import soundfile as SoundFile

from threading import Thread
import time

AudioThread = None
Sound, Sample = None, None

def PlayAudio():
    Sound, Sample = SoundFile.read("C:/Users/ryanz/downloaded_site/Documents/Audacity/Indian Villige Song.mp3")

    SoundDevice.play(Sound, Sample)
    SoundDevice.wait()
    
AudioThread = Thread(target = PlayAudio())

def PauseAudio():
    SoundDevice.stop()

AudioThread.start()
