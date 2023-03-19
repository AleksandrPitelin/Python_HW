import self as self


class Bot:
    def __init__(self, name):
        self.name = name
    def send_message(self,message):
        print(message)

    def say_name(self):
        print(f"My name is {self.name}")

b=Bot("Aleks")
b.say_name()
b.send_message("Hello")


class TelegramBot(Bot):
    def __init__(self,name,url=None,chat_id=None):
        super().__init__(name)
        self.url = url
        self.chat_id = chat_id

    def set_url(self, url):
        self.url = url
    def set_chat_id(self,chat_id):
        self.chat_id = chat_id
    def send_message(self, message):
        print(f"{message}, i have URL: {self.url} with {self.chat_id}")


tb=TelegramBot("Aleksandr","https://www.gismeteo.ua/weather-dnipro-5077/", "nomer XXXXXXX")
tb.send_message("I am a TelegramBot")
