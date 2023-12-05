import whisper
import soundfile as sf
import simpleaudio as sa

from txtai.pipeline import TextToSpeech

model = whisper.load_model("small")

audio_name = input("Digite o nome do audio: ")
audio_lang = input("Em qual linguagem esta o audio? ")

results = model.transcribe(audio_name, language=audio_lang, task="translate")

# print the recognized text
print("Result:\n")
print(results["text"])

# Build pipeline
tts = TextToSpeech("NeuML/ljspeech-jets-onnx")

tts_text = results["text"]

# Generate speech
speech = tts(tts_text)

# Write to file
sf.write("out.wav", speech, 22050)

# Read the file
wave_obj = sa.WaveObject.from_wave_file("out.wav")

# Play audio
play_obj = wave_obj.play()
play_obj.wait_done() 