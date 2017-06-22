from datetime import datetime


class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_mssge = "Hey! i'm using spyChat"


class ChatMssg:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Pankhuri', 'Ms.', 21, 4.5)

friend_one = Spy('Avinash', 'Dr.', 4.8, 25)
friend_two = Spy('shefali', 'Ms.', 4.3, 21)
friend_three = Spy('Pallavi', 'Ms.', 4.9, 23)


friends = [friend_one, friend_two, friend_three]