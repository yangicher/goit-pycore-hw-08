import re
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Birthday(Field):
    def __init__(self, value):
        try:
            res = datetime.strptime(value, "%d.%m.%Y")
            self.value = res
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")
    
class Name(Field):
    pass

class Phone(Field):
    pattern = r"^\d{10}$"

    def __init__(self, value):
        super().__init__(value)
        if re.match(self.pattern, value):
            self.value = value
        else:
            print("Invalid phone number")

class Record:
    def __init__(self, name : Name):
        self.name = name
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}, bday: {self.birthday.value.date()}"
    
    def get_all_phones(self):
        return self.phones
        
    def add_phone(self, phone_number: Phone):
        phone = Phone(phone_number)
        self.phones.append(phone_number)

    def remove_phone(self, phone: Phone):
        for i, phone in self.phones:
            if phone.value == phone:
                self.phones.pop(i)
                break

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone == old_phone:
                phone = new_phone
                break

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone == phone_number:
                return phone
        return None
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        print(self.birthday)

    def show_birthdays(self):
        return self.birthday