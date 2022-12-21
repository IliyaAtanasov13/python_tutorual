'''
table
object reference count
'''

a = 'nyc'
b = 'nyc'

a = 123

print(a)
print(b)

b = 456
print(b)
c = 'nyc'
d = c
print(c == d)
print(d is c)