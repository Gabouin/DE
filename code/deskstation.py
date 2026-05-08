import dht
from machine import Pin
from machine import Pin, SoftI2C, ADC
from ssd1306 import SSD1306_I2C
import time

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

temphum = dht.DHT22(Pin(14))

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

ldr = ADC(Pin(26))

trig = Pin(28, Pin.OUT)
echo = Pin(27, Pin.IN)

def get_distance():
    
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()
    
    timing = machine.time_pulse_us(echo, 1, 30000) # Timeout 30ms
    
    distance = (timing * 0.0343) / 2
    return distance

while True:
    dist = get_distance()

    if 0 < dist < 50:

        temphum.measure()
        temphum.temperature()
        temphum.humidity()

        ldr_value = ldr.read_u16()
        oled.fill(0)

        if ldr_value >= 32727: # equal <= 100 lux
            
            oled.text("Bright : {}".format(int(ldr_value)), 7, 0)
            oled.text("Please turn on", 7, 20)
            oled.text("the light !", 25, 40)
            oled.show()
        else:
            oled.fill(0)
            oled.text("Hi Sir !", 32, 0)   
            oled.text("Humidity: {}%".format(temphum.humidity()), 0, 25)
            oled.text("Temp: {}C".format(temphum.temperature()), 14, 50)
            oled.show()
            time.sleep(5)
    else:
        oled.fill(0)
        oled.text("Nobody Detected", 5, 10)
        oled.text("Shutdowned", 25, 30)
        oled.show()
