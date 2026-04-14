radius = 42

def square(radius: int):
    pi = 3.1415926
    return round(pi * (radius ** 2), 4)

s = square(radius)
# print(s)


point_1 = (23, 34)
point_2 = (30, 30)

def inCircle(point: tuple[int, int], radius: int):
    distance = ((point[0] ** 2) + (point[1] ** 2)) ** 0.5
    return True if distance < radius else False

# print(inCircle(point_1, radius))
# print(inCircle(point_2, radius))