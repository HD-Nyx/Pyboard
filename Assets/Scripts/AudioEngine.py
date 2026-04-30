import sounddevice as SoundDevice
import soundfile as SoundFile

from threading import Thread
import numpy
import time

# for testing
Sound, Sample = SoundFile.read(
    r"C:\.Coding\GitHub\Pyboard\RAHHH.wav",
    dtype="float32"    
)

print(f"Sample rate: {Sample}")
print(f"Shape: {Sound.shape}") 
print(f"dtype: {Sound.dtype}")  

# Gets YOUR microphone (if it is looking for microphone array then it is just for testing)
MicIndex = next((i for i, D in enumerate(SoundDevice.query_devices()) if "Microphone Array" in D["name"]), None)
# Gets CABLE Input from list
CableIndex = next((i for i, D in enumerate(iterable=SoundDevice.query_devices()) if "CABLE Input" in D["name"]), None)

def PlayAudio():
    # Had to wrap this in a func with a with statement to let the aduio pass through
    def PlayFeedback():
        with SoundDevice.OutputStream(samplerate=Sample, channels=Sound.shape[1], dtype='float32') as Stream:
            Stream.write(Sound)

    # Feedback so that you KNOW the sound has been played
    Thread(target=PlayFeedback).start()
    # Playing audio through cable mic
    SoundDevice.play(Sound, Sample, device=CableIndex)
    print("Played audio")

    SoundDevice.wait()

# Audio thread so that it doesn't block anything else
AudioThread = Thread(target=PlayAudio)
AudioThread.name = "AudioThread"
AudioThread.start()
