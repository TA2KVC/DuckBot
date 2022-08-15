import utelegram
import network
import makine
import twitter
import _thread

makine.bootled()

ssid = 'XXXXXXX'
password = 'xxxxxxxxxxxxxxxxxxxxxxxx'
token ='xxxxxxxxxxxxxxx:yyyyyyyyyyyyyyyyyyyyyyyyyy'

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
    ordek=twitter.otaduck()
    yt,tt=twitter.otatube()
    bot.photo(message['message']['chat']['id'], ordek, 'Vakvak created by Volkan TA2KVC\nClick /vakvak')
    makine.blink()
    twitter.tweet(ordek,yt,tt)
    
def volbot(message):
    yt,tt=twitter.otatube()
    vol = 'Volkan TA2KVC YouTube Bot\n'
    vol += tt
    vol += '\n'
    vol += yt
    bot.send(message['message']['chat']['id'], vol)
    makine.blink()

def catbot(message):
    cat=twitter.otacat()
    yt,tt=twitter.otatube()
    bot.photo(message['message']['chat']['id'], cat, 'Miiv created by Volkan TA2KVC\nClick /miyav')
    makine.blink()
    twitter.tweet(cat,yt,tt)

def dogbot(message):
    dog=twitter.otadog()
    yt,tt=twitter.otatube()
    bot.photo(message['message']['chat']['id'], dog, 'Puppy created by Volkan TA2KVC\nClick /hav')
    makine.blink()
    twitter.tweet(dog,yt,tt)

def cutebot(message):
    mix=twitter.otamix()
    yt,tt=twitter.otatube()
    bot.photo(message['message']['chat']['id'], mix, 'Mixx created by Volkan TA2KVC\nClick /mix')
    makine.blink()
    twitter.tweet(mix,yt,tt)

_thread.start_new_thread(makine.vreset, ())
bot = utelegram.ubot(token)
bot.register('Ördek', duckbot)
bot.register('Vakvak', duckbot)
bot.register('/vakvak', duckbot)
bot.register('/vak', duckbot)
bot.register('/miyav', catbot)
bot.register('/hav', dogbot)
bot.register('/mix', cutebot)
bot.register('/volkan', volbot)
bot.register('/start', welcome)
bot.set_default_handler(welcome)
print('BOT HAZIR')
bot.listen()
