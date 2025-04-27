import playsound
import os
import sys
import time 

# --- Ajuste para detectar o caminho correto ---
if getattr(sys, 'frozen', False):
    caminho_base = sys._MEIPASS
else:
    caminho_base = os.path.dirname(os.path.abspath(__file__))

caminho_audio = os.path.join(caminho_base, 'tuc.mp3')

# --- Teste de informações ---
print("Caminho base:", caminho_base)
print("Caminho do áudio:", caminho_audio)
print("Arquivo existe?", os.path.exists(caminho_audio))

# --- Tentando tocar o áudio ---
playsound.playsound(caminho_audio)


time.sleep(40)