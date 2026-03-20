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