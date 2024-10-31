from collections import UserDict
from models import Record
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def __str__(self):
        count = len(self.data)
        return f"Address Book with {count} records"

    def add_record(self, record: Record):
        if not self.data.get(record.name):
            self.data[record.name] = record
        else:
            print(f"Contact with name: {record.name} already exists")

    def find(self, name: str):
        return self.data.get(name, None)

    def delete(self, name: str):
        result = self.data.pop(name)
        return result

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        upcoming_period = 7
        days_in_week = 7
        today = datetime.now()

        for user in self.data.values():
            user_birthday = user.birthday.value
            birthday_this_year = user_birthday.date().replace(year=today.year)
            
            if (birthday_this_year < today.date()):
                birthday_this_year = user_birthday.date().replace(year=today.year + 1)

            diff = (birthday_this_year - today.date()).days

            if(diff >= 0 and diff <= upcoming_period): 
                weekday = birthday_this_year.weekday()
                if(weekday == 6 or weekday == 5):
                    begin_week = birthday_this_year + timedelta(days = days_in_week - weekday)
                    upcoming_birthdays.append(f"name: {user.name}, congratulation_date: {begin_week.strftime("%d.%m.%Y")}")
                else:
                    upcoming_birthdays.append(f"name: {user.name}, congratulation_date: {birthday_this_year.strftime("%d.%m.%Y")}")
        return upcoming_birthdays