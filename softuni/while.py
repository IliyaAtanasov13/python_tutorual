# 01. Numbers Ending in 7
text = input()
while text != 'Stop':
    print(text)
    text = input()

# 02. Password
name = input()
password = input()
user_input = input()
while user_input != password:
    user_input = input()
print(f'Welcome {name}!')

# 03. Sum Numbers
initial_number = int(input())
sum = int(input())
while sum < initial_number:
    number = int(input())
    sum += number
print(sum)

# 04. Sequence 2k+1
initial_number = int(input())
number = 1
while number <= initial_number:
    print(number)
    number = number * 2 + 1

# 05. Account Balance
payment = input()
sum = 0
while payment != 'NoMoreMoney':
    payment = float(payment)
    if payment < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {payment:.2f}')
    sum += payment
    payment = input()
print(f'Total: {sum:.2f}')

# 06. Max Number
import sys

number = input()
biggest = -sys.maxsize
while number != 'Stop':
    number = int(number)
    if number > biggest:
        biggest = number
    number = input()
print(f'{biggest}')

# 07. Min Number
import sys

number = input()
smallest = sys.maxsize
while number != 'Stop':
    number = int(number)
    if number < smallest:
        smallest = number
    number = input()
print(f'{smallest}')

# 08. Graduation
name = input()
year = 0
bad_assessment = 0
sum_assessments = 0
assessment = 0
while True:
    year += 1
    assessment = float(input())
    if assessment < 4:
        bad_assessment += 1
        if bad_assessment == 2:
            print(f'{name} has been excluded at {year} grade')
            break
        year -= 1
    else:
        sum_assessments += assessment
    if year == 12:
        average_assessment = sum_assessments / 12
        print(f'{name} graduated. Average grade: {average_assessment:.2f}')
        break

# 01. Old Books
favourite_book = input()
next_book = 0
book_counter = 0
while True:
    next_book = input()
    if next_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_counter} books.')
        break

    if next_book == favourite_book:
        print(f'You checked {book_counter} books and found it.')
        break
    book_counter += 1

# 02. Exam Preparation
bad_grades = int(input())
enough = False
counter_grades = 0
counter_bad_grades = 0
sum_grades = 0
last_task = 0
while not enough:
    task = input()
    if task == 'Enough':
        average_grade = sum_grades / counter_grades
        print(f'Average score: {average_grade:.2f}')
        print(f'Number of problems: {counter_grades}')
        print(f'Last problem: {last_task}')
        break
    grade = int(input())
    if grade <= 4:
        counter_bad_grades += 1
        if counter_bad_grades == bad_grades:
            print(f'You need a break, {bad_grades} poor grades.')
            break
    counter_grades += 1
    sum_grades += grade
    last_task = task

# 03. Vacation
money_needed = float(input())
money = float(input())
counter_days = 0
consecutive_spend = 0
while money < money_needed:
    action = input()
    money_action = float(input())
    counter_days += 1
    if action == 'spend':
        consecutive_spend += 1
        money = money - money_action
        if money <= 0:
            money = 0
        if consecutive_spend == 5:
            print("You can't save the money.")
            print(counter_days)
            break
    else:
        consecutive_spend = 0
        money = money + money_action
    if money >= money_needed:
        print(f'You saved the money for {counter_days} days.')
        break

# 04. Walking
steps_per_day = input()
total_steps = 0
while steps_per_day != 'Going home':
    steps_per_day = int(steps_per_day)
    total_steps += steps_per_day
    if total_steps >= 10000:
        difference = total_steps - 10000
        print(f'Goal reached! Good job!')
        print(f'{difference} steps over the goal!')
        break
    steps_per_day = input()
    if steps_per_day == 'Going home':
        steps_per_day = int(input())
        total_steps += steps_per_day
        if total_steps < 10000:
            difference = 10000 - total_steps
            print(f'{difference} more steps to reach goal.')
            break
        else:
            difference = total_steps - 10000
            print(f'Goal reached! Good job!')
            print(f'{difference} steps over the goal!')
            break
if steps_per_day == 'Going home':
    steps_per_day = int(input())
    total_steps += steps_per_day
    if total_steps < 10000:
        difference = 10000 - total_steps
        print(f'{difference} more steps to reach goal.')
    else:
        difference = total_steps - 10000
        print(f'Goal reached! Good job!')
        print(f'{difference} steps over the goal!')

# 05. Coins
change = float(input())
change = int(change * 100)
coins = 0
if change >= 200:
    coins = int(change / 200)
    change = change % 200
if change >= 100:
    coins += 1
    change = change % 100
if change >= 50:
    coins += 1
    change = change % 50
if change >= 20:
    coins += int(change / 20)
    change = (change % 20)
if change >= 10:
    coins += 1
    change = (change % 10)
if change >= 5:
    coins += 1
    change = (change % 5)
if change >= 2:
    coins += int(change / 2)
    change = (change % 2)
if change == 1:
    coins += 1
print(coins)

# 06. Cake
width = int(input())
length = int(input())
pieces_left = width * length
pieces = input()
while True:
    if pieces != 'STOP':
        pieces = int(pieces)
        pieces_left -= pieces
        if pieces_left <= 0:
            pieces_needed = abs(pieces_left)
            print(f'No more cake left! You need {pieces_needed} pieces more.')
            break
        pieces = input()
    else:
        print(f'{pieces_left} pieces are left.')
        break

# 07. Moving
width = int(input())
length = int(input())
height = int(input())
space_left = width * length * height
boxes = input()
while True:
    if boxes != 'Done':
        boxes = int(boxes)
        space_left -= boxes
        if space_left <= 0:
            space_needed = abs(space_left)
            print(f"No more free space! You need {space_needed} Cubic meters more.")
            break
        boxes = input()
    else:
        print(f"{space_left} Cubic meters left.")
        break