from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        if not name:
            raise ValueError("Name is a required field.")
        super().__init__(name)


class Phone(Field):
    # Можемо перевіряти формат телефону в цьому класі
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            raise ValueError("Invalid phone format")
        
    def __str__(self):
        return self.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone: str):
        phone = Phone(phone)
        self.phones.append(phone)


    def edit_phone(self, phone, new_phone):
        phone = Phone(phone)
        new_phone = Phone(new_phone)
        try:
            index = self.phones.index(phone) 
            self.phones[index] = new_phone
        except ValueError:
            print("Phone not found")


    def find_phone(self, phone):
        phone = Phone(phone)
        for p in self.phones:
            if p == phone:
                return p
        return None
        
    
    def remove_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print('Phone doesn`t exist')
            

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def __init__(self):
        self.data = {}  # Словник для зберігання записів
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        record = self.data.get(name)
        if record:
            return record
        return None       
    
    def delete(self, name):
        if name in self.data:
           del self.data[name]
        else:
            print("Contact not found")

    def __str__(self):
        if not self.data:
            return "Address Book is empty."

        result = "Address Book:\n"
        for record in self.data.values():
            result += str(record) + "\n"
        return result.strip()  # Видаляємо зайві пробіли або нові рядки в кінці        

