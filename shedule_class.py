from watchdog.events import FileSystemEventHandler
from utils import Filereader

class FileShedule(FileSystemEventHandler):
    def __init__(self, file_path) -> None:
        self._file_path = file_path

    def on_modified(self, event):
        if(event.src_path == self._file_path):
            last_res = FileReader.last_line(self._file_path)
            print(last_res)
