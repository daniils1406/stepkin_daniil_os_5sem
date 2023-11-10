 #!/usr/bin/python3

import os
import signal
import sys

pipe1 = os.pipe()
pipe0 = os.pipe()
pipe2 = os.pipe()
pid1 = os.fork()

if pid1 == 0:
    os.close(pipe1[0])
    os.dup2(pipe1[1], sys.stdout.fileno())  
    os.execl('producer', 'producer')

pid2 = os.fork()
if pid2 == 0:
    os.close(pipe0[1])
    os.dup2(pipe0[0], sys.stdin.fileno())  
    os.close(pipe2[0])
    os.dup2(pipe2[1], sys.stdout.fileno()) 
    os.execl("/usr/bin/bc", "bc")
os.close(pipe1[1])
os.close(pipe0[0])
os.close(pipe2[1])
produced_count = 0
def sigusr1_handler(signum, frame):
    global produced_count
    message = f"Produced: {produced_count}\n"
    sys.stderr.write(message)
    sys.stderr.flush()
signal.signal(signal.SIGUSR1, sigusr1_handler)
while True:
    data = os.read(pipe1[0], 1024)
    if not data:
        break
    os.write(pipe0[1], data)
    result = os.read(pipe2[0], 1024)
    arithmetic_expression = data.decode().strip()
    result = result.decode().strip()
    produced_count += 1
    sys.stdout.write(f"{arithmetic_expression} = {result}\n")
    sys.stdout.flush()
os.close(pipe1[0])
os.close(pipe0[1])
os.close(pipe2[0])

os.kill(pid1, signal.SIGTERM)
os.kill(pid2, signal.SIGTERM)
