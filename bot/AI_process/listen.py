import speech_recognition as sr
from gtts import gTTS
import json
import tempfile
import os
import sys
import time
import datetime

# Instalar = sudo apt-get install ffmpeg


def dateTimeNow():
    now = datetime.datetime.now()
    nowHour = now.hour

    # Validar a hora
    if 0 <= nowHour < 12:
        phrase = "Bom dia "
    elif 12 <= nowHour < 18:
        phrase = "Boa tarde "
    else:
        phrase = "Boa noite "

    return phrase


def read_process(text_number):
    '''
        - Leitura inicial (Teste)
    '''
    text = text_number
    if text:
        try:
            print(text_number)
            tts = gTTS(text=text, lang='pt-br')
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
                temp_audio_path = temp_audio.name
                tts.write_to_fp(temp_audio)

                # Reproduz o áudio
                os.system(f"ffplay -nodisp -autoexit {temp_audio_path}")

                # Apaga o arquivo temporário
                os.remove(temp_audio_path)
        except:
            print('Sem conexão, tentaremos mais tarde')
    else:
        print('Não foi possível iniciar o processo')


def read_content(fileToSpeak):
    try:
        with open(fileToSpeak, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f'Erro ao consultar arquivo json {e}')

