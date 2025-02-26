import RPi.GPIO as GPIO
import time 
#dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
p=GPIO.PWM(21,0.5)
p.start(1)
try:
    while True:
        t=float(input('Ввод='))
        p.ChangeDutyCycle(t)
        print(t*3.3/100)

finally:
    GPIO.output(21,0)
    p.stop()
    GPIO.cleanup()