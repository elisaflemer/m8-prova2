from txtai.pipeline import TextToSpeech
from playsound import playsound
import soundfile as sf

tts = TextToSpeech("NeuML/ljspeech-jets-onnx")

print("Bem-vindo ao sintetizador de voz.")
counter = 1

while True:
    user_input = input('Escreva frases e aperte ENTER para gerar áudio: ')

    speech = tts(user_input)
    # Write to file

    sf.write(f"out{counter}.wav", speech, 22050)

    playsound(f'./out{counter}.wav')
    counter += 1