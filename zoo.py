
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self, food):
        print(f"{self.name} кормится {food}.")



class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} курлыкает.")


class Mammal(Animal):
    def __init__(self, name, age, has_fur=True):
        super().__init__(name, age)
        self.has_fur = has_fur

    def make_sound(self):
        print(f"{self.name} рычит.")


class Reptile(Animal):
    def __init__(self, name, age, is_venomous=False):
        super().__init__(name, age)
        self.is_venomous = is_venomous

    def make_sound(self):
        print(f"{self.name} шипит.")



def animal_sound(animals):
    for animal in animals:
        animal.make_sound()




class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлен {animal.name} в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Добавлен {staff_member.name} в штат сотрудников зоопарка.")



class Staff:
    def __init__(self, name):
        self.name = name


class ZooKeeper(Staff):
    def feed_animal(self, animal, food):
        print(f"{self.name} кормит {animal.name} {food}.")
        animal.eat(food)


class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} делает прививку {animal.name}.")


if __name__ == "__main__":

    zoo = Zoo()

    crane = Bird("Журавль", 3)
    leopard = Mammal("Барс", 5)
    snake = Reptile("Удав", 2)

    zoo.add_animal(crane)
    zoo.add_animal(leopard)
    zoo.add_animal(snake)

    animal_sound(zoo.animals)

    keeper = ZooKeeper("Андрей")
    vet = Veterinarian("Даша")

    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    keeper.feed_animal(leopard, "мясо")
    vet.heal_animal(snake)