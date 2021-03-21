from individual import Individual
import random
import math



class Population:
    """
        A class that describes a population of virtual individuals
    """

    def __init__(self, target, size, mutation_rate):
        self.population = []
        self.generations = 0
        self.target = target
        self.mutation_rate = mutation_rate
        self.best_ind = None
        self.finished = False
        self.perfect_score = 1.0
        self.max_fitness = 0.0
        self.average_fitness = 0.0
        self.mating_pool = []

        for i in range(size):
            ind = Individual(len(target))
            ind.calc_fitness(target)

            if ind.fitness > self.max_fitness:
                self.max_fitness = ind.fitness
                self.best_ind = ind

            self.average_fitness += ind.fitness
            self.population.append(ind)

        self.average_fitness /= size

    def print_population_status(self):
        print("\nPopulation " + str(self.generations))
        print("Average fitness: " + str(self.average_fitness))
        print("Best individual: " + str(self.best_ind))

    # Generate a mating pool according to the probability of each individual
    def natural_selection(self):

        self.population.sort(key = lambda x: x.fitness, reverse=True)
        self.mating_pool = []
      
        number_fit_individuals = int(len(self.population) * 0.25)
        if number_fit_individuals < 5:
            number_fit_individuals = len(self.population)
        
        for i in range(number_fit_individuals):
                j = (number_fit_individuals - i + 1)
                while j > 0:
                    self.mating_pool.append(self.population[i])
                    j -= 1
        for i in range(number_fit_individuals + 1, len(self.population)):
            self.mating_pool.append(self.population[i])
        
    def generate_parents(self):
        dad = self.best_ind if random.randint(0,10) <= 8 else random.choice(self.mating_pool)
        mom = random.choice(self.mating_pool)
        return [dad, mom]
        

    # Generate the new population based on the natural selection function
    def generate_new_population(self):
        new_population = []
        for i in range(len(self.population)):
            dad, mom = self.generate_parents()
            child = mom.crossover(dad)
            child.mutate(self.mutation_rate)
            child.calc_fitness(self.target)
            new_population.append(child)
        self.population = new_population
        self.generations += 1

    # Compute/Identify the current "most fit" individual within the population
    def evaluate(self):
        average_fitness = 0
        for ind in self.population:
            average_fitness += ind.fitness
            if ind.fitness > self.max_fitness:
                self.best_ind = ind
                self.max_fitness = ind.fitness
        self.average_fitness = average_fitness / len(self.population)
        if self.max_fitness == 1:
            self.finished = True

