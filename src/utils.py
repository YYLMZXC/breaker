import time

def getCurrentTime():
    # 获取当前时间的时间戳（秒）
    t = time.time()
     # 将时间戳转换为毫秒，并返回整数值
    return int(t * 1000)

