from time import sleep


def simple_task(number):
    print(number*number)
    return number


def expensive_io_task(time):
    sleep(time)
    print("Finished sleeping for {} seconds".format(time))
    return time


def expensive_cpu_task(num):
    elements = []
    for number in range(1000000):
        elements.append(hash(number*num))

    elements.sort(reverse=True)

    print("Finished executing expensive CPU task with value: {}".format(num))
    return elements
