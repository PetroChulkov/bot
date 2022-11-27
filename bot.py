contacts = {} #словник для збереження контактів

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact does not exists'
        except IndexError:
            return 'Give me name and phone please'
        except ValueError:
            return 'Enter data in correct format'
    return wrapper



@input_error
def hello_func(): #функція привітання
    return 'How can I help you?'


@input_error
def exit_func(): #функція закриття
    return 'good bye'


@input_error
def add_func(data): #додавання контакту
    name, phone = split_data(data)
    if name in contacts:
        raise ValueError('This contact already exist.')
    contacts[name] = phone
    return f'You added new contact: {name} with number: {phone}.'

@input_error
def change_func(data): #редагування контакту
    name, phone = split_data(data)
    if name in contacts:
        contacts[name] = phone
        return f'You changed number for {name}.'
    return 'Add contact before updating'

@input_error
def search_func(name): #пошук контакту
    if name.strip() not in contacts:
        raise ValueError('This contact does not exist.')
    return contacts.get(name.strip())

@input_error
def show_func(): #показ контакту
    contact = ''
    for k, v in contacts.items():
        contact += f'{k}: {v} \n'
    return contact

COMMANDS = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': add_func,
    'change': change_func,
    'show all': show_func,
    'phone': search_func
}
def command_recognition(command): #розпізнання контакту
    new_input = command
    data = ''
    for key in COMMANDS:
        if command.strip().lower().startswith(key):
            new_input = key
            data = command[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()

def reaction_func(reaction):
    return COMMANDS.get(reaction, break_func)

def split_data(command): #підготовка введеної інформації для обробки 
    new_data = command.strip().split(' ')
    name = new_data[0]
    phone = new_data[1]
    if name.isdigit():
        raise ValueError
    if not phone.isdigit():
        raise ValueError
    return name, phone


def break_func(): #невідома команда
    return 'Unknown command.'

def main(): #основна функція
    while True:
        user_input = input('Enter your command (for exit print: "good bye", "close", "exit")')
        result = command_recognition(user_input)
        print(result)
        if result == 'good bye':
            break

if __name__ == '__main__':
    main()
