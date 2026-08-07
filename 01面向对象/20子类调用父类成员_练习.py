class Animal:
    def eat(self):
        print('阿姆阿姆')

class Dog(Animal):
    def eat(self):
        print('吭哧吭哧')
    def super_eat(self):
        super().eat()

dog = Dog()
dog.eat()
dog.super_eat()
