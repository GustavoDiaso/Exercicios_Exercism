from datetime import  datetime, timedelta
import calendar

def meetup_solution(encounter_purpose: str) -> str:
    WEEKDAYS = [weekday_.lower() for weekday_ in list(calendar.day_name)]
    MONTHS = [month_.lower() for month_ in list(calendar.month_name)]
    DATE_FORMAT = '%d-%m-%Y'

    encounter_purpose = encounter_purpose.strip().lower()

    # identifying the keywords
    encounter_keywords = {
        'week_keyword': None,
        'week_day': None,
        'month': None,
        'year': None
    }

    for word in encounter_purpose.split():
        if word in ['first', 'second', 'third', 'fourth', 'teenth', 'last']:
            encounter_keywords['week_keyword'] = word

        if word in WEEKDAYS:
            encounter_keywords['week_day'] = word

        if word in MONTHS:
            encounter_keywords['month'] = word

        try:
            encounter_keywords['year'] = int(word)
        except ValueError:
            continue


    for value in encounter_keywords.values():
        if value is None:
            raise ValueError('Erro qualquer')

    # ----------------------------------------------------------------------------------

    encounter_month_index = MONTHS.index(encounter_keywords['month'])
    last_day_encounter_mounth =  calendar.monthrange(encounter_keywords['year'], encounter_month_index)[1]
    encounter_date = None

    for day in range(1, last_day_encounter_mounth):
        if WEEKDAYS[calendar.weekday(encounter_keywords['year'], encounter_month_index, day)] == encounter_keywords['week_day']:
            encounter_date = datetime(encounter_keywords['year'], encounter_month_index, day)
            break


    match encounter_keywords['week_keyword']:
        case 'first':
            return encounter_date.strftime(DATE_FORMAT)

        case 'second':
            encounter_date = encounter_date + timedelta(7)
            return encounter_date.strftime(DATE_FORMAT)

        case 'third':
            encounter_date = encounter_date + timedelta(14)
            return encounter_date.strftime(DATE_FORMAT)

        case 'fourth':
            encounter_date = encounter_date + timedelta(21)
            return encounter_date.strftime(DATE_FORMAT)

        case 'last':
            for day in range(last_day_encounter_mounth, 0, -1):
                if WEEKDAYS[calendar.weekday(encounter_keywords['year'], encounter_month_index, day)] == encounter_keywords['week_day']:
                    encounter_date = datetime(encounter_keywords['year'], encounter_month_index, day)
                    break
            return encounter_date.strftime(DATE_FORMAT)

        case 'teenth':
            # teeeth = from day 13 to 19
            for day in range(13, 20):
                if WEEKDAYS[calendar.weekday(encounter_keywords['year'], encounter_month_index, day)] == encounter_keywords['week_day']:
                    encounter_date = datetime(encounter_keywords['year'], encounter_month_index, day)
                    break

            return encounter_date.strftime(DATE_FORMAT)

print('--------------------------------')
print(meetup_solution('the teenth Saturday of August 1953'))