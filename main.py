import multiprocessing


def get_input():
    while True:
        x, y = [int(x) for x in input().split()]
        if x == '' or y == '':
            break
        else:
            return x, y


def get_numbers(queue):
    number = get_input()
    # x, y = [int(x) for x in input().split()]
    queue.put(number[1])
    queue.put(number[2])


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
                    file.write(step)
    except Exception:
        print("Что-то пошло не так ...")
    except KeyboardInterrupt:
        print("Завершение")


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    firstProcess = multiprocessing.Process(target=get_numbers, args=(queue,))
    secondProcess = multiprocessing.Process(target=get_result, args=(queue,))
    firstProcess.start()
    secondProcess.start()

    firstProcess.join()
    while not queue.empty():
        pass
    print("Конец")
