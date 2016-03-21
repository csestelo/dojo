def fizzbuzz(valor):
    if is_divisible(valor, 15):
        return 'fizzbuzz'
    elif is_divisible(valor, 3):
        return 'fizz'
    elif is_divisible(valor, 5):
        return 'buzz'
    else:
        return valor

def is_divisible(dividendo, divisor):
    return dividendo % divisor == 0
