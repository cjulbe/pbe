#!/usr/bin/env python
from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Rfid_RC522:
    # return uid in hex str 
    def read_uid(self):
           reader= SimpleMFRC522()
           GPIO.cleanup()
           id,text = reader.read()
           id_hex= hex(int(id)).upper()
           return id_hex

if __name__ == "__main__":
    try:
        while True:
            print("Hold a tag near the reader")
            rf= Rfid_RC522()
            uid= rf.read_uid()
            print("ID: %s\n" % (uid[2:10]))
            sleep(5)
    except KeyboardInterrupt:
            GPIO.cleanup()
            raise
