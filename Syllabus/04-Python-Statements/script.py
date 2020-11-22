from random import shuffle
from random import randint

# If, Elif and Else Statements

var = 2

if var < 1:
    print('This is correct')
else:
    print('This is incorrect')


var1 = 'a'

if var1 == 'b':
    print('This is a b')
elif var1 == 'c':
    print('This is a c')
else:
    print('This is a')

name = 'Frankie'

if name == 'Sam':
    print("Hello Sam")
elif name == 'Frankie':
    print('Hello Frankie')
else:
    print('We don\'t have you on the system. What is your name?')

# For Loops

my_iterable = [1, 2, 3]
for item in my_iterable:
    print(item)

mynum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mynum:
    print(num * 2)

# for newnum in mynum:
#     if newnum % 2 == 0:
#         print(newnum)
#     else:
#         print(f'Odd number {newnum} found in sequence')

list_sum = 0

for num in mynum:
    list_sum = list_sum + num
    print(list_sum)

for letter in 'Hello World':
    print(letter)

tup_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for a, b in tup_list:
    print(a)
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}

for k, v in d.items():
    print(k)
    print(v)

# While Loops

x = 0
while x < 5:
    x += 1
    print(f'The current value of x is {x}')
else:
    print('X is not less than 5')

x = [1, 2, 3]
for item in x:
    pass

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

# Python Operators

for num in range(0, 10, 2):
    print(num)

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcde'

for item in enumerate(word):
    print(item)

for item, letter in enumerate(word):
    print(item)
    print(letter)

mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

mylist4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_list = shuffle(mylist4)
print(mylist4)

print(randint(0, 100))
my_num = randint(0, 100)
print(my_num)

result = input('What is your name? ')

new_phrase = (f'Hello, {result}!')
print(new_phrase)
