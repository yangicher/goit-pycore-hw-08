from address_book import AddressBook
from models import Record

HELP = """
    Commands:
    - hello: Greeting.
    - add <name> <phone>:Add new contact.
    - phone <name>: Get contact.
    - change <name> <phone>: Change the phone number of a contact.
    - all: All contacts.
    - add-birthday
    - show-birthday
    - birthdays
    - help: All commands.
    - close/exit: Close the assistant.
    """

def input_error(func):
    def inner(*args, **kwargs):
        func_name = func.__name__
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"ValueError in '{func_name}'."
        except IndexError:
            return f"IndexError in '{func_name}'."
        except KeyError:
            return f"KeyError in '{func_name}' Contact {args[0]} not found."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def hello():
    return "How can I help you?"

@input_error
def close():
    return "Good bye!"

@input_error
def help():
    return HELP

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message  


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record == None:
        return "Cant find records"
    else:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated"

@input_error
def get_phone(args, book: AddressBook):
    name = args[0]
    record : Record = book.find(name)
    if record == None:
        print("Cant find records")
    else:
        phones = record.get_all_phones()
        print(f"Phones: ")
        print("\n".join(phone for phone in phones))

@input_error
def get_all_contacts(book: AddressBook):
    for record in book.data.values():
        print(record)

@input_error
def add_birthday(args, book : AddressBook):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        print(f"Birthday {birthday} added to {name}.")
    else:
        print(f"Contact {name} not found.")

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record != None:
        birthday = record.show_birthdays()
        print(f"{name}'s birthday: {birthday}")
    else:
        print(f"Contact {name} not found.")

@input_error
def birthdays(book : AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if len(upcoming) > 0:
        return upcoming
    else:
        return "No upcoming birthdays."

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        match command:
            case "close" | "exit":
                print(close())
                break
            case "hello":
                print(hello())
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "phone":
                print(get_phone(args, book))
            case "all":
                print(get_all_contacts(book))
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                print(birthdays(book))
            case "help":
                print(help())

if __name__ == "__main__":
    main()