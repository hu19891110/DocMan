import time


def getDateTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

