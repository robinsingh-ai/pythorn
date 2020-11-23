"""
Author : Robin Singh
Programs List:
1.Queue 
2.Circular Queue
3.Double Ended Queue
"""

import inspect


class Queue(object):
    def __init__(self, length=5):
        """
        :param length: pass queue length while making object otherwise default value will be 5
        """
        self.items = []
        self.size = 0
        self.front = 0
        self.rear = 0
        self.limit = length

    def isEmpty(self):
        """
        checks the queue if its empty or not
        """
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, data):
        """
        inserts an element into the queue
        """
        if self.size >= self.limit:
            return -1
        else:
            self.items.append(data)

        if self.front == None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size = self.size+1

    def dequeue(self):
        """
        removes an element from the queue
        """
        if self.isEmpty():
            return -1
        else:
            self.size = self.size-1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1
            return self.items.pop(0)

    def Size(self):
        """
        returns size of the queue
        """
        return self.size

    def display(self):
        """
        displays full queue
        """
        if self.items == []:
            return -1
        else:
            print(self.items)

    @staticmethod
    def get_code():
        """
        :return: source code
        """
        return inspect.getsource(Queue)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return " Time Complexity of enqueue: O(1) "\
               " Time Complexity of dequeue: O(n)"\
               " Optimizations : We can implement both enqueu and dequeue operations in O(1) time. To achive this, we can either use linked list implementaion of queue or circular implementation of queue"


class CircularQueue(object):
    """
    :param length: pass queue length while making object otherwise default value will be  5

    """

    def __init__(self, length=5):
        """
        """
        self.items = []
        self.rear = 0
        self.front = 0
        self.length = length

    def isEmpty(self):
        """
        Checks whether queue is empty or not
        """
        if self.items == []:
            return True
        else:
            return False

    def isQueuefull(self):
        """
        checks whether queue is full or not
        """
        if len(self.items) == self.length:
            return True
        else:
            return False

    def enqueue(self, data):
        """
        inserts an element into the queue
        """
        if (self.isQueuefull()):
            # Queue is full then return print
            return print("queue is full")

        elif self.isEmpty():
            self.front = self.rear = 0
            self.items.append(data)
        else:
            self.rear += 1
            self.items.append(data)

    def dequeue(self):
        """
        removes an element from the queue
        """
        if self.isEmpty():
            return -1
        else:
            self.front += 1
            return self.items.pop(0)

    def display(self):
        """
        displays full queue
        """

        if self.items == []:
            return True
        else:
            print(self.items)

    @staticmethod
    def get_code():
        """
        :return: source code
        """
        return inspect.getsource(CircularQueue)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return " Time Complexity of enqueue: O(1)"\
               " Time Complexity of dequeue: O(1)"


class Deque(object):
    """
    :param length: pass queue length while making object otherwise default value will be 5

    """

    def __init__(self, length=5):
        """
        :param length: pass queue length while making object otherwise default value will be 5
        """
        self.items = []
        self.length = length

    def isFull(self):
        """
        checks whether queue is full or not
        """
        if len(self.items) == self.length:
            return True
        else:
            return False

    def isEmpty(self):
        """
        Checks whether queue is empty or not
        """
        if self.items == []:
            return True
        else:
            return False

    def enqueue_start(self, element):
        """
        inserts an element at the start of the queue
        """
        if (self.isFull()):
            return print("queue is full")
        else:
            self.items.insert(0, element)

    def enqueue_end(self, ele):
        """
        inserts an element at the end of the queue
        """
        if (self.isFull()):
            return print("queue is full")
        else:
            self.items.append(ele)

    def dequeue_start(self):
        """
        deletes an element from the start of the queue
        """
        if (self.isEmpty()):
            return print("empty queue..!")
        else:
            return self.items.pop(0)

    def dequeue_end(self):
        """
        deletes an element from the end of the queue
        """
        if (self.isEmpty()):
            return print("empty queue")
        else:
            return self.items.pop()

    def display(self):
        """
        displays full queue
        """
        if self.items == []:
            return True
        else:
            print(self.items)

    @staticmethod
    def get_code():
        """
        :return: source code 
        """
        return inspect.getsource(Deque)

    @staticmethod
    def time_complexity():
        """

        :return: time complexity
        """
        return " Time Complexity of all the above operations is constant : O(1)"
