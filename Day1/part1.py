from math import floor

with open('input.txt', 'r') as file:
    print(sum([(int(x) // 3) - 2 for x in file.read().split('\n')]))
