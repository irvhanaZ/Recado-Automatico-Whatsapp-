# Versão 1.0.0 - Criação da automação
    Bugs conhecidos: o pyautogui mal interpreta a tecla "down" fazendo com que qualquer usuário com o numlock ativado acabe prejudicando o 
    andamento da automação, pois o pyautogui digita "2" ao invés de descer para a opção programada. Como contornar: desativar o numlock antes de iniciar a automação.

    Há um bug na tela de inicialização da automação, onde mesmo com um temporizador de 0,05 segundos a tela não sai automaticamente. Como contornar: Apenas mexa o mouse.

## Versão 1.0.5 - Pequenos ajustes
    Literalmente isso, pequenos ajustes em textos, nenhuma alteração na funcionalidade da automação em si.

## Versão 1.1 
     Retirada da biblioteca Pygame. Embora ter uma tela sinalizando o inicio na automação, a mesma mais atrapalha do que ajuda. Como o objetivo é ser uma automação rápida e leve para não atrapalhar a gameplay, é irônico ter uma tela consumindo recursos só pra avisar que o script está trabalhando.

     Bugs Consertados: Bug da tela de apresentação da automação. Como a biblioteca Pygame foi retirada, não existe mais tela de apresentação, logo, não existe mais bug.
     
## Mudanças futuras: 
    Migração do Pyautogui para o Pynpt
