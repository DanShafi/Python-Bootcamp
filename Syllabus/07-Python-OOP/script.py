class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # perform some action
        print(self.param1)


class Dog():

    species = 'mammal'

    def __init__(self, mybreed, name):

        self.breed = mybreed
        self.name = name

    def bark(self):
        print('Woof! My name is {}'.format(self.name))


first_dog = Dog(mybreed='Pom', name='Bob')
second_dog = Dog(mybreed='Lab', name='Leo')
third_dog = Dog(mybreed='Jack Spaniel', name='Sammy')

my_dog = Dog('Lab', 'Frankie')
my_dog.bark()

print(first_dog.breed)


class Circle():

    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius
        self.area = radius*radius*Circle.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle()
my_circle.radius(30)
my_circle.get_circumference()
