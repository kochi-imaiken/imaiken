# LoRa communication with python

import sys
import serial
from time import sleep

# Function of send command
def sendCommand(ser, time, command):
    sleep(time)
    ser.write(command + "\r\n")

# Port open
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = None)

# Send set up command
sendCommand(ser, 1.00, "SKSREG S08 1A")
sendCommand(ser, 1.00, "SKSREG S01 12345678abcdef05")
sendCommand(ser, 1.00, "SKSREG S05 12345678")
sendCommand(ser, 3.00, "SKSETPSK 11111111222222223333333344444444")
sendCommand(ser, 1.00, "SKSREG S02 1")

try:
    # Receive loop start
    while 1:
        receive_data = ser.readline()
        print receive_data

        # Send data
        if "ERXBCN" in receive_data:
            ser.write("SKSEND 0000000000000000 5 aabbccddee" + "\r\n")
            print("********** SKSEND to Station **********" + "\r\n")

# Exit with [Ctrl + C]
except KeyboardInterrupt:
    ser.close()    #port close
    print ("\r\n" + "Bye")
    sys.exit
