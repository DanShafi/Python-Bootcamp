**Basic Data Types**

-   Lists are Python's version of arrays.
-   Dictionaries are like JS Objects or Ruby Hashes.
-   Tuples are immutable sequence of objects.
-   Sets are unordered collection of unique objects.
-   Booleans in Python, utilise capitalised True or False.

**Numbers**

-   Two main number types are integers and floats.
-   The Modulo operator will always show a remainder.
-   To know if a number is even or odd, if we use `% 2` and it returns 0, that means there would be no remainders, however an odd would have a remainder.
-   Basic order of maths will multiply first and then addition. Use parentheses if you want to follow BEDMAS.
-   Why doesn't `0.1+0.2 - 0.3 = 0.0` ? This is to do with floating point accuracy and a computers ability to represent numbers in memory.

**Variable Assignments**

-   We can use variables to store data types and be able to reference them at a later point.
-   In Python, variable names cannot start with a number, there cannot be a space in the name, we use snake_case and we cannot use any special characters.
-   Global variable names can be in all caps.
-   Python uses **Dynamic Typing** meaning we can reassign variables to different data types, as opposed to other languages which are **Statically Typed,** such as C++.
-   **Dynamic Typing** means it's easier to work with and has faster development time, however it may result in bugs due to unexpected data types and you need to be aware of what the type is.
-   To find out the type of a Class (so an object in Python), we use `type(class_to_check)`
-   Avoid using Python keywords for variable names i.e. `int` or `str`

**Strings**

-   We can use single and double quotes. If we want to include a string that uses a single quote, we can wrap the string in double quotes.
-   Strings used ordered sequences meaning we can use indexing and slicing.
-   We use square bracket notation to grab an index position for a string.
-   We can use reverse indexing available so we can grab **-1** to grab the last letter of the string, irrespective of how long the string is.
-   In order to slice in Python, we use **[start:stop:step].** `start` is a numerical index for the slice start. `stop` is the index you will go up to **but not include** and `step` is the size of the 'jump' you take.
-   We can use escape sequences for example `print('hello \nworld')`. The `\n` will execute the string to the next line. We can use `\t` to add a tab.
-   To work out the length of a string, we use `len(str)`. Whitespace counts towards the length of a string.
-   `mystring[0]` will return the first char in a string. `mystring[-1]` will return the last char in the string.
-   `mystring[2:]` will return the sliced string from the referenced index to the end of the string.
-   `mystring[:3]` will return the sliced string from 0 to 2. The sliced reference is **up to but not including. It will not return the 4th character.**
-   `mystring[3:6]` will return **the third index up to the 5th index, it does not include the 6th index.**
-   We can use `mystring[::]` which will return the full string.
-   We can also use the step size syntax `mystring[::2]` - **this means that it will only return every second index in the string.**
-   We can also use `mystring[2:7:2]` that will **start from index 2, stop at index 6 (not including 7) and only return every second character.**
-   `mystring[::-1]` will return a reverse of your string. Not advised for interviews.

**String Props and Methods**

-   Immutability means you cannot change something. You cannot change strings by index as they are immutable. For example, you cannot have `name = "bob"` and then try change the name to rob by doing `name[0] = 'r'`. Python will throw an err.
-   We can use concatenation and variable assignment to achieve this.
-   Concatenation will not add space unless specifically expressed.
-   Keep in mind that if a user adds a number as a string and you use concat, it will add the strings together, not execute the maths that you may require.
-   When we use methods in Python, it similar to JS in that we need to execute with brackets i.e. `x.upper()`.
-   If you try to run a method without the `()`, Python will throw an err like `<function str.upper>`. So if you get an interview test on why this is happening, it's because the method does not contain the `()`.
-   The `.split()` method will split a string into an 'array' or list as mentioned in Python.
-   By default `.split()` will default the split on whitespace, but we can pass reference to it for example `.split('l')` on `"hello world!"` will split it like this `["he", "", "o wor", "d!"]`. It means it will now include the whitespace and split the list at the passed reference.

**String Formatting**

-   String interpolation in Python is using `{}.format(str_to_insert).` For example: `print('I am using string {}'.format('interpolation'))`.
-   We can pass as many arguments we need to `.format()`, as long as we have the same args of `{}`. For example `print('The {} {} {} jumped over the fence'.format('quick','brown','fox'))`
-   We can supply the index position into the curly braces if our args are not in the same order. For example: `print('The {1} {2} {0} jumped over the fence'.format('quick','brown','fox'))`
-   We can just use the same index over and over again if we need, even if we have multiple args. Python will ignore it.
-   We can also use variable names to insert interpolation. For example: `print('The {q} {b} {f} jumped over the fence'.format(q='quick',b='brown',f='fox'))`
-   We can format how we want the interpolated code using the following format: `{value:width:precision f}` - the f stands for formatting.
-   `print("The result was {r:1.3f}".format(r=result))` ← here, we are saying that start the index from the number(s) before the decimal point (_this could be multiple digits i.e. 140.343)_, then after the decimal point, include 3 characters to a float i.e. rounded.
-   Instead of using `.format()`, we can just use the keyword `f` and then reference an external variable in to the `{}`. i.e. `print(f'Hello my name is {name}')` ← This is new in Python 3.6
-   The `_future_` module allows you to use Python3 functionality in a Python2 env.

**Lists**

-   Just like arrays, they wrapped in square brackets and separated by commas. They can hold any data type.
-   We can use `len(my_list)` and will return the number of elements in the list.
-   In order to join two lists (or multiples), we can just concat two lists. They will then join as one depending on which list you referenced first.
-   We can mutate lists by index reference.
-   Use `.append(new_item)` to push a new item into the list at the end.
-   `new_list.pop()` will delete the last item. We don't need to reference any args.
-   We can save a popped item as a variable `variable_name = list.pop()`
-   We can delete items in a list by just referencing their index number. `my_list.pop(2)`
-   We can sort a list using `my_list.sort()`.
-   a `NoneType` is a type for a None object - which you can use for no value, similar to nil. It's a common default return value for a function that returns nothing.
-   In order to access a nested list, you would first reference the index of the nested list and then reference the index within the list.

**Dictionaries**

-   They are unordered mappings for storing objects. They are basically the same as objects in JS. They store a key and value and also follow the same syntax `{k:v}`
-   Dictionaries **can not be sorted**.
-   Dictionaries can hold lists, integers, booleans etc and host other dictionaries in them.
-   **You cannot make a dictionary have a variable name i.e.** `{my_life = {name: 'Dan')`. The `name` will throw an error as an undefined variable, so we have to put it in a string.
-   If I want to see the keys or values in a Dictionary, I can use the following items: `dict.keys()`, `dict.values()` and `dict.items()`.
-   If you want to keep the capabilities of a dictionary but would also like ordering, you can use the **ordereddict** object.

**Tuples**

-   Tuples are similar to lists - once an element is inside a tuple, it **cannot be muted**.
-   Tuples use parentheses and commas but work similar to a list (array)
-   You can always confirm what type something is by using `type()`.
-   We can mix different object types, just like lists.
-   We can also still use indexing and slicing like lists.
-   A built in method we can use on tuples is `tuple.count(param)` which will count how many of the same iterations occur in that tuple. We can also use `tuple.index(param)` which will show us the index where the param first appears.
-   Tuples do not allow item assignment so we cannot add something to a hardcoded tuple.
-   The main advantage of using tuples over lists are to ensure that your objects do not accidentally get changed or overwritten/reassignments in your program.
