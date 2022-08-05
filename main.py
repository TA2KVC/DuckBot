import utelegram
import network
import random
import makine
import twitter
import _thread
from ducks import data
from cats import cata
from dogs import kata
from cute import mixe

makine.bootled()

ssid = 'xxxxxxxxxx'
password = 'xxxxxxxxxxxx'
token ='xxxxxxx:yyyyyyyyyyyyyyyyyyyyy'

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)
print("Bağlanıyor...")
while sta_if.isconnected() == False:
    pass
print("Bağlandı!")
status1 = sta_if.config('ssid')
print( 'Wifi SSID :' + status1 )
status2 = sta_if.ifconfig()
print( 'IP Adresi :' + status2[0] )

def welcome(message):
    gif = "https://ibb.co/hXvchZt"
    bot.photo(message['message']['chat']['id'], gif, '')
    vid = "https://user-images.githubusercontent.com/62475996/180663340-4099a88c-d84e-437c-a984-2f6908380520.mp4"
    #bot.action(message['message']['chat']['id'], 'upload_video')
    bot.video(message['message']['chat']['id'], vid, 'Vakvak created by Volkan TA2KVC\nClick /vakvak')
    makine.blink()
    #print(message)

def duckbot(message):
    ordek=random.choice(data)
    bot.photo(message['message']['chat']['id'], ordek, 'Vakvak created by Volkan TA2KVC\nClick /vakvak')
    makine.blink()
    twit.tweet(ordek)

def catbot(message):
    cat=random.choice(cata)
    bot.photo(message['message']['chat']['id'], cat, 'Miyav created by Volkan TA2KVC\nClick /miyav')
    makine.blink()
    twit.tweet(cat)

def dogbot(message):
    dog=random.choice(kata)
    bot.photo(message['message']['chat']['id'], dog, 'Puppy created by Volkan TA2KVC\nClick /hav')
    makine.blink()
    twit.tweet(dog)

def cutebot(message):
    mix=random.choice(mixe)
    bot.photo(message['message']['chat']['id'], mix, 'Mixx created by Volkan TA2KVC\nClick /mix')
    makine.blink()
    twit.tweet(mix)

_thread.start_new_thread(makine.vreset, ())

twit = twitter.twiit()
bot = utelegram.ubot(token)
bot.register('Ördek', duckbot)
bot.register('ördek', duckbot)
bot.register('vakvak', duckbot)
bot.register('Vakvak', duckbot)
bot.register('/vakvak', duckbot)
bot.register('vak', duckbot)
bot.register('/vak', duckbot)
bot.register('Vak', duckbot)
bot.register('/miyav', catbot)
bot.register('/hav', dogbot)
bot.register('/mix', cutebot)
bot.register('/start', welcome)
bot.set_default_handler(welcome)
print('BOT HAZIR')
bot.listen()