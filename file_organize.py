import os
import shutil
import sys

def remove_empty_dirs(src_folder):
    for root, dirs, files in os.walk(src_folder, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

def ext_organize(src_folder):
    extensions_paths = {
        '.js': 'scripts',
        '.css': 'styles',
        '.pdf': 'docs',
        '.ttf': 'fonts'
    }
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp']
    images_dir = os.path.join(src_folder, 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    html_dir = os.path.join(src_folder, 'html')
    os.makedirs(html_dir, exist_ok=True)

    ignore_files_dirs = {'readme.md', '.gitignore', '.git'}  # Ignored directories and files

    for root, dirs, files in os.walk(src_folder, topdown=True):
        files = [f for f in files if f.lower() not in ignore_files_dirs]
        dirs[:] = [d for d in dirs if d not in ignore_files_dirs]

        for file in files:
            if file.lower() == 'index.html':
                continue
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)

            if file.endswith('.html'):
                target_path = html_dir
            elif ext in image_extensions:
                target_path = images_dir
            elif ext in extensions_paths:
                target_path = os.path.join(src_folder, extensions_paths[ext])
                os.makedirs(target_path, exist_ok=True)
            else:
                continue

            shutil.move(file_path, os.path.join(target_path, file))

    remove_empty_dirs(src_folder)
    print("Files organized by extension.")

def section_organize(src_folder):
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp']
    images_dir = os.path.join(src_folder, 'images')
    os.makedirs(images_dir, exist_ok=True)

    ignore_files_dirs = {'readme.md', '.gitignore', '.git', 'index.html'}  # Ignored directories and files

    for root, dirs, files in os.walk(src_folder, topdown=True):
        files = [f for f in files if f.lower() not in ignore_files_dirs]
        dirs[:] = [d for d in dirs if d not in ignore_files_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)

            if ext in image_extensions:
                target_path = images_dir
            elif ext == '.pdf':
                target_path = os.path.join(src_folder, 'docs')
                os.makedirs(target_path, exist_ok=True)
            elif ext == '.ttf':
                target_path = os.path.join(src_folder, 'fonts')
                os.makedirs(target_path, exist_ok=True)
            else:
                target_path = os.path.join(src_folder, file.rsplit('.', 1)[0])
                os.makedirs(target_path, exist_ok=True)

            shutil.move(file_path, os.path.join(target_path, file))

    remove_empty_dirs(src_folder)
    print("Files organized by section.")

def menu():
    if len(sys.argv) != 2:
        print("Use: python file_organize.py <source_directory>")
        sys.exit(1)
    
    source_directory = sys.argv[1]
    print("Select an organization method:")
    print(" 1.By extension")
    print(" 2.By function")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        ext_organize(source_directory)
    elif choice == '2':
        section_organize(source_directory)
    else:
        print("Invalid choice. Please enter 1 or 2.")

menu()
