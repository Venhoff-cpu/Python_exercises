import re


def zip_code_split(zip_code):
    _ = zip_code.split('-')
    zip_code_value = int(''.join(_))
    return zip_code_value


def zip_code_validation(zip_code):
    if re.match(r'\d{2}-\d{3}', zip_code):
        return True

    return False


def zip_code_range(zip_1, zip_2):
    zip_value_1 = zip_code_split(zip_1)
    zip_value_2 = zip_code_split(zip_2)

    if zip_value_1 < zip_value_2:
        start = zip_value_1
        end = zip_value_2

    elif zip_value_1 > zip_value_2:
        start = zip_value_2
        end = zip_value_1

    else:
        return 'Pusty przedział'

    # Zwracamy otwarty przdział pomiędzy podanymi kodami pocztowymi (bez uwzglednienia podanych wartości brzegowych).
    return [f'{str(i // 1000).zfill(2)}-{str(i % 1000).zfill(3)}'
            for i in range(start+1, end)]


if __name__ == '__main__':
    zip_code_1 = '79-900'
    zip_code_2 = '80-155'
    print(zip_code_range(zip_code_1, zip_code_2))
