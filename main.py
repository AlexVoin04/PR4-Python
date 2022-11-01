import multiprocessing
from datetime import datetime


def get_input():
    while True:
        x, y = [int(x) for x in input().split()]
        if x == '' or y == '':
           break
        else:
           return x, y


def get_numbers(queue, x, y):
    #number = get_input()
    #x, y = [int(x) for x in input().split()]
    queue.put(x)
    queue.put(y)
    #try:
        #x, y = [int(x) for x in input().split()]
        #queue.put(x)
        #queue.put(y)
    #except Exception:
    #    pass


def get_result(queue):

    try:
        while True:
            if not queue.empty():
                x = queue.get()
                y = queue.get()
                step = x ** y
                sum = 0
                for i in range(step):
                    sum += i
                filename = r"./test.txt"
                with open(filename, 'a') as file:
                    now = datetime.now()
                    date_format = "{}.{}.{}  {}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute,
                                                              now.second)
                    file.write(f"{date_format} {x} {y} {step}\n")
    except Exception:
        print("Что-то пошло не так ...")
    except KeyboardInterrupt:
        print("Завершение")


if __name__ == '__main__':

    queue = multiprocessing.Queue()

    try:
        while True:
            x, y = [int(x) for x in input().split()]

            firstProcess = multiprocessing.Process(target=get_numbers, args=(queue, x, y))
            secondProcess = multiprocessing.Process(target=get_result, args=(queue,))
            firstProcess.start()
            secondProcess.start()

            firstProcess.join()
            while not queue.empty():
                pass
            print("Конец")

    except Exception:
        print("Что-то пошло не так ...")
