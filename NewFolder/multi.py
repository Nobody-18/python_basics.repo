from ast import arguments
import os 
import time
from multiprocessing import Process
def sqno():
    for i in range(20):
        i*i
        time.sleep(0.1)
processes = []
num_pro = os.cpu_count()
for i in range(num_pro):
    p = Process(target=sqno )
    processes.append(p)
for p in processes:
    p.start()
for p in processes:
    p.join()
    
print('end main')