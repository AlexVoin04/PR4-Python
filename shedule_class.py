
from watchdog.events import FileSystemEventHandler


class FileShedule(FileSystemEventHandler):
    def __init__(self, file_path) -> None:
        self._file_path = file_path

    def on_modified(self, event):
        if(event.src_path == self._file_path):
            with open(self._file_path) as f:
                for line in f:
                    pass
                last_res = line.split(" ")
            print(f"{last_res[0]} {last_res[1]}>>{last_res[3]}^{last_res[4]}={last_res[5]}")
