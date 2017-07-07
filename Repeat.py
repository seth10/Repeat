import time

def repeat(action, interval, unless):
    timeout = time.time()
    while not unless():
        if time.time() > timeout:
            timeout = time.time() + interval
            action()
