from population import Population
import time

def evaluate_settings(pop_size, mutation_rate):
    target = "To be or not to be."
    pop = Population(target, pop_size, mutation_rate, standard_mutation=True)

    # you don't need to call this function when the ones right bellow are fully implemented
    pop.print_population_status()
    start_time = time.time()
    i = 0
    while not pop.finished:
        pop.natural_selection()
        pop.generate_new_population()
        pop.evaluate()
        if i % 10 == 0:
            pop.print_population_status()
        i += 1
    return [pop.generations, time.time() - start_time]

def main():
    print("===========================================")
    setting_generations = []
    setting_time = []
    population_size = 200
    mutation_rate = 0.02
    print("Setting: ", "population_size", population_size, "mutation_rate", mutation_rate)
    for i in range(0, 20):
        print("Simulation: ", i)
        generations, time_elapsed = evaluate_settings(population_size, mutation_rate)
        setting_generations.append(generations)
        setting_time.append(time_elapsed)
    print("Setting: ", "population_size", population_size, "mutation_rate", mutation_rate)
    print("Average generations: ",sum(setting_generations)/ len(setting_generations))
    print("Total time: ",sum(setting_time))  
    print("===========================================")
    

if __name__ == "__main__":
    main()

    
    
