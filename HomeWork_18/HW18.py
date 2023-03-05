import self as self


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
    u = "https://www.gismeteo.ua/weather-dnipro-5077/"
    c = "id_number 535366"
    def __init__(self,name,message,url=u,chat_id=c):
        super().__init__(name,message)
        self.url = url
        self.chat_id = chat_id

    def set_url(self):
        print(f"my url : {self.url}")
    def set_chat_id(self):
        print(f"My ID is: {self.chat_id}")
    def send_message(self):
        print(f"{self.name},{self.message}, i have {self.url} with {self.chat_id}")



u = TelegramBot("https://www.gismeteo.ua/weather-dnipro-5077/","weazer")
c = TelegramBot("id_number bla-bla-bla","535366")
tb=TelegramBot("Aleksandr", "How are you?")
tb.send_message()
u.set_url()
c.set_chat_id()