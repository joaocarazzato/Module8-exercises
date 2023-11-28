# Chatbot com LLM usufruindo de contextos externos
O objetivo desse repositório, é demonstrar como é possível a realização de webscrapping utilizando a biblioteca Langchain e como é possível passar o contexto recebido para uso no chatbot através de um banco de dados vetorizado.


https://github.com/joaocarazzato/Module8-exercises/assets/99187756/0a304a52-6398-4c50-b672-0a7f0a0d1e10


## Como funciona?

O script primeiro carrega uma URL de forma assíncrona que depois de carregado extrai o conteúdo da página a partir da tag `main`, e então, no caso do site escolhido, captura o conteúdo importante dessa página na variável `docs_text` e transforma seu conteúdo em um banco de dados vetorizado, passando o mesmo para um prompt de template e em seguida respondendo a pergunta a partir desse contexto.

## Como usar?
Para esse tutorial, consideramos que o usuário já possua o projeto Ollama instalado em seu pc, caso não tenha, é possível ir para seu instalador [clicando aqui](https://ollama.ai/download).

Para instalar as dependências do projeto, é necessário instalar o langchain e o modelo utilizado do Ollama com os seguintes comandos:
```
ollama run mistral
```
(Após isso, o ollama pode ser encerrado no terminal.)

```
pip install langchain
```

Com ambas dependências já baixadas, é só executar o código utilizando `python3 webscrap.py`, e caso queira, alterar a pergunta diretamente no código.

*(Pretendo adicionar a opção de input de pergunta mais tarde caso eu lembre).*
