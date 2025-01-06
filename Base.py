import playsound
import pyautogui as pag
import time
import pygame
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

    pygame.init()
    screen = pygame.display.set_mode((1366, 768), pygame.NOFRAME)
    pygame.display.set_caption("Iniciando Script...")
    font = pygame.font.Font("Dash-Horizon-Demo.otf", 74)
    text_color = (255, 255, 255)
    background_color = (0,0,0)

    def display_text_gradually(screen, text, font, color, position, delay= 0.05):
        for i in range(1, len(text) + 1):
            screen.fill(background_color)
            partial_text = text[:i]
            text_surface = font.render(partial_text, True, color)
            text_rect = text_surface.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))
            screen.blit(text_surface, text_rect.topleft)
            pygame.display.flip()
            time.sleep(0.05)

    text = "iniciando Script. Mexa o mouse para continuar"
    screen_size = screen.get_size()

    correndo = True
    exibiu_texto = False
    start_time = None
    

    while correndo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correndo = False
            
            if not exibiu_texto:
                display_text_gradually(screen, text, font, text_color, screen_size)
                exibiu_texto = True
                start_time = time.time()

            if exibiu_texto and time.time() - start_time > 1:
                correndo = False

    pygame.quit()

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