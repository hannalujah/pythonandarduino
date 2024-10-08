import serial
import time

arduino = serial.Serial(port='COM5',  baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    time.sleep(0.5)
    data = arduino.readline()
    return data


while True:
    x = input("Enter a number: \n")    
    if x == 'exit':
        arduino.close()
        exit()
    value  = int(write_read(x))
    print(value)

