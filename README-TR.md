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
    Dosyalarınızı yerel ağ üzerinden hızlıca dönüştürün, sıkıştırın, toplu isimlendirin ve video indirin.
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
    <a href="#features">Özellikler</a> •
    <a href="#technologies">Teknolojiler</a> •
    <a href="#installation">Kurulum</a> •
    <a href="#how-does-it-work">Nasıl Kullanılır?</a> •
    <a href="#project-structure">Proje Yapısı</a> •
    <a href="#license">Lisans</a> •
    <a href="#gallery">Galeri</a>
  </p>

  <br />
  <br />
</div>



## 📋 Hakkında

**Kintaro Tools**, tüm medya işlemlerinizi internete yükleme yapmadan kendi bilgisayarınızda güvenle halletmenizi sağlar. Format dönüştürme, boyut küçültme ve toplu isimlendirme gibi yorucu işleri tek bir arayüzde toplar. Verileriniz dışarı çıkmadan, hızlı ve zahmetsizce sonuç alırsınız.

<img src="static/md/20260225135733123_oy5b0wg0.jpg" width="auto"  />

## ✨ Özellikler <a id="features"></a>

### Format Dönüştürücü

Dosyaları farklı formatlar arasında dönüştürün.

- **Resim:** `JPG`, `PNG`, `WEBP`
- **Video:** `MP4`, `AVI`, `MOV`, `WEBM`
- **Ses:** `MP3`, `WAV`, `AAC`, `FLAC`, `OGG`

### Dosya Sıkıştırıcı

Video ve ses dosyalarının boyutlarını küçültün.

- Video sıkıştırma için önceden ayarlanmış ve özel bit hızı seçenekleri
- Ayarlanabilir video bit hızı
- Ayarlanabilir ses bit hızı

### Toplu Yeniden Adlandırıcı

Birden fazla dosyayı aynı anda tutarlı bir adlandırma deseniyle yeniden adlandırın.

- Dosya adında prefix belirleme
- Yapılandırılabilir sıfırla doldurulmuş numaralandırma (3 ila 6 basamak)
- Orijinal dosya uzantılarını korur

**Örnek**: "_picture_001.jpg_", "_picture_002.jpg_", "_picture_003.jpg_"

### Video İndirici

[yt-dlp](https://github.com/yt-dlp/yt-dlp) kullanarak çeşitli platformlardan videolar indirin.

- YouTube, Instagram, TikTok ve yt-dlp'nin desteklediği diğer platformları destekler.
- İndirilen dosyalar zaman damgalı dosya adıyla kaydedilir.

## 🛠️ Teknolojiler <a id="technologies"></a>

- **Backend:** `Python`, `Flask`
- **Frontend:** `HTML`, `CSS`, `Bootstrap`, `jQuery`
- **Media Processing:** `Pillow`, `MoviePy`, `FFmpeg`
- **Downloading:** `yt-dlp`

## 🚀 Kurulum <a id="installation"></a>

1. **Depoyu klonlayın:**

   ```bash
   git clone https://github.com/xkintaro/kintaro-py-tools.git
   cd kintaro-py-tools
   ```

2. **Bağımlılıkları yükleyin:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı çalıştırın:**

   ```bash
   python app.py
   ```

Uygulama, varsayılan tarayıcınızda otomatik olarak `http://127.0.0.1:5000` adresini açacaktır.

## ⚙️ Nasıl Kullanılır? <a id="how-does-it-work"></a>

Uygulama klasör tabanlı bir iş akışı kullanır:

1. Dosyaları ilgili `Start` klasörüne yükleyin.

2. Ayarlarınızı seçin ve sistemi başlatın.

3. İşlenmiş dosyalar ilgili `Finish` klasöründe görünür. Kaynak dosyalar, başarılı işlemden sonra ilgili `Start` ​​klasöründen kaldırılır.

Her aracın kendine ait bir çalışma dizini çifti vardır:

| Tool       | Input Folder       | Output Folder       |
| ---------- | ------------------ | ------------------- |
| Converter  | `converterStart/`  | `converterFinish/`  |
| Compressor | `compressorStart/` | `compressorFinish/` |
| Renamer    | `renamerStart/`    | `renamerFinish/`    |
| Downloader | —                  | `downloads/`        |

Bu klasörleri doğrudan web arayüzünden de açabilir veya tek bir tıklamayla silebilirsiniz.

## 📂 Proje Yapısı <a id="project-structure"></a>

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

## 📄 Lisans <a id="license"></a>

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasını inceleyebilirsiniz.

## 🖼️ Galeri <a id="gallery"></a>

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
