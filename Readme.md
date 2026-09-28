# Python File Organizer

A simple Python utility that automatically organizes files into folders based on their file extensions.

## Features

* Automatically detects file types
* Creates folders for different file categories
* Moves files into their corresponding folders
* Helps keep the Downloads folder organized
* Simple command-line based Python project

## File Categories

The organizer can sort files such as:

* Images → `Images/`
* Videos → `Videos/`
* Documents → `Documents/`
* PDFs → `PDFs/`
* Music → `Music/`
* ZIP files → `Archives/`
* Other files → `Others/`

## Requirements

* Python 3.x

No external libraries are required if the project uses only Python's standard library.

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-file-organizer.git
```

Go into the project folder:

```bash
cd python-file-organizer
```

Run the program:

```bash
python organizer.py
```

## Example

Before:

```text
Downloads/
├── photo.jpg
├── movie.mp4
├── resume.pdf
├── song.mp3
└── notes.txt
```

After running the organizer:

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Videos/
│   └── movie.mp4
├── PDFs/
│   └── resume.pdf
├── Music/
│   └── song.mp3
└── Documents/
    └── notes.txt
```

## Technologies Used

* Python
* `os`
* `shutil`
* File system operations

## Author

Your Name
