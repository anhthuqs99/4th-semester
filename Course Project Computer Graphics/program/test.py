from threading import Thread 
from time import time

def z_buff(a):
    s = 0
    for i in range(a):
        s += i 
    

def z_buff_a(a):
    s = 0
    for i in range(a):
        s += i 

A = 1000
t_begin = time()
z_buff(A)
z_buff_a(A)
t_end = time()
print(t_end - t_begin)

t_begin = time()
t1 = Thread(target = z_buff, args = (A,))
t2 = Thread(target = z_buff_a, args = (A,))
t1.start()
t2.start()
t1.join()
t2.join()
t_end = time()
print(t_end - t_begin)