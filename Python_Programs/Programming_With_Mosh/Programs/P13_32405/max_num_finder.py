import random
import utils

numbers = []
for i in range(random.randint(0, 100)):
    count = random.randint(0, 100)
    numbers.append(count)
result = utils.find_max(numbers)
print(result)
