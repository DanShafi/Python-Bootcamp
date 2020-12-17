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
