class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__rear = -1
        self.__front = 0

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__rear == self.__max_size-1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full...Cannot enqueue any element!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty...Cannot dequeue any element!!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            print(data)

    def display(self):
        for i in range(self.__front, self.__rear + 1):
            print(self.__elements[i])


queue = Queue(4)

queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(9)
queue.enqueue(10)
queue.enqueue(7)

queue.dequeue()

#queue.display()

# dummy_queue = []
# q1 = [1,2,3]
# q2 = [4,5,6]
#
# while q1 not empty:
#     ele = q1.dequeue()
#     dummy_queue.append(ele)
#
# while q2 not empty:
#     ele = q2.dequeue()
#     dummy_queue.append(ele)
#
# print(dummy_queue)