# Chatbot com LLM
O repositório tem por objetivo apresentar uma solução de um Chatbot utilizando LLM, mais precisamente o modelo Dolphin disponibilizado no projeto open-source **Ollama**. O chatbot disponibilizado aquui, por sua vez, responde somente sobre medidas de segurança em ambientes industriais, qualquer pergunta fora disso não é respondida pelo mesmo.


https://github.com/joaocarazzato/Module8-exercises/assets/99187756/29cf24fa-c766-4526-b8af-0babe71881f3


# Como usar?

O primeiro passo para poder utilizar o chatbot, é ter o Ollama e o Python baixados em sua máquina, caso não tenha, é possível seguir o tutorial de seus respectivos sites. Após isso, é possível iniciar a instalação de suas dependências, nesse caso, o modelo e as bibliotecas Python:

- Para instalar o modelo do chatbot em sua máquina é preciso digitar no terminal dentro da pasta do projeto:

```
ollama create security-expert -f Modelfile
```

Onde o comando indica o nome do modelo(security-expert) que iremos criar e o nome do arquivo de modelo, no nosso caso, **Modelfile**.


- Para instalar as bibliotecas Python é preciso digitar no terminal dentro da pasta do projeto:
```
pip install -r requirements.txt
```

Após isso, você terá todas as dependências necessárias baixadas e prontas para o uso em seu computador.

Para executar o chatbot e usá-lo, é necessário abrir o terminal na pasta do projeto e digitar o seguinte:
```
python3 Chatbot.py
```

E então seu chatbot estará disponível no ip `http://localhost:7860` e pronto para uso como apresentado no vídeo **(exemplo de uso)**.

Caso queira modificar o Chatbot para seu próprio uso, é necessário alterar o contexto definido no arquivo `Modelfile` e também alterar a linha de `model` localizada no script python `Chatbot.py` na linha 11.
