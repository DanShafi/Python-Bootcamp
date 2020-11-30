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
    print('The current value of x is {x}')
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

# result = input('What is your name? ')

# new_phrase = ('Hello, {result}!')
# print(new_phrase)

# List Comprehensions

# mystrings = 'hello'

# my_list = []
# for letter in mystring:
#     my_list.append(letter)

# my_new_list = [letter for letter in mystrings]
# print(my_new_list)

# mynumlist = [num**2 for num in range(0, 11)]
# mymodlist = [num for num in range(0, 11) if x % 2 == 0]

# celsius = [0, 10, 20, 34.5]
# farenheit = [((9/5)*temp + 32) for temp in celsius]

# farenheit = []
# for temp in celsius:
#     farenheit.append(((9/5)*temp + 32))

# results = [x if x % 2 == 0 else 'Odd' for x in range(0, 11)]

# newlist = []
# for x in [2, 4, 6]:
#     for y in [100, 200, 300]:
#         newlist.append(x*y)

# Module Tests

st = 'Print only the words that start with s in this sentence'
st.split()

for word in st.split():
    if word[0].lower() == 's':
        print(word)

test = list(range(0, 11, 2))
print(test)

divisable = [x for x in range(1, 51) if x % 3 == 0]
print(divisable)

evenst = 'Print only the words that start with s in this sentence'

for word in evenst.split():
    if len(word) % 2 == 0:
        print(word + ' is even!')

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

firstst = 'Print only the words that start with s in this sentence'
stsplit = [word[0] for word in firstst.split()]
print(stsplit)
