class Bot:
    def __init__(self, name, message):
        self.name = name
        self.message = message
    def send_message(self):
        print(f"{self.name} say {self.message}")

    def say_name(self):
        print(f"My name is {self.name}")

n = Bot("Aleksandr", "I'm study")
m = Bot("Hello", "How are you?")
n.say_name()
m.send_message()


class TelegramBot(Bot):
    def __init__(self,url,chat_id):
        self.url = url
        self.chat_id = chat_id
    def set_url(self):
        print(f"my url : {self.url}")
    def set_chat_id(self):
        print(f"My ID is: {self.chat_id}")

    def send_message(self):
        super.__init__(self.message,self.name)
        print(f"{self.message},{self.name} and i have {self.url} with {self.chat_id} ")



url = TelegramBot("https://www.gismeteo.ua/weather-dnipro-5077/","weazer")
chat = TelegramBot("id_number bla-bla-bla","535366")
url.set_url()
chat.set_chat_id()