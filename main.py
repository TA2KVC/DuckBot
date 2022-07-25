import utelegram
import network
import random

ssid = 'xxxxxxx'
password = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
token ='xxxxxxxx:yyyyyyyyyyyyyyyyyyyyy'

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

data=['https://someimagehostingsite/ordek.jpg',
'https://someimagehostingsite/ordek1.jpg',
'https://someimagehostingsite/ordek2.jpg',
'https://someimagehostingsite/ordek3.jpg']

def welcome(message):
    gif = "https://someimagehostingsite/hosgeldin.jpg"
    bot.photo(message['message']['chat']['id'], gif, '')
    vid = "https://someimagehostingsite/ordek.mp4"
    #bot.action(message['message']['chat']['id'], 'upload_video')
    bot.video(message['message']['chat']['id'], vid, 'VakVak created by Volkan TA2KVC\nClick /vakvak')
    #print(message)

def duckbot(message):
    ordek=random.choice(data)
    #bot.action(message['message']['chat']['id'], 'upload_photo')
    bot.photo(message['message']['chat']['id'], ordek, 'VakVak created by Volkan TA2KVC\nClick /vakvak')

bot = utelegram.ubot(token)
bot.register('Ördek', duckbot)
bot.register('ördek', duckbot)
bot.register('vakvak', duckbot)
bot.register('Vakvak', duckbot)
bot.register('/vakvak', duckbot)
bot.register('vak', duckbot)
bot.register('Vak', duckbot)
bot.register('/start', welcome)
bot.set_default_handler(welcome)
print('BOT HAZIR')
bot.listen()