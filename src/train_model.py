from ultralytics import YOLO

# Carregar um modelo pré-treinado ou seu modelo específico
model = YOLO("yolo11n.pt") # Use um modelo disponível ou seu modelo específico

# Treinar o modelo
train_results = model.train(
    data='caminho/do/file.yaml',  # Caminho para o arquivo de configuração YAML
    epochs=5,  # Número de épocas para o treinamento
    imgsz=640,  # Tamanho das imagens de entrada
    device="cpu",  # Definir o dispositivo para treinamento (cpu ou gpu)
)

# Avaliar o desempenho do modelo no conjunto de validação
metrics = model.val()

# Exportar o modelo para o formato ONNX
path = model.export(format="onnx")  # Caminho para o modelo exportado
print(f"Modelo exportado para o formato ONNX em: {path}")
