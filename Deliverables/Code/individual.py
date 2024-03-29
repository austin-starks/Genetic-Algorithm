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
            score += int(abs(t-g))
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
            if mutation_type <= 4:
                # minor point mutation - change one random nucleotide to a nearby nucleotide
                char = self.encode(self.genes[random_index])[0] + random.randint(-5, 5)
                char = min(110000, char)
                char = max(0, char)
                self.genes[random_index] = chr(char)
            elif mutation_type <= 6:
                # major point mutation - change one random nucleotide to a random nucleotide
                new_char = random.choice(string.printable)
                self.genes[random_index] = new_char
            elif mutation_type <= 7:
                # frameshift mutation right hand side
                # left halve of gene is untouched; right half of gene is severely affected
                mutated_gene = []
                for i in range(0, random_index):
                    mutated_gene.append(random.choice(string.printable))
                mutated_gene += self.genes[random_index:]
                self.genes = mutated_gene
            elif mutation_type <= 8:
                # frameshift mutation right hand side
                # left halve of gene is untouched; right half of gene is minorly affected
                mutated_gene = self.genes[0:random_index]
                for i in range(random_index, len(self.genes)):
                    char = self.encode(self.genes[i])[0] + random.randint(-5, 5)
                    char = min(110000, char)
                    char = max(0, char)
                    mutated_gene.append(chr(char))
                self.genes = mutated_gene
            elif mutation_type <= 9:
                # frameshift mutation right hand side
                # left halve of gene is untouched; right half of gene is severely affected
                mutated_gene = self.genes[0:random_index]
                for i in range(random_index, len(self.genes)):
                    mutated_gene.append(random.choice(string.printable))
                self.genes = mutated_gene
            else:
                # frameshift mutation left hand side
                # right half of gene is untouched, left half of gene is minorly affected
                mutated_gene = []
                for i in range(0, random_index):
                    char = self.encode(self.genes[i])[0] + random.randint(-5, 5)
                    char = min(110000, char)
                    char = max(0, char)
                    mutated_gene.append(chr(char))
                mutated_gene += self.genes[random_index:]
                self.genes = mutated_gene
 






