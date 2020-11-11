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
