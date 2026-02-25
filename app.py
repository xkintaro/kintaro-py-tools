import os
import socket
import webbrowser
from flask import Flask, request
from flask.templating import render_template
from werkzeug.serving import is_running_from_reloader

def find_free_port(start_port=5000):
    port = start_port
    while port < start_port + 100:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', port))
                return port
            except OSError:
                port += 1
    raise RuntimeError(f'{start_port}-{start_port + 99} no free port!')

from modules.kintaroConverter import init_routes as init_converter_routes
from modules.kintaroCompressor import init_routes as init_compressor_routes
from modules.kintaroDownloader import init_routes as init_downloader_routes
from modules.kintaroRenamer import init_routes as init_renamer_routes
from modules.kintaroOpenFolder import init_routes as init_open_folder_routes
from modules.kintaroClearFolder import init_routes as init_clear_folder_routes
from modules.kintaroUploadFiles import init_routes as init_upload_routes

app = Flask(__name__)

from modules.config import *

@app.route('/')
def index():
    return render_template('index.html')

init_converter_routes(app)
init_compressor_routes(app)
init_downloader_routes(app)
init_renamer_routes(app)
init_open_folder_routes(app)
init_clear_folder_routes(app)
init_upload_routes(app)

if __name__ == '__main__':
    for directory in [CONVERTER_START_DIR, CONVERTER_FINISH_DIR, COMPRESSOR_START_DIR, COMPRESSOR_FINISH_DIR, DOWNLOAD_DIR, RENAMER_START_DIR, RENAMER_FINISH_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    port = find_free_port(5000)
    if not is_running_from_reloader():
        webbrowser.open(f'http://127.0.0.1:{port}')
    app.run(debug=True, port=port)