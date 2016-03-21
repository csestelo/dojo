# coding: utf-8
def min_value(sample):
    if not sample:
        return None

    min_ = sample[0]
    for number in sample:
        if number < min_:
            min_ = number
    return min_

def max_value(sample):
    if not sample:
        return None

    def m(acc, el):
        if acc > el:
            return acc
        else:
            return el
    return reduce(m, sample)

def lenght(sample):
    return reduce(lambda acc, el: acc + 1, sample, 0)

def mean(sample):
    def r(acc, el):
        return acc + el
    return reduce(r, sample, 0.0) / lenght(sample)

# Existe operador ternário :: ex. max value :
# return reduce(lambda acc if acc > el el)
