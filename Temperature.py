from time import sleep

# Get the temperature from the internal RP2040 temperature sensor.
Sensor_Temp = machine.ADC(4)

# this from Raspberry Pi Pico datasheet for the conversion factor.
CONVERSION_FACTOR = 3.3 / (65535)
while True:
    # Get a temperature reading.
    reading = Sensor_Temp.read_u16() * CONVERSION_FACTOR

    # Convert the temperature into degrees celsius.
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    sleep(1)