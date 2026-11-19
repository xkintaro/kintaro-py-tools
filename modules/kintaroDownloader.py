from flask import render_template, request, jsonify
import os
import yt_dlp
import deno
import imageio_ffmpeg
from datetime import datetime
from .utils import shorten_filename, DISPLAY_FILENAME_LENGTH
from .config import DOWNLOAD_DIR

def init_routes(app):
    @app.route('/kintaroDownloader')
    def kintaro_downloader():
        download_files = [shorten_filename(f, DISPLAY_FILENAME_LENGTH) for f in os.listdir(DOWNLOAD_DIR)]
        return render_template('kintaroDownloader.html', download_files=download_files)

    @app.route('/download', methods=['POST'])
    def download():
        url = request.form.get('url')
        success, error = download_video(url, DOWNLOAD_DIR)
        if success:
            return jsonify(success=True), 200
        return jsonify(error=error), 400

def download_video(url, download_dir):
    if not url or not url.strip():
        return False, "URL cannot be empty"

    if not os.path.exists(download_dir):
        try:
            os.makedirs(download_dir)
        except Exception as e:
            return False, f"Failed to create download directory: {str(e)}"

    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]

    ydl_opts = {
        'outtmpl': os.path.join(download_dir, f'{current_time}.%(ext)s'),
        'format': 'bv*+ba/b',
        'format_sort': ['res', 'vcodec:h264', 'acodec:m4a'],
        'merge_output_format': 'mp4',
        'js_runtimes': {'deno': {'path': deno.find_deno_bin()}},
        'ffmpeg_location': imageio_ffmpeg.get_ffmpeg_exe(),
        'restrictfilenames': True,
        'noplaylist': True,
        'quiet': True,
        'noprogress': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.extract_info(url.strip(), download=True)
                return True, None
            except yt_dlp.utils.DownloadError as e:
                return False, f"Download failed: {str(e)}"
            except yt_dlp.utils.ExtractorError as e:
                return False, f"Failed to extract video info: {str(e)}"
    except Exception as e:
        return False, f"Unexpected error during download: {str(e)}"