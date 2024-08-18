
class MagicalContact:
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def describe(self):
        return f"Name: {self.__name}, Email: {self.__email}, Phone: {self.__phone_number}"

#bos ya sadiky elmentor ana 7awelt bekol el toroq enni akamel bas fashalt we kol shuwaya yetla3ly error ya sadiky al mentor