def happy_number(number):
    verification = []
    while number != 1:
        str_number = str(number)
        calculating_number = []
        for digit in str_number:
            calculating_number.append(int(digit)**2)
        number = sum(calculating_number)
        if number in verification:
                return False
        verification.append(number)
    return number == 1


def happy_number2(number):
    verification = set()
    while number != 1 and number not in verification:
        verification.add(number)
        str_number = str(number)
        number = 0
        for digit in str_number:
            number += int(digit)**2
    return number == 1


def happy_number3(number):
    def is_happy(num, verification):
        if num == 1 or num in verification:
            return num == 1
        else:
            verification.append(num)
            str_number = str(num)
            num = 0
            for digit in str_number:
                num += int(digit)**2
            return is_happy(num, verification)
    return is_happy(number, set())
