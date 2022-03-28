import threading
import time

# print(threading.active_count())

def func(n):
    for i in range(n):
        print(i)
        time.sleep(0.5)

x = threading.Thread(target=func, args=(5,))
y = threading.Thread(target=func, args=(5,))

x.start()
y.start()

x.join()
y.join()

print("Done")
