
# Projeto: Detecção de Pikachu com YOLO v11

![Imagem Externa](https://raw.githubusercontent.com/pedroveronez2/YOLO-v11-Pikachu/refs/heads/main/val_batch0_labels.jpg)


## Descrição do Projeto
Este é um projeto de aprendizado de máquina focado na detecção de Pikachu em imagens utilizando o modelo YOLO (You Only Look Once) versão 11 e a linguagem de programação Python. O objetivo principal foi prática de habilidades em análise de dados e aprendizado de máquina, realizando testes para compreender o impacto de diferentes distribuições de dados e visualizando o desempenho do modelo. Link do yolo 11: https://github.com/ultralytics/ultralytics

## Objetivos do Projeto
- **Treinar o modelo YOLO v11 para detectar Pikachu em imagens.**
- **Analisar a melhor distribuição dos dados** para o treinamento do modelo.
- **Visualizar e avaliar o desempenho do modelo** com base em diferentes métricas.
- **Aprender sobre o impacto de infraestrutura computacional** no treinamento de modelos de IA.

## Estrutura do Projeto
### 1. **Distribuição de Dados**
Foram realizados experimentos com diferentes proporções de dados de treino, validação e teste, como:
- **70/20/10:** 70% para treino, 20% para validação e 10% para teste.
- **80/10/10:** 80% para treino, 10% para validação e 10% para teste.

Foi dada atenção especial à **variedade e balanceamento** dos dados, incluindo diferentes condições de iluminação, tamanhos e posições do Pikachu.

### 2. **Anotações**
As imagens foram anotadas manualmente utilizando a ferramenta [LabelImg](https://github.com/heartexlabs/labelImg). As anotações foram salvas no formato compatível com o YOLO (“.bounding boxes” em arquivos `.txt`).

### 3. **Treinamento do Modelo**
O treinamento foi realizado utilizando a biblioteca **YOLO v11** com Python.

- **Configurações:**
  - Taxa de aprendizado ajustada.
  - Redimensionamento das imagens para 416x416.
  - Aumento de dados (Data Augmentation) aplicado para melhorar a generalização do modelo.
- **Infraestrutura:** O treinamento foi realizado em um computador pessoal, com tempo aproximado de **10 horas para 100 épocas**.

### 4. **Avaliação do Modelo**
O modelo foi avaliado utilizando:
- **Métricas de desempenho:**
  - Precisão.
  - Recall.
  - F1-Score.
  - AP (Average Precision).
- **Visualização de resultados:**
  - Gráficos da perda de treino e validação ao longo das épocas.
  - Imagens com as predições do modelo destacando o Pikachu detectado.

### 5. **Conclusão**
O modelo YOLO v11 demonstrou ser **muito eficaz na detecção de Pikachu**, desde que os dados sejam anotados corretamente e haja uma boa distribuição entre treino, validação e teste. No entanto, um dos maiores desafios foi a necessidade de **infraestrutura computacional robusta**:
- O treinamento levou cerca de **10 horas para 100 épocas** em um computador pessoal.
- Para acelerar o processo, é recomendado o uso de GPUs de alto desempenho.

## Tecnologias Utilizadas
- **Linguagem:** Python.
- **Modelo:** YOLO v11.
- **Ferramentas:**
  - LabelImg para anotação de dados.
  - Bibliotecas Python para treinamento e análise:
    - PyTorch/TensorFlow (dependendo da implementação do YOLO).
    - Matplotlib para visualização de gráficos.
    - NumPy e Pandas para análise de dados.

## Como Reproduzir o Projeto
1. **Preparar os Dados:**
   - Coletar imagens contendo Pikachu e imagens negativas (sem Pikachu).
   - Anotar as imagens utilizando o LabelImg.

2. **Configurar o Ambiente:**
   - Instalar as dependências necessárias:
     ```bash
     pip install -r requirements.txt
     ```

3. **Treinar o Modelo:**
   - Executar o script de treinamento com as configurações desejadas.

4. **Avaliar o Modelo:**
   - Rodar os scripts de avaliação e visualizar os resultados.

## Licença
Este projeto é de uso livre para fins educacionais e pessoais.
