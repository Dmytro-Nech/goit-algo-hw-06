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
        if len(phone) == 10 and phone.isdigit():
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
        new_phone = Phone(new_phone)
        for p in self.phones:
            if p.value == phone:
                index = self.phones.index(p) 
                self.phones[index] = new_phone
                return

        raise ValueError


    def find_phone(self, phone):
        phone = Phone(phone)
        return next((p for p in self.phones if p.value == phone.value), None)

        
    
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
               self.phones.remove(p)
        else:
            print('Phone doesn`t exist')
            

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    
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

