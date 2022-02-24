import time

print(f'You have successfully loaded `my_time_library`:\nCurrent time: {time.ctime()}')

def current_time() -> str:
    return time.ctime()

