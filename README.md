# Calibrador Magnético

Este repositório contém uma implementação em Python de um calibrador magnético. O código tem como objetivo ajustar os parâmetros de calibração de um magnetômetro a partir de um conjunto de dados brutos em formato CSV. O processo de calibração é dividido em etapas específicas, realizadas por diferentes funções.

## Principais Etapas do Código

Aqui estão as principais etapas do código:

- A função `offset(D, R)` recebe os dados brutos do magnetômetro (D) e o valor esperado do módulo do campo magnético no ambiente (R). Essa função ajusta os parâmetros de calibração e retorna um vetor contendo os valores de x0, y0, z0, a, b e c, que são os coeficientes de correção calculados.

- A função `show(vector, H)` recebe o vetor de coeficientes de correção e o valor do módulo do campo magnético no ambiente. Ela exibe os resultados da calibração, incluindo os valores dos coeficientes de correção e as equações de correção.

- A função `readcsv()` solicita ao usuário que selecione um arquivo CSV contendo os dados do magnetômetro. Em seguida, ela lê o arquivo e retorna o conteúdo como uma string.

- A função `dados(leitura)` recebe a string com os dados do magnetômetro e a converte em um vetor de dados chamado B. Essa função percorre a string, separa os valores de x, y e z para cada linha e os armazena no vetor B.

- A função `main()` é a função principal do programa. Ela chama as outras funções em sequência para executar o processo de calibração. Primeiro, lê o arquivo CSV com os dados do magnetômetro; em seguida, converte os dados em um formato adequado. Em seguida, exibe um gráfico tridimensional dos dados brutos do magnetômetro. Realiza a calibração usando a função `offset()` e exibe o gráfico novamente com os dados corrigidos. Por fim, chama a função `show()` para exibir os resultados da calibração.

O objetivo final do código é calibrar os dados do magnetômetro, ajustando os parâmetros de calibração para obter medições mais precisas e corrigidas do campo magnético.

## Utilização

Para utilizar este código, siga as etapas abaixo:

1. Certifique-se de ter o Python instalado em sua máquina.

2. Clone este repositório em sua máquina local usando o seguinte comando:

**git clone https://github.com/thiagohfsilva/calibrador_magnetico**

3. Navegue até o diretório clonado.

4. Execute o código Python:
   
**python Calibrador.py**

5. Siga as instruções fornecidas pelo programa para selecionar o arquivo CSV com os dados do magnetômetro.

6. Após a execução, serão exibidos os resultados da calibração e os gráficos dos dados brutos e corrigidos.

## Contribuição

Se você deseja contribuir para este repositório, sinta-se à vontade para enviar um pull request com suas melhorias. Toda contribuição é bem-vinda!



