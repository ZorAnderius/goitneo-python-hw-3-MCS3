from datetime import datetime


class Birthday:
    def __init__(self, year: int, month: int, day: int):
        if self.__day_is_valid(year, month, day):
            self.__birthday = datetime(year, month, day).date()
        else:
            self.__birthday = None

    @property
    def birthday(self) -> datetime:
        return self.__birthday

    @birthday.setter
    def set_birthday(self, birthday: datetime):
        self.__birthday = birthday

    def birthday_year(self):
        if self.birthday:
            return self.__birthday.year

    def birthday_month(self):
        if self.birthday:
            return self.birthday.month

    def birthday_day(self):
        if self.birthday:
            return self.__birthday.day

    def replace_year(self, year):
        return self.__birthday.replace(year)

    def __repr__(self):
        return self.__birthday.strftime("%d.%m.%Y")

    def __day_is_valid(self, year, month, day):
        if year >= 1 and year <= datetime.today().date().year and day >= 1 and day <= 31 and month >= 1 and month <= 12:
            return True
        else:
            return False


if __name__ == '__main__':
    birth = Birthday(2030, 10, 1)
    print(birth.birthday_year())
