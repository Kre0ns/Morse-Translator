# importing libs
from pydub import AudioSegment
import os

dotSound = AudioSegment.from_wav(os.path.join(os.path.dirname(__file__), "sounds", "dot.wav"))
dashSound = AudioSegment.from_wav(os.path.join(os.path.dirname(__file__), "sounds", "dash.wav"))
shortPauseSound = AudioSegment.from_wav(os.path.join(os.path.dirname(__file__), "sounds", "short_pause.wav"))
mediumPauseSound = AudioSegment.from_wav(os.path.join(os.path.dirname(__file__), "sounds", "medium_pause.wav"))
longtPauseSound = AudioSegment.from_wav(os.path.join(os.path.dirname(__file__), "sounds", "long_pause.wav"))

morseString = ".-.. . - .----. ... / .- -.. -.. / .- / -. . .-- / ..-. . .- - ..- .-. . / - --- / -- -.-- / .--. .-. --- --. .-. .- -- -.-.--"

def morseToAudio(morseString):
    
    morseList = morseString.split(" ")
    
    audioFile = AudioSegment.silent(duration=0)

    for entry in morseList:

        for index, char in enumerate(list(entry)):

            if char == ".":
                
                audioFile += dotSound

                if index != len(entry) - 1:

                    audioFile += shortPauseSound

            elif char == "-":

                audioFile += dashSound

                if index != len(entry) - 1:

                    audioFile += shortPauseSound

    
    audioFile.export("audio.wav", format="wav")



morseToAudio(morseString)