import machine
import time
import twitter

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
    duck=twitter.otaduck()
    yt,tt=twitter.otatube()
    blink()
    twitter.tweet(duck,yt,tt)
    time.sleep(1)
    machine.reset()
    
def vreset():
    timer.init(period=3480000, callback=reset)
    
