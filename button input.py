from machine import Pin
from time import sleep
led = Pin(25,Pin.OUT) #build in led pin
Sw = Pin(15, Pin.IN)

while True :
    if Sw.value() == 1 :
        led(1)
    else :
        led(0)