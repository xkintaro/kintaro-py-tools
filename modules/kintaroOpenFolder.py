from flask import request, jsonify
import os
import platform
import subprocess

from .config import *

def init_routes(app):
    @app.route('/open_folder', methods=['POST'])
    def open_folder():
        folder = request.form['folder']
        dir_path = os.path.abspath(CONVERTER_START_DIR if folder == 'converterStart' 
                              else CONVERTER_FINISH_DIR if folder == 'converterFinish' 
                              else COMPRESSOR_START_DIR if folder == 'compressorStart' 
                              else COMPRESSOR_FINISH_DIR if folder == 'compressorFinish' 
                              else DOWNLOAD_DIR if folder == 'downloads' 
                              else RENAMER_START_DIR if folder == 'renamerStart' 
                              else RENAMER_FINISH_DIR if folder == 'renamerFinish' 
                              else None)
        if not dir_path:
            return jsonify(error="Invalid folder"), 400

        try:
            if platform.system() == "Windows":
                os.startfile(dir_path)
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", dir_path])
            else:
                subprocess.Popen(["xdg-open", dir_path])
            return jsonify(success=True), 200
        except Exception as e:
            return jsonify(error=str(e)), 500