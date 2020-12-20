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


first_dog = Dog(mybreed='Pom', name='Bob')
second_dog = Dog(mybreed='Lab', name='Leo')
third_dog = Dog(mybreed='Jack Spaniel', name='Sammy')

print(first_dog.breed)
