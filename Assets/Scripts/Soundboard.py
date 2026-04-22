import os

SoundboardsPath = os.path.join(os.path.dirname(__file__), "../../Soundboards")

def CreateSoundboard(Name: str):
    os.makedirs(os.path.join(SoundboardsPath, Name), exist_ok = True)
    
    return f'Created soundboard {Name} at {SoundboardsPath}'

def DeleteSoundboard(Name: str):
    Soundboard = os.path.join(SoundboardsPath, Name)

    if os.path.isdir(Soundboard):
        for File in os.listdir(Soundboard):
            os.remove(os.path.join(Soundboard, File))
        os.rmdir(Soundboard)

        return f'Removed soundboard {Name}'
    else:
        return f'Soundboard {Name} not found'
    

    

