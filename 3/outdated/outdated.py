import re

month_to_date = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
def main():
    try:
        user_date = input('Date: ')
        print(f"{convert(user_date)}".replace('None', '').replace("\n", ''))
    except ValueError:
        return main()

def convert(date):
    year, day, month = re.split('/| ', date.replace(',', '').strip())[::-1]
    modified_date = [year, month, day]
    if year in month_to_date or day in month_to_date:
        main()
    if_month = ''
    result = ''
    for time in modified_date:
        if time in month_to_date:
            if_month = ','
            if month_to_date[time] < 10:
                result += f"-0{month_to_date[time]}"
            else:
                result += f"-{month_to_date[time]}"
        else:
            if int(time) < 10:
                result += f"-0{time}"
            else:
                result += f"-{time}"
    if if_month in date:
        if bool(re.search('^([0-2][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])$', result[1:])):
            return result[1:]
        else:
            return main()
    else:
        return main()


if __name__ == "__main__":
    main()