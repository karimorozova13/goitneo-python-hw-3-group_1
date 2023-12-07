import pickle
from address_book import Record, AddressBook

def write_to_file():
    with open('data.bin', 'wb') as fh:
        pickle.dump(contacts, fh)
        
def read_from_file():
    with open('data.bin', 'rb') as fh:
        unpacked = pickle.load(fh)
        return unpacked


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(fn):
    def inner(*args, **kwargs):
        
        try:
            return fn(args, kwargs)
        except ValueError as e:
            print(e)
        except TypeError:
            print("Enter correct type")
        except NameError:
            print('Such contact does not exist')
        except IndexError:
            print("Not enough values to unpack.")
            
    return inner

@input_error
def add_contact(args,kwargs):
    name= args[0][0]
    phone= args[0][1]
    
    if phone and name:
        record = Record(name)
        record.add_phone(phone)
        
        contacts.add_record(record)
        print("Contact added")
    else:
        raise IndexError('Phone should be at least 10 caracters')

@input_error
def change_contact(args,kwargs):
    name= args[0][0]
    phone= args[0][1]
    if name in contacts.data.keys():
        record = contacts.find(name)
        record.edit_phone(phone)
        
        print('Contact was updated')
    else:
        raise NameError

@input_error
def show_phone(args, kwargs):
    name= args[0][0]
    if name in contacts.data.keys():
        record = contacts.find(name)
        return record.phone
    else:
        raise NameError
  
@input_error
def show_all(args, kwargs):
    for name,record in contacts.data.items():
        print(record)
    return contacts

@input_error
def add_birthday(args, kwargs):
    name= args[0][0]
    birthday= ' '.join(args[0][1::])
    
    if name in contacts.data.keys():
        record = contacts.find(name)
        record.add_birthday(birthday)
        print('Birthday was added')
    else:
        raise NameError
    
@input_error
def show_birthday(args,kwargs):
    name= args[0][0]
    if name in contacts.data.keys():
        record = contacts.find(name)
        return record.show_birthday()
    else:
        raise NameError
    
@input_error
def show_all_birthdays(args, kwargs):
    return contacts.birthdays()
    
    
contacts = AddressBook()
  
    
def main():
    print('Welcome to the assistant bot!')
    global contacts
    try:
        contacts= read_from_file()
    except:
        contacts = AddressBook()
        
    
    while True:
        user_input =input("Enter the command >>>>>")
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
            write_to_file()
            print('Good bye')
            break
        elif command=='hello':
            print('How can I help you?')
        elif command == 'add':
            add_contact(args)
        elif command == 'change':
            change_contact(args)
        elif command =='phone':
            print(show_phone(args))
        elif command == 'all':
            show_all()
        elif command == "add-birthday":
            add_birthday(args)
        elif command == "show-birthday":
            print(show_birthday(args))
        elif command == "birthdays":
            print(show_all_birthdays(args))
        else:
            print('Invalid command')


if __name__ == '__main__':
    main()