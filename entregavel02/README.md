# Chatbot utilizando expressões regulares(regex)
O objetivo desse repositório é apresentar a criação de um chatbot utilizando expressões regulares para se movimentar até pontos específicos, mas que pode ser adaptado para realizar outras funções de acordo com a necessidade do usuário.

https://github.com/joaocarazzato/Module8-exercises/assets/99187756/730cfaf5-2d08-474e-bb09-35783fd041c9

# Como usar?

Caso o pacote seja baixado diretamente do repositório, ela já estará buildado e pronto para execução, **para evitar erros, recomendamos adicionar o source do pacote ao seu interpretador de terminal preferido**(**.bashrc**, **.zshrc** e afins). Caso opte por não realizar isso, você terá que digitar o seguinte source em seu terminal dentro da pasta do pacote na hora de executar:
```
source install/local_setup.bash #Caso você tenha zsh, troque o bash por .zsh
```

Após isso, seu pacote estará pronto para uso! Com ele, você terá acesso a um nó chamado **rule-based**:

**Para iniciar o nó, é necessário utilizar o seguinte comando:**
```
ros2 run ros2_entregavel2 rule-based
```

(Importante ressaltar que o comando citado não vai funcionar caso você não tenha iniciado o pacote com o comando de source)

Após isso, é só iniciar o nó, e dizer como quer ir ao ponto. No momento, temos três pontos e algumas formas de dizer para o chat bot ir até o ponto:

- **Pontos:**
  - **ponto 1** - x = 2.0; y = 2.0; z = 0.0
  - **ponto 2** - x = 2.0; y = 0.0; z = 0.0
  - **ponto 3** - x = 0.0; y = 2.0; z = 0.0

- **Como dizer:**
  - **"Locomova-se até o [ponto]"**
  - **"Se mova até o [ponto]"**
  - **"Ande até o [ponto]"**
  - **"Vá ao [ponto]"**
 
Então, ao digitar por exemplo: **"Locomova-se até o ponto 1"**, o chatbot entenderá essa ação e se moverá ao ponto 1, como demonstrado no vídeo.
