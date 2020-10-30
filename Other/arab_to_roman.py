from collections import OrderedDict


def get_int_roman_dictord():
    """Create OrderedDict for roman numeral conversion."""
    d_int_roman = OrderedDict()

    d_int_roman[1000] = "M"
    d_int_roman[900] = "CM"
    d_int_roman[500] = "D"
    d_int_roman[400] = "CD"
    d_int_roman[100] = "C"
    d_int_roman[90] = "XC"
    d_int_roman[50] = "L"
    d_int_roman[40] = "XL"
    d_int_roman[10] = "X"
    d_int_roman[9] = "IX"
    d_int_roman[5] = "V"
    d_int_roman[4] = "IV"
    d_int_roman[1] = "I"

    return d_int_roman


def int_to_roman(int_roman_dictord, integer):
    """Convert Integer to Roman numeral."""
    roman_list = []

    # Handle conversion rules detailed in specification
    # while iterating over conversion ordered dictionary
    for key in int_roman_dictord:
        if key > integer:
            continue  # Restart loop until input int <= key
        q = integer // key  # // instead of divmod, remainder unused
        if not q:
            continue
        roman_list.append(int_roman_dictord[key] * q)
        integer -= (key * q)
        if not integer:
            break

    return ''.join(roman_list)


print(int_to_roman(int_roman_dictord=get_int_roman_dictord(), integer=123))
