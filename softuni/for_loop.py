# 01. Numbers from 1 to 100
for n in range(1, 101):
    print(n)

# 02. Numbers 1...N with Step 3
n = int(input())
for num in range(1, n + 1, 3):
    print(num)

# 03. Even Powers of 2
n = int(input())
for num in range(n + 1):
    if num % 2 == 0:
        print(2 ** num)

# 04. Numbers N...1
n = int(input())
for num in range(n, 0, -1):
    print(num)

# 05. Character Sequence
word = input()
for i in word:
    print(i)

# 06. Vowels Sum
word = input()
letter = 0
for ch in word:
    if ch == 'a':
        letter = letter + 1
    elif ch == 'e':
        letter = letter + 2
    elif ch == 'i':
        letter = letter + 3
    elif ch == 'o':
        letter = letter + 4
    elif ch == 'u':
        letter = letter + 5
print(letter)

# 07. Sum Numbers
n = int(input())
total_sum = 0
for _ in range(0, n):
    current_number = int(input())
    total_sum += current_number
print(total_sum)

# 08. Number sequence
import sys

n = int(input())
biggest = -sys.maxsize
smallest = sys.maxsize
for _ in range(n):
    current_number = int(input())
    if biggest < current_number:
        biggest = current_number
    if current_number < smallest:
        smallest = current_number
print(f'Max number: {biggest}')
print(f'Min number: {smallest}')

# 09. Left and Right
n = int(input())
sum1 = 0
sum2 = 0
for num in range(0, n):
    num1 = int(input())
    sum1 += num1
for num in range(0, n):
    num2 = int(input())
    sum2 += num2
if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
elif sum1 > sum2:
    difference = sum1 - sum2
    print(f"No, diff = {difference}")
else:
    difference = sum2 - sum1
    print(f"No, diff = {difference}")

# 10. Odd Even Sum
n = int(input())
odd = 0
even = 0
for i in range(0, n):
    current_number = int(input())
    if i % 2 == 0:
        even += current_number
    else:
        odd += current_number
if even == odd:
    print(f'Yes')
    print(f'Sum = {even}')
elif even > odd:
    difference = even - odd
    print(f'No')
    print(f'Diff = {difference}')
else:
    difference = odd - even
    print(f'No')
    print(f'Diff = {difference}')

# 01. Numbers Ending in 7
for num in range(1, 1001):
    if num % 10 == 7:
        print(num)

# 02. Half Sum Element
import sys

n = int(input())
biggest = -sys.maxsize
sum = 0
for _ in range(n):
    num = int(input())
    sum += num
    if biggest < num:
        biggest = num
sum = sum - biggest
if sum == biggest:
    print('Yes')
    print(f'Sum = {sum}')
elif sum > biggest:
    difference = sum - biggest
    print('No')
    print(f'Diff = {difference}')
else:
    difference = biggest - sum
    print('No')
    print(f'Diff = {difference}')
# or
#else:
#    print('No')
#    print(f'Diff = {abs(sum - biggest)}')

# 03. Histogram
n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for _ in range(n):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num < 400:
        p2 += 1
    elif 400 <= num < 600:
        p3 += 1
    elif 600 <= num < 800:
        p4 += 1
    else:
        p5 += 1
p1 = (p1 / n * 100)
p2 = (p2 / n * 100)
p3 = (p3 / n * 100)
p4 = (p4 / n * 100)
p5 = (p5 / n * 100)
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')

# 04. Clever Lily
age = int(input())
price_washer = float(input())
price_of_single_toy = int(input())
money = 0
toys = 0
brother = 0
for num in range(1, age + 1):
    if num % 2 == 0:
        money += (num * 5)
        brother += 1
    else:
        toys += 1
money_saved = (money + (toys * price_of_single_toy)) - brother
if money_saved >= price_washer:
    difference = money_saved - price_washer
    print(f'Yes! {difference:.2f}')
else:
    difference = price_washer - money_saved
    print(f'No! {difference:.2f}')

# 05. Salary
tabs = int(input())
salary = int(input())
for _ in range(tabs):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50
if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)

# 06. Oscars
name = input()
points = float(input())
assessors = int(input())
for _ in range(assessors):
    name_assessor = input()
    points_assessor = float(input())
    name_assessor = len(name_assessor)
    points += (name_assessor * points_assessor) / 2
    if points > 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
        break
if points <= 1250.5:
    difference = 1250.5 - points
    print(f'Sorry, {name} you need {difference:.1f} more!')

# 07. Trekking Mania
groups = int(input())
musala = 0
monblank = 0
kilimanjaro = 0
k2 = 0
everest = 0
for _ in range(groups):
    people_in_group = int(input())
    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        monblank += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimanjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group
total_people = musala + monblank + kilimanjaro + k2 + everest
musala = musala / total_people * 100
monblank = monblank / total_people * 100
kilimanjaro = kilimanjaro / total_people * 100
k2 = k2 / total_people * 100
everest = everest / total_people * 100
print(f'{musala:.2f}%')
print(f'{monblank:.2f}%')
print(f'{kilimanjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')

# 08. Tennis Ranklist
import math

tournaments = int(input())
starting_points = int(input())
points = 0
wins = 0
for _ in range(tournaments):
    tournament_round = input()
    if tournament_round == 'W':
        points += 2000
        wins += 1
    elif tournament_round == 'F':
        points += 1200
    elif tournament_round == 'SF':
        points += 720
win_percentage = wins / tournaments * 100
average_points = math.floor(points / tournaments)
total_points = starting_points + points
print(f'Final points: {total_points}')
print(f'Average points: {average_points:.0f}')
print(f'{win_percentage:.2f}%')