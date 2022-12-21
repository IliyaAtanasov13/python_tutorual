#name = "gosho"
#for i in name:
#    print(i)

#name_one = iter('pesho')
#print(next(name_one))
# will bring the nex letter in pesho - in our case it will be the first one "p"
word = input()
for i in word:
    print(i)
# the bellow statement gives the same result as above
word = input()
for i in range(0, len(word)):
    print(word[i])