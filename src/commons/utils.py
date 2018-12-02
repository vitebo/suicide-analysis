def get_years_available():
    return __make_years_for_range(00, 17) + __make_years_for_range(96, 100)


def get_x_suicide_available():
    return list(f'X {i}' for i in range(60, 85))


def __make_years_for_range(start, end):
    return list(__format_to_two_decimal_place(year) for year in range(start, end))


def __format_to_two_decimal_place(number):
    return f'0{number}' if number < 10 else number
