#!/usr/bin/env python
from time import sleep
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
GPIO.cleanup()

try:
    while True:
        print("Hold a tag near the reader")
        id,text = reader.read()
        id_hex= hex(int(id))
        print("ID: %s\n" % (id_hex[2:10]).upper())
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
