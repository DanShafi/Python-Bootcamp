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

-
