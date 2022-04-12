import threading
from threading import Thread
# to do multiprocessing instead of threading use multiprocessing, everything else is the same
import multiprocessing
from multiprocessing import Process
import time

def func(n):
	for i in range(n):
		print(i)
		time.sleep(0.5)

thread1 = threading.Thread(target=func, args=(5,)) # args must be a tuple
thread2 = threading.Thread(target=func, args=(5,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("DONE")
