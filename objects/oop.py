class Country:
    name = ""
    population = 0
    area = 0

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        return self.area > other.area

    def population_density(self):
        return self.area / self.population

    def __str__(self):
        return self.name, " has a population of ", self.population, " and is ", \
               self.population_density(), " Square km."

    def __repr__(self):
        return [self.name, self.population, self.area]


canada = Country("Canada", 37000000, 9000000)
spain = Country("Spain", 900000, 1235121)


print(canada.area)
print(spain.name)
print(spain.is_larger(canada))
print(spain.population_density())
print(spain.__str__())
print(spain.__repr__())
