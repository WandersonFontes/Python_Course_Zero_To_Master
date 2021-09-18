from collections import deque


class Battery:
    def __init__(self):
        self.myBattery = deque()

    def insertBattery(self, val):
        return self.myBattery.append(val)

    def removeBattery(self):
        return self.myBattery.pop()

    def __repr__(self):
        return f"BATTERY => [{', '.join(str(x) for x in self.myBattery)}]"

    def startBattery(self):
        while 1 == 1:
            command = int(input('Choose an option:\n1- Insert battery\n2- Remove Battery\n3- Exit\n==> '))
            if command == 1:
                self.insertBattery('1')
            elif command == 2:
                self.removeBattery()
            else:
                exit = int(input('Exit ?\n0-No\n1-Yes\n==> '))
                if exit == 0:
                    pass
                else:
                    print(f'Finish => {self.myBattery}\nTotal => {sum(self.myBattery)}')
                    break


processQueue = Battery()
processQueue.startBattery()

