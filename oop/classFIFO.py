from collections import deque


class Queue:
    def __init__(self):
        self.myQueue = deque()

    def enterRow(self, val):
        return self.myQueue.append(val)

    def exitRow(self):
        return self.myQueue.popleft()

    def __repr__(self):
        return f"FILA => [{', '.join(str(x) for x in self.myQueue)}]"

    def starQueue(self):
        while 1 == 1:
            command = int(input('Choose an option:\n1- Enter Queue\n2- Exit Queue\n3- Breack\n==> '))
            if command == 1:
                self.enterRow('1')
            elif command == 2:
                self.exitRow()
            else:
                print(f'Finish => {processQueue}\nTotal => {sum(processQueue)}')
                break


processQueue = Queue()
processQueue.starQueue()

