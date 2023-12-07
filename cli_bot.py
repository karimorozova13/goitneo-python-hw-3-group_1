def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# def change_contact(args,contacts):
#     name,phone = args
#     contacts.update({name:phone})
#     return "Contact updated"

def input_error(fn):
    def inner(*args, **kwargs):
        
        try:
            return fn(args, kwargs)
        except ValueError:
            print("Not enough values to unpack. Give me name and phone please")
            return kwargs
        except TypeError:
            print("Enter correct type")
            return kwargs
        except NameError:
            print('Such contact does not exist')
            return kwargs
        except IndexError:
            print("We do not have this contact or Not enough values to unpack.")
            return kwargs
             
    return inner

@input_error
def add_contact(args,contacts):
    name= args[0][0]
    phone= args[0][1]
    
    if phone and name:
        contacts[name] =phone
        print("Contact added")
        return contacts
    else:
        raise IndexError

@input_error
def change_contact(args,contacts):
    name= args[0][0]
    phone= args[0][1]
    
    if name in contacts.keys():
        contacts.update({name:phone})
        print('Contact was updated')
        return contacts
    else:
        raise NameError

@input_error
def show_all(args,contacts):
    print(contacts)
    return contacts

@input_error
def show_phone(args, contacts):
    name= args[0][0]
    if name in contacts.keys():
        return contacts[name]
    else:
        raise NameError
    
    
def main():
    print('Welcome to the assistant bot!')
    contacts = {}
    while True:
        user_input =input("Enter the command >>>>>")
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
            print('Good bye')
            break
        elif command=='hello':
            print('How can I help you?')
        elif command == 'add':
            contacts = add_contact(args, **contacts)
        elif command == 'change':
            contacts = change_contact(args, **contacts)
        elif command == 'all':
            print(show_all(**contacts))
        elif command =='phone':
            print(show_phone(args, **contacts))
        else:
            print('Invalid command')

if __name__ == '__main__':
    main()