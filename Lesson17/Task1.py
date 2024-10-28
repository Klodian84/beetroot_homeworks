class Animal:

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("Woof woof")


class Cat(Animal):
    def talk(self):
        print("Meow")


def make_animal_talk(animal: Animal):
    animal.talk()


dog = Dog()
cat = Cat()

make_animal_talk(dog)
make_animal_talk(cat)
