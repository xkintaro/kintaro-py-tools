from flask import request, jsonify
import os
from werkzeug.utils import secure_filename

from .config import CONVERTER_START_DIR, COMPRESSOR_START_DIR, RENAMER_START_DIR

MAX_FILENAME_LENGTH = 100

def init_routes(app):
    @app.route('/upload', methods=['POST'])
    def upload():
        files = request.files.getlist('files[]')
        folder = request.form['folder']
        directory = CONVERTER_START_DIR if folder == 'converter' else COMPRESSOR_START_DIR if folder == 'compressor' else RENAMER_START_DIR if folder == 'renamer' else None

        if not directory:
            return jsonify(error="Invalid folder"), 400

        for file in files:
            filename = secure_filename(file.filename)
            if len(filename) > MAX_FILENAME_LENGTH:
                name, ext = os.path.splitext(filename)
                filename = name[:MAX_FILENAME_LENGTH - len(ext)] + ext
            file.save(os.path.join(directory, filename))
        return jsonify(success=True), 200