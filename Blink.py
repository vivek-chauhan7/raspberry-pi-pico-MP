from machine import Pin
from time import sleep
led = Pin(25,Pin.OUT) #build in led pin

while True:
    led(1)
    sleep(0.02)
    led(0)
    sleep(1)