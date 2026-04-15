import doctest
from itertools import permutations

class Task1:
    def __init__(self, nums: int, notation: int):
        self.nums = nums
        self.notation = notation
    
    def solve(self):
        """
        >>> Task1(1, 2).solve()
        1
        >>> Task1(2, 3).solve()
        3
        >>> Task1(5, 8).solve()
        504
        """
        digits = [int(i) for i in range(self.notation)]

        even_digits = {i for i in digits if i % 2 == 0}
        odd_digits = {i for i in digits if i % 2 != 0}

        count = 0

        for code in permutations(digits, self.nums):
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


expression = (81**17) + (3**24) - 45

class Task2:
    def __init__(self, expression, notation: int, count_num: int):
        self.expression = expression
        self.notation = notation
        self.count_num = count_num
    
    def solve(self):
        """
        >>> Task2(10, 2, 1).solve()
        2
        >>> Task2(255, 16, 15).solve()
        2
        >>> Task2(expression, 9, 8).solve()
        10
        """
        result = 0

        def translator(num):
            res = ''
            while num > 0:
                res = str(num % self.notation) + res
                num //= self.notation
            return res
        
        new_expr = translator(self.expression)
        result = new_expr.count(str(self.count_num))

        return result


class Task3:
    def __init__(self, left: int, right: int, count_divs: int):
        self.left = left
        self.right = right
        self.count_divs = count_divs
    
    def solve(self):
        """
        >>> Task3(1, 1000, 3).solve()
        16 8
        81 27
        625 125
        >>> Task3(123456789, 223456789, 3).solve()
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
        
        for number in range(int(self.left ** 0.25), int(self.right ** 0.25) + 1):
            if self.left <= number ** 4 <= self.right:
                divs = find_divs(number ** 4)
                if len(divs) == self.count_divs:
                    print(number ** 4, max(divs))
