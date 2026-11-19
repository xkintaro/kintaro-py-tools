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
        base_filename = request.form.get('baseFilename', '').strip()
        pattern = request.form.get('pattern', '001')
        errors = []
        successes = []

        if any(c in base_filename for c in '<>:"/\\|?*'):
            return jsonify(success=False, errors=["The file name contains invalid characters."], successes=[]), 200
        if pattern not in ('001', '0001', '00001', '000001'):
            pattern = '001'

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