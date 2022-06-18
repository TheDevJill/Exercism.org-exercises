def leap_year(year):
    """year divisible by 4 and not divisible by 100 is leap year"""
    if year % 4 == 0 and year % 100 != 0:
        return True

    """year divisible by 400 is leap year"""
    if year % 400 == 0:
        return True
    else:
        return False
