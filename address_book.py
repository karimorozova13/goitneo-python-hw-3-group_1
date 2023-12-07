from collections import UserDict
from datetime import datetime
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
            raise ValueError("Invalid phone number. At least 10 characters")
    def is_valid_phone(self):
        return len(str(self.value)) == 10
  
class Birthday(Field):
    def __init__(self, val):
        
        if not self.is_valid_date_format(val):
            raise ValueError('Enter your birthday date in such format: 13 September 1989')
        
        new_v= datetime.strptime(val, '%d %B %Y')
        formatted_date = new_v.strftime('%d.%m.%Y')
       
        super().__init__(formatted_date) 
         
    def is_valid_date_format(self, val):
        
        try:
            datetime.strptime(val, '%d %B %Y')
            return True
        except ValueError:
            return False 
        
    def to_datetime(self):
        return datetime.strptime(str(self), '%d.%m.%Y')
        
class Record:
    def __init__(self,name) -> None:
        self.name = Name(name)
        self.phone =''
        self.birthday =''
        
    def add_phone(self,phone):
        self.phone = (Phone(phone))
        
    def remove_phone(self,phone):
        self.phone = ''
        
    def edit_phone(self, new_phone):
        self.phone = Phone(new_phone)
        
    def find_phone(self,phone):
        return next((p for p in self.phones if p.value == phone), None)
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
    
    def show_birthday(self):
        return self.birthday.value
    
    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phone: {self.phone}, birthday: {self.birthday} "
    
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
       
