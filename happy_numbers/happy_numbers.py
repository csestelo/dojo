def happy_number(number):
    while number != 1:
        str_number = str(number)
        calculating_number = []
        for digit in str_number:
            calculating_number.append(int(digit)**2)
        number = sum(calculating_number)
    return number == 1
