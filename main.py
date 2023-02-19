import translationLayer
import webgpt
import textSpeech
import pathlib
import openai
import whisper
import pyaudio
import wave

frames = [] # Storing frames

numChunks = 1024  # Num samples in chunk
sampleFormat = pyaudio.paInt16  # Bits per sample
numChannels = 1
numSamples = 44100  # Num samples per second
numSeconds = 3
recordname = "record.wav"
whisperInput = "activeListening.txt"

interface = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

voiceStream = interface.open(format = sampleFormat , channels = numChannels , rate = numSamples , frames_per_buffer = numSamples , input = True)

# Store data in chunks for x seconds
for i in range(0, int(numSamples / numChunks * numSeconds)):
    temp = voiceStream.read(numChunks)
    frames.append(temp)

voiceStream.stop_stream()
voiceStream.close()

interface.terminate()

print('Finished recording')

# Saving into .wav file
record = wave.open(recordname, 'wb')
record.setnchannels(numChannels)
record.setsampwidth(interface.get_sample_size(sampleFormat))
record.setframerate(numSamples)
record.writeframes(b''.join(frames))
record.close()

output = open(whisperInput, "w")
print('Transcribing audio')

model = whisper.load_model("base")
result = model.transcribe("record.wav")

print('Writing to a file')
output.write(result["text"])
print('Done')
output.close()

filename = "replyInput.txt"
text = "activeListening.txt"
inputText = pathlib.Path(text).read_text(encoding="utf-8")
intentResult = translationLayer.translationLayer(inputText)
print(intentResult)

prompt = "respond to the statement"

data = {
    "prompt":f"{prompt} {inputText}",
    "max_tokens":50
}

if intentResult == 'affirm':
    response = openai.Completion.create(engine="text-davinci-003", prompt=data["prompt"], max_tokens=data["max_tokens"])
    responseOut = open(filename, "w")
    responseOut.write(response.choices[0].text)
    responseOut.close()
    
if intentResult == 'greet':
    response = openai.Completion.create(engine="text-davinci-003", prompt=data["prompt"], max_tokens=data["max_tokens"])
    responseOut = open(filename, "w")
    responseOut.write(response.choices[0].text)
    responseOut.close()
    
if intentResult == 'personal':
    response = openai.Completion.create(engine="text-davinci-003", prompt=data["prompt"], max_tokens=data["max_tokens"])
    responseOut = open(filename, "w")
    responseOut.write(response.choices[0].text)
    responseOut.close()
        
if intentResult == 'goodbye':
    response = openai.Completion.create(engine="text-davinci-003", prompt=data["prompt"], max_tokens=data["max_tokens"])
    responseOut = open(filename, "w")
    responseOut.write(response.choices[0].text)
    responseOut.close()
    
if intentResult == 'command':
    response = openai.Completion.create(engine="text-davinci-003", prompt=data["prompt"], max_tokens=data["max_tokens"])
    responseOut = open(filename, "w")
    responseOut.write(response.choices[0].text)
    responseOut.close()
        
if intentResult =='question':
    query = inputText
    response = webgpt.webgpt(query)
    responseOut = open(filename, "w")
    responseOut.write(response.choices[0].text)
    responseOut.close()
    
speechInput = "replyInput.txt"
textSpeech.textspeech(speechInput)


