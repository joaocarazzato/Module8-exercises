# Classificação MNIST através de uma rede neural convolucional
O objetivo desse repositório é a criação de uma rede neural convolucional para classificar o dataset MNIST de classificação de números de 0 a 9.

[video]

## Como funciona?
O notebook é composto de 3 células de código, a primeira sendo carregando o dataset e o dividindo nas variáveis necessárias, o segundo montando as camadas da rede e compilando o modelo da rede neural convolucional, e a terceira treinando o modelo.

Em nossa rede neural, possuímos 7 camadas, sendo duas de convolução 2D, duas de Pooling máximo em 2D, uma de achatamento(mudando as dimensões da imagem) e duas camadas densas(que se conectam todos os nós).

## Como executar?
Para executar o notebook é muito simples, primeiro é necessário baixar as dependências caso queira rodar local, ou importar o notebook ao Google Collab e executar o código. É recomendado o Google Collab caso a potência do computador a ser usado seja baixa.
