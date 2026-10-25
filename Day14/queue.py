class QueueError(Exception):
    pass

class Queue:

    def __init__(self):
        self.__queue_list = []

    def put(self, elem):
        self.__queue_list.insert(0, elem)

    def get(self):
        if len(self.__queue_list) > 0:
            val = self.__queue_list[-1]
            del self.__queue_list[-1]
            return val

        raise QueueError("Queue is empty")

    def display(self):
        print(self.__queue_list)

president = Queue()
president.put("Ranil")
president.put("Maninda")
president.put("Malith")
president.put("Namal")
president.put("Roshitha")
president.display()

try:
    print(president.get())

except QueueError as e:
    print(e)
