# NOVIDADES 💫

(em breve)
    


# RPG-TEXTO-PYTHON🎮
Esse é um RPG de texto feito em Python, ele não tem visual nem sprites, criei esse projeto com o objetivo de melhorar minha lógica de programação e aprender programação orientada a objeto.

<img width="720" height="480" alt="20250607_0025_Programador Mágico em Ação_remix_01jx46nz02eq8s040y2hz9svmz" src="https://github.com/user-attachments/assets/607a3e7f-fca0-40f8-93b8-4a12975dc48a" />


🧩 Funcionalidades

- Sistema de combate com dados 🎲
- Inventário 🎒
- Multiplayer local 👥
- Eventos aleatórios (em breve)
- Geração de equipamentos ⚔️
- Loja dinâmica 🪙
- NPC (em breve)

## 🎮 Como funciona o jogo
o Jogo é de PVP de turnos, Multijogador local , permitindo que vários jogadores joguem na mesma máquina, ou o jogador principal compartilhar sua tela em qualquer software de comunicação (discord, whatsApp,skype e etc) pra jogarem juntos

<img width="690" height="215" alt="Captura de tela 2026-05-15 140015" src="https://github.com/user-attachments/assets/6b0b825d-8427-475f-9169-d81d5272dc5a" />

ao entrar o jogo a primeira coisa que você faz é informar quantos jogadores terão na partida, o nome e o hp deles.

<img width="1505" height="841" alt="image" src="https://github.com/user-attachments/assets/32909986-8ce5-4b3b-9f71-79a83c75d3b6" />






essa é a tela principal, onde o jogador poderá ATACAR, ver a LOJA ou ver o INVENTÁRIO

## ⚔️COMBATE⚔️

No combate o jogador vai jogar o dado de 20 lados (dado de agilidade), se cair um número maior que 10 ele ataca, 
pra atacar ele vai jogar mais um dado, de 10 lados (dado de ataque), que vai ser o dano do jogador

### Dado de agilidade🎲💨
o dado de agilidade serve para ver se o jogador vai acertar ou errar o golpe, o bônus de agilidade pode ajudar a acertar os golpes, se o jogador tirar 20 no dado, o dano será dobrado!. pra cada 10 de bônus de agilidade aumenta 1 no dado.

### dado de ataque 🎲⚔️
Define o dano do jogador, somando bônus e equipamentos.
## 🪙 Loja

<img width="1565" height="811" alt="image" src="https://github.com/user-attachments/assets/9b82a850-57d9-4d4a-a44f-34dc26c7380f" />


de começo a loja começa vazia, apenas com 3 opções :
- Comprar slot
- atualizar loja
- sair

  cada rodada tem uma chance de 33% da loja atualizar, ela começa com apenas 3 slots (3 itens).
  a loja contém o estoque compartilhado entre os jogadores, então se um jogador comprar algum item, ele vai sumir pra todos.

  A loja é totalmente dinâmica, os itens vão ficando melhores conforme os turnos vão passando :

  ### loja no turno 1 :
 <img width="1470" height="846" alt="image" src="https://github.com/user-attachments/assets/d993f26f-a027-4ac5-b42c-97a8ac33cdbf" />


  
  ### Loja no turno 51 :
 <img width="1469" height="853" alt="image" src="https://github.com/user-attachments/assets/b2733d41-aaa8-41c2-8819-59f93a509631" />


