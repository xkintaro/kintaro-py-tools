<a href="README.md">
  <img src="https://img.shields.io/badge/Language-English-blue?style=flat-square&logo=google-translate&logoColor=white" alt="English">
</a>
<a href="README-TR.md">
  <img src="https://img.shields.io/badge/Dil-Türkçe-red?style=flat-square&logo=google-translate&logoColor=white" alt="Türkçe">
</a>

  <br />
  <br />

<div align="center">
  <img src="static/md/kintaro.png" width="120" height="120" />

  <br />
  <br />

  <p>
    Quickly convert, compress, batch rename, and download videos over your local network.
  </p>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-00568F?style=for-the-badge&logo=python&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)
![MoviePy](https://img.shields.io/badge/MoviePy-2C3E50?style=for-the-badge&logo=python&logoColor=white)
![yt-dlp](https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

  <p>
    <a href="#features">Features</a> •
    <a href="#technologies">Technologies</a> •
    <a href="#installation">Installation</a> •
    <a href="#how-does-it-work">How to Use?</a> •
    <a href="#project-structure">Project Structure</a> •
    <a href="#license">License</a> •
    <a href="#gallery">Gallery</a>
  </p>

  <br />
  <br />
</div>

## 📋 About

**Kintaro Tools** allows you to safely handle all your media operations on your own computer without uploading them to the internet. It brings together tedious tasks such as format conversion, size reduction, and batch renaming in a single interface. You get fast and effortless results without your data leaving your device.

<img src="static/md/20260225135733123_oy5b0wg0.jpg" width="auto"  />

## ✨ Features <a id="features"></a>

### File Converter

Convert files between different formats.

- **Images:** `JPG`, `PNG`, `WEBP`
- **Videos:** `MP4`, `AVI`, `MOV`, `WEBM`
- **Audio:** `MP3`, `WAV`, `AAC`, `FLAC`, `OGG`

### File Compressor

Reduce the size of video and audio files.

- Preset and custom bitrate options for video compression
- Adjustable video bitrate
- Adjustable audio bitrate

### Batch Renamer

Rename multiple files at once with a consistent naming pattern.

- Specify prefix in the filename
- Configurable zero-padded numbering (3 to 6 digits)
- Preserves original file extensions

**Example**: "_picture_001.jpg_", "_picture_002.jpg_", "_picture_003.jpg_"

### Video Downloader

Download videos from various platforms using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

- Supports YouTube, Instagram, TikTok, and other platforms supported by yt-dlp.
- Downloaded files are saved with a timestamped filename.

## 🛠️ Technologies <a id="technologies"></a>

- **Backend:** `Python`, `Flask`
- **Frontend:** `HTML`, `CSS`, `Bootstrap`, `jQuery`
- **Media Processing:** `Pillow`, `MoviePy`, `FFmpeg`
- **Downloading:** `yt-dlp`

## 🚀 Installation <a id="installation"></a>

1. **Clone the repository:**

   ```bash
   git clone https://github.com/xkintaro/kintaro-py-tools.git
   cd kintaro-py-tools
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

The application will automatically open `http://127.0.0.1:5000` in your default browser.

## ⚙️ How to Use? <a id="how-does-it-work"></a>

The application uses a folder-based workflow:

1. Upload files to the corresponding `Start` folder.

2. Select your settings and start the process.

3. Processed files appear in the corresponding `Finish` folder. Source files are removed from the `Start` folder after successful processing.

Each tool has its own pair of working directories:

| Tool       | Input Folder       | Output Folder       |
| ---------- | ------------------ | ------------------- |
| Converter  | `converterStart/`  | `converterFinish/`  |
| Compressor | `compressorStart/` | `compressorFinish/` |
| Renamer    | `renamerStart/`    | `renamerFinish/`    |
| Downloader | —                  | `downloads/`        |

You can also open these folders directly from the web interface or delete them with a single click.

## 📂 Project Structure <a id="project-structure"></a>

```
kintaro-py-tools/
├── app.py
├── requirements.txt
├── run.bat
├── install_requirements.bat
├── modules/
│   ├── config.py
│   ├── utils.py
│   ├── kintaroConverter.py
│   ├── kintaroCompressor.py
│   ├── kintaroDownloader.py
│   ├── kintaroRenamer.py
│   ├── kintaroClearFolder.py
│   ├── kintaroOpenFolder.py
│   └── kintaroUploadFiles.py
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── kintaroConverter.html
│   ├── kintaroCompressor.html
│   ├── kintaroDownloader.html
│   └── kintaroRenamer.html
└── static/
    ├── styles.css
    ├── fileUploader.js
    ├── folderOperations.js
    ├── formHandlers.js
    ├── fileListUpdater.js
    └── uiHelpers.js
```

## 📄 License <a id="license"></a>

This project is licensed under the MIT License. You can check the [LICENSE](LICENSE) file for details.

## 🖼️ Gallery <a id="gallery"></a>

<img src="static/md/20260225135733185_8a8gwrdh.jpg" width="auto"  />

#

<img src="static/md/20260225135733250_is51xyvr.jpg" width="auto"  />

#

<img src="static/md/20260225135733315_atlvossg.jpg" width="auto"  />

#

<img src="static/md/20260225135733381_fg9mow1p.jpg" width="auto"  />

#

<p align="center">
  <sub>❤️ Developed by "Mustafa TAŞAL" (kintaro)</sub>
</p>
