# Versão 1.0.0 - Criação da automação
    Bugs conhecidos: o pyautogui mal interpreta a tecla "down" fazendo com que qualquer usuário com o numlock ativado acabe prejudicando o 
    andamento da automação, pois o pyautogui digita "2" ao invés de descer para a opção programada. Como contornar: desativar o numlock antes de iniciar a automação.

    Há um bug na tela de inicialização da automação, onde mesmo com um temporizador de 0,05 segundos a tela não sai automaticamente. Como contornar: Apenas mexa o mouse.

## Versão 1.0.5 - Pequenos ajustes
    Literalmente isso, pequenos ajustes em textos, nenhuma alteração na funcionalidade da automação em si.

## Versão 1.1 
     Retirada da biblioteca Pygame. Embora ter uma tela sinalizando o inicio na automação seja legal, a mesma mais atrapalha do que ajuda. Como o objetivo é ser uma automação rápida e leve para não atrapalhar a gameplay, é irônico ter uma tela consumindo recursos só pra avisar que o script está iniciando.

     Bugs Consertados: Bug da tela de apresentação da automação. Como a biblioteca Pygame foi retirada, não existe mais tela de apresentação, logo, não existe mais bug.

## Versão 1.1(hotfix) - Ajustes de emergência
    Retirada do arquivo .otf que fazia parte da tela de apresentação.
     
## Versão 1.5
    Migração da biblioteca pyautogui para a biblioteca pynput. Nada de errado com o pyautogui, é uma ótima biblioteca. Porém, percebi que ele tem um pouco de dificuldade em lidar com teclados que possuem o teclado númerico, sendo mais específico, ao usar ativar a função numlock do teclado, o pyautogui acaba pressionando 2 ao invés da seta para baixo. Esse bug estava atrapalhando o andamento da automação, tonando necessária a mudança de biblioteca.

    Como o pyautogui foi removido, a automação agora usa somente o teclado, não sendo necessário arquivos .png para guiar o mouse. Isso pode ser benéfico para sistemas linux, pois ao testar essa automação em uma máquina virtual com Bazzite OS, havia problemas do pyautogui com o wayland.

    Bugs consertados: Usuários que possuem e fazem uso do teclado númerico podem ficar despreocupados, a biblioteca pyntup reconhece o botão "down" como a seta para baixo, dessa forma, evitando conflitos com a função numlock do teclado.

## Versão 2.0 - Executável!
    Criação de um executável do projeto, dessa forma permitindo que o usuário final possa usar o programa caso o mesmo não posssua uma IDE em seu computador.

    Executável: Agora o executável possui um icone. É um icone temporário, o famoso placeholder, apenas usado para substituir o icone padrão do pyinstaller. Em versões futuras o programa terá um icone próprio.

    Temporizador: Foi adicionado um temporizador entre as mensagens, pois foi notado que havia um atraso crítico para a automação quando a mesma funcionava em um sistema com alta carga de cpu. Isso provavelmente também ajudará o andamento da automação em sistemas mais modestos.

    Arquivo .py renomeado de "base" para "recadoautomatico" seguido da versão do programa.

## Versão 2.5.5 - Correções
    Corrigido um bug crítico no executável onde o mesmo quebrava após inserir o nome do contato e as mensagens. Isso acontecia graças a uma dependencia do arquivo de audio que infelizmente não estava sendo empacotado junto ao código, fazendo com que ao baixar somente o arquivo .exe, o bug acontecesse. Após ajustes tanto no código quando na forma de empacotamento do mesmo, o programa está funcionando perfeitamente de forma standalone.

    Bugs conhecidos: O programa ficará em segundo plano durante a contagem de 5 minutos, onde a unica forma de interrompe-lo é apagando seu processo no gerenciador de tarefas. Não é exatamente um bug, porém isso pode causar um certo incomodo caso um usuario mais leigo não precise mais do programa e não saiba como desativa-lo por este método. 

## Mudanças futuras / Planejadas
    Adicionar uma parada de emergência caso seja necessário interromper as ativadades do programa. Atualmente a unica forma de interrompe-lo é encerrando seu processo no gerenciador de tarefas.

    Criação de um icone próprio, atualmente o programa está usuando um incone livre de direitos autorais como placeholder.