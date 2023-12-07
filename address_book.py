from collections import UserDict
from datetime import datetime, timedelta
from collections import defaultdict

from birthdays import get_birthdays_per_week 

class Field:
    def __init__(self,val):
        self.value = val
    def __str__(self) -> str:
        return str(self.value)
    
class Name(Field):
    def __init__(self,name) -> None:
        super().__init__(name)
        
class Phone(Field):
    def __init__(self, val) -> None:
        super().__init__(val)
        if not self.is_valid_phone():
            raise ValueError("Invalid phone number")
    def is_valid_phone(self):
        return len(str(self.value)) == 10
  
class Birthday(Field):
    def __init__(self, val):
        try:
            new_v= datetime.strptime(val, '%d %B %Y')
            formatted_date = new_v.strftime('%d.%m.%Y')
            super().__init__(formatted_date)  
        except ValueError:
            print('Please enter your birthday date in such format: 13 September 1989')
    def to_datetime(self):
        return datetime.strptime(str(self), '%d.%m.%Y')
        

class Record:
    def __init__(self,name) -> None:
        self.name = Name(name)
        self.phones =[]
        self.birthday =''
        
    def add_phone(self,phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self,phone):
        self.phones = [p for p in self.phones if p.value != phone]
        
    def edit_phone(self,phone, new_phone):
        for i in self.phones:
            if(i.value == phone):
                i.value = new_phone
                break
        
    def find_phone(self,phone):
        return next((p for p in self.phones if p.value == phone), None)
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
    
    def show_birthday(self):
        return self.birthday.value
    
    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {';'.join(p.value for p in self.phones)}, "
    
class AddressBook(UserDict):
    def add_record(self,user):
       self.data[user.name.value] = user
    def find(self,name):
        return self.data[name] if name in self.data.keys() else None
    def delete(self,name):
        if name in self.data:
            del self.data[name]
    def birthdays(self):
        today = datetime.now()
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        grouped_birthdays = {day: [] for day in week_days}

        for record in self.data.values():
            if isinstance(record.birthday, Birthday):
                birthday_this_year = record.birthday.to_datetime().replace(year=today.year)
                
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days
                
                if 0 <= delta_days < 7:
                    week_day = birthday_this_year.weekday()
                    if week_day == 6 or week_day == 5:
                        week_day = 0
                    grouped_birthdays[week_days[week_day]].append(record.name.value)

        sorted_data = dict(sorted(grouped_birthdays.items(), key=lambda x: week_days.index(x[0])))
        output = ''
        for day, names in sorted_data.items():
            output += f'{day}: {", ".join(names)}\n'

        return output
        
    
book = AddressBook()
kari_record = Record('Kari')
kari_record.add_phone('1309198934')
kari_record.add_phone('0909202003')
kari_record.add_birthday('11 December 1989')
kari_record.edit_phone('0909202003', '1313131313')

book.add_record(kari_record)

platon_record = Record('Platon')
platon_record.add_phone('7894561230')
platon_record.add_phone('0123654789')
platon_record.add_birthday('13 December 1989')

book.add_record(platon_record)

kari = book.find('Kari')
search =kari_record.find_phone('0909202003')


for name,record in book.data.items():
    print(name, 'fghf')
    

