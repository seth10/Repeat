import time

def repeat(action, interval, unless, delay=0.05):
    timeout = time.time()
    while not unless():
        if time.time() > timeout:
            timeout = time.time() + interval
            action()
        if delay:
            time.sleep(delay)
