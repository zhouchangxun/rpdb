#!/bin/python

import multiprocessing
import pdb
import rpdb
 
def child_process():
    print "Child-Process begin"
    dbg = rpdb.pdb()
    dbg.set_trace()
    var = "breakpoint1!"
    print 'do something'
    dbg.set_trace()
    print "chile exit!"
    return 0
 
def main_process():
    print "Parent-Process"
    p = multiprocessing.Process(target = child_process)
    p.start()
    pdb.set_trace()
    p.join()
    print "main exit!"
    return 0
 
if __name__ == "__main__":
    main_process()
