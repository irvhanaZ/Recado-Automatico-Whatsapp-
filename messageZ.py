import tkinter as tk
from pynput.keyboard import Key, Controller
from tkinter import simpledialog
import os
import sys

if getattr(sys, 'frozen', False):
      caminho_base = sys._MEIPASS
else:
      caminho_base = os.path.dirname(os.path.abspath(__file__))

caminho_audio = os.path.join(caminho_base, 'tuc.mp3')

def main():
        root =  tk.Tk()
        root.withdraw()

selecionar_app = simpledialog.askstring("Bem vindo", "Digite qual app deseja usar")

while selecionar_app not in("whatsapp", "telegram"):
       selecionar_app = input("Você selecionou (whatsapp ou telegram): ").lower()

if selecionar_app == "whatsapp":
       import messageZ_whatsapp
       
elif selecionar_app == "telegram":
       import messageZ_telegram
       
