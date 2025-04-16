import playsound
import pyautogui as pag
import time
import tkinter as tk
from tkinter import simpledialog
pag.PAUSE = 2
procurar = "encontrado"

Contato = simpledialog.askstring("Entrada", "Digite o nome do contato")
Mensagem1 = simpledialog.askstring("Entrada", "Digite a primeira mensagem") 
Mensagem2 = simpledialog.askstring("Entrada", "Digite a segunda mensagem") 
Mensagem3 = simpledialog.askstring("Entrada", "Digite a terceira mensagem")
Mensagem4 = simpledialog.askstring("Entrada", "Digite a Última mensagem")
def main():
        root =  tk.Tk()
        root.withdraw()


for i in range(10):
    playsound.playsound('tuc.mp3')
    time.sleep(0.5)
    pag.hotkey("win", "d")
    pag.press("win") 
    pag.write("whatsapp", interval= 0.25)

    while procurar == "encontrado":
        try:
            imagem = pag.locateCenterOnScreen('whatsapp.png')
            if imagem:
                pag.click(imagem.x, imagem.y)
                break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    time.sleep(4)
    
    pag.write(Contato, interval= 0.25)
    pag.press("down")
    pag.press("enter")
    pag.write(Mensagem1, interval= 0.25)
    time.sleep(2)
    pag.press("enter")
    pag.write(Mensagem2, interval= 0.25)
    time.sleep(2)
    pag.press("enter")
    pag.write(Mensagem3, interval= 0.25)
    time.sleep(2)
    pag.press("enter")
    pag.write(Mensagem4, interval= 0.25)
    time.sleep(2)
    pag.press("enter")

    while procurar == "encontrado":
        try:
            fechar = pag.locateCenterOnScreen('fechar.png')
            if fechar:
                pag.click(fechar.x, fechar.y)
                break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    time.sleep(300)