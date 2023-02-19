import gtts
from playsound import playsound

def textspeech(speechInput):
    soundResponse = 'response.mp3'

    infile = open(speechInput , "r")

    myline = infile.readline()
    while myline:
        if myline == '\n':
            myline = infile.readline()
        else:
            tts = gtts.gTTS(text=myline, lang="en", tld="co.uk")
            tts.save(soundResponse)
            playsound(soundResponse)
            myline = infile.readline()

    infile.close()