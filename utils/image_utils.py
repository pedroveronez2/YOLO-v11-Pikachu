import os
from PIL import Image

def resize_images(input_dir, output_dir, size=(128, 128)):
    # Cria o diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Percorre todos os arquivos nos subdiretórios do diretório de entrada
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # Adicione mais extensões se necessário
                img_path = os.path.join(root, filename)
                
                # Cria o diretório de saída correspondente para a imagem, se não existir
                relative_dir = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_dir)
                os.makedirs(output_subdir, exist_ok=True)

                try:
                    # Abre a imagem
                    with Image.open(img_path) as img:
                        # Redimensiona a imagem
                        img_resized = img.resize(size)
                        # Salva a imagem redimensionada no diretório de saída
                        img_resized.save(os.path.join(output_subdir, filename))
                        print(f'Resize: {filename} -> {output_subdir}/{filename}')
                except Exception as e:
                    print(f'Error processing {filename}: {e}')

if __name__ == "__main__":
    # Defina os diretórios de entrada e saída
    input_directory = r'./data'  # Diretório de entrada
    output_directory = r'./data/processed'  # Diretório de saída
    
    resize_images(input_directory, output_directory)
    print('Data resized successfully')
