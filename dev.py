import sys
import time
import subprocess
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

last_trigger_time = time.time()

class Handler(FileSystemEventHandler):
    def __init__(self):
        self.process = self.start_process()

    def on_modified(self, event):
        global last_trigger_time

        current_time = time.time()
        if event.src_path.find('~') == -1 and (current_time - last_trigger_time) > 1:
            last_trigger_time = current_time
            self.restart_process()

    def restart_process(self):
        logging.info("Reloading...")

        if self.process is not None:
            self.process.kill()
            self.process.wait() 

        self.process = self.start_process()

    
    def start_process(self):
        logging.info("Starting...")
        return subprocess.Popen([sys.executable, 'main.py'])

if __name__ == "__main__":
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path='app', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
