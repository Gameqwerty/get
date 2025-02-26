import RPi.GPIO as GPIO
import time 
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
t=0
def d2b(value):
 return [int(bit) for bit in bin(value)[2:].zfill(8)]
try:
    while True:
        t=input()
        if t=="q":
            break
        try:
            v=int(t)
            if v<0:
                print("ввод отрицательного значения")
                continue
            elif v>255:
                print("превышение значения")
            else:
                GPIO.output(dac,d2b(v))
                print(3.3*v/256)
        except ValueError:
            print('Не число')
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()

#GPIO.cleanup()
#print(d2b(10))