# Формула Лейбница
def pi_leibniz(iterations: int) -> float:
    pi = 0.0
    for k in range(iterations):
        pi += ((-1) ** k) / (2 * k + 1)
        yield pi * 4

for i in pi_leibniz(136123):
    print(i)