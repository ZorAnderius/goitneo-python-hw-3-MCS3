from colorama import Fore

from .Name import Name
from .Phone import Phone


class Record:
    def __init__(self, name: str, phone: str=''):
        self.__name = Name(name)
        if phone:
            phone = Phone(phone)
            self.__phones = [phone]
        else:
            self.__phones = []

    @property
    def name(self) -> Name:
        return self.__name

    @name.setter
    def set_name(self, name: str):
        self.__name = Name(name)

    @property  
    def phones(self) -> list[Phone]:
        return self.__phones

    @phones.setter
    def set_phones(self, phones: list[Phone]):
        self.__phones = phones

    def __repr__(self) -> str:
        if self.phones:  
            str1 = Fore.YELLOW + "Contact name:   "
            str2 = Fore.LIGHTMAGENTA_EX + str(self.name)
            str3 = Fore.YELLOW + "phones: "
            str4 = Fore.WHITE + '; '.join(phone.value for phone in self.phones)
            return "{0}{1: >15} {2}\n".format(str1,  str2, (str3 + str4))
        if not self.phones and self.name.name is None:   
            return 'None'
        return f"{self.name}: Phonebook is empty"

    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        if new_phone.phone in self.phones:
            raise ValueError(Fore.YELLOW + f"Phone {phone} is already in your phonebook. If you want to change phone use 'change' operation")
        elif new_phone.phone:
            self.__phones.append(new_phone)
            

    def find_phone(self, phone: str) -> str or None:
        if list(filter(lambda p: p.value == phone, self.phones)):
            return phone

    def remove_phone(self, phone: str) -> int or None:
        if self.find_phone(phone):
            index = list(map(str, self.phones)).index(phone)
            del self.phones[index]
            return index

    def edit_phone(self, old_phone: str, new_phone: str):
        new_phone = Phone(new_phone)
        if new_phone.phone:
            if self.find_phone(old_phone):
                index = self.remove_phone(old_phone)
                if index >= 0:
                    self.phones.insert(index, new_phone)
            else:
                print(f"Phone number {old_phone} is not in the {self.name} record list")