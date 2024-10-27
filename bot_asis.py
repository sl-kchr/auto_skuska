from collections import UserDict
#––––––––––––––––––––––––––––––––––––––
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
#––––––––––––––––––––––––––––––––––––––
class Name(Field):
    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return str(self.value)
    
#––––––––––––––––––––––––––––––––––––––
class Phone(Field):
    def __init__(self, phone):
        if not len(phone) == 10 or not phone.isdigit():
            raise ValueError('The phone number must contain exactly 10 digits')
        super().__init__(phone)

    def __str__(self):
        return str(self.value)           
                
#––––––––––––––––––––––––––––––––––––––
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        return self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
    
    def edit_phone (self, old_phone, new_phone):
        try:
            for i in range(len(self.phones)):
                if self.phones[i].value == old_phone:
                    self.phones[i] = Phone(new_phone)
                    return self.phones[i]
        except ValueError:
            return ValueError
            
    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i 
 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

#––––––––––––––––––––––––––––––––––––––
class AddressBook(UserDict):

    def add_record(self, Record):
        self.data[Record.name.value] = Record

    def find(self, name):
        try:
            return self.data[name]
        except KeyError:
            return None
    

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
john = book.find('John')
john.edit_phone("1234567890", "1112223333")

print(john)

