import os
import sys
import time
import datetime
import calendar
import random
import math
import statistics
import json

# OS module
print(os.getcwd())
print(os.listdir())
print(os.name)
# print(os.uname())
print(os.getlogin())


# sys module
print(sys.path)
print(sys.platform)
print(sys.version)

# time module
print(time.time())
print(time.localtime())
# YYY-MMM-DDD H:M:S
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

# date time module
print(datetime.datetime.now())


# calendar
print(calendar.month(2022, 9))

# random module
print(random.random())
print(random.choice([1, 4, 65, 6, 7]))
print(random.sample(range(1, 10), 4))


# statistics
print(statistics.mean([1, 3, 5, 2, 6, 7]))
print(statistics.median([1, 3, 5, 2, 6, 7]))
print(statistics.stdev([1, 3, 5, 2, 6, 7]))

# json module
js_str = '{"name": "John", "age": "30"}'
print(json.loads(js_str))
print(json.dumps(json.loads(js_str)))
