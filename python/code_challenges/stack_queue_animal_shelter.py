class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        if animal.species == "dog":
            self.dogs.append(animal)
        elif animal.species == "cat":
            self.cats.append(animal)
        else:
            print("Invalid animal species.")

    def dequeue(self, pref):
        if pref == "dog":
            if self.dogs:
                return self.dogs.pop(0)
            else:
                return None
        elif pref == "cat":
            if self.cats:
                return self.cats.pop(0)
            else:
                return None
        else:
            print("Invalid preference.")
            return None


class Cat:
    def __init__(self, name):
        self.name = name
        self.species = "cat"

    def __str__(self):
        return f"Cat {self.name}"


class Dog:
    def __init__(self, name):
        self.name = name
        self.species = "dog"

    def __str__(self):
        return f"Dog {self.name}"



