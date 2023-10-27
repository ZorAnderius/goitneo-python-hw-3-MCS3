from Name import Name
from Phone import Phone


class Record:
    def __init__(self, name: str):
        self.__name = Name(name)
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
            return f"{self.name}: {', '.join(phone.value for phone in self.phones)}"
        if not self.phones and self.name.name is None:   
            return 'None'
        
        return f"{self.name}: Phonebook is empty"
    
    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        if new_phone.phone:
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
                if index:
                    self.phones.insert(index, new_phone)
            else:
                print(f"Phone number {old_phone} is not in the {self.name} record list")