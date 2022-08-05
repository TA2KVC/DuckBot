import machine
import time
import random
import twitter
from ducks import data

twit = twitter.twiit()
timer = machine.Timer()
led = machine.Pin('LED', machine.Pin.OUT)
resetlog = time.time()

def bootled():
    led.on()
    time.sleep(3)
    led.off()
    
def blink():
    for v in range(15):
        led.on()
        time.sleep(0.04)
        led.off()
        time.sleep(0.04)
            
def reset(timer):
    duck=random.choice(data)
    blink()
    twit.tweet(duck)
    print("Auto tweet sent!")
    time.sleep(1)
    machine.reset()
    
def vreset():
    timer.init(period=3480000, callback=reset)
