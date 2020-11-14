**If, Elif & Else**

-   Mainly concerned in the need for **control flow**.
-   We use these statements when we only want certain code to execute in a program that execugtes when a particular condition has been met.
-   Control flow syntax makes use of colons and indentation. This indentation system is crucial to Python and unique to the language.
-   Any IDE that runs a .py file should automatically indent for you when you run if/else statements.

**For Loops**

-   **Iterable** means to iterate over every object. It means you can perform an action for every object in a particular data structure.
-   The syntax for a **for** loop in Python, is the following:

```python
my_interable = [1,2,3] #1
for item in my_iterable: #2
	print item #3
```

-   #1 is the variable in which we would like to iterate over. #2, we call the `for` keyword and the `item` in this code block represents each individual item in an object. The `in my_iterable` is declaring what we would like to iterate over. Similar to if/else statements, we then use a colon to open the code block and then #3 is the code we would like to execute.
-   In a for loop, we can have conditionals attached i.e if and else statement meaning we can execute a large code block in one go, rather than waiting for an iteration to occur and then reference the variable in another block.
-   Have to be careful to make sure that indentation is correct or it will affect the way the code runs.
-   You don't have to assign a variable to something you want to iterate over - you can directly run it in the for loop.
-   A common syntax we can use is `for _ in 'Hello World'`. The `_` is used in lieu of us using variable, for example if our codeblock does not need to reference the variable.
-   We can use a for loop for a tuple too. However, there is a special quality in for loops for tuples. If we have a list of tuples and run a for loop, Python will just return back the tuples as items in the list. If we want to extract, we use a concept called **tuple unpacking**. Essentially, we duplicate the tuple syntax in the for loop to tell Python that we're looking for a pair etc.

    ```python
    tup_list = [(1,2),(3,4),(5,6),(7,8)]

    for a,b in tup_list:
    	print(a)
    	print(b)
    ```

-   In Dictionary iteration using a for loop, it will only return the keys. If you want to iterate through the values too, your for loop syntax needs to be as such: `for item in var.items()` - This will return tuples of the key value pair. We can then use tuple unpacking and amend our variable to include the key value items.
-   **While Loops**

-   While Loops will continue to execute a block of code **while** some condition remains `True`. It will only break when said condition has been met.
-   Syntax: `while some_boolean_condition: #do something.`We can also combine an else statement to a while.
-   Three useful keywords for loops are `break`, `continue` and `pass`. `break` will break out of the current closest enclosing loop. `continue` goes to the top of the closest enclosing loop and `pass` does nothing at all.
-   EOF stands for End Of File.
-   In a loop block, you cannot just use a comment or keep a block open without a code block, so we can just use `pass` . We can use this as a holder for a function that we may want to test later and this will avoid syntax errors.
-   `continue` will tell the program to go back to the closest enclosing loop. That means once the condition has been called prior to the `continue`, it will then go back to the loop beginning and continue to run it from there:

```python
for letter in mystring:
   if letter == 'a':
      continue
   print(letter)
```

-   `break` will stop the loop if the condition within the loop has been met. The output will just be any code before the the break condition.

**Useful Operators**

-   Instead of iterating through a range of numbers in a list stored in a variable, we can just use the `range()` syntax. For example:

```python
for num in range(10):
	print(num)
```

-   In range, we can specify what range we want to iterate through for example `range(3,10)`. Remember, the last integer specified is not inclusive and will not be returned i.e. `range(10)` will return up until 9.
-   We can also use a step size as a third argument. For example `range(0,10,2)` which will iterate through 0-10 and only return every other number in a step of 2.
-   `range()` is what we call a **generator** - a special type of function which will generate information rather than saving it to memory.
-   The `enumerate()` generator takes a variable argument for example a string of letters and allows you to index each iteration it outputs. This will generate tuples.
-   A `zip()` generator will combine two or more lists together and output it as a tuple. Depending on which list is in the order in the args, Python will match each index and output. If one list is larger than the others, Python will immediately only run the zip function to the length with the shortest list. This is why tuple unpacking is important because most outputs in Python will be tuples.

```python
mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1, mylist2, mylist3):
	print(item)
```
