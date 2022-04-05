import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHamdler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.C:/Users/maxwe/Downloads/pro 102/lol.py} has ben created!")
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.C:/Users/maxwe/Downloads/pro 102/lol.py}!")
event_handler = FileSystemEventHandler():

observer = Observer()

observer.schedule(event_handler, From_dir, recersive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()