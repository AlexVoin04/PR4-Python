from datetime import datetime
import multiprocessing


def get_result(queue):
    try:
        while True:
            if queue.empty():
                continue
            x, y = queue.get()
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

    process = multiprocessing.Process(target=get_result, args=(queue,))
    process.start()

    try:
        while True:
            x, y = [int(x) for x in input("Введите число и степень: ").split()]
            put = [x, y]
            queue.put(put)
    except KeyboardInterrupt:
        print("Конец")
    except ValueError:
        print("Завершение")
    except Exception:
        print("Что-то пошло не так ...")