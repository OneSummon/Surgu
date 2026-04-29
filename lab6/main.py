from datetime import datetime
import threading
from typing import List

# Формула Лейбница
def pi_leibniz(start: int, end: int, results: List[float], index: int):
    part_pi = 0.0
    for k in range(start, end):
        part_pi += ((-1) ** k) / (2 * k + 1)
    results[index] = part_pi

n = 136123
parts = 4
chunk = n // parts
part_results = [0.0] * parts

threads = []

for i in range(parts):
    start = i * chunk
    end = (i + 1) * chunk if i < parts - 1 else n

    task = threading.Thread(target=pi_leibniz, args=(start, end, part_results, i))
    threads.append(task)

before = datetime.now()
for t in threads:
    t.start()

for t in threads:
    t.join()

pi = sum(part_results) * 4

after = datetime.now()

print(f"Число Пи равно: {pi}")
print(f"Время выполнения: {after - before}")

# В задании просили сделать именно МНОГОПОТОЧНУЮ версию, а не многопроцессорную, поэтому разница в производительности минимальна, так как
# GIL просто блокирует выполнение нескольких потоков, получается что они копятся в очереди, выполняются последовательно, и скорость почти не меняется
# Многопоточная версия быстрее всего лишь на 0,014 секунд