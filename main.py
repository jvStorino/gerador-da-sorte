# gerador de numeros para a loteria
from random import randint

nums = set()

r = int(input('Quantos numeros? '))
minimum = int(input('Qual é o valor minimo? '))
maximum = int(input('Qual é o valor maximo? '))

while len(nums) < r:
    nums.add(randint(minimum, maximum))

print(f'O valores sorteados foram {nums}')
