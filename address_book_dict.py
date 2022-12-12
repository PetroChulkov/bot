from collections import UserDict
from datetime import datetime



class Field:
    def __init__(self, name):
        self._value = None
        self.value = name

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value

class Name(Field):
    pass

class Phone(Field):
    @Field.value.setter

    def value(self, value):
        for phone in value:

            if len(value) > 12:
                raise ValueError("Too many symbols in phone number")
            if not phone.isnumeric():
               raise ValueError('Wrong phones.')
        self._value = value


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        current_date = datetime.now().date()
        birthdate = datetime.strptime(value,'%Y-%m-%d').date()
        if birthdate > current_date:
            raise ValueError('nope')
        self._value = value



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    def add_phone(self, phones):

        self.phones.append(Phone(phones[0:]))



    def change_phone(self, phones):
        for phone in self.phones:
            for phone_number in phones:
                if phone_number != phone:
                    self.add_phone(phone_number)
                    self.phones.remove(phone)

    def delete_phone(self, phone):
        for number in self.phones:
            for subst in number.value:
                if subst == phone:
                    number.value.remove(subst)
                    return True

        return False
    def show_record(self):
        phones_show = ''
        birthday_show = ''
        for phone in self.phones:
            for number in phone.value:
                phones_show += f'{number}, '
        if self.birthday:
            birthday_show = f'{self.birthday.value}'


        return f'{self.name.value}: {phones_show}{birthday_show}'


    def add_birthday(self, date):
        self.birthday = Birthday(date)


    def days_to_birthday(self):
        if not self.birthday:
            raise ValueError("Birthday info is missing for this contact")

        day = (datetime.strptime(self.birthday.value,'%Y-%m-%d').date()).day
        month = (datetime.strptime(self.birthday.value,'%Y-%m-%d').date()).month
        current_date = datetime.now().date()
        today = datetime.now()
        current_year = current_date.year
        if current_date.day >= day or current_date.month >= month:
            next_year = datetime(year=(current_year + 1), month = month, day = day)
            return (next_year - today).days
        else:
            this_year = datetime(year=current_year, month=month, day=day)
            return (this_year - today).days



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    def delete_contact(self, name):
        del self.data[name]
    def show_all(self):
        return self.data
    def iterator(self, count=5):
        page = []
        i = 0
        for record in self.data.values():
            page.append(record)
            i += 1
            if i == count:
                yield page
                page = []
                i = 0
        if page:
            yield page


contacts = AddressBook()