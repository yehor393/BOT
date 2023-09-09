contacts = {}


def input_error(handler):
    def wrap(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except KeyError:
            print(f'Sorry this contact is not found')
        except ValueError:
            print('Invalid format. Please use "<command> <name> <phone>"')
        except IndexError:
            print('Command is incomplete. Please provide both name and phone')

    return wrap


def print_hi():
    print('How can I help you?')


@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    print(f"Contact {name} added with phone number {phone}")


@input_error
def change_contact(command):
    _, name, phone = command.split()
    if name in contacts:
        contacts[name] = phone
        print(f"Contact {name} have a new phone number {phone}")
    else:
        raise KeyError


@input_error
def phone_contact(command):
    _, name = command.split()
    if name in contacts:
        phone = contacts.get(name)
        print(f"{name}'s phone number is {phone}")
    else:
        raise KeyError


@input_error
def show_contact():
    print('|{:_^15}|{:_^15}|'.format('Contact name', 'Phone number'))
    for i, ii in contacts.items():
        print('|{:_^15}|{:_^15}|'.format(i, ii))


if __name__ == '__main__':
    while True:
        user_input = input('Enter a command: ')
        command_user_input = user_input.lower()

        if command_user_input == 'hello':
            print_hi()
        elif command_user_input.startswith('add '):
            add_contact(user_input)
        elif command_user_input.startswith('change '):
            change_contact(user_input)
        elif command_user_input.startswith('phone '):
            phone_contact(user_input)
        elif command_user_input == 'show all':
            show_contact()
        elif command_user_input in ['good bye', 'close', 'exit']:
            print("Good bye!")
            break
        else:
            print('Invalid command. Try again')
