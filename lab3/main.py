from itertools import permutations

def solve_ex1():
    digits = [0,1,2,3,4,5,6,7]
    even_digits = {0,2,4,6}
    odd_digits = {1,3,5,7}

    count = 0

    for code in permutations(digits, 5):
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

print(solve_ex1())


def solve_ex2():
    expression = (81**17) + (3**24) - 45
    result = 0

    def translator(num):
        res = ''
        while num > 0:
            res = str(num % 9) + res
            num //= 9
        return res
    
    new_expr = translator(expression)
    result = new_expr.count("8")

    return result

print(solve_ex2())

def solve_ex3():

    def find_divs(number):
        divs = set()
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                divs.add(i)
                divs.add(number // i)
        return divs
    
    result = []
    for number in range(int(123456789 ** 0.25), int(223456789 ** 0.25) + 1):
        if 123456789 <= number ** 4 <= 223456789:
            divs = find_divs(number ** 4)
            if len(divs) == 3:
                print(number ** 4, max(divs))
solve_ex3()