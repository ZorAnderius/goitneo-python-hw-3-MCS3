import re

from Field import Field


class Name(Field):
    def __init__(self, name: str):
        try:
            name = self.__formatted_name(name)
            if self.__is_valid(name):
                self.__name = name
            else:
                raise ValueError(f"{name} is invalid name")
            super().__init__(self.name)
        except ValueError as e:
            self.__name = None
            print(e)
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def set_name(self, name: str):
        name = self.__formatted_name(name)
        if self.__is_valid(name):
            self.__name = name
        else:
            raise ValueError(f"{name} is invalid name")
        
    def __is_valid(self, name: str) -> bool:
        return True if re.match(r'\b[a-zA-Z ]+\b', name) else False
    
    def __formatted_name(self, name: str) -> str:
        res = list(filter(lambda x: x, name.split(' ')))
        return ' '.join(res)
    
    def __repr__(self) -> bool:
        if self.__name:
            return f"{self.__name}"
        return "Name field is empty"