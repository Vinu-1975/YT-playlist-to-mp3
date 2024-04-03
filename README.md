# YouTube Playlist MP3 Downloader

YouTube Playlist MP3 Downloader is a Python script that enables users to effortlessly download the audio tracks from a YouTube playlist and convert them to MP3 format. With this tool, users can build a local collection of MP3 files from their favorite YouTube playlists.

## Setup Virtual Environment (macOS)

1. Open Terminal.
2. Install virtualenv using pip if you haven't already:
    ```bash
    pip install virtualenv
    ```
3. Navigate to your project directory.
4. Create a virtual environment:
    ```bash
    virtualenv venv
    ```
5. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

## Setup Virtual Environment (Windows)

1. Open Command Prompt.
2. Install virtualenv using pip if you haven't already:
   
    ```bash
    pip install virtualenv
    ```
4. Navigate to your project directory.
5. Create a virtual environment:
    ```bash
    virtualenv venv
    ```
6. Activate the virtual environment:
    ```bash
    .\venv\Scripts\activate
    ```

## Install Dependencies

Once the virtual environment is activated, install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

Ensure the virtual environment is activated.
Run the main.py script:
```bash
python main.py
```
Wait for the script to download and convert the audio tracks.
The MP3 files will be saved in the "Audio" folder within the project directory.
