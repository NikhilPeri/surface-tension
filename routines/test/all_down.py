import serial
from lib.wall import Wall
import time

def run(wall):
        wall.write([
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1],
        ])
        time.sleep(6)

if __name__ == '__main__':
    wall = Wall()
    run(wall)
