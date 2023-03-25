from datetime import datetime



month_names = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım"
    ,"Aralık"]


def get_day(date_string):
    return str(int(date_string.split(".")[0]))

def has_comma(string):
    return "," in string

def convert_dateTo_Number(date_string):
    if(has_comma(date_string)):
        date_parts = date_string.split(", ")
    else:
        date_parts = date_string.split(" ")
    month_number = month_names.index(date_parts[0]) + 1
    return f"{month_number:02}.{date_parts[1]}"




def compare_dates(date1_string, date2_string):
    date1 = datetime.strptime(date1_string, "%d.%m.%Y")
    date2 = datetime.strptime(date2_string, "%m.%Y")

    date2 = date2.replace(day=1)

    if date1.year > date2.year:
        return 1
    elif date1.year < date2.year:
        return -1
    else:
        if date1.month > date2.month:
            return 1
        elif date1.month < date2.month:
            return -1
        else:
            return 0




def format_date(date_string):

    date = datetime.strptime(date_string, "%d.%m.%Y")
    month_number = int(date.strftime("%m"))
    return f"{month_names[month_number - 1]}, {date.year}"



