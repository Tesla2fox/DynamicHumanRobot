# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:19:10 2018

@author: stef_leonA
"""


#import multiprocessing
#
#def hello():
#    print("qt invoke python")
#    
#def f(x):
#    return x*x
#cores = multiprocessing.cpu_count()
#
#pool = multiprocessing.Pool(processes=cores)
#
#xs=range(5)
#
#print(pool.map(f,xs))

#from multiprocessing import Process
#import time 
#import threading
#def work(name):
#    print('task<%s> is running' %name)
#    print('--0-')
#    time.sleep(2)
#    print('task<%s> is done' %name)
#
##for i in range(10):
##    p =Process(target=work,args=(str(i)))
##    print('0-0___',i)
##    p.start()
##    p.run()
#    
#p1 = Process(target=work,args=('egon',))
#p2 = Process(target=work,args=('alex',))
#
#
#p1.start()
#p2.start()
#
#p1.run()
#p2.run()

#
#
#work('0-0')
#print('wtf')


#from cython.parallel import prange,parallel,threadid
#
#cdef int i
#cdef in sum = 0



from multiprocessing import Pool
import time

def f(x):
    return x*x
if __name__ =='__main__':
    start =time.clock()
    
    with Pool(processes=7) as pool:
        pool.map(f,range(1000000))
    elapsed = (time.clock()-start)    
    print('time used :',elapsed)


    start1 =time.clock()
    
    for i in range(1000000):
        f(i)
    elapsed = (time.clock()-start1)    
    print('time used :',elapsed)
        
        
#        for i in pool.imap_unordered(f,range(1000)):
#            print(i)
            


#from multiprocessing import Process
#import os
#
#def info(title):
#    print(title)
#    print('moduleName:', __name__)
#    print('parent process :',os.getppid())
#    print('process id :',os.getpid())
#    
#def f(name):
#    info('function f')
#    print('hello',name)
#
#
