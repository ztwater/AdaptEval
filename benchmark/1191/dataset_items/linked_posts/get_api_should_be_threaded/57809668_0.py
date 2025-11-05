import threading
from queue import Queue

def display_worker(display_queue):
    while True:
        line = display_queue.get()
        if line is None:  # simple termination logic, other sentinels can be used
            break
        print(line, flush=True)  # remove flush if slow or using Python2


def some_other_worker(display_queue, other_args):
    # NOTE accepts queue reference as an argument, though it could be a global
    display_queue.put("something which should be printed from this thread")


def main():
    display_queue = Queue()  # synchronizes console output
    screen_printing_thread = threading.Thread(
        target=display_worker,
        args=(display_queue,),
    )
    screen_printing_thread.start()

    ### other logic ###

    display_queue.put(None)  # end screen_printing_thread
    screen_printing_thread.stop()
