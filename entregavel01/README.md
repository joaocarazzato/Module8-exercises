# Sistema de launch files para mapeamento e navegação
O objetivo dessa entrega desse repositório é disponibilizar o deploy de um sistema de mapeamento e de navegação no framework ros2 utilizando o sistema de simulação Gazebo.


https://github.com/joaocarazzato/Module8-exercises/assets/99187756/eb2d8b3a-6665-4a59-87ae-98cb4f836199


## Como usar?

Caso o pacote seja baixado diretamente do repositório, ela já estará buildado e pronto para execução, **para evitar erros, recomendamos adicionar o source do pacote ao seu interpretador de terminal preferido**(**.bashrc**, **.zshrc** e afins). Caso opte por não realizar isso, você terá que digitar o seguinte source em seu terminal dentro da pasta do pacote na hora de executar:
```
source install/local_setup.bash #Caso você tenha zsh, troque o bash por .zsh
```

Após isso, seu pacote estará pronto para uso! Com ele, você terá acesso a três nós e a três launch files:
- **Nós**
  - **teste** - Um "Hello World" do pacote
  - **set_initial_pose** - Seta a posição inicial do robô no RVIz partindo do gazebo
  - **go_to_pose** - Vai até pontos definidos no RVIz utilizando a representação do gazebo(necessário utilizar o nó **set_initial_pose** primeiramente)

**Para iniciar os nós, é necessário utilizar o seguinte comando:**
```
ros2 run ros2_entregavel01 <nome_do_nó>
```

- **Launch Files**
  - **mapping-launcher.launch.py** - Lança(abre) todo o sistema necessário para você mapear o mapa disponibilizado no gazebo utilizando a biblioteca do turtlebot3
  - **map-saver.launch.py** - Salva o mapa que foi mapeado e apresentado no RVIz para a pasta atual(do terminal)
  - **navigation-launcher.launch.py** - Lança(abre) todo o sistema necessário para você navegar no mapa criado a partir do mapeamento no RVIz com pontos já pré-definidos.
 
**Para iniciar os launch files, é necessário utilizar o seguinte comando:**
```
ros2 launch ros2_entregavel01 <nome_do_launch_file>
```

(Importante ressaltar que nenhum dos comandos citados vão funcionar caso você não tenha iniciado o pacote com o comando de source)

A ordem correta de utilização, é primeiro executar o launch file de mapeamento e usá-lo da seguinte forma:


https://github.com/joaocarazzato/Module8-exercises/assets/99187756/0547133a-f7b7-425b-9e35-d4c4972f06ea


Em seguida, é necessário executar o launch file para salvar o mapa, e então, é possível utilizar o launch file de navegação:


https://github.com/joaocarazzato/Module8-exercises/assets/99187756/5aa49cdc-99f8-420d-b8e9-81403f4e0a23


Assim, seu sistema deverá estar todo funcionando e já testado!
