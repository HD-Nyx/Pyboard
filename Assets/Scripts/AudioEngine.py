import sounddevice as SoundDevice
import soundfile as SoundFile

from threading import Thread
import time

# for testing
Sound, Sample = SoundFile.read(r"C:\.Coding\GitHub\Pyboard\RAHHH.wav")
print(f"Sample rate: {Sample}")
print(f"Shape: {Sound.shape}") 
print(f"dtype: {Sound.dtype}")  

# Gets CABLE Input from list
CableIndex = next((i for i, D in enumerate(SoundDevice.query_devices()) if "CABLE Input" in D["name"]), None)

def PlayAudio():
    SoundDevice.play(Sound, 44100, device=CableIndex)

    print("Played audio\n")

    SoundDevice.wait()

# audio thread so that it doesn't block anything else
AudioThread = Thread(target=PlayAudio)
AudioThread.name = "AudioThread"
AudioThread.start()
