#!/usr/bin/python3

import random 
import time
import sys

N = random.randint(120, 180)

operations = ['+', '-', '*', '/']

for _ in range (N):
  x = random.randint(1, 9)
  y = random.randint(1, 9)
  op = random.choice(operations)
  sys.stdout.write(f"{x} {op} {y}\n")
  sys.stdout.flush()
  time.sleep(1)
