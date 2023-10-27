from colorama import Fore


def added_contact(args, contacts):
    name, phone = args


def change_contact(args, contacts):
    name, phone = args


def find_phone(args, contacts):
    name = args[0]


def show_all(contacts):
    pass


def parse_input(user_input):
    cmd, *args = user_input.split()
    print('cmd', cmd)
    print('args', args)
    cmd = cmd.strip().lower()
    print('cmd', cmd)
    return cmd, *args


def main():
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        
        if command in ['close', 'exit']:
            print(Fore.BLUE + "How can I help you?")
            break
        elif command == 'hello':
            print('hello')
        elif command == 'add':
            pass
        elif command == 'change':
            pass
        elif command == "phone":
            pass
        elif command == "all":
            pass

if __name__ == '__main__':
    main()