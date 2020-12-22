**Introduction**

-   OOP allows programmers to create their own objects that have methods and attributes.
-   These methods act as function that use information about the object as well as the object itself to return results.
-   OOP allows us to create code that is repeatable.
-   OOP utilises the `self` keyword.
-   For larger code bases, functions by themselves aren't enough for organisation - commonly repeated tasks should use OOP.
-   The way to define an object (also known as a class) is to use the `class` keyword. The name of the class always uses camelCase like JS. Once we have established this, we use a special method call `__init__` that allows us to create an **instance** of the class. We then use the `self` keyword as a param.

```python
class NameOfClass():

		def __init__(self,param1,param2):
				self.param1 = param1
				self.param2 = param2

		def some_method(self):
				# perform some action
				print(self.param1)
```

-   As a placeholder class, we can just use the `pass` keyword.
-   Any function that runs inside a Class, is called a **method**.
-   When we create a class, we always begin with a `def __init__(self)` - so we can always connect with the class.
-   `__init__` is a constructor of the class. It will always get called automatically when an instance of the class has been generated.
-   Attributes are _characteristics_ of the object. We tell Python that we want to create an instance of the object and have that instance being build on the attributes of the parent.

**OOP Part Two**

-   In an object, we can define a **class object attribute**. We define these **above** the `def __init__` and we don't need to call `self` on them because they will always be defined in the object.
-   When we call the instance of the method, the **class object attribute** will always be present as part of the object/class. So if we call the instance of the object, we don't need to define it as a param.
-   We know that the **class object attribute** will always be the same no matter what instance of the class, hence why we don't use the `self` keyword.
-   Methods are functions defined in the body of the class → Important interview concept.
-   Attributes never have `()` . Instead, they're characteristics of the class that you callback.
-   When we're working with objects, we have to reference the instance of the object. So, if for example we're referencing a name in a string in an method, we won't use `.format(name)`, we have to use `.format(self.name)`.
-   We can have more params for a method in an object. We provide the argument as usual like normal functions.
-   We can reference the class name when calling the self.methods inside the `__init__` method. So, instead of self.pi, we can have Circle.pi
