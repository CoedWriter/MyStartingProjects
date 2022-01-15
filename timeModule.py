import flask
import numpy

import time

initializer = time.time()

k = 0
while k < 45:
    print("bhai...")
    time.sleep(2)
    k += 1

print("While loop took", time.time() - initializer,"seconds")

init2 = time.time()
for i in range(46):
    print("bhai...")
print(f"For loop took {time.time() - init2} seconds")


# ------------------------------
# localtime = time.asctime(time.localtime(time.time()))   #or time.asctime() bas!
# print(localtime)
# -------------------------
# time.sleep()