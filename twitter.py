import urequests
                  
class twiit:
    
    def __init__(self):
        self.url = "https://maker.ifttt.com/trigger/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx?value1="
        
    def tweet(self, tweet , timeout=10):
        try:
            response = urequests.post(self.url + tweet)
            response.close()
            return True
        except:
            return False