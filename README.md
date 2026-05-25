# 📂 Smart File Organizer using Python

A Python automation project that automatically organizes files into categorized folders based on their file extensions.

---

## 🚀 Features

✅ Automatically detects files in a folder
✅ Creates folders automatically if they do not exist
✅ Organizes files into categories like:

* Images
* Videos
* Documents
* Music

✅ Beginner-friendly Python automation project
✅ Real-world useful project
✅ Clean and simple code structure

---

# 🛠️ Technologies Used

* Python
* os module
* shutil module

---

# 📁 Supported File Types

| Category  | Extensions  |
| --------- | ----------- |
| Images    | .jpg, .png  |
| Videos    | .mp4        |
| Documents | .pdf, .docx |
| Music     | .mp3        |

---

# 📸 Project Demo

## Before Running

```text
project-folder/
│
├── photo.jpg
├── notes.pdf
├── song.mp3
├── movie.mp4
└── organizer.py
```

## After Running

```text
project-folder/
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── notes.pdf
│
├── Music/
│   └── song.mp3
│
├── Videos/
│   └── movie.mp4
│
└── organizer.py
```

---

# ▶️ How to Run the Project

## Step 1

Clone the repository:

```bash
git clone https://github.com/your-username/smart-file-organizer.git
```

## Step 2

Open the project folder:

```bash
cd smart-file-organizer
```

## Step 3

Run the Python script:

```bash
python organizer.py
```

---

# 📜 Project Code

```python
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
```

---

# 🧠 Concepts Learned

* Python Automation
* File Handling
* OS Module
* shutil Module
* Loops and Conditions
* Dictionaries
* Folder Management

---

# 🌟 Future Improvements

* GUI using Tkinter
* Drag and Drop Support
* Organize Downloads Folder Automatically
* Duplicate File Remover
* Auto Scheduler
* More File Type Support

---

# 👨‍💻 Author

Developed by Devaraj 🚀


