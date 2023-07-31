# from zoo import Zoo
class Animal:
    all_animal = []
    def __init__(self, species, weight, nickname, zoo):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo
        Animal.all_animal.append(self)
    # def nickname(self):
    #     return self.nickname
    # def weight(self):
    #     return self.weight
    # def species(self):
    #     return self.species

    # def zoo(self):
    #     return self.zoo
    @property
    def species(self):
        return self._species
    @species.setter
    def species(self, value):
        if isinstance(value, str):
            self._species = value
    @property
    def nickname(self):
        return self._nickname
    @nickname.setter
    def nickname(self, value):
        if isinstance(value, str):
            self._nickname = value
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        if isinstance(value, int):
            self._weight = value
    # @property
    # def zoo(self):
    #     return self._zoo
    # @zoo.setter
    # def zoo(self, value):
    #     if isinstance(value, Zoo):
    #         self._zoo = value
            
    @classmethod
    def find_by_species(cls, speciesCheck):
        return [animal for animal in cls.all_animal if animal.species == speciesCheck]
    
if __name__ == "__main__":
    import ipdb
    ipdb.set_trace()

