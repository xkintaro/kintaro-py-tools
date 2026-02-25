from flask import request, jsonify, render_template
from moviepy.editor import VideoFileClip, AudioFileClip
from PIL import Image
import os
from .utils import safe_remove, shorten_filename, DISPLAY_FILENAME_LENGTH
from .config import COMPRESSOR_START_DIR, COMPRESSOR_FINISH_DIR

ALLOWED_IMAGE_INPUT_EXTS = ['.jpg', '.jpeg', '.png', '.webp']
ALLOWED_VIDEO_INPUT_EXTS = ['.mp4', '.avi', '.mov', '.webm']
ALLOWED_AUDIO_INPUT_EXTS = ['.mp3', '.wav', '.aac', '.flac', '.ogg']

def determine_audio_codec(ext):
    ext = ext.lower()
    if ext in ['.mp3']:
        return 'mp3'
    elif ext in ['.wav']:
        return None 
    elif ext in ['.aac']:
        return 'aac'
    elif ext in ['.flac']:
        return 'flac'
    elif ext in ['.ogg']:
        return 'libvorbis'
    else:
        return None

def compress_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        lower_output = output_path.lower()
        if lower_output.endswith(('.jpg', '.jpeg')):
            img.save(output_path, 'JPEG', quality=60, optimize=True)
        elif lower_output.endswith('.png'):
            img.save(output_path, 'PNG', optimize=True)
        elif lower_output.endswith('.webp'):
            img.save(output_path, 'WEBP', quality=60, method=6)
        else:
            img.save(output_path)
    except Exception as e:
        raise e
    finally:
        if 'img' in locals():
            img.close()

def compress_video(input_path, output_path):
    clip = None
    try:
        clip = VideoFileClip(input_path)
        bitrate = request.form.get('bitrate', '1000k')
        lower_output = output_path.lower()
        if lower_output.endswith('.webm'):
            clip.write_videofile(output_path,
                bitrate=bitrate,
                codec='libvpx-vp9',
                preset='medium',
                ffmpeg_params=['-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2'],
                audio_codec='libvorbis')
        else:
            clip.write_videofile(output_path,
                bitrate=bitrate,
                codec='libx264',
                preset='medium',
                ffmpeg_params=['-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2', '-c:a', 'aac'],
                audio_codec='aac')
    except Exception as e:
        if os.path.exists(output_path):
            try:
                os.remove(output_path)
            except Exception:
                pass
        raise e
    finally:
        if clip:
            try:
                clip.close()
            except Exception:
                pass

def compress_audio(input_path, output_path):
    clip = None
    try:
        clip = AudioFileClip(input_path)
        bitrate = request.form.get('audiobitrate', '128k')
        ext = os.path.splitext(output_path)[1]
        codec = determine_audio_codec(ext)
        clip.write_audiofile(output_path, bitrate=bitrate, codec=codec)
    except Exception as e:
        if os.path.exists(output_path):
            try:
                os.remove(output_path)
            except Exception:
                pass
        raise e
    finally:
        if clip:
            try:
                clip.close()
            except Exception:
                pass

def init_routes(app):
    @app.route('/kintaroCompressor')
    def kintaro_compressor():
        start_files = [shorten_filename(f, DISPLAY_FILENAME_LENGTH) for f in os.listdir(COMPRESSOR_START_DIR)]
        finish_files = [shorten_filename(f, DISPLAY_FILENAME_LENGTH) for f in os.listdir(COMPRESSOR_FINISH_DIR)]
        return render_template('kintaroCompressor.html', start_files=start_files, finish_files=finish_files)

    @app.route('/compress', methods=['POST'])
    def compress():
        errors = []    
        successes = []

        for filename in os.listdir(COMPRESSOR_START_DIR):
            input_path = os.path.join(COMPRESSOR_START_DIR, filename)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(COMPRESSOR_FINISH_DIR, f"{name}{ext}")

            if os.path.exists(output_path):
                errors.append(f"File {name}{ext} already exists in the finish directory.")
                continue

            ext_lower = ext.lower()
            try:
                if ext_lower in ALLOWED_IMAGE_INPUT_EXTS:
                    compress_image(input_path, output_path)
                    if safe_remove(input_path):
                        successes.append(f"Successfully compressed {filename} and moved to finish folder.")
                    else:
                        successes.append(f"Successfully compressed {filename}, but could not remove from start folder.")
                elif ext_lower in ALLOWED_VIDEO_INPUT_EXTS:
                    compress_video(input_path, output_path)
                    if safe_remove(input_path):
                        successes.append(f"Successfully compressed {filename} and moved to finish folder.")
                    else:
                        successes.append(f"Successfully compressed {filename}, but could not remove from start folder.")
                elif ext_lower in ALLOWED_AUDIO_INPUT_EXTS:
                    compress_audio(input_path, output_path)
                    if safe_remove(input_path):
                        successes.append(f"Successfully compressed {filename} and moved to finish folder.")
                    else:
                        successes.append(f"Successfully compressed {filename}, but could not remove from start folder.")
                else:
                    errors.append(f"Unsupported file format for {filename}")
            except Exception as e:
                errors.append(f"Failed to compress {filename}: {str(e)}")
                if os.path.exists(output_path):
                    try:
                        os.remove(output_path)
                    except Exception:
                        pass

        return jsonify({
            'success': True if successes else False,
            'errors': errors,
            'successes': successes
        }), 200
