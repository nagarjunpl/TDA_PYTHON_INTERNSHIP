import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"]
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(source_folder):
    for filename in os.listdir(source_folder):
        filepath = os.path.join(source_folder, filename)
        
        # Skip folders
        if os.path.isdir(filepath):
            continue
        
        category = get_category(filename)
        category_folder = os.path.join(source_folder, category)
        
        # Create folder if not exists
        os.makedirs(category_folder, exist_ok=True)
        
        # Move file into category folder
        shutil.move(filepath, os.path.join(category_folder, filename))
        print(f"Moved: {filename} -> {category}")


folder_path = input("Enter the folder path to organize: ")
organize_files(folder_path)
print("✅ Files organized successfully!")
