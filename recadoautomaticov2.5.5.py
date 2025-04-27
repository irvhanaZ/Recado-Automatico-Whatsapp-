import playsound
import time
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


Contato = simpledialog.askstring("Entrada", "Digite o nome do contato")
Mensagem1 = simpledialog.askstring("Entrada", "Digite a primeira mensagem") 
Mensagem2 = simpledialog.askstring("Entrada", "Digite a segunda mensagem") 
Mensagem3 = simpledialog.askstring("Entrada", "Digite a terceira mensagem")
Mensagem4 = simpledialog.askstring("Entrada", "Digite a Última mensagem")

keyboard = Controller()

for i in range(10):
    playsound.playsound(caminho_audio)
    time.sleep(0.5)
    
    keyboard.press(Key.cmd)
    keyboard.press('d')
    keyboard.release(Key.cmd)
    keyboard.release('d')
    time.sleep(1)
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(3)

    # Iniciando Whattsapp
    keyboard.type('wh')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(7)
    
    # Digitando o contato
    keyboard.type(Contato)
    time.sleep(1.0)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)

    # Digitando a primeira mensagem
    time.sleep(1)
    keyboard.type(Mensagem1)
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    # Digitando a segunda mensagem
    keyboard.type(Mensagem2)
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    # Digitando a terceira mensagem
    keyboard.type(Mensagem3)
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    # Digitando a quarta mensagem
    keyboard.type(Mensagem4)
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

    keyboard.press(Key.alt)
    keyboard.press(Key.f4)
    keyboard.release(Key.alt)
    keyboard.release(Key.f4)

    time.sleep(300)

if __name__ == "__main__":
      main()