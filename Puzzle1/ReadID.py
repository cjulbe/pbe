#!/usr/bin/env python
import os
import RPi.GPIO as GPIO
from mfrc522 import *

class Rfid_RC522:
    # return uid in hex str 
    def read_uid(self):
           reader= SimpleMFRC522()
           id= reader.read_id()
           id_hex= hex(id).upper()
           return id_hex

if __name__ == "__main__":
    try:
            print("Hold your card near the reader")
            rf= Rfid_RC522()
            uid= rf.read_uid()
            print("ID: %s\n" % (uid[2:10]))
    except KeyboardInterrupt:
            GPIO.cleanup()
            raise
