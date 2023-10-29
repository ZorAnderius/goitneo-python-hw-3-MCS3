from collections import UserDict, defaultdict
from datetime import datetime
import json

from .Record import Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    @property
    def book(self):
        return self.data

    @book.setter
    def set_book(self, data):
        self.data = data
        
    def add_book(self, data):
        for key, record in data.items():
            name = record['name']
            phones = record['phones']
            birthday = record['birthday']
            new_record = Record(name)
            if phones and len(phones):
                new_record.add_phones(phones)
            if birthday:
                day, month, year = [int(day) for day in birthday.split('.')]
                new_record.add_birthday(year, month, day)
            self.data[key] = new_record
        return self

    def add_record(self, record):
        if record:
            if record.name.value in self.data:
                self.data[record.name.value].add_phone(record.phones[0].value)
            else:
                self.data[record.name.value] = record
        else:
            raise ValueError("Invalid record")

    def find(self, name):
        if not len(self.data):
            raise ValueError("Phonebook is empty")
        if name in self.data:
            return self.data[name]
        else:
            raise ValueError("Contact not found")

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def serialize(self):
        if len(self.data):
            nested_dict = dict()
            for key, record in self.data.items():
                nested_dict[key] = record.serialize()

        return {'data': nested_dict}

    def de_serialize(self, data):
        new_book = data['data']
        return new_book

    def save_to_file(self, filename=''):
        if filename and len(self.data):
            with open(filename, 'w') as f_write:
                json.dump(self.serialize(), f_write)

    def read_from_file(self, filename):
        if filename:
            with open(filename, 'r') as f_read:
                try:
                    res = json.load(f_read)
                except:
                    return None
                if len(res):
                    res = self.de_serialize(res)
                return res


    def __repr__(self):
        string = ''
        for record in self.data.values():
            string += str(record) + '\n'
        return string[:-1:]

    def get_birthdays_per_week(self):
        if not len(self.data.values()):
            raise ValueError("Your phonebook is empty")
        users_birthdays_dict = defaultdict(list)
        dict_of_users = dict()
        
        current_date = datetime.today().date()
        for record in self.data.values():
            name = record.name.value
            if record.birthday:
                birthday = record.birthday
            else:
                birthday = None
            
            if not name or birthday is not None:
                print(birthday)
                birthday_this_year = birthday.replace_year(year=current_date.year)
                
                # replace users year for current year
                if birthday_this_year < current_date:
                    birthday_this_year = birthday_this_year.replace_year(year=(current_date.year + 1))
                
                # replace notice day
                birthday_this_year = replace_birthday_date(birthday_this_year)  
                
                # looking for different between current date and user's birthday
                delta_days = (birthday_this_year - current_date).days
                if delta_days < 7:
                    weekday = birthday_this_year.weekday()
                    birthday_weekday = birthday_this_year.strftime('%A')
                    
                    # if we already have this weekday we just add new user's birthday 
                    # to birthday's list for current day
                    if weekday in dict_of_users:
                        dict_of_users[weekday][birthday_weekday].append(name)
                    else:
                        # if user's birthday is meet first time we check if we don't 
                        # take user's birthday from previous day and add to dict
                        users_birthdays_dict[birthday_weekday].append(name)
                        if len(users_birthdays_dict) > 1:
                            key = list(users_birthdays_dict.keys())[0]
                            del users_birthdays_dict[key]
                        dict_of_users[weekday] = dict(users_birthdays_dict)
        # sort user's birthdays from nearest to further
        dict_of_users = self.__sorted_users_notes(sorted(dict_of_users.items()), current_date.weekday())
        if not dict_of_users:
            raise ValueError("Your calendar is empty")
        return dict_of_users

    def __sorted_users_notes(self, users_birthdays_dict, current_day):
        first_dict = dict()
        second_dict = dict()
        for day, values in users_birthdays_dict:
            if day >= current_day:
                first_dict[day] = values
            else:
                second_dict[day] = values
        return first_dict | second_dict


def replace_birthday_date(date):   
    """ replace notice day if birthday it is: 
    -weekend day
    -last day of the month
    -last day of the year
"""     
    if date.weekday() == 5:
        if date.month == 2 and date.day >= 27:
            if date.year % 2 == 0 and date.day == 28:
                date = date.replace(month=date.month + 1, day=1)
            elif date.year % 2 == 0 and date.day == 29: 
                date = date.replace(month=date.month + 1, day=2)   
            elif date.year % 2 != 0 and date.day == 27:
                date = date.replace(month=date.month + 1, day=1)
            elif date.year % 2 != 0 and date.day == 28: 
                date = date.replace(month=date.month + 1, day=2)  
        elif date.month in [1, 3, 5, 7, 8, 10, 12] and date.day >= 30:   
            if date.month == 12:
                if date.day == 30:
                    date = date.replace(year=date.year + 1, month=1, day=1)
                elif date.day == 31:
                    date = date.replace(year=date.year + 1, month=1, day=2)
            elif date.day == 30:
                date = date.replace(month=date.month + 1, day=1)
            elif date.day == 31:
                date = date.replace(month=date.month + 1, day=2)
        elif date.month in [4, 6, 9, 11] and date.day >= 29:
            if date.day == 29:
                date = date.replace(month=date.month + 1, day=1)
            elif date.day == 30:
                date = date.replace(month=date.month + 1, day=2)
        else:
            date = date.replace(day=date.day + 2)
    if date.weekday() == 6:    
        if date.month == 2 and date.day >= 28:
            if date.year % 2 == 0 and date.day == 29: 
                date = date.replace(month=date.month + 1, day=1)   
            elif date.year % 2 != 0 and date.day == 28: 
                date = date.replace(month=date.month + 1, day=1)  
        elif date.month in [1, 3, 5, 7, 8, 10, 12] and date.day >= 29:   
            if date.month == 12:
                if date.day == 31:
                    date = date.replace(year=date.year + 1, month=1, day=1)
            elif date.day == 31:
                date = date.replace(month=date.month + 1, day=1)
        elif date.month in [4, 6, 9, 11] and date.day == 30:
            date = date.replace(month=date.month + 1, day=1)
        else:
            date = date.replace(day=date.day + 1)
    return date