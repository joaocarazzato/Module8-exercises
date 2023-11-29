# Criação de um perceptron para portas lógicas
O objetivo desse repositório é demonstrar a criação de um perceptron em Python, responsável por identificar e ser treinado para encontrar as portas lógicas AND, OR, NAND e XOR.


https://github.com/joaocarazzato/Module8-exercises/assets/99187756/5f1a3a44-2a4b-42b5-95d2-e37c5ad86814


## Como funciona?
O perceptron funciona através da criação de uma classe e 3 funções essenciais além de seu iniciador:
* activation_function - Responsável por determinar a resposta do que foi predito
* predict - Predição do perceptron sobre um input
* train - Uma função de treinamento do perceptron para encontrar os pesos e o bias funcional para cada porta.

Após isso, temos um dicionário com os dados de cada porta lógica que queremos encontrar, e então passamos por um for que realiza as ações necessárias para cada porta, nesse caso, sua instância da classe, seu treinamento e as respostas do perceptron treinado para cada classe. É possível adicionar novas portas através da adição da mesma no dicionário exposto no código.

**É importante ressaltar que apesar da porta XOR estar implementada, não é possível encontrar os valores corretos de peso e bias para seu funcionamento. O principal motivo para que isso aconteça, é que só usamos um perceptron, sendo usado para problemas lineares, enquanto o XOR, é um problema não linear. Para funcionar, precisariamos criar um segundo perceptron(nesse caso, uma camada oculta entre o input e o resultado) e trocar a função linear por uma função sigmoide.**
