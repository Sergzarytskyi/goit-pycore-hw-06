from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Номер має бути рядком")
        if not value.isdigit():
            raise ValueError("Номер має містити лише цифри")
        if len(value) != 10:                        
            raise ValueError("Номер має складатися з 10 цифр")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_object = self.find_phone(phone) # Шукаємо  об'єкт Phone
        if phone_object:
            raise ValueError(f"Номер {phone} був доданий раніше")
        
        self.phones.append(Phone(phone)) # створити Phone з рядка і додати в self.phones

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone: # номер цього Phone збігається з шуканим
                return p
        return None

    def remove_phone(self, phone):
        phone_object = self.find_phone(phone)  # Шукаємо  об'єкт Phone
        if phone_object is None:
            raise ValueError(f"Номер {phone} не знайдено")
        self.phones.remove(phone_object)  # видаляє, але дає помилку якщо не знайде номер, треба через цикл робити 

    def edit_phone(self, old_phone, new_phone):
        phone_object = self.find_phone(old_phone) # Шукаємо  об'єкт Phone
        if phone_object is None:
             raise ValueError(f"Номер {old_phone} не знайдено")

        phone_index = self.phones.index(phone_object)  # Шукаємо індекс об'єкта Phone
        self.phones[phone_index] = Phone(new_phone) # заміна старого на новий по індексу        


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record 

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        return self.data.pop(name)

if __name__ == "__main__":
   # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону в записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
