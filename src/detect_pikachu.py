from ultralytics import YOLO


my_model = YOLO('caminho/do/modelo_treinado')

# Perform object detection on an image
results = my_model("caminho/img.png")
results[0].show()