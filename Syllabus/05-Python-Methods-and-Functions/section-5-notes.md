**Methods:**

-   Methods are built-in objects in Python.
-   Use the Python Docs page to check all methods available to us, in particular **Library Reference**.
-   The docs also share common sequence operations which will explain various different methods and the correct way of using them.
-   We can use `help(var.method)` if we want to understand what the method does or what params it requires.
-   Functions allow us to create blocks of code that can be repeated many times, keeping our code **DRY.**

**def Keyword**

-   Creating a function in Python requires the `def` keyword and specific syntax.
-   We use snake_casing as a convention when defining a function name i.e. `def function_name():`
-   A Docstring means using a triple quote that allows us to embed a comment in our function so an external person can understand what purpose the function serves for example:

    ```python
    def my_function():
    	""
      My function will do something cool
    	""
    	print('Cool')
    ```

-   Everything inside a function will be indented.
-   Typically, we use the **return** keyword in order to execute the code in a function.
-   Return allows us to assign the output of the function to a new variable so we can use this for other reasons.

**Basics of Python Functions**

-   If you call a function name without the `()`, Python will just tell you that what you've called is a function.
-   We can overwrite functions by rewriting them.
-   If we forget to put in an arg where a param is required, we can use a default value, by using an equal i.e. `def say_hello(name='User')`
-   If you try to check a type of a function that only prints the output, it will come back as a NoneType.
-   Python is statically typed so it does not ask you to declare what a variable is before you write it in a function - this could mean that if you are expecting a user to input an int, Python will accept that input as a string and if you were doing arithmetics, you could be doing string concat rather than integer maths.

**Functions with Logic**

-   In logic statement, if we use the keyword `pass` it tells Python to not do anything.
-   In an if/else statement, if we put the else to return false then Python will only evaluate the first condition which would throw a bug.
-   Instead, we will pass the `return False` at the end of the for loop, basically instructing Python to run the entire for loop, if this is completed and we never broke out of the function then return False.

```python
def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass

    return False
```

-   It's very common in a function call to define an empty placeholder within the function (think empty array).

**Tuple Unpacking with Functions**

-   With standard tuple unpacking, we can just run a for loop for the key value object.
-   We can create functions that can do the tuple unpacking for us - imagine a scenario where we have a subset of data that we want to compare against, i.e. employee of the month who has worked the longest number of hours. It could look something like this:

```python
def employee_month(work_hours):

    current_max = 0
    employee_of_the_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass

    return (f'Employee of the month is {employee_of_the_month} having worked {current_max} hours!')
```

-   If you try to unpack more tuples than they are in a function call, you will get a ValueError. Best way to check is assign all values to a single variable and then review how many values you have.

**Interactions between Python Functions**

-   Typically a python script contains several functions interacting with other.
-   Remember, we can import libs in order to help us carry out basic methods, i.e. shuffle etc.
-   We can't store the shuffle method in a variable, we have to create a function to do this.
-   In a .py file, it's good convention to keep all your functions at the top.

**\*Args & **Kwargs in Python\*\*

-   Arguments and **keyword arguments**.
-   We can use \*args to take an arbitrary number of arguments in a function. For example:

```python
def myfunc(*args):
	return sum(args) * 0.05
```

-   This way, we can continue to add arguments to our liking without having to define a pre-approved numbers of params.
-   We don't need to use the word _args_, we can replace this with anything as long as it follows the same convention with the asterisk. However, by convention its good to just use \*args.
-   \*args always returns a tuples.
-   \*\*kwargs builds and always returns a dictionary of k,v pairs.

```python
def myfunc(**kwargs):
	if 'fruit' in kwargs:
		print('My fruit of choice is {}'.format(kwargs['fruit']))
	else:
		print('I did not find any fruit here')

myfunc(fruit='apple', veggie='lettuce')

# Output: My fruit of choice is apple.
```

-   A function can accept both \*args and \*\*kwargs together. However, we need to ensure that we only call the right args depending on the position they have been set, or Python will throw an error.
