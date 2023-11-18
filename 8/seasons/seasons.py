from datetime import date
from datetime import datetime
import re
from inflect import engine as num_to_english_converter
import sys

def main():
    print(get(input('Date of Birth: ')))


def get(user_date):
    if matches := re.search('^([0-2][0-9][0-9][0-9])-([0-1][0-9])-([0-4][0-9])$', user_date):
        final = ''
        from_user_date = datetime(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
        year, month, day = re.findall(r'([0-9]?[0-9]?[0-9][0-9])', f"{date.today()}")
        days = abs(datetime(int(year), int(month), int(day)) - datetime(int(matches.group(1)), int(matches.group(2)), int(matches.group(3))))
        minutes = int(f"{days}".split("days")[0]) * 24 * 60
        minutes_english = num_to_english_converter().number_to_words(int(minutes))
        return f"{minutes_english[:1].upper() + minutes_english[1:]} minutes".replace('and ', '')
    else:
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()
