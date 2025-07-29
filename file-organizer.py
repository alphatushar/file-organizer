import os
import shutil

# Change this to the folder you want to organize
path = '/Users/yourusername/Downloads'

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv'],
    'Audio': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz']
}

def organize_files(path):
    for file in os.listdir(path):
        filename, extension = os.path.splitext(file)
        if extension:
            moved = False
            for folder, extensions in file_types.items():
                if extension.lower() in extensions:
                    folder_path = os.path.join(path, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(os.path.join(path, file), os.path.join(folder_path, file))
                    moved = True
                    break
            if not moved:
                others_path = os.path.join(path, 'Others')
                if not os.path.exists(others_path):
                    os.makedirs(others_path)
                shutil.move(os.path.join(path, file), os.path.join(others_path, file))

if __name__ == "__main__":
    organize_files(path)
    print("Files organized successfully!")