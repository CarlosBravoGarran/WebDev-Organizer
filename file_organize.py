import os
import shutil
import sys

def eliminar_directorios_vacios(src_folder):
    # Recorre todos los directorios y subdirectorios
    for root, dirs, files in os.walk(src_folder, topdown=False):  # topdown=False para empezar por los más profundos
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):  # Comprueba si el directorio está vacío
                os.rmdir(dir_path)  # Elimina directorios vacíos
                print(f"Eliminado directorio vacío: {dir_path}")

def organizar_por_extension(src_folder):
    extensions_paths = {
        '.js': 'scripts',
        '.css': 'styles',
        '.pdf': 'docs'
    }
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']
    images_dir = os.path.join(src_folder, 'images')  # Directorio de imágenes en la carpeta raíz
    os.makedirs(images_dir, exist_ok=True)
    
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file == 'index.html':
                continue  # No mover el index.html
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            
            if ext in image_extensions:
                target_path = images_dir
            elif ext in extensions_paths:
                target_path = os.path.join(src_folder, extensions_paths[ext])
                os.makedirs(target_path, exist_ok=True)
            else:
                continue

            shutil.move(file_path, os.path.join(target_path, file))

    eliminar_directorios_vacios(src_folder)
    print("Archivos organizados por extensión incluyendo imágenes en 'images'.")

def organizar_por_funcion(src_folder):
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp']
    images_dir = os.path.join(src_folder, 'images')  # Directorio de imágenes en la carpeta raíz
    os.makedirs(images_dir, exist_ok=True)
    
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file == 'index.html':
                continue  # No mover el index.html
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            
            if ext in image_extensions:
                target_path = images_dir
            elif ext == '.pdf':
                target_path = os.path.join(src_folder, 'docs')
                os.makedirs(target_path, exist_ok=True)
            else:
                target_path = os.path.join(src_folder, file.rsplit('.', 1)[0])  # Crea directorios basados en el nombre sin la extensión
                os.makedirs(target_path, exist_ok=True)

            shutil.move(file_path, os.path.join(target_path, file))

    eliminar_directorios_vacios(src_folder)
    print("Archivos organizados por función incluyendo imágenes en 'images'.")

def menu():
    if len(sys.argv) != 2:
        print("Uso: python file_organize.py <directorio>")
        sys.exit(1)
    
    source_directory = sys.argv[1]
    print("Selecciona el método de organización de archivos:")
    print("1. Organizar por extensión")
    print("2. Organizar por función")
    choice = input("Introduce tu elección (1 o 2): ")
    
    if choice == '1':
        organizar_por_extension(source_directory)
    elif choice == '2':
        organizar_por_funcion(source_directory)
    else:
        print("Opción no válida. Por favor, introduce 1 o 2.")

# Ejecutar el menú
menu()
