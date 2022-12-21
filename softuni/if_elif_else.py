# 01. Excellent Result
grade = float(input())
if grade >= 5.5:
    print("Excellent!")

# 02. Greater Number
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

# 03. Even or Odd
number = int(input())
if number % 2 == 0:
    print('even')
else:
    print('odd')

# 04. Password Guess
password = input()
if password == "s3cr3t!P@ssw0rd":
    print('Welcome')
else:
    print("Wrong password!")

# 05. Number 100...200
number = int(input())
if number < 100:
    print('Less than 100')
elif 100 <= number <= 200:
    print("Between 100 and 200")
elif 200 < number:
    print('Greater than 200')

# 06. Speed Info
speed = float(input())
if speed <= 10:
    print('slow')
elif 10 < speed <= 50:
    print('average')
elif 50 < speed <= 150:
    print('fast')
elif 150 < speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")

# 07. Area of Figures
import math

figure = input()
area = 0
if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == 'circle':
    radius = float(input())
    area = math.pi * (radius ** 2)
elif figure == 'triangle':
    length = float(input())
    height = float(input())
    area = length * height / 2
print(f"{area:.3f}")

# 01. Sum Seconds
import math
contestant_one = int(input())
contestant_two = int(input())
contestant_three = int(input())
total_time = contestant_three + contestant_two + contestant_one
minutes = math.floor(total_time / 60)
seconds = total_time % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")

# 02. Bonus Score
number = int(input())
bonus_points1 = 0
bonus_points2 = 0
if number <= 100:
    bonus_points1 = 5
elif 100 < number <= 1000:
    bonus_points1 = number * 0.2
elif 1000 < number:
    bonus_points1 = number * 0.1
if number % 2 == 0:
    bonus_points2 = bonus_points2 + 1
elif number % 10 == 5:
    bonus_points2 = bonus_points2 + 2
bonus_points_total = bonus_points1 + bonus_points2
print(bonus_points_total)
print(number + bonus_points_total)

# 03. Time + 15 Minutes
import math

hours = int(input())
minutes = int(input())
time_in_future = hours * 60 + minutes + 15
new_hours = math.floor(time_in_future / 60)
new_minutes = time_in_future % 60
if new_hours < 24 and new_minutes < 10:
    print(f"{new_hours}:0{new_minutes}")
elif new_hours < 24 and new_minutes >= 10:
    print(f"{new_hours}:{new_minutes}")
elif new_hours >= 24 and new_minutes < 10:
    print(f"0:0{new_minutes}")
elif new_hours >= 24 and new_minutes >= 10:
    print(f"0:{new_minutes}")

# 04. Toy Shop
trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
sum_toys = puzzles + dolls + bears + minions + trucks
toys_profit = puzzles * 2.6 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
if sum_toys >= 50:
    toys_profit = toys_profit * 0.75
rent = toys_profit * 0.1
profit = toys_profit - rent
if profit >= trip_price:
    money_left = profit - trip_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = trip_price - profit
    print(f'Not enough money! {money_needed:.2f} lv needed.')

# 05. Godzilla vs. Kong
budget = float(input())
statists = int(input())
clothes_prise = float(input())
decor_price = budget * 0.1
if statists > 150:
    clothes_prise = clothes_prise * 0.9
expenses = decor_price + clothes_prise * statists
if expenses > budget:
    money = expenses - budget
    print("Not enough money!")
    print(f"Wingard needs {money:.2f} leva more.")
else:
    money = budget - expenses
    print("Action!")
    print(f"Wingard starts filming with {money:.2f} leva left.")

# 06. World Swimming Record
import math

record_in_seconds = float(input())
distance = float(input())
seconds_per_meter = float(input())
delay = (distance // 15) * 12.5
# delay = (math.floor(distance / 15)) * 12.5
# delay = int(distance / 15) * 12.5
time = (distance * seconds_per_meter) + delay
if time >= record_in_seconds:
    seconds = time - record_in_seconds
    print(f"No, he failed! He was {seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")

# 07. Shopping
budget = float(input())
gpus = int(input())
cpus = int(input())
ram = int(input())
gpu_price = gpus * 250
cpu_price = (gpu_price * 0.35) * cpus
ram_price = (gpu_price * 0.1) * ram
total_price = gpu_price + cpu_price + ram_price
if gpus > cpus:
    total_price = total_price * 0.85
if budget >= total_price:
    budget = budget - total_price
    print(f"You have {budget:.2f} leva left!")
else:
    budget = total_price - budget
    print(f"Not enough money! You need {budget:.2f} leva more!")

# 08. Lunch Break
import math

name = input()
length_of_episode = int(input())
length_of_break = int(input())
length_of_lunch = length_of_break / 8
rest_time = length_of_break / 4
time_to_watch = length_of_break - length_of_lunch - rest_time
if time_to_watch >= length_of_episode:
    time_left = math.ceil(time_to_watch - length_of_episode)
    print(f"You have enough time to watch {name} and left with {time_left} minutes free time.")
else:
    time_needed = math.ceil(length_of_episode - time_to_watch)
    print(f"You don't have enough time to watch {name}, you need {time_needed} more minutes.")