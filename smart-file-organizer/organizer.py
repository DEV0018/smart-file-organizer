import os
import shutil

path = "."

files = os.listdir(path)

folders = {
    "Images": [".jpg", ".png"],
    "Videos": [".mp4"],
    "Documents": [".pdf", ".docx"],
    "Music": [".mp3"]
}

# Create folders if not exist
for folder in folders:

    if not os.path.exists(folder):

        os.mkdir(folder)

# Move files
for file in files:

    # Skip folders and python file
    if os.path.isdir(file) or file == "organizer.py":
        continue

    for folder, extensions in folders.items():

        for ext in extensions:

            if file.endswith(ext):

                source = file
                destination = os.path.join(folder, file)

                shutil.move(source, destination)

                print(f"Moved {file} → {folder}")