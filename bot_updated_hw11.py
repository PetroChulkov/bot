from address_book_dict import contacts, Record

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
    name, phones = split_data(data)
    if name in contacts:
        raise ValueError('This contact already exist.')
    record = Record(name)


    record.add_phone(phones)


    contacts.add_record(record)
    return f'You added new contact: {name} with number/s: {phones}.'

@input_error
def change_func(data): #редагування контакту
    name, *phones = split_data(data)
    record = contacts[name]
    for phone in phones:
        record.change_phone(phone)
    return 'Done'

@input_error
def search_func(name): #пошук контакту
    if name.strip() not in contacts:
        raise ValueError('This contact does not exist.')
    return contacts.get(name.strip())

@input_error
def show_func(): #показ контакту
    contact = ''
    page = 1
    for info in contacts.iterator():
        contact += f'Page {page}\n'
        for record in info:
            contact += f'{record.show_record()}\n'
        page += 1
    return contact

@input_error
def delete_phone(phone):
    name, phones = split_data(phone)
    record = contacts[name]
    for phone in phones:
        if record.delete_phone(phone):
            return f'Phone number for contact: {name} was deleted successfully'
        return f'The number does not exist'

@input_error
def delete_contact(name):
    name = name.strip()
    contacts.delete_contact(name)
    return 'Contact has been deleted'

@input_error
def birthday(data):
    name, date = data.strip().split(' ')

    record = contacts[name]
    record.add_birthday(date)

    return f"Date of birthday was linked with contact: {name}"

@input_error
def count_days_birthday(name):
    name = name.strip()
    record = contacts[name]
    return f'There are {record.days_to_birthday()} remaining till users {name} Birthday'

COMMANDS = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'add': add_func,
    'change': change_func,
    'show all': show_func,
    'phone': search_func,
    'delete phone': delete_phone,
    'delete': delete_contact,
    'birthday': birthday,
    'count': count_days_birthday
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
    phones = new_data[1:]
    if name.isdigit():
        raise ValueError
    for phone in phones:
        if not phone.isdigit():
            raise ValueError
    return name, phones


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
