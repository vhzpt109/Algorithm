import threading


# 리스트는 thread-safe하지 않습니다.
def isEmpty(lst):
    return not bool(lst)


def pop(lst):
    return lst.pop(0)


def _print1(name, lst):
    while not isEmpty(lst):
        if evt.is_set():
            print(name, pop(lst))
            evt.clear()


def _print2(name, lst):
    while not isEmpty(lst):
        if not evt.is_set():
            print(name, pop(lst))
            evt.set()


evt = threading.Event()
def concurrentPrint(lst):
    thread1 = threading.Thread(target=_print1, args=("thread1", lst,))
    thread2 = threading.Thread(target=_print2, args=("thread2", lst,))

    evt.set()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


input_list = ["a", "b", "c", "d", "e", "f"]
concurrentPrint(input_list)

