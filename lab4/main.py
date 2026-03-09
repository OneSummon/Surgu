def get_matches_result_recursion(k: int):
    result = []
    a, b = 0, 0
    path = [f'{a}:{b}']

    def helper(a, b, path):

        if max(a, b) == k:
            result.append(path)
            return
    
        helper(a + 1, b, path + [f'{a + 1}:{b}'])
        helper(a, b + 1, path + [f'{a}:{b + 1}'])

    helper(a, b, path)
    return result

print(get_matches_result_recursion(1))
print(get_matches_result_recursion(2))

def get_matches_result_no_recursion(k: int):
    result = []
    a, b = 0, 0
    path = [f'{a}:{b}']
    stack = [(a, b, path)]

    while stack:
        a, b, path = stack.pop()

        if max(a, b) == k:
            result.append(path)
        
        else:
            stack.append((a + 1, b, path + [f'{a + 1}:{b}']))
            stack.append((a, b + 1, path + [f'{a}:{b + 1}']))
    
    return result

print(get_matches_result_no_recursion(1))
print(get_matches_result_no_recursion(2))


def find_x_recursion(x, i):
    if i == 0:
        return x
    else:
        prev = find_x_recursion(x, i - 1)
        return (prev + 1) / (prev + 2)

print(find_x_recursion(1, 1))
print(find_x_recursion(1, 2))

def find_x_no_recursion(x, i):
    for _ in range(i):
        x = (x + 1) / (x + 2)
    return x

print(find_x_no_recursion(1, 1))
print(find_x_no_recursion(1, 2))