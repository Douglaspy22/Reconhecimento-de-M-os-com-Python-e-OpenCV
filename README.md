🖐️ Projeto de Reconhecimento de Mãos com Contagem e Identificação de Dedos Usando Python, OpenCV e MediaPipe
Este projeto tem como objetivo desenvolver uma solução interativa de visão computacional, capaz de reconhecer mãos, detectar quais dedos estão levantados e identificá-los individualmente em tempo real, utilizando apenas uma webcam comum. A aplicação combina a biblioteca MediaPipe, da Google, com a poderosa manipulação de vídeo do OpenCV, em Python.

🎯 Objetivo da Solução
O sistema foi projetado para:

Detectar mãos em tempo real por meio da webcam.

Identificar os cinco dedos da mão separadamente: Polegar, Indicador, Médio, Anelar e Mínimo.

Determinar automaticamente quais dedos estão estendidos.

Exibir a quantidade total de dedos levantados.

Criar uma interface simples com quadrados numerados que podem ser clicados para mostrar qual dedo corresponde àquela região da mão.

Essa abordagem pode ser usada em interfaces interativas, aplicações educativas, sistemas de controle por gestos ou até como base para projetos de acessibilidade.

🧠 Como Funciona
A solução é dividida em três etapas principais:

1. Captura e Processamento da Imagem
A webcam é usada para capturar imagens em tempo real.

Cada quadro (frame) é convertido para o formato RGB, pois o MediaPipe trabalha com essa codificação.

2. Detecção da Mão com MediaPipe
O MediaPipe Hands detecta até uma mão e retorna 21 pontos de referência (landmarks), correspondentes às articulações da mão.

Esses pontos incluem a ponta de cada dedo, suas articulações intermediárias, a base dos dedos e o punho.

3. Contagem e Identificação dos Dedos
O sistema analisa a posição relativa dos pontos da ponta dos dedos e suas articulações para determinar se um dedo está levantado ou dobrado.

Para os dedos indicadores ao mínimo, é feita a comparação entre o eixo Y dos pontos.

Para o polegar, a comparação é no eixo X, devido à sua orientação lateral.

Os resultados são exibidos na tela com texto e marcadores visuais.

🖼️ Interface Interativa
A imagem da câmera exibe a mão detectada com suas conexões desenhadas.

São adicionados cinco quadrados numerados de 0 a 4 representando cada dedo:

0 = Polegar

1 = Indicador

2 = Médio

3 = Anelar

4 = Mínimo

Ao clicar com o mouse sobre qualquer quadrado, o nome correspondente do dedo será exibido na tela.

📦 Estrutura do Código
O código principal contém:

Inicialização do MediaPipe e OpenCV.

Função contar_dedos() que realiza a contagem de dedos levantados.

Laço principal que:

Lê os frames da webcam.

Detecta a mão e desenha os landmarks.

Conta os dedos e exibe a quantidade.

Desenha os quadradinhos de interação.

Detecta o clique do usuário e mostra o nome do dedo clicado.

🧰 Tecnologias Utilizadas
Python 3.8+

OpenCV – Para captura de vídeo e interface gráfica.

MediaPipe – Para detecção precisa dos pontos da mão.

NumPy (se desejar manipulações vetoriais adicionais).

💡 Aplicações Possíveis
Controle de sistemas por gestos manuais.

Aulas interativas de anatomia ou linguagem de sinais.

Ferramentas de acessibilidade para pessoas com deficiência motora.

Desenvolvimento de jogos ou interfaces para realidade aumentada.

Automatização de comandos por gestos.

▶️ Como Executar
1. Instale as dependências:
bash
Copiar
Editar
pip install opencv-python mediapipe
2. Execute o script:
bash
Copiar
Editar
python reconhecimento_maos.py
3. Use o mouse para interagir com os quadradinhos numerados na tela.
📷 Exemplo Visual
Você pode adicionar um gif ou imagem aqui demonstrando a detecção dos dedos e a interação com os quadradinhos.

📝 Considerações Finais
Esta solução é uma introdução prática ao uso de visão computacional em tempo real, usando bibliotecas modernas e de alto desempenho. Por ser simples, ela pode ser expandida facilmente para incluir múltiplas mãos, reconhecer gestos específicos, controlar sistemas ou até ser integrada a interfaces gráficas mais avançadas.

