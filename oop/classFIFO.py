from collections import deque


class Queue:
    def __init__(self):
        self.myQueue = deque()

    def enterRow(self, val):
        return self.myQueue.append(val)

    def exitRow(self):
        if len(self.myQueue) > 0:
            return self.myQueue.popleft()
        else:
            print('\nEmpty queue!\n')
            pass

    def __repr__(self):
        return f"QUEUE => [{', '.join(str(x) for x in self.myQueue)}]"

    def starQueue(self):
        while 1 == 1:
            command = int(input('Choose an option:\n1- Enter Queue\n2- Exit Queue\n3- Breack\n==> '))
            if command == 1:
                self.enterRow(1)
            elif command == 2:
                self.exitRow()
            else:
                exit = int(input('Exit ?\n0-No\n1-Yes\n==> '))
                if exit == 0:
                    pass
                else:
                    print(f'Finish => {self.myQueue}\nTotal => {sum(self.myQueue)}')
                    break


processQueue = Queue()
processQueue.starQueue()

