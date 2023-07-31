

class Zoo:
    zoo_all = []
    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.zoo_all.append(self)
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value, str):
            self._name = value
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self,value):
        if isinstance(value, str):
            self._location = value
    def animal_species(self):
        # for animal in Animal.all_animal:
        #     if animal.zoo == self.name:
        #         return animal.species
        return set(animal.species for animal in Animal.all_animal if animal.zoo == self.name)
    
    def find_by_species(self,target):
        res = []
        for animal in Animal.all_animal:
            if animal.zoo == self.name:
                if animal.species == target:
                    res.append(animal)
        return res
    def animal_nicknames(self):
        res = []
        for animal in Animal.all_animal:
            if animal.zoo == self.name:
                res.append(animal.nickname)
        return res
    @classmethod
    def find_by_location(cls, target):
        res = []
        for zoo in cls.zoo_all:
            if zoo.location == target:
                res.append(zoo)
        return res


if __name__ == "__main__":
    import ipdb
    from animal import Animal
    zoo1 =Zoo("Denver Zoo", "Denver")
    zoo2 = Zoo("LA Zoo", "LA")
    zoo3 = Zoo("Flatiron Zoo", "Denver")
    animal1 = Animal("dog", 10, "doggo", "LA Zoo")
    animal2 = Animal("Cat", 10, "catto", "Denver Zoo")
    animal3 = Animal("Cat", 10, "kitty", "LA Zoo")
    animal4 = Animal("Cat", 10, "kitten", "Denver Zoo")
    animal5 = Animal("Sheep", 10, "sheepdog", "Denver Zoo")
    animal6 = Animal("dog", 10, "pupper", "Denver Zoo")
    ipdb.set_trace()
    
        
    