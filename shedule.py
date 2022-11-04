import time
from shedule_class import FileShedule
from watchdog.observers import Observer

path_to_file = "C:\\Alex\\PythonProject\\PR4-Python"
event_handler = FileShedule()
observer = Observer()
observer.schedule(event_handler, path=path_to_file, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Завершение")
finally:
    observer.stop()
    observer.join()