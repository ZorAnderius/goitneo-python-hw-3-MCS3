from colorama import Fore

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
    name, phone = args


def find_phone(args, book):
    name = args[0]


def show_all(book):
    general_str = ''
    for _, record in book.items():
        general_str += str(record)
    return general_str[:-1:]

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    book = AddressBook()
    while True:
        user_input = input("Enter a command: ")
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
                print(find_phone(args, book))
            elif command == "all":
                print(show_all(book))
            else:
                print(Fore.YELLOW + "Invalid command")


if __name__ == '__main__':
    main()