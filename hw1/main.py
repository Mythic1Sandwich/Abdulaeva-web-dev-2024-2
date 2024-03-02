# прибавляет 2 к каждому элементу коллекции
def plus2(nums):
    result = []
    for num in nums:
        result.append(num + 2)
    return result

# умножает на 2 каждый элемент коллекции
def multiply2(nums):
    result = []
    for num in nums:
        result.append(num * 2)
    return result

# возводит в степень 2 каждый элемент коллекции
def exponent2(nums):
    result = []
    for num in nums:
        result.append(num ** 2)
    return result