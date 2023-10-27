from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    @property
    def book(self):
        return self.data

    @book.setter
    def set_book(self, data):
        self.data = data

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __repr__(self):
        string = ''
        for record in self.data.values():
            string += str(record) + '\n'
        return string[:-1:]
