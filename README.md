## 💭💭Como surgiu o messageZ?💭💭
As vezes enquanto trabalho eu fico preocupado com a minha esposa e pra piorar muitas das vezes ela usa fones de ouvido, fazendo com que eu tivesse que ir até ela para verificar se estava tudo bem.
Até que pensei comigo mesmo. Porquê não criar uma forma automática de enviar recados via whatsapp ou telegram a cada 5 minutos para ver se ela precisa de alguma coisa? Bom, isso era só o começo.
A ideia foi crescendo e amadurecendo e aí novamente eu pensei:

"E se eu fizesse com que essa automação funcionasse para qualquer contato, enviando qualquer mensagem?"

Então foi aí que nasceu o "messageZ".

## 🤔🤔 Como funciona? 🤔🤔
 Utlizando o pynput, tkinter e entre outros módulos, o script gera 6 prompts:

Primeiro Prompt - Aqui o usuario deve digitar o nome do app que deseja usar: Atualmente suportados: Whatsapp ou Telegram:

![prompt 1](https://github.com/user-attachments/assets/c5a3e5a7-6660-4086-b6fb-617c3201c9b8)


Segundo Prompt - Nesse o usuario deve fornecer o nome do contato:

![prompt 2](https://github.com/user-attachments/assets/2e5b3294-a6df-41af-b3f8-17a26d604b50)


Terceiro Prompt - Agora o usuario deve digitar a primeira mensagem:

![prompt 3](https://github.com/user-attachments/assets/cea5de85-442d-44ff-902a-d80737ca1fc8)

Quarto Prompt - Agora a segunda:

![prompt 4](https://github.com/user-attachments/assets/306c14a6-fa2c-4001-a378-18f5caaaf450)

Quinto Prompt - A terceira:

![prompt 5](https://github.com/user-attachments/assets/06391abe-4cae-4673-94e8-09daf0889869)


Sexto Prompt - E por fim, a última mensagem:

![prompt 6](https://github.com/user-attachments/assets/e8996605-707c-4f3e-97fd-868e2365ad74)

Após esses 6 prompts, o script irá começar de fato, enviando as mensagens para o contato escolhido anteriormente. Não é necessário repetir o processo,
pois como dito antes, o processo ocorre a cada 5 minutos.

## ⚠️ Atenção ⚠️

É necessário estar logado no app que deseja usar, caso contrário a automação não funcionará.

Confira as notas de versão no arquivo changelog.md para saber as mudanças e o que está por vir no messageZ!!

Então, é isso. Até a próxima!