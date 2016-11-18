import random
import time


class randomNum():
    def __init__(self):
        self.code_list = []
        for i in range(10):
            self.code_list.append(str(i))
        for i in range(65, 91):
            self.code_list.append(chr(i))
        for i in range(97, 123):
            self.code_list.append(chr(i))

    def makeNumber(self, num):
        myslice = random.sample(self.code_list, num)
        number = ''
        for n in myslice:
            number += n + ''
        return number


class randomNums():
    def __init__(self):
        self.code_list = []
        for i in range(10):
            self.code_list.append(str(i))

    def makeNumber(self, num):
        myslice = random.sample(self.code_list, num)
        number = ''
        for n in myslice:
            number += n + ''
        times = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        return times + '' + number

    def makeNumber1(self, num):
        myslice = random.sample(self.code_list, num)
        number = ''
        for n in myslice:
            number += n + ''

        myslice = random.sample(self.code_list, num)
        number1 = ''
        for n in myslice:
            number1 += n + ''

        times = time.strftime("%Y%m%d")
        return times + '' + number + '' + number1


if __name__ == '__main__':
    print randomNums().makeNumber1(2)
