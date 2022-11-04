from datetime import datetime
import multiprocessing


def get_result(queue):
    try:
        while True:
            x = queue.get()
            y = queue.get()
            step = x ** y
            sum = 0
            for i in range(step):
                sum += i
            filename = r"./test.txt"
            with open(filename, 'a') as file:
                now = datetime.now()
                date_format = "{}.{}.{} {}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute,
                                                          now.second)
                file.write(f"{date_format} {x} {y} {step}\n")
    except Exception:
        print("Что-то пошло не так ...")


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    list_process = []
    try:
        while True:
            x, y = [int(x) for x in input("Введите число и степень: ").split()]
            queue.put(x)
            queue.put(y)
            process = multiprocessing.Process(target=get_result, args=(queue,))
            process.start()
            list_process.append(process)
    except KeyboardInterrupt:
        print("Конец")
    except ValueError:
        print("Завершение")
    except Exception:
        print("Что-то пошло не так ...")
    [process.join() for process in list_process]
