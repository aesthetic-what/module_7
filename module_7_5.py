import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_info = {
            'name': file,
            'path': file_path,
            'formatted_time': time.ctime(os.path.getatime(file_path)),
            'size': os.path.getsize(file_path),
            'parent_dir': os.path.dirname(file_path)
        }
        print(file_info)
