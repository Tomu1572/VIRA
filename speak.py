import os
import time
# import wave
import winsound
# from io import BytesIO
import soundfile as sf
import sounddevice as sd
import requests
import urllib
# import pydub
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
# import resampy

VOICEVOX_PORT = 50021
BASE_URL = f'http://127.0.0.1:{VOICEVOX_PORT}'

speech_path = r'./audio'  
speech_filename = r'speech.wav'  

def speak(sentence):
    # Generate initial query 
    speaker_id = 10 # 6: (四国めたん:  "ツンツン"), 14: (冥鳴ひまり: "ノーマル", 20 = cute, 13 = handsome, 10 = supercute)
    params_encoded = urllib.parse.urlencode({'text': sentence, 'speaker': speaker_id})
    print(f'{BASE_URL}/audio_query?{params_encoded}')
    r = requests.post(f'{BASE_URL}/audio_query?{params_encoded}')
    voicevox_query = r.json()
    voicevox_query['speedScale'] = 1
    voicevox_query['volumeScale'] = 4.0
    voicevox_query['intonationScale'] = 1.5
    voicevox_query['prePhonemeLength'] = 1.0
    voicevox_query['postPhonemeLength'] = 1.0

    # Synthesis voice as wav file 
    params_encoded = urllib.parse.urlencode({'speaker':speaker_id})
    r = requests.post(f'{BASE_URL}/synthesis?{params_encoded}', json=voicevox_query)
    print(f'{BASE_URL}/synthesis?{params_encoded}')

    if not os.path.exists(speech_path):
        os.makedirs(speech_path)

    speech_target = os.path.join(speech_path, speech_filename)
    time.sleep(1)

    with open(speech_target, 'wb') as outfile:
        outfile.write(r.content)
    
    # Play audio file
    # winsound.PlaySound(speech_target, winsound.SND_FILENAME)
    audio = AudioSegment.from_file(speech_target)
    play(audio)
    
if __name__ == '__main__':
    speak('こんにちは、音声合成の世界へようこそ')
    print(sd.query_devices())
    
    #speak('こんにちは')