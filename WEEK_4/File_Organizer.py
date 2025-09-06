import os
import shutil

def organize_folder(folder_path):
    # Categories and their extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
        "Music": [".mp3", ".wav"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Archives": [".zip", ".rar", ".tar"],
        "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"]
    }

    # Create category folders if not exist
    for category in categories.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Find the right category
        moved = False
        for category, extensions in categories.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, category, filename))
                print(f"Moved: {filename} → {category}")
                moved = True
                break

        # If no category matched → put in "Others"
        if not moved:
            others_path = os.path.join(folder_path, "Others")
            if not os.path.exists(others_path):
                os.mkdir(others_path)
            shutil.move(file_path, os.path.join(others_path, filename))
            print(f"Moved: {filename} → Others")

# === Run the Organizer ===
folder = input("Enter the folder path to organize: ")
organize_folder(folder)
print("\nFolder organized successfully!")
