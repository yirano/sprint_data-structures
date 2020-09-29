class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ind = 0
        self.queue = []

    def __str__(self):
        return self.queue

    def append(self, item):
        if (len(self.queue) < self.capacity):
            self.queue.append(item)
        else:
            self.queue.pop(self.ind)
            self.queue.insert(self.ind, item)
            if self.ind < self.capacity - 1:
                self.ind += 1
            else:
                self.ind = 0

    def get(self):
        return self.queue
