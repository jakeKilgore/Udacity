# Represents the number of days through the year given a month.
days_so_far = [
    0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334
]


def days_between_dates(year1, month1, day1, year2, month2, day2):
    """Calculates the number of days between two dates."""

    days = date_in_days(year2, month2, day2) - date_in_days(year1, month1, day1)
    return days


def date_in_days(year, month, day):
    """Turns a date into an integer of days."""

    # Year and month are subtracted by one because they are in-progress.
    days = year_as_days(year - 1)
    days += month_as_days(month - 1, year)
    days += day
    return days


def year_as_days(year):
    """Represents a year as a number of days from the year 0, accounting for leap years."""

    days = 365 * year
    days += num_leap_years(year)
    return days


def num_leap_years(year):
    """Find the number of leap years since the year 0."""

    leap_years = int(year / 4)
    leap_years -= int(year / 100)
    leap_years += int(year / 400)
    return leap_years


def month_as_days(month, year):
    """Find the number of days through the year given a month."""

    days = days_so_far[month]
    # If we have finished February and it's a leap year, add one.
    if month >= 2 and is_leap_year(year):
        days += 1
    return days


def is_leap_year(year):
    """Check if a given year is a leap year."""

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def test_days_between_dates():
    # test same day
    assert (days_between_dates(2017, 12, 30,
                               2017, 12, 30) == 0)
    # test adjacent days
    assert (days_between_dates(2017, 12, 30,
                               2017, 12, 31) == 1)
    # test new year
    assert (days_between_dates(2017, 12, 30,
                               2018, 1, 1) == 2)
    # test full year difference
    assert (days_between_dates(2012, 6, 29,
                               2013, 6, 29) == 365)

    assert (days_between_dates(1900, 1, 1,
                               1999, 12, 31) == 36523)

    assert (days_between_dates(2012, 1, 1,
                               2012, 2, 28) == 58)

    assert (days_between_dates(2012, 1, 1,
                               2012, 3, 1) == 60)

    assert (days_between_dates(2011, 6, 30,
                               2012, 6, 30) == 366)

    assert (days_between_dates(2011, 1, 1,
                               2012, 8, 8) == 585)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


test_days_between_dates()
