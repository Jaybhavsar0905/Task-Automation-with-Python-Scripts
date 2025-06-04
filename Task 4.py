import os
import shutil

# Path to your Downloads folder
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

# Folder categories and their corresponding file extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in FILE_TYPES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    move_to_category_folder(file_path, folder_path, category)
                    moved = True
                    break
            if not moved:
                move_to_category_folder(file_path, folder_path, "Others")

def move_to_category_folder(file_path, base_path, category):
    category_path = os.path.join(base_path, category)
    os.makedirs(category_path, exist_ok=True)
    shutil.move(file_path, os.path.join(category_path, os.path.basename(file_path)))
    print(f"Moved: {file_path} -> {category_path}")

if __name__ == "__main__":
    organize_files(DOWNLOADS_FOLDER)
