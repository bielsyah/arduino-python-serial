import serial

myArduino = serial.Serial('COM3',9600)

while True :
    # line = myArduino.readline().decode('utf-8').rstrip()
    # print(line)
    msg = input().encode()
    myArduino.write(msg)