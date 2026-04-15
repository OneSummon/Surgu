import doctest
from itertools import permutations


def solve_ex1(nums: int, notation: int):
    """
    >>> solve_ex1(1, 2)
    1
    >>> solve_ex1(2, 3)
    3
    >>> solve_ex1(5, 8)
    504
    """
    digits = [int(i) for i in range(notation)]

    even_digits = {i for i in digits if i % 2 == 0}
    odd_digits = {i for i in digits if i % 2 != 0}

    count = 0

    for code in permutations(digits, nums):
        if code[0] == 0:
            continue
        
        flag = True

        for i in range(len(code) - 1):
            digit, next_d = code[i], code[i + 1]

            if digit in even_digits and next_d in even_digits:
                flag = False
                break

            if digit in odd_digits and next_d in odd_digits:
                flag = False
                break
        
        if flag:
            count += 1
    return count

print(solve_ex1(5, 8))


expression = (81**17) + (3**24) - 45
def solve_ex2(expression, notation: int, count_num: int):
    """
    >>> solve_ex2(10, 2, 1)
    2
    >>> solve_ex2(255, 16, 15)
    2
    >>> solve_ex2(expression, 9, 8)
    10
    """
    result = 0

    def translator(num):
        res = ''
        while num > 0:
            res = str(num % notation) + res
            num //= notation
        return res
    
    new_expr = translator(expression)
    result = new_expr.count(str(count_num))

    return result

print(solve_ex2(expression, 9, 8))

def solve_ex3(left: int, right: int, count_divs: int):
    """
    >>> solve_ex3(1, 1000, 3)
    16 8
    81 27
    625 125
    >>> solve_ex3(123456789, 223456789, 3)
    131079601 1225043
    141158161 1295029
    163047361 1442897
    """

    def find_divs(number):
        divs = set()
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                divs.add(i)
                divs.add(number // i)
        return divs
    
    for number in range(int(left ** 0.25), int(right ** 0.25) + 1):
        if left <= number ** 4 <= right:
            divs = find_divs(number ** 4)
            if len(divs) == count_divs:
                print(number ** 4, max(divs))

solve_ex3(123456789, 223456789, 3)