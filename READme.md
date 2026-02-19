# 🎵 JukeBox Simulation

A desktop music player application built with Python, following the **MVC (Model-View-Controller)** architecture. It allows users to manage tracks, create playlists, add favorites, and play music — all through a clean Tkinter GUI.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the App](#running-the-app)
- [Running Tests](#running-tests)
- [Diagrams](#diagrams)
- [Personal Achievement](#personal-achievement)

---

## ✨ Features

- **Track Management** — Add, update, delete, and view music tracks with cover art
- **Playlist Management** — Create playlists and add tracks to them
- **Favorites** — Mark tracks as favorites and manage them
- **Music Player** — Play and stop MP3 tracks using VLC with a real-time progress bar
- **Persistent Storage** — All data stored in a MySQL database (XAMPP)

---

## 🛠️ Tech Stack

| Layer      | Technology                     |
|------------|-------------------------------|
| Language   | Python 3.12                   |
| GUI        | Tkinter                        |
| Database   | MySQL (via XAMPP)             |
| ORM        | mysql-connector-python         |
| Audio      | python-vlc, pygame             |
| Images     | Pillow (PIL)                  |
| Testing    | unittest / pytest              |

---

## 📁 Project Structure

```
JukeBox/
├── Controllers/
│   ├── favorite_controller.py      # Handles favorite track logic
│   ├── musicplayer_controller.py   # Handles play/stop actions
│   ├── track_controller.py         # Handles CRUD for tracks
│   └── track_list_controller.py    # Handles playlist management
│
├── Models/
│   ├── favorite.py                 # Favorite data model
│   ├── musicplayer.py              # Music playback model (VLC)
│   ├── track.py                    # Track data model
│   └── track_list.py              # TrackList data model
│
├── Views/
│   ├── BaseView.py                 # Abstract base view (Tkinter)
│   ├── favorite_view.py            # Favorites tab UI
│   ├── musicplayer_view.py         # Music player tab UI
│   ├── track_list_view.py          # Playlist tab UI
│   └── track_view.py              # Track management tab UI
│
├── database/
│   ├── favorite_db.py             # Favorites DB operations
│   ├── track_db.py                # Tracks DB operations
│   └── tracklist_db.py            # Tracklist DB operations
│
├── db.sql                          # SQL schema for MySQL
├── main_GUI.py                     # Application entry point
├── font_manager.py                 # Font configuration
├── JukeBox_test.py                # Unit tests
└── requirement.txt                # Python dependencies
```

---

## ✅ Prerequisites

- **Python 3.12** — [Download](https://www.python.org/downloads/)
- **XAMPP** (MySQL) — [Download](https://www.apachefriends.org/download.html)
- **VLC Media Player** — [Download](https://www.videolan.org/vlc/)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DK0310/OOPCW
cd OOPCW
```

### 2. Set Up the Database

1. Start **XAMPP** and launch **Apache** and **MySQL** modules
2. Open **phpMyAdmin** at `http://localhost/phpmyadmin`
3. Create a new database named exactly **`jukebox`**
4. Import the schema by running the contents of `db.sql` into the `jukebox` database

### 3. Create and Activate a Virtual Environment

```bash
# Create virtual environment with Python 3.12
python3.12 -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirement.txt
```

### 5. Configure VLC Path

Open `Models/musicplayer.py` and update line 14 with your VLC installation path:

```python
# Example — update this to match your VLC install location
os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")
```

> **Tip:** Look for the folder containing `libvlc.dll` — that's the path to use.

---

## ▶️ Running the App

```bash
python main_GUI.py
```

---

## 🧪 Running Tests

```bash
python -m pytest JukeBox_test.py -v
```

The test suite covers:

- Track creation and attribute updates
- Playlist track addition and clearing
- Favorite track management
- Music player play/stop behavior

---

## 📊 Diagrams

### Use Case Diagram


![Use Case Diagram](usecase.png)

---

### Class Diagram


![Class Diagram](classDiagram.png)

---

## 🏆 Personal Achievement


![Personal Achievement](achievement.png)

---

## 📄 License

This project was created for academic purposes as part of an Object-Oriented Programming coursework.