veja mais detalhes da programação da loja nesse [vídeo](https://youtu.be/nK_9r1_OSCA)


## sistema de geração de equipamentos ⚔️

o jogo escolhe um nome aleatório em uma lista de nomes, e uma raridade aleatória com peso (é mais difícil pegar equipamentos mais raros)

o jogo multiplica um certo valor pelo turno, dependendo da raridade do equipamento, esse valor será seu dano máximo, após isso ele vai escolher um número aleatório entre o dano mínimo e o dano máximo (veja mais detalhes do código sobre criação de equipamentos aleatórios nesse [vídeo](https://youtu.be/IsAhmIPsct0)

<img width="720" height="480" alt="Captura de tela 2026-08-01 210358" src="https://github.com/user-attachments/assets/b068338a-6279-4dfe-88e4-edd32bbe8737" />


<img width="569" height="103" alt="image" src="https://github.com/user-attachments/assets/d30a6849-7342-4671-aacb-727d553fd72e" />

o preço do equipamento será 70% do seu valor.



## 🎒 Inventário
<img width="1064" height="706" alt="image" src="https://github.com/user-attachments/assets/fd42ed3f-e851-4a40-b9ca-85f7360c63d1" />


O inventário mostra todos os itens do jogador e permite equipá-los ou desequipa-los.

## ⬆️ Sistema de Upgrades
O sistema de upgrades permite que os jogadores evoluam seus personagens ao longo da partida, tornando-os progressivamente mais fortes.

Ao acumular experiência (XP) suficiente, o jogador sobe de nível e recebe 3 aprimoramentos aleatórios. Cada upgrade pode melhorar diferentes atributos do personagem, permitindo que cada partida tenha combinações e possibilidades diferentes.

Entre os atributos que podem receber melhorias estão:
- ⚔️ Dano no dado: aumenta o valor máximo do dado utilizado no cálculo do ataque.
- 💥 Dano bônus: aumenta o dano adicional causado pelo jogador.
- 💰 Bônus de moedas: aumenta o bônus relacionado à obtenção de moedas.
- 🏃 Agilidade: melhora os atributos relacionados à agilidade do personagem.
- 🍀 Sorte: aumenta a sorte do jogador, respeitando o limite máximo de 1.6.
- 🎯 Crítico: aumenta o multiplicador de dano dos ataques críticos.
- 🔥 Chance de crítico: aumenta a possibilidade de conseguir um ataque crítico.

  <img width="635" height="214" alt="image" src="https://github.com/user-attachments/assets/e497d96b-4149-4786-8f4f-df72c2b3c111" />
  


  <img width="453" height="393" alt="image" src="https://github.com/user-attachments/assets/c6400d31-8a85-4225-8738-507cac7b0893" />


##🍀 Atributo: Sorte
A sorte é um atributo que influencia os acontecimentos aleatórios durante a partida. Ela pode favorecer o jogador em determinadas situações, tornando os resultados menos previsíveis e adicionando um elemento de surpresa ao combate.

O jogador pode aumentar seu atributo de sorte por meio dos aprimoramentos recebidos ao subir de nível. Entretanto, esse atributo possui um limite máximo de 1.6, evitando que seu crescimento seja ilimitado.

## 🛡️ Armadura
A armadura é um equipamento defensivo que ajuda o jogador a reduzir os danos recebidos durante os combates.

Diferentemente de um equipamento com durabilidade infinita, a armadura possui um sistema de resistência: ao absorver dano, sua durabilidade é consumida. Quando ela se desgasta completamente, deixa de oferecer proteção.

Isso faz com que a armadura seja um recurso que precisa ser administrado durante a partida. Embora ofereça proteção contra ataques, o jogador precisa considerar sua durabilidade e estar preparado para quando ela quebrar.

A sorte adiciona mais uma camada estratégica à partida: além de investir em atributos ofensivos e defensivos, o jogador também pode apostar em melhorar suas chances nos acontecimentos aleatórios.

# 🕹️ como posso jogar o jogo? 

<img width="1855" height="887" alt="image" src="https://github.com/user-attachments/assets/6477111c-7a16-4446-bc54-82278f8b6750" />



Acesse a página no Itch.io, para baixar o jogo : https://ola-python.itch.io/terminal-pvp


# 🤝 ajude na programação

Contribuições são bem-vindas!

- Faça um fork
- Crie uma branch
- Faça alterações
- Envie um Pull Request

Esse é um projeto feito por um Estudante de programação para outros estudantes ou amantes de programação, então eu te incentivo a baixar o projeto, ver como tudo foi feito, editar o código, fazer testes, crie novas features do seu jeito, você pode até postar no seu github, eu adoraria ver os seus projetos :)

<img width="240" height="240" alt="20260305_1155_Image Generation_remix_01kjz7wh0dft5vsz8pzrwefmyz" src="https://github.com/user-attachments/assets/7bb26727-5383-4634-bcad-ddd379822129" />





