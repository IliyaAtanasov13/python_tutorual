# 01. Hello SoftUni

print('Hello SoftUni')

# 02. Nums 1...10
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# 03. Rectangle Area
a = int(input())
b = int(input())
print(a * b)

# 04. Inches to Centimeters
number = float(input())
print(number * 2.54)

# 05. Greeting by Name
name = input()
print("Hello, " + name + "!")

# 06. Concatenate Data
first_name = input()
last_name = input()
age = int(input())
city = input()
print(f"You are {first_name} {last_name}, a {age}-years old person from {city}.")

# 01. USD to BGN
usd = float(input())
print(usd * 1.79549)

# 02. Radians to Degrees
import math

radians = float(input())
pi = math.pi
degrees = radians * 180 / pi
print(degrees)

# 03. Deposit Calculator
deposit = float(input())
time = int(input())
interest = float(input())
interest_yearly = deposit * (interest/100)
interest_monthly = interest_yearly / 12
total_sum = deposit + time * interest_monthly
print(total_sum)

# 04. Vacation books list
import math
number_of_pages = int(input())
pages = int(input())
days = int(input())
time_reading = number_of_pages / pages
time_per_day = time_reading / days
print(round(time_per_day))

# 05. Supplies for School
pens = int(input())
markers = int(input())
chemical = int(input())
discount_percentage = int(input())
pens_price = pens * 5.80
markers_price = markers * 7.20
chemical_price = chemical * 1.2
price = pens_price + markers_price + chemical_price
discount = (discount_percentage / 100) * price
print(price - discount)

# 06. Repainting
naylon = int(input())
paint = int(input())
razreditel = int(input())
time = int(input())
naylon_price = (naylon + 2) * 1.5
paint_price = (paint * 1.1) * 14.5
razreditel_price = razreditel * 5
total_price = naylon_price + paint_price + razreditel_price + 0.40
workers_price = (total_price * 0.3) * 8
print(total_price + workers_price)

# 07. Food Delivery
chicken_dishes = int(input())
fish_dishes = int(input())
vegetarian_dishes = int(input())
main_dishes_price = chicken_dishes * 10.35 + fish_dishes * 12.4 + vegetarian_dishes * 8.15
sweets = main_dishes_price * 0.2
print(main_dishes_price + sweets + 2.5)

# 08. Basketball Equipment
tax_yearly = int(input())
shoes = tax_yearly * 0.6
shirts = shoes * 0.8
balls = shirts * 0.25
stuff = balls * 0.2
print(tax_yearly + shirts + shoes + balls + stuff)

# 09. Fish Tank
lenght = int(input())
width = int(input())
height = int(input())
percentage = float(input())
displacement = lenght * width * height
displacement_liters = displacement * 0.001
percentage_new = percentage / 100
print(displacement_liters * (1 - percentage_new))

# 07. Projects Creation

name = input()
projects = int(input())
completion_time = projects * 3

print(f"The architect {name} will need {completion_time} hours to complete {projects} project/s.")

# 08. Pet Shop

dog_food = int(input())
cat_food = int(input())
dog_food_price = dog_food * 2.5
cat_food_price = cat_food * 4
total_price = dog_food_price + cat_food_price
print(f"{total_price} lv.")

# 09. Yard Greening

square_meters = float(input())
price = square_meters * 7.61
discount = price * 0.18
final_price = price - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")

# something
first_name = input()
last_name = input()
age = int(input())
city = input()
print(f"You are {first_name} {last_name}, a {age}-years old person from {city}.")