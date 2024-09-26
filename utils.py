def insertOnIndex(param: list, i: int, value):
    while len(param) < i:
        param.append(None)
    return param.append(value)

# ------------------------------------------------------------
def isPrime(param: int) -> bool:
    if param <= 1: return False # Numbers less or equal to 1 are not prime.
    if param % 2 == 0 or param % 3 == 0: return False # Eliminate multiples of 2 and 3.
    # Only check odd numbers starting from 5 and skip multiples of 2 and/or 3.
    num = 5
    while num * num <= param:
        if param % num == 0 or param % (num + 2) == 0: return False
        num += 6 # Check num and num + 2, then increment by 6 (2 * 3)
    return True

# ------------------------------------------------------------
def getFactors(param: int) -> list:
    factors: list = []
    count = 0
    # Dividir por 2 hasta que ya no sea posible:
    while param % 2 == 0:
        count += 1
        # Divide by 2 to check further factors:
        param //= 2
    if count: factors.append((2, count))
    # Trabajar con números impares a partir del 3:
    for num in range(3, int(param ** 0.5) + 1, 2):
        count = 0
        while param % num == 0:
            count += 1
            # Divide by num to check further factors:
            param //= num
        if count: factors.append((num, count))
    # Check if no remaining factors:
    if param > 2:
        factors.append((param, 1))
    return factors

# ------------------------------------------------------------
def formatFactors(callback):
    result = 1
    rows = []
    for base, exponent in callback:
        tuplePow = base ** exponent
        result *= tuplePow
        rows.append(f'{base:02} ** {exponent:02} = {tuplePow:,} '.ljust(40, '.') + f' | {result:,}')
    # return print(rows)
    print('\n'.join(rows))

result = getFactors(720)
formatFactors(result)

# ------------------------------------------------------------
def filterPrimes(param: list):
    return [num for num in param if isPrime(num)]
