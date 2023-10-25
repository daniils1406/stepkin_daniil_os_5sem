#!/usr/bin/python3
import time
import random
import os
import sys

def child():
    s = int(sys.argv[1])
    print(f'Child[{os.getpid()}]: I am started. My PID {os.getpid()}. Parent PID {os.getppid()}.')
    time.sleep(s)
    print(f'Child[{os.getpid()}]: I am ended. PID {os.getpid()}. Parent PID {os.getppid()}.')
    exit_status = random.randint(0, 1)
    os._exit(exit_status)

child()