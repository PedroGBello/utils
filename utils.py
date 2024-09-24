def insertOnIndex(param: list, i: int, value):
    while len(param) < i:
        param.append(None)
    return param.append(value)

def isPrime(param: int):
    # Numbers less or equal to 1 are not prime:
    if param <= 1:
        return False
    for i in range(2, int(param ** 0.5) + 1):
        if param % i == 0:
            return False
    return True

def filterPrimes(param: list):
    return [num for num in param if isPrime(num)]

def getFactors(param: list):
    factors: list = []
    for i in range(2, param + 1):
        while param % i == 0:
            isPrime(i) and factors.append(i)
            # Divide by i to check further factors:
            param //= i
    return factors

print(isPrime(89))
print(getFactors(88))
print(filterPrimes(range(100)))
