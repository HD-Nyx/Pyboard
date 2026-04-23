import sounddevice as SoundDevice
import soundfile as SoundFile

from threading import Thread
import time

Sound, Sample = SoundFile.read(r"C:\.Coding\GitHub\Pyboard\RAHHH.wav")

def PlayAudio():
    SoundDevice.play(Sound, Sample)

    print("Played audio")

    SoundDevice.wait()

AudioThread = Thread(target=PlayAudio)
AudioThread.name = "AudioThread"
AudioThread.start()
