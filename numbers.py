import random
num_adds = 0
for i in range(10000000):
    accum = 0
    while accum < 1:
        accum += random.random()
        num_adds += 1

print(num_adds / 10000000)

