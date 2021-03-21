import random
import string


class Individual:
    """
        Individual in the population
    """

    def __init__(self, size):
        self.fitness = 0
        self.genes = self.generate_random_genes(size)
    
    def encode(self, target):
        """
        Encodes the word
        """
        result = []
        for char in target:
            result.append(ord(char))
        return result

    # Fitness function: returns a floating points of "correct" characters
    def calc_fitness(self, target):
        score = 0
        encoded_target = self.encode(target)
        encoded_genes = self.encode(self.genes)
        for t, g in zip(encoded_target, encoded_genes):
            score += int(((t-g)**2)**0.5)
        # insert your code to calculate the individual fitness here
        self.fitness = 1/(1+(score * 0.05))
        

    def __repr__(self):
        return ''.join(self.genes) + " -> fitness: " + str(self.fitness)

    @staticmethod
    def generate_random_genes(size):
        genes = []

        for i in range(size):
            genes.append(random.choice(string.printable))
        return genes

    # The crossover function selects pairs of individuals to be mated, generating a third individual (child)
    def crossover(self, partner):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        ind_len = len(self.genes)
        child = Individual(ind_len)
        gene = []
        
        for i, (t, g) in enumerate(zip(partner.genes, self.genes)):
            if random.randint(0, 9) < 5:
                gene.append(t)
            else: 
                gene.append(g)

        child.genes = gene

        return child

    # Mutation: based on a mutation probability, the function picks a new random character and replace a gene with it
    def mutate(self, mutation_rate):
        # random number is betwen 0 and 1
        # mutation rate is a number between 0 and 1
        # if mutation rate is 0, never mutate
        # if mutation rate is 1, always mutate
        # if mutation rate is greater than random number, mutate

        random_number = random.random()
        if mutation_rate > random_number:
            mutation_type = random.randint(0, 10)
            random_index = random.randrange(len(self.genes))
            if mutation_type <= 6:
                # major point mutation
                new_char = random.choice(string.printable)
                self.genes[random_index] = new_char
            elif mutation_type <= 8:
                # frameshift mutation left hand side
                mutated_gene = self.genes[0:random_index]
                for i in range(random_index, len(self.genes)):
                    mutated_gene.append(random.choice(string.printable))
                self.genes = mutated_gene
            else:
                # frameshift mutation right hand side
                mutated_gene = []
                for i in range(0, random_index):
                    mutated_gene.append(random.choice(string.printable))
                mutated_gene += self.genes[random_index:]
                self.genes = mutated_gene
 






