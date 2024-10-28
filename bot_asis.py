from collections import UserDict
#––––––––––––––––––––––––––––––––––––––
# Базовий клас для полів запису.

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
#––––––––––––––––––––––––––––––––––––––
#Клас для зберігання імені контакту.

class Name(Field):
    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return str(self.value)
    
#––––––––––––––––––––––––––––––––––––––
#Клас для зберігання номера телефону. (10 цифр)

class Phone(Field):
    def __init__(self, phone):
        if not len(phone) == 10 or not phone.isdigit():
            raise ValueError('The phone number must contain exactly 10 digits')
        super().__init__(phone)

    def __str__(self):
        return str(self.value)           
                
#––––––––––––––––––––––––––––––––––––––
#Клас для зберігання інформації про контакт.

class Record:
    def __init__(self, name):
        self.name = Name(name) # зберігання об'єкта Name в атрибуті name.
        self.phones = [] # зберігання списку об'єктів Phone в атрибуті phones.

    def add_phone(self, phone): # 1 метод для додавання.
        return self.phones.append(Phone(phone))
    
    def remove_phone(self, phone): # 2 метод для видалення.
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
    
    def edit_phone (self, old_phone, new_phone): # 3 метод для редагування.
        try:
            for i in range(len(self.phones)):
                if self.phones[i].value == old_phone:
                    self.phones[i] = Phone(new_phone)
                    return self.phones[i]
        except ValueError:
            return ValueError
            
    def find_phone(self, phone): # метод для пошуку об'єктів Phone.
        for i in self.phones:
            if i.value == phone:
                return i 
 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

#––––––––––––––––––––––––––––––––––––––
# Клас для зберігання та управління записами.
class AddressBook(UserDict):

    def add_record(self, Record): # 1 додає запис до self.data.
        self.data[Record.name.value] = Record

    def find(self, name): # 2 знаходить запис за ім'ям.
        try:
            return self.data[name]
        except KeyError:
            return None
    
    def delete(self, name): # 3 видаляє запис за ім'ям.
        del self.data[name]

#––––––––––––––––––––––––––––––––––––––
# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record('John')
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)

    # Знаходження та редагування телефону для John
jane = book.find('Jane')
jane.edit_phone("9876543210", "1112223333")
print(book)
book.delete('Jane')

print(book.find('Jane'))