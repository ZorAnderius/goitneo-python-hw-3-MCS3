from Field import Field


class Phone(Field):
    def __init__(self, phone: str):
        try:
            if self.is_valid(phone):
                self.__phone = phone
            else:
                raise ValueError(f"{phone} is invalid phone number. Length must be 10 numbers")
            super().__init__(self.phone)
        except ValueError as e:
            self.__phone = None
            print(e)

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def set_phone(self, phone: str):
        try:
            if self.is_valid(phone):
                self.__phone = phone
            else:
                raise ValueError(f"{phone} is invalid phone number. Length must be 10 numbers")
        except ValueError as e:
            self.__phone = None
            print(e)

    def is_valid(self, phone: str) -> bool:
        return True if len(phone) == 10 else False

    def __repr__(self) -> str:
        if self.__phone:
            return f"{self.__phone}"

    def __str__(self) -> str:
        if self.__phone:
            return f"{self.__phone}"