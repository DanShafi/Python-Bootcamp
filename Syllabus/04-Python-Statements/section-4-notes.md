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
-
