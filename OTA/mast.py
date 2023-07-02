import twitter
import requests
import os
import telebot
#import urllib.parse
import time
import threading
import schedule
import subprocess
import datetime
from collections import defaultdict, deque
import random
from mastodon import Mastodon


bot = telebot.TeleBot('xxxxxxxxxxxxxxxxxxxxxxxxxx') #TA2KVCMASTOBOT

#mastodon = Mastodon(
#    access_token = 'vakvak_bot.secret',
#    api_base_url = 'https://mastodon.online'
#)

ta2kvc = Mastodon(
    access_token = 'ta2kvc.secret',
    api_base_url = 'https://mastodon.online'
)


def foto(futu):
    file = 'temp.jpg'
    request = requests.get(futu, stream=True)
    if request.status_code == 200:
        with open(file, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    return file


def fotoo(futuu):
    filee = 'logo.jpg'
    request = requests.get(futuu, stream=True)
    if request.status_code == 200:
        with open(filee, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    return filee


def selam():
    hour = datetime.datetime.now().hour
    slm = "İyi geceler" if 0<=hour<5 else "Günaydın" if hour<=10 else "İyi günler" if hour<=16 else "İyi akşamlar" if hour<=21 else "İyi geceler"
    return slm


@bot.message_handler(commands=['start','help'])
def welcome(message):
    gif = "https://i.ibb.co/cbdwMC7/IMG-20220725-021219.jpg"
    bot.send_photo(message.chat.id, gif)
    vid = "https://github.com/TA2KVC/DuckBot/raw/main/OTA/duckvid.mp4"
    bot.send_video(message.chat.id, vid)


@bot.message_handler(commands=['vak','vakvak'])
@bot.message_handler(regexp="Ördek")
@bot.message_handler(regexp="Vak")
@bot.message_handler(regexp="Vakvak")
def duckbot(message):
    ordeek=twitter.otaduck()
    ordek = foto(ordeek)
    slm = selam()
    tip = "Sevgili Ördeksever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, ordeek, 'Vakvak created by Volkan TA2KVC\nClick /vakvak')
    stat = slm+" "+tip+"\n\n"+tt+"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    medya = ta2kvc.media_post(ordek)
    ta2kvc.status_post(status=stat, media_ids=medya)


@bot.message_handler(commands=['miyav'])
def catbot(message):
    caat=twitter.otacat()
    cat = foto(caat)
    slm = selam()
    tipc = "Sevgili Kedisever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, caat, 'Miiv created by Volkan TA2KVC\nClick /miyav')
    stat = slm+" "+tipc+"\n\n"+tt+"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    medya = ta2kvc.media_post(cat)
    #medyaa = mastodon.media_post(cat)
    ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


@bot.message_handler(commands=['hav'])
def dogbot(message):
    doog=twitter.otadog()
    dog = foto(doog)
    slm = selam()
    tipd = "Sevgili Patisever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, doog, 'Puppy created by Volkan TA2KVC\nClick /hav')
    stat = slm+" "+tipd+"\n\n"+tt+"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    medya = ta2kvc.media_post(dog)
    #medyaa = mastodon.media_post(dog)
    ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


@bot.message_handler(commands=['mix'])
def cutebot(message):
    miix=twitter.otamix()
    mix = foto(miix)
    slm = selam()
    tipx = "Sevgili Hayvansever Dostlarım. \U0001F986"
    yt,tt=twitter.otatube()
    bot.send_photo(message.chat.id, miix, 'Mixx created by Volkan TA2KVC\nClick /mix')
    stat = slm+" "+tipx+"\n\n"+tt+"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    medya = ta2kvc.media_post(mix)
    #medyaa = mastodon.media_post(mix)
    ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)



@bot.message_handler(commands=['istek'])
def istek(message):
    sar = "https://ibb.co/m8ZHsSz"
    bot.send_photo(message.chat.id, sar)


@bot.message_handler(regexp="http://www.youtube.com")
def volbot2(message):
    ordeek = twitter.otaduck()
    ordek = foto(ordeek)
    slm = selam()
    tips = "Sevgili Ördeksever Dostlarım. \U0001F986"
    nam = message.chat.first_name
    name = urllib.parse.quote(nam)
    link = message.text
    title = twitter.tubeparse(link)
    tit = urllib.parse.quote(title)
    voli = 'Sevgili ' + nam + '; \n'
    voli += 'istek parcan: \n' + title + ' \n'
    voli += 'birazdan twitlenecek..!'
    bot.send_message(message.chat.id, voli)
    stat = slm+" "+tips+"\n\n"+nam+" 'ın dinlemek istediği şarkı: \n"+title+"\n"+link+"\n\n\U0001F986\U0001F916 @VakvakBot"
    medya = ta2kvc.media_post(ordek)
    #medyaa = mastodon.media_post(ordek)
    ta2kvc.status_post(status=stat, media_ids=medya)
    #mastodon.status_post(status=stat, media_ids=medyaa)


def botlisten():
    bot.infinity_polling(interval=0, timeout=20)


def auto():
    oto,tipo=twitter.otofunc()
    slm = selam()
    yt,tt=twitter.otatube()
    foti = foto(oto)
    hvd = slm +" "
    hvd += "Sevgili " + tipo + "\n"
    stat = hvd+"\n\""+tt+"\"\n"+yt+"\n\n\U0001F986\U0001F916 @VakvakBot"
    medya = ta2kvc.media_post(foti)
    ta2kvc.status_post(status=stat, media_ids=medya)


@bot.message_handler(commands=['oto'])
def oto(message):
    auto()
    bot.send_message(message.chat.id, "Otomatik tweet gonderildi.")


def botstop():
    botstop = system_call_with_response("sudo systemctl stop mastodonbot")
    return botstop


def vakbotstatus():
    botstatus = system_call_with_response("systemctl status mastodonbot")
    return botstatus


def botreset():
    botstop = system_call_with_response("sudo systemctl restart mastodonbot")
    return botreset


@bot.message_handler(commands=['botstop'])
def botstp(message):
    bot.send_message(message.chat.id, "VolPi4 bot durduruldu.")
    botstop()


@bot.message_handler(commands=['botrestart'])
def botrst(message):
    bot.send_message(message.chat.id, "VolPi4 bot yeniden baslatildi.")
    botreset()


@bot.message_handler(commands=['botstatus'])
def botstatus(message):
    status = vakbotstatus()
    bot.send_message(message.chat.id, status)


@bot.message_handler(commands=['ata'])
def atato(message):
    ata()
    bot.send_message(message.chat.id, "Mustafa Kemal ATATÜRK...")


def ata():
    ata1,ata2,ata3 = twitter.otatubeski()
    atam = "Ebedi Başkomutan, Ölümsüz Türk... \n"
    atamm = "\" " +ata3+ " \""
    atamm += "\n\n"
    atamm += ata2
    ataa1 = foto(ata1)
    stat = atam+"\n"+atamm+"\n"
    medya = ta2kvc.media_post(ataa1)
    ta2kvc.status_post(status=stat, media_ids=medya)


@bot.message_handler(commands=['havaa'])
def havauto(message):
    accuhava()
    bot.send_message(message.chat.id, "Hava durumu bilgileri tweetlenecek...")

def accuhava():
    info,scak,nem,rzghz,rzgyn = twitter.accu()
    otoo,tipo=twitter.otofunc()
    slm = selam()
    oto = foto(otoo)
    hvd = slm +" "
    hvd += "Sevgili " + tipo + "\n"
    hvdu = "Başkentimiz Ankara'nın hava durumu: \n"
    hvdu += "Gökyüzü : " +info + "\n"
    hvdu += "Sıcaklık : " +scak + " °C\n"
    hvdu += "Nem : %" +nem + "\n"
    hvdu += "Rüzgar : " +rzghz+ " km/s hızla " +rzgyn+ " yönünde\n"
    stat = hvd+"\n"+hvdu+"\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    medya = ta2kvc.media_post(oto)
    ta2kvc.status_post(status=stat, media_ids=medya)


@bot.message_handler(commands=['hava'])
@bot.message_handler(regexp="Hava")
@bot.message_handler(regexp="hava")
def havadurumu(message):
    nam = message.chat.first_name
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Hatalı işlem yaptınız.. Kullanımı: hava sehirismi")
        return
    citya = args[1]
    city = citya.title()
    info,scak,nem,rzghz,rzgyn = twitter.accukod(city)
    hvvi = 'Sevgili ' + nam + '; \n'
    hvvi += "" +city + ' şehrinin hava durumu bilgisi \n'
    hvvi += 'birazdan twitlenecek..!'
    bot.send_message(message.chat.id, hvvi)
    otoo,tipo=twitter.otofunc()
    oto = foto(otoo)
    slm = selam()
    hvvd = slm
    hvvd += " Sevgili " + nam +"; \n"
    hvvdu = "Hava durumunu öğrenmek istediğin " +city+ " şehrinin bilgileri: \n"
    hvvdu += "Gökyüzü : " +info + "\n"
    hvvdu += "Sıcaklık : " +scak + " °C\n"
    hvvdu += "Nem : %" +nem + "\n"
    hvvdu += "Rüzgar : " +rzghz+ " km/s hızla " +rzgyn+ " yönünde\n"
    stat = hvvd+"\n"+hvvdu+"\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    medya = ta2kvc.media_post(oto)
    ta2kvc.status_post(status=stat, media_ids=medya)
    bot.reply_to(message, hvvdu)


@bot.message_handler(commands=['piyasa'])
def piyssa(message):
    piysa()
    bot.send_message(message.chat.id, "Piyasa bilgileri birazdan tweetlenecek...")

def piysa():
    usa,uss,eua,eus,aua,aus,aga,ags = twitter.piyasa()
    borsa = twitter.borsa()
    tarh = datey()
    ordeek = twitter.otaduck()
    ordek = foto(ordeek)
    pyss = "Piyasalar: \n"
    pyss += "\U0001F986 Amerikan Ördeği :  " +usa+ "  -  " +uss+ "\n"
    pyss += "\U0001F986 Avrupa Ördeği :  " +eua + "  -  " +eus+ "\n"
    pyss += "\U0001F986 Altın Ördek :  " +aua + "  -  " +aus+ "\n"
    pyss += "\U0001F986 Gümüş Ördek :  " +aga + "  -  " +ags+ "\n"
    pyss += "\U0001F986 B-Ördek100 :  " +borsa+ "\n\n"
    pyss += tarh
    stat = pyss+"\n\U0001F986\U0001F916 @VakvakBot\U00002122"
    medya = ta2kvc.media_post(ordek)
    ta2kvc.status_post(status=stat, media_ids=medya)



def isimi():
    ordeek = twitter.otaduck()
    ordek = foto(ordeek)
    ff = twitter.kizisimci()
    mm = twitter.erkisimci()
    hvdu = "Bugün yumurtadan çıkan ördekler için isim önerileri: \n\n"
    hvdu += "Kız Ördek: " +ff+ "\n"
    hvdu += "Erkek Ördek : " +mm+ "\n"
    stat = hvdu+"\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    medya = ta2kvc.media_post(ordek)
    ta2kvc.status_post(status=stat, media_ids=medya)


@bot.message_handler(commands=['isim'])
def isimlik(message):
    isimi()
    bot.send_message(message.chat.id, "isimler birazdan tweetlenecek...")


@bot.message_handler(commands=['isimci'])
def isimci(message):
    args = message.text.split()
    if len(args) < 3:
        bot.reply_to(message, "Hata! Kullanım: /isimci [kız ismi] [erkek ismi]")
        return
    kiz = args[1]
    ff = kiz.title()
    erkek = args[2]
    mm = erkek.title()
    ordeek = twitter.otaduck()
    ordek = foto(ordeek)
    nam = "Bugün yumurtadan çıkan ördekler için isim önerileri: \n\n"
    nam += "Kız Ördek: " +ff+ "\n"
    nam += "Erkek Ördek : " +mm+ "\n"
    stat = nam + "\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    medya = ta2kvc.media_post(ordek)
    ta2kvc.status_post(status=stat, media_ids=medya)
    bot.send_message(message.chat.id, "isimler birazdan twitlenecek...")


@bot.message_handler(commands=['places'])
def placeoto(message):
    places()
    bot.send_message(message.chat.id, "Manzaralar twitleniyor...")


def places():
    plink,pdat = twitter.place()
    plll = "Dünya Ördeklerinin yaşadığı en güzel yerler: \n\n"
    plll+= "\" " +pdat+ " \"\n"
    flink = foto(plink)
    stat = plll + "\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    medya = ta2kvc.media_post(flink)
    ta2kvc.status_post(status=stat, media_ids=medya)


@bot.message_handler(commands=['yemek'])
def pisiroto(message):
    pisir()
    bot.send_message(message.chat.id, "Yemekler twitleniyor...")


def pisir():
    crb=twitter.corba()
    ymk=twitter.yemek()
    ymk2=twitter.yemek()
    slt=twitter.salata()
    ick=twitter.icki()
    tat=twitter.tatli()
    ymkft="https://i.ibb.co/tm4Cs7H/yemek2.gif"
    neymk = "\U0001F986 \U0001F372  Akşam Ne Pişireceğiz?  \U0001F372 \U0001F986\n\n"
    neymk += "\U0001F963 " +crb + "\n"
    neymk += "\U0001F372 " +ymk + " veya " +ymk2 + "\n"
    neymk += "\U0001F957 " +slt + "\n"
    neymk += "\U0001F36E " +tat + "\n"
    neymk += "\U0001F379 " +ick + "\n\n"
    ymfot = foto(ymkft)
    stat = neymk + "\n \U0001F986\U0001F916 @VakvakBot\U00002122"
    medya = ta2kvc.media_post(ymfot)
    ta2kvc.status_post(status=stat, media_ids=medya)


def system_call_with_response(command):
    with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE) as task:
        output = task.stdout.read()
        task.wait()
        return output.decode("utf-8").strip()


def datey():
    cmnd = "date "+"\"+%d.%m.%Y  %H:%M\""
    deyt = system_call_with_response(cmnd)
    return deyt


t1=threading.Thread(target=botlisten)
schedule.every(59).minutes.do(auto)
schedule.every(61).minutes.do(piysa)
schedule.every().day.at("19:40").do(ata)
schedule.every().day.at("09:00").do(places)
schedule.every().day.at("09:01").do(isimi)
schedule.every().day.at("09:02").do(piysa)
schedule.every().day.at("09:03").do(accuhava)
schedule.every().day.at("12:05").do(pisir)
schedule.every(1).hours.do(accuhava)
t1.start()


while True:
    schedule.run_pending()
    #respondToTweet()
    time.sleep(30)

