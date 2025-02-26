import RPi.GPIO as GPIO
import time 
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac,0)
GPIO.cleanup()
def d2b(value):
 return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac, GPIO.OUT)
    p=float(input("period= "))
    sd=p/512
    while True:
        for v in range(256):
            GPIO.output(dac,d2b(v))
            time.sleep(sd)
        for v in range(255,-1,-1):
            GPIO.output(dac,d2b(v))
            time.sleep(sd)

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()