from flask import request, jsonify, render_template
import os
from .utils import safe_remove, shorten_filename, DISPLAY_FILENAME_LENGTH
from .config import RENAMER_START_DIR, RENAMER_FINISH_DIR

def init_routes(app):
    @app.route('/kintaroRenamer')
    def kintaro_renamer():
        start_files = [shorten_filename(f, DISPLAY_FILENAME_LENGTH) for f in os.listdir(RENAMER_START_DIR)]
        finish_files = [shorten_filename(f, DISPLAY_FILENAME_LENGTH) for f in os.listdir(RENAMER_FINISH_DIR)]
        return render_template('kintaroRenamer.html', start_files=start_files, finish_files=finish_files)

    @app.route('/rename', methods=['POST'])
    def rename():
        base_filename = request.form['baseFilename']
        pattern = request.form['pattern']
        errors = []
        successes = []

        files = sorted(os.listdir(RENAMER_START_DIR))
        for i, filename in enumerate(files, 1):
            input_path = os.path.join(RENAMER_START_DIR, filename)
            _, ext = os.path.splitext(filename)
            new_filename = f"{base_filename}{str(i).zfill(len(pattern))}{ext}"
            output_path = os.path.join(RENAMER_FINISH_DIR, new_filename)

            try:
                if os.path.exists(output_path):
                    errors.append(f"File {new_filename} already exists in the finish directory.")
                    continue

                os.rename(input_path, output_path)
                successes.append(f"Successfully renamed {filename} to {new_filename} and removed from start folder.")
            except Exception as e:
                errors.append(f"Failed to rename {filename}: {e}")

        return jsonify({
            'success': True if successes else False,
            'errors': errors,
            'successes': successes
        }), 200