contacts = {} #словник для збереження контактів

def input_error(func):
    def wrapper():
        try:
            func()
        except KeyError:
            print('This contact does not exists')
            main()
        except IndexError:
            print('Give me name and phone please')
            main
        except ValueError:
            print('Enter user name please')
            main()
        except Exception:
            print('Unknown command.')
            main()
    return wrapper

@input_error
def main(): # Основна фуннція - всі input та print реалізовані в цій функції

    wait_for_input = True
    while wait_for_input:
        print('Enter your command (for exit print: "good bye", "close", "exit")')
        command = input()
        closure_list = ['good bye', 'close', 'exit']
        if command.lower() == 'hello':
            print('How can I help you?')
        elif command.split(' ')[0] == 'add':
            save_contact(command.split(' ')[1:])
        elif command.lower() in closure_list:
            wait_for_input = False
        elif command.split(' ')[0] == 'phone':
            print(contacts[command.split(' ')[1]])
        elif command.split(' ')[0] == 'change':
            change_contact(command.split(' ')[1:])
        elif command.lower() == 'show all':
            for key, value in contacts.items():
                print('{0}: {1}'.format(key, value))
        else:
            raise Exception #викликає виключення для невідомої команди


def save_contact(contact_list = ""): #використовується для збереження контакту
    if contact_list[0].isdigit():
        raise ValueError
    else:
        contacts[contact_list[0]] = contact_list[1]


def change_contact(contact_list = ""): #використовується для зміни контакту
    if contact_list[0].isdigit():
        raise ValueError
    else:
        contacts[contact_list[0]] = contact_list[1]


if __name__ == '__main__':
    main()
