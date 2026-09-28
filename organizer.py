from pathlib import Path

folder = Path.home() / "Downloads"

folders = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".zip": "Archives",
    ".rar": "Archives",
}

for file in folder.iterdir():

    if file.is_file():
        extension = file.suffix.lower()

        if extension in folders:
            destination_folder = folder / folders[extension]
            destination_folder.mkdir(exist_ok=True)

            destination = destination_folder / file.name
            file.rename(destination)

            print(f"Moved: {file.name} → {folders[extension]}")

print("Done!")