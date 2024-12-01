from queue import Queue
from enemy import *


class Tunnel:
    def __init__(self):
        self.next_step = Empty()
        self.contents = Queue()
        for i in range(15): self.contents.put(Empty())
        print(self.contents.qsize())

    def append_step(self, step):
        self.contents.get()
        self.contents.put(self.next_step)
        self.next_step = step

    def get_as_str(self) -> str:
        result = [i.char for i in self.contents.queue]
        return "".join(result)