from colorama import Fore
from pathlib import Path
import os.path

from main_classes.AddressBook import AddressBook
from main_classes.Record import Record


def added_contact(args, book):
    try:
        name, phone = args
        record = Record(name, phone)
        book.add_record(record)
    except ValueError as e:
        return Fore.RED + str(e)
    return Fore.GREEN + 'Contact added.'


def change_contact(args, book):
    if len(args) == 3:
        name, old_phone, new_phone  = args
        try:    
            contact = book.find(name)
            contact.edit_phone(old_phone, new_phone)
        except ValueError as e:
            return Fore.RED + str(e)
    else: 
        return Fore.RED + 'Invalid format. To change phone use next command - [change name old_phone new_phone]'
    return Fore.GREEN + 'Contact changed.'

def find_phone(args, book):
    try:
        name = args[0]
        return book.find(name)
    except ValueError as e:
        return Fore.RED + str(e)


def show_all(book):
    general_str = ''
    for _, record in book.items():
        general_str += str(record)
    return general_str[:-1:]

def add_birthday(args, book):
    if len(args) == 4:
        name, year, month, day = args
        try:
            contact = book.find(name)
            
            contact.add_birthday(int(year), int(month), int(day))
        except ValueError as e:
            return Fore.RED + str(e)
        return Fore.GREEN + 'Birthday was added.'

def show_birthday(args, book):
    name = args[0]
    try:
        contact = book.find(name)
        return contact.birthday
    except ValueError as e:
        return Fore.RED + str(e)


def show_week_birthdays(book):
    birth_str = ''
    try:
        birthday_dict = book.get_birthdays_per_week()
    except ValueError as e:
        return Fore.YELLOW + str(e)
    for _, value in birthday_dict.items():
        for weekday, names in value.items():
            weekdey_str = Fore.BLUE + '{: >10}'.format(weekday)
            names_str = Fore.YELLOW+ '{: <10}'.format(', '.join(names))
            birth_str += (f"{weekdey_str} : {names_str}\n")
    return birth_str[:-1:]

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

path = Path('Task1/data.json')

def main():
    book = AddressBook()
    if os.path.exists(path):
        new_book = book.read_from_file(path)
        if new_book:
            book = book.add_book(new_book)
    while True:
        user_input = input(Fore.CYAN + "Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
            if command in ['close', 'exit']:
                print(Fore.BLUE + "Good bye!")
                break
            elif command == 'hello':
                print(Fore.BLUE + "How can I help you?")
            elif command == 'add':
                print(added_contact(args, book))
            elif command == 'change':
                print(change_contact(args, book))
            elif command == "phone":
                print(find_phone(args, book)[:-1:])
            elif command == "all":
                print(show_all(book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(show_week_birthdays(book))
            else:
                print(Fore.YELLOW + "Invalid command")
    
    book.save_to_file(path)


if __name__ == '__main__':
    main()