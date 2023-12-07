from datetime import datetime
from collections import defaultdict

users = [
    {"name": "Kari Mo", "birthday": datetime(1989, 9, 13)},
    {"name": "Oleksii Mo", "birthday": datetime(1983, 11, 29)},
    {"name": "Iana Lenser", "birthday": datetime(2000, 11, 29)},
    
    {"name": "Platon Mo", "birthday": datetime(2020, 9, 9)},
    {"name": "Maryna Kuz", "birthday": datetime(1987, 12, 1)},
    {"name": "Alla Vdo", "birthday": datetime(1990, 11, 30)},
    {"name": "Alla New", "birthday": datetime(1990, 12, 3)},
]
week_days= ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def get_birthdays_per_week(users):
    today = datetime.now().date()
    grouped_l = defaultdict(list)
    output = ''
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date() 
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year+1)
        delta_days = (birthday_this_year - today).days
        if delta_days <7:
            week_day = birthday_this_year.weekday()
            if week_day == 6 or week_day ==5:
                week_day= 0
            grouped_l[week_days[week_day]].append(name)
    sorted_data = dict(sorted(grouped_l.items(), key=lambda x: week_days.index(x[0])))
    for key,val in sorted_data.items():
        output += f'{key}: {", ".join(val)}\n'
        
    return output

print(get_birthdays_per_week(users))