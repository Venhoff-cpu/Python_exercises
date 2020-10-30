def validate_pesel(pesel):
    try:
        if len(pesel) != 11:
            raise Exception("Pesel musi miec 11 cyfr naturlanych.")
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        pesel_lista = [int(i) for i in pesel]
        suma = 0
        for i in range(10):
            suma = suma + (wagi[i] * pesel_lista[i])
        suma_modulo = 10 - (suma % 10)
        if suma_modulo == 10:
            suma_modulo = 0
        if pesel_lista[-1] == suma_modulo:
            return f"Pesel o numerze {pesel} jest poprawny."
        else:
            return f"Pesel o numerze {pesel} jest niepoprawny"
    except Exception as e:
        return f"Błąd typu: {e}"


print(validate_pesel("91080602512"))
print(validate_pesel("95080602512"))
print(validate_pesel("a9108060251"))
print(validate_pesel("111111"))
