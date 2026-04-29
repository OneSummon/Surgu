def pi_leibniz(iterations: int) -> float:
    pi = 0.0
    for k in range(iterations):
        pi += ((-1) ** k) / (2 * k + 1)
        yield pi * 4