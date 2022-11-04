
from watchdog.events import FileSystemEventHandler


class FileShedule(FileSystemEventHandler):

    def on_modified(self, event):
        with open("test.txt", 'r') as f:
            for line in f:
                pass
            last_res = line.split(" ")
        print(f"{last_res[0]} {last_res[1]} >> {last_res[2]}^{last_res[3]}={last_res[4]}")
