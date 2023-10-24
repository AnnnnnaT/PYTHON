# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, 
# если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

from sys import argv
 
def check_date(date: str):
    # date = input("Input date in DD.MM.YYYY format: ")
    day, month, year = date.split(".")
    if len(year) == 4 and 1 <= int(year) <= 9999:
        if len(month) == 2 and 1 <= int(month) <=12:
            if len(day) == 2 and 1 <= int (day) <= 31:
                if month in ["01", "03", "05", "07", "08", "10", "12"]:
                    return True
                elif month in ["04", "06", "09", "11"] and day != '31':
                    return True
                elif month == "02":
                    if __leap_year_check(int(year)) and day not in ["30", "31"]:
                        return True
                    elif day not in ["29", "30", "31"]:
                        return True
                    else:
                        return f"This date doesn't exsist in {month} month of the {year} year"
                else:
                    return f"This date doesn't exsist in {month} month of the {year} year"
            else:
                return "Day entered incorrectly"
        else:
            return "Month entered incorrectly"    
    else:
        return "Year entered incorrectly"
 
def __leap_year_check(year: int):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):
        return True
    else:
        return False
 
if __name__ == '__main__':
    date = argv[1:]
    if date:
        print(date[0], check_date(date[0]))

