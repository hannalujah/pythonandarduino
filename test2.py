import time, datetime, serial, random
random.seed(time.time())
disturbance = [1,1,1,2,2,2,3,3,3,4,4,4]
random.shuffle(disturbance)

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=0.1)
if arduino.is_open:
    for i in range(len(disturbance)):
        dist_type = str(disturbance[i])
        arduino.write(bytes(dist_type,  'utf-8'))
        time.sleep(0.5)
        data = arduino.readline().decode('utf-8').strip('\r\n')
        if data == '':
            print('0')
        else:
            print(data)


arduino.close()
