from typing import List


my_family = ["Алмаз", "Мама", "Папа", "Злата", "Юля", "Бабушка", "Дедушка", "Симон(мопс)"]


my_family_height = [
    ["Алмаз", 177],
    ["Мама", 158],
    ["Папа", 160],
    ["Злата", 140],
    ["Юля", 120],
    ["Бабушка", 150],
    ["Дедушка", 173],
    ["Симон(мопс)", 30],
]


def height_father(family_list: List[str], list_height: List[List]):
    for i in range(len(family_list)):
        if family_list[i] == "Папа":
            return f"Рост отца - {list_height[i][1]} см"
        
# print(height_father(my_family, my_family_height))


def sum_height(family_list: List[str], list_height: List[List]):
    result = 0
    for i in range(len(family_list)):
        result += list_height[i][1]
    return f"Общий рост моей семьи - {result} см"

# print(sum_height(my_family, my_family_height))