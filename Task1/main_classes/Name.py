from Field import Field


class Name(Field):
    def __init__(self, name: str):
        try:
            if self.is_valid(name):
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
    def set_name(self, name):
        if self.is_valid(name):
            self.__name = name
        else:
            raise ValueError(f"{name} is invalid name")
        
    def is_valid(self, name: str) -> bool:
        return True if name.isalpha() else False
    
    def __repr__(self) -> bool:
        if self.__name:
            return f"{self.__name}"
        return "Name field is empty"