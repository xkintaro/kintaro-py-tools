import os
import time

DISPLAY_FILENAME_LENGTH = 60

def shorten_filename(filename, length):
    if len(filename) > length:
        return filename[:length] + '...'
    return filename

def safe_remove(file_path, max_attempts=3, delay=1):
    if not os.path.exists(file_path):
        return True
    
    for attempt in range(max_attempts):
        try:
            os.remove(file_path)
            return True
        except PermissionError:
            if attempt < max_attempts - 1:
                time.sleep(delay)
                continue
            return False
        except FileNotFoundError:
            return True
        except OSError as e:
            if attempt < max_attempts - 1:
                time.sleep(delay)
                continue
            return False

def init_routes(app):
     pass