from flask import request, jsonify, render_template
from moviepy.editor import VideoFileClip, AudioFileClip
from PIL import Image
import os
from .utils import safe_remove, shorten_filename, DISPLAY_FILENAME_LENGTH
from .config import CONVERTER_START_DIR, CONVERTER_FINISH_DIR

ALLOWED_IMAGE_INPUT_EXTS = ['.jpg', '.jpeg', '.png', '.webp']
ALLOWED_IMAGE_OUTPUT_FORMATS = ['jpg', 'jpeg', 'png', 'webp']

ALLOWED_VIDEO_INPUT_EXTS = ['.mp4', '.avi', '.mov', '.webm']
ALLOWED_VIDEO_OUTPUT_FORMATS = ['mp4', 'avi', 'mov', 'webm']

ALLOWED_AUDIO_INPUT_EXTS = ['.mp3', '.wav', '.aac', '.flac', '.ogg']
ALLOWED_AUDIO_OUTPUT_FORMATS = ['mp3', 'wav', 'aac', 'flac', 'ogg']

def determine_audio_codec(output_format):
    fmt = output_format.lower()
    if fmt == 'mp3':
        return 'mp3'
    elif fmt == 'wav':
        return None
    elif fmt == 'aac':
        return 'aac'
    elif fmt == 'flac':
        return 'flac'
    elif fmt == 'ogg':
        return 'libvorbis'
    else:
        return None

def convert_image(input_path, output_path, output_format):
    img = Image.open(input_path)
    out_format = output_format.lower()
    if out_format in ['jpg', 'jpeg']:
        pil_format = 'JPEG'
        img = img.convert('RGB')
    else:
        pil_format = output_format.upper()
    img.save(output_path, format=pil_format)

def convert_audio(input_path, output_path, output_format):
    clip = None
    try:
        clip = AudioFileClip(input_path)
        codec = determine_audio_codec(output_format)
        clip.write_audiofile(output_path, codec=codec)
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

def convert_video(input_path, output_path, output_format):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    clip = None
    try:
        clip = VideoFileClip(input_path)
        out_format = output_format.lower()
        if out_format in ALLOWED_AUDIO_OUTPUT_FORMATS:
            if not clip.audio:
                raise ValueError("No audio stream found in the video file")
            codec = determine_audio_codec(out_format)
            clip.audio.write_audiofile(output_path, codec=codec)
        elif out_format in ALLOWED_VIDEO_OUTPUT_FORMATS:
            if out_format == 'webm':
                video_codec = 'libvpx'
                audio_codec = 'libvorbis'
                extra_params = ['-vf', 'scale=iw:-1']
            elif out_format in ['mp4', 'mov']:
                video_codec = 'libx264'
                audio_codec = 'aac'
                extra_params = ['-vf', 'scale=iw:-1', '-c:a', 'aac']
            elif out_format == 'avi':
                video_codec = 'mpeg4'
                audio_codec = 'mp3'
                extra_params = ['-vf', 'scale=iw:-1']
            else:
                raise ValueError(f"Unsupported output format for video conversion: {output_format}")

            clip.write_videofile(
                output_path,
                codec=video_codec,
                preset='medium',
                ffmpeg_params=extra_params,
                audio_codec=audio_codec
            )
        else:
            raise ValueError(f"Unsupported output format for video conversion: {output_format}")
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
    @app.route('/kintaroConverter')
    def kintaro_converter():
        start_files = [shorten_filename(f, DISPLAY_FILENAME_LENGTH) for f in os.listdir(CONVERTER_START_DIR)]
        finish_files = [shorten_filename(f, DISPLAY_FILENAME_LENGTH) for f in os.listdir(CONVERTER_FINISH_DIR)]
        return render_template('kintaroConverter.html', start_files=start_files, finish_files=finish_files)

    @app.route('/convert', methods=['POST'])
    def convert():
        file_format = request.form['format'].lower()
        errors = []
        successes = []

        for filename in os.listdir(CONVERTER_START_DIR):
            input_path = os.path.join(CONVERTER_START_DIR, filename)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(CONVERTER_FINISH_DIR, f"{name}.{file_format}")

            if os.path.exists(output_path):
                errors.append(f"File {name}.{file_format} already exists in the finish directory.")
                continue

            ext_lower = ext.lower()
            try:
                if ext_lower in ALLOWED_IMAGE_INPUT_EXTS:
                    if file_format not in ALLOWED_IMAGE_OUTPUT_FORMATS:
                        errors.append(f"Cannot convert image file {filename} to format {file_format}.")
                    else:
                        convert_image(input_path, output_path, file_format)
                        if safe_remove(input_path):
                            successes.append(f"Successfully converted {filename} to {file_format} and removed from start folder.")
                        else:
                            successes.append(f"Successfully converted {filename} to {file_format}, but could not remove from start folder.")
                elif ext_lower in ALLOWED_VIDEO_INPUT_EXTS:
                    if file_format not in (ALLOWED_VIDEO_OUTPUT_FORMATS + ALLOWED_AUDIO_OUTPUT_FORMATS):
                        errors.append(f"Cannot convert video file {filename} to format {file_format}.")
                    else:
                        convert_video(input_path, output_path, file_format)
                        if safe_remove(input_path):
                            successes.append(f"Successfully converted {filename} to {file_format} and removed from start folder.")
                        else:
                            successes.append(f"Successfully converted {filename} to {file_format}, but could not remove from start folder.")
                elif ext_lower in ALLOWED_AUDIO_INPUT_EXTS:
                    if file_format not in ALLOWED_AUDIO_OUTPUT_FORMATS:
                        errors.append(f"Cannot convert audio file {filename} to format {file_format}.")
                    else:
                        convert_audio(input_path, output_path, file_format)
                        if safe_remove(input_path):
                            successes.append(f"Successfully converted {filename} to {file_format} and removed from start folder.")
                        else:
                            successes.append(f"Successfully converted {filename} to {file_format}, but could not remove from start folder.")
                else:
                    errors.append(f"Unsupported file type for {filename}.")
            except Exception as e:
                errors.append(f"Failed to convert {filename}: {e}")

        return jsonify(errors=errors, successes=successes), 200
