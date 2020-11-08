# Basic Maths
print(2+1)
2-1
2*2
3/2

(10*2) + (160/2)

# Variables

a = 5
print(a)

a = 10
a + a  # 20
a += a

type(a)  # class int

my_income = 100
tax_rate = 0.2
my_taxes = my_income * tax_rate

print(my_taxes)

# Strings

'Single quote'
"Double quote"
" We can use a ' in here if we wrap them in double quotes "

print('hello \nworld')
print('hello \tworld')  # To add tab

mystring = "Hello World"
print(mystring[0])
print(mystring[-1])  # To grab the last index in the string

mystring[2:]
mystring[:3]
mystring[3:6]


new_string = 'abcdefgh'
print(new_string[2:5])

print(new_string[::2])
print(new_string[2:7:2])

mystring[::-1]  # Will reverse the string.

# String Props and Methods

my_name = "bob"  # now change the name to rob without reassigning it.

print(my_name[1:3])
last_letters = my_name[1:3]

new_name = 'r' + last_letters
print(new_name)

x = "Hello World!"
y = " I am learning Python"

print(x + y)

print(x.upper())
print(x)
print(x.split('l'))

# String Formatting

print('I am using string {}'.format('interpolation'))
print('The {} {} {} jumped over the fence'.format('quick', 'brown', 'fox'))
print('The {1} {2} {0} jumped over the fence'.format('quick', 'brown', 'fox'))
print('The {q} {b} {f} jumped over the fence'.format(
    q='quick', b='brown', f='fox'))

result = 100/777
# Output: 0.1287001287001287

print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))  # To round the float.
print(f"The result was {result:1.3f}")

# Lists

my_list = [1, 2, 3]
len(my_list)

print(my_list[0])

new_list = [4, 5, 6]
print(my_list + new_list)  # Concating lists to merge

new_list.append('7')
print(new_list)
new_list.pop()
print(new_list)

test_list = [1, 2, 3, 4, 5, 6]
test_list.pop(4)
print(test_list)

to_sort_list = [4, 6, 7, 1, 16, 2]
to_sort_list.sort()
my_sorted_list = to_sort_list
print(my_sorted_list)

my_sorted_list.reverse()
print(my_sorted_list)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[2][0])

# Dictionaries

my_dictionary = {'key1': 'value1', 'key2': 'value2'}
print(my_dictionary['key1'])

price_lookup = {
    'apple': 2.99,
    'pear': 1.99
}

print(price_lookup['apple'])

my_life = {
    'name': 'Dan',
    'age': '27',
    'languages': {
        'coding1': 'python',
        'coding2': 'javascript',
        'coding3': 'reactjs'
    }
}

print(my_life['languages']['coding1'])
print(my_life['languages']['coding3'].upper())  # Stack call

# Tuples

t = ('a', 'b', 'c')
print(t.count('a'))
print(t.index('c'))
