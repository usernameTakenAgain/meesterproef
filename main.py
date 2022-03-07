import os
import serial

file = "data"

size = os.path.getsize(file)

def readbyte(pointer):
    f = open(file, "r")
    f.seek(pointer)
    re: str = f.read(1)
    return re


if __name__ == "__main__":
    pointer = 0

    connectie = serial.Serial('/dev/ttyACM0',baudrate=1200)
    print(connectie)
    while True:
        for x in range(size):
            returned = readbyte(pointer)
            print(returned.encode('utf-8').hex())
            connectie.write(bytes(returned, 'utf-8'))
            if pointer == size:
                pointer = 0
            else:
                pointer = pointer + 1
