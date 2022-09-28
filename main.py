import datetime


def current_year():
    return datetime.date.today().year


def current_month():
    return datetime.date.today().month


# Exercize #1 - Request user to input birth year, then calculate and print
#               out the users age based on the given year.
def main():
    cur_year = current_year()
    cur_month = current_month()
    print("The current year and month is %s/%s." % (cur_year, cur_month))
    # Put your code here


if __name__ == '__main__':
    main()
