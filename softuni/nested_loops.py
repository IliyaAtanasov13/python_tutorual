# 01. Clock
for hours in range(0, 24):
    for minutes in range(0, 60):
        print(f'{hours}:{minutes}')

# 02. Multiplication Table
for n1 in range (1, 11):
    for n2 in range(1, 11):
        result = n1 * n2
        print(f'{n1} * {n2} = {result}')

# 03. Combinations
n = int(input())
combinations = 0
for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if x1 + x2 + x3 == n:
                combinations += 1
print(combinations)

# 04. Sum of Two Numbers
begin = int(input())
end = int(input())
magic_number = int(input())
positive_combinations = 0
combination_counter = False
for n1 in range(begin, end + 1):
    for n2 in range(begin, end + 1):
        combination_counter += 1
        if n1 + n2 == magic_number:
            positive_combinations = True
            break
    if positive_combinations:
        break
if positive_combinations:
    print(f'Combination N:{combination_counter} ({n1} + {n2} = {magic_number})')
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")

# 05. Travelling
destination = input()
budget = float(input())
saving = 0
while destination != 'End':
    money = float(input())
    saving += money
    if saving >= budget:
        print(f'Going to {destination}!')
        destination = input()
        if destination == 'End':
            break
        budget = float(input())
        saving = 0

# 06. Building
floors = int(input())
rooms_per_floor = int(input())
room = 0
for fl in range (floors, 0, -1):
    if fl == floors:
        while room < rooms_per_floor:
            print(f'L{fl}{room}', end=' ')
            room += 1
            if room == rooms_per_floor:
                room = 0
                break
    if fl % 2 == 0 and fl != floors:
        while room < rooms_per_floor:
            print(f'O{fl}{room}', end=' ')
            room += 1
            if room == rooms_per_floor:
                room = 0
                break
    if fl % 2 == 1 and fl != floors:
        while room < rooms_per_floor:
            print(f'A{fl}{room}', end=' ')
            room += 1
            if room == rooms_per_floor:
                room = 0
                break
    print() # принтирането между циклите вкарва нов ред за новата порция принтиране от цикъла

# or
floors = int(input())
rooms_per_floor = int(input())
for fl in range (floors, 0, -1):
    for room in range(rooms_per_floor):
        number = fl * 10 + room
        if fl == floors:
            print(f'L{number}', end=' ')
        if fl % 2 == 0 and fl != floors:
            print(f'O{number}', end=' ')
        if fl % 2 == 1 and fl != floors:
            print(f'A{number}', end=' ')
    print()

# 01. Number Pyramid
n = int(input())
current = 1
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current > n:
            break
        print(f'{current} ', end="")
        current += 1
    if current > n:
        break
    print()

# 02. Equal Sums Even Odd Position
num1 = int(input())
num2 = int(input())
odd = 0
even = 0
for num in range(num1, num2 + 1):
    num = str(num)
    length = len(num)
    odd = int(num[0]) + int(num[2]) + int(num[4])
    even = int(num[1]) + int(num[3]) + int(num[5])
    if odd == even:
        print(f'{num}', end=' ')

# 03. Sum Prime Non Prime
number = input()
prime_number = 0
non_prime_number = 0
flag = False
negative = False
while number != 'stop':
    number = int(number)
    if number < 0:
        print('Number is negative.')
        negative = True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
    if flag is True and negative is False:
        non_prime_number += number
        flag = False
    elif flag is False and negative is False:
        prime_number += number
    number = input()
    negative = False
    if number == 'stop':
        break
print(f'Sum of all prime numbers is: {prime_number}')
print(f'Sum of all non prime numbers is: {non_prime_number}')

# 04. Train The Trainers


# 05. Special Numbers


# 06. Cinema Tickets