import os
import shutil

def organize_files(directory):
    file_types = {
        'images': ['jpg', 'jpeg', 'png', 'gif'],
        'documents': ['pdf', 'docx', 'txt'],
        'audio': ['mp3', 'wav'],
        'video': ['mp4', 'mov', 'avi'],
        'archives': ['zip', 'rar', 'tar', 'gz']
    }
    
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_ext = filename.split('.')[-1].lower()
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    folder_path = os.path.join(directory, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(os.path.join(directory, filename), folder_path)
                    break
            else:
                others_folder = os.path.join(directory, 'others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(os.path.join(directory, filename), others_folder)

if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ")
    organize_files(directory)
    print("Files organized.")
