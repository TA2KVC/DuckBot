import urequests
import random

def tweet(val1, val2 , val3, timeout=15):
    try:
        url = "https://maker.ifttt.com/trigger/vakvak/with/key/xxxxxxxxIFTTT_SIFRExxxxxxxx?"
        response = urequests.post(url + "value1=" + val1 + "&" + "value2=" + val2 + "&" + "value3=" + val3)
        response.close()
        return True
    except:
        return False

def otaduck(timeout=15):
    try:
        online = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/ducks.py")
        data = (online.text).splitlines()
        ota = random.choice(data)
        online.close()
        return ota
    except:
        return False

def otacat(timeout=15):
    try:
        online1 = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/cats.py")
        data1 = (online1.text).splitlines()
        ota1 = random.choice(data1)
        online1.close()
        return ota1
    except:
        return False

def otadog(timeout=15):
     try:
        online2 = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/dogs.py")
        data2 = (online2.text).splitlines()
        ota2 = random.choice(data2)
        online2.close()
        return ota2
     except:
        return False

def otamix(timeout=15):
    try:
        online3 = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/cute.py")
        data3 = (online3.text).splitlines()
        ota3 = random.choice(data3)
        online3.close()
        return ota3
    except:
        return False

def otatube(timeout=15):
    try:
        online4 = urequests.get("https://raw.githubusercontent.com/TA2KVC/DuckBot/main/OTA/list.txt")
        data4 = (online4.text).splitlines()
        ota4 = random.choice(data4)
        tup = ota4
        tube = tup.split(",",1)
        val2 = tube[0]
        val3 = tube[1]
        online4.close()
        return val2,val3
    except:
        return False
