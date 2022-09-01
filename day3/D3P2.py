import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

pictures = ['jpg', 'jpeg', 'bmp', 'svg', 'png', 'webp']
videos = ['mp4', 'webm', 'mov', 'mkv']
docs = ['doc','docx','pdf', 'xls', 'txt', 'exe']
comp = ["zip", "rar", "tar", "gz", "iso", "7z"]
audios = ["mp3", "wav", "aif"]

class MessyFile(FileSystemEventHandler):
    def on_created(self, event):
        files = os.listdir(path)
        print(len(files))
        for file in files:
            source = os.path.join(path, file)
            if os.path.isdir(source):
                continue
            file_type = file.split(".")
            if file_type[-1] in pictures:
                foldername = "pictures"
            elif file_type[-1] in videos:
                foldername = "videoss"      
            elif file_type[-1] in docs:
                foldername = "docs"
            elif file_type[-1] in comp:
                foldername = "compressed files"
            elif file_type[-1] in audios:
                foldername = "audios"
            else:
                foldername = "others"
            # print(foldername)
            # GEts the path of the folder 
            folder = os.path.join(path, foldername)
            if not os.path.exists(folder):
                os.mkdir(folder)
            destination = os.path.join(folder,file)
            shutil.move(source, destination)
path = r"C:\Users\DELL\downloads"
eventhandler = MessyFile()
observer = Observer()
observer.schedule(eventhandler, path, recursive = False)
observer.start()


try:
    while True:
        import time
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()