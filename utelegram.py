import time
import gc
import ujson
import urequests


class ubot:
    
    def __init__(self, token, offset=0):
        self.url = 'https://api.telegram.org/bot' + token
        self.commands = {}
        self.default_handler = None
        self.message_offset = offset
        self.sleep_btw_updates = 3

        messages = self.read_messages()
        if messages:
            if self.message_offset==0:
                self.message_offset = messages[-1]['update_id']
            else:
                for message in messages:
                    if message['update_id'] >= self.message_offset:
                        self.message_offset = message['update_id']
                        break


    def send(self, chat_id, text):
        data = {'chat_id': chat_id, 'text': text}
        try:
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            response = urequests.post(self.url + '/sendMessage', json=data, headers=headers)
            response.close()
            return True
        except:
            return False
        
    def photo(self, chat_id, photo, caption):
        data = {'chat_id': chat_id, 'photo': photo, 'caption': caption}
        try:
            response = urequests.post(self.url + '/sendPhoto', json=data)
            response.close()
            return True
        except:
            return False
        
    def video(self, chat_id, video, caption):
        data = {'chat_id': chat_id, 'video': video, 'caption': caption}
        try:
            response = urequests.post(self.url + '/sendVideo', json=data)
            response.close()
            return True
        except:
            return False

    def anime(self, chat_id, animation, caption):
        data = {'chat_id': chat_id, 'animation': animation, 'caption': caption}
        try:
            response = urequests.post(self.url + '/sendAnimation', json=data)
            response.close()
            return True
        except:
            return False

    def audio(self, chat_id, audio):
        data = {'chat_id': chat_id, 'audio': audio}
        try:
            response = urequests.post(self.url + '/sendAudio', json=data)
            response.close()
            return True
        except:
            return False

    def voice(self, chat_id, voice):
        data = {'chat_id': chat_id, 'voice': voice}
        try:
            response = urequests.post(self.url + '/sendVoice', json=data)
            response.close()
            return True
        except:
            return False
        
    def action(self, chat_id, action):
        data = {'chat_id': chat_id, 'action': action}
        try:
            response = urequests.post(self.url + '/sendChatAction', json=data)
            response.close()
            return True
        except:
            return False
        
    def read_messages(self):
        result = []
        self.query_updates = {
            'offset': self.message_offset + 1,
            'limit': 1,
            'timeout': 40,
            'allowed_updates': ['message']}

        try:
            update_messages = urequests.post(self.url + '/getUpdates', json=self.query_updates).json() 
            if 'result' in update_messages:
                for item in update_messages['result']:
                    result.append(item)
            return result
        except (ValueError):
            return None
        except (OSError):
            print("OSError: request timed out")
            return None

    def listen(self):
        while True:
            self.read_once()
            time.sleep(self.sleep_btw_updates)
            gc.collect()

    def read_once(self):
        messages = self.read_messages()
        if messages:
            if self.message_offset==0:
                self.message_offset = messages[-1]['update_id']
                self.message_handler(messages[-1])
            else:
                for message in messages:
                    if message['update_id'] >= self.message_offset:
                        self.message_offset = message['update_id']
                        self.message_handler(message)
                        break
    
    def register(self, command, handler):
        self.commands[command] = handler

    def set_default_handler(self, handler):
        self.default_handler = handler

    def set_sleep_btw_updates(self, sleep_time):
        self.sleep_btw_updates = sleep_time

    def message_handler(self, message):
        if 'text' in message['message']:
            parts = message['message']['text'].split(' ')
            if parts[0] in self.commands:
                self.commands[parts[0]](message)
            else:
                if self.default_handler:
                    self.default_handler(message)
