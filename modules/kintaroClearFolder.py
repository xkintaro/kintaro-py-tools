from flask import jsonify, request
import os
from .utils import safe_remove
from .config import *

def init_routes(app):
    @app.route('/clear', methods=['POST'])
    def clear():
        folder = request.form['folder']
        dir_path = CONVERTER_START_DIR if folder == 'converterStart' \
                  else CONVERTER_FINISH_DIR if folder == 'converterFinish' \
                  else COMPRESSOR_START_DIR if folder == 'compressorStart' \
                  else COMPRESSOR_FINISH_DIR if folder == 'compressorFinish' \
                  else RENAMER_START_DIR if folder == 'renamerStart' \
                  else RENAMER_FINISH_DIR if folder == 'renamerFinish' \
                  else None
        if not dir_path:
            return jsonify(error="Invalid folder"), 400

        errors = []
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if not safe_remove(file_path):
                errors.append(f"Could not remove {filename}")

        if errors:
            return jsonify(error="Some files could not be removed: " + ", ".join(errors)), 500

        return jsonify(success=True), 200