import random
import numpy as np
import time 

nq = 8 
maxFitness = (nq*(nq-1))/2

def random_chromosome(size): #random permutation 
    arr = np.array([i for i in range(size)]) 
    random.shuffle(arr)
    return arr

def fitness(chromosome): #use number of attacking pairs as fitness
    numOfAttacking = 0
    N = len(chromosome)
    for i in range(N-1):
        for j in range(i+1, N):
            if abs(chromosome[i] - chromosome[j]) == (j - i):
                numOfAttacking += 1

    return int(maxFitness - numOfAttacking)

def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
        
def reproduce(x, y): #order crossover
    n = len(x)
    l = random.randint(0, n - 1)
    r = random.randint(0, n - 1)
    if l > r:
        l, r = r, l
    z = [-1] * n
    z[l:r+1] = x[l:r+1]
    index = r+1
    for i in range(r+1, r+1+n):
        if index == n:
            index = 0
        if index == l:
            break
        if y[i%n] not in z:
            z[index] = y[i%n]
            index += 1
    return z

def mutate(x):  #inversion mutation
    n = len(x)
    l = random.randint(0, n - 1)
    r = random.randint(0, n - 1)
    if l > r:
        l, r = r, l
    y = x[:]
    y[l:r+1] = x[l:r+1][::-1] 
    return y

def genetic_queen(population, fitness):
    mutation_probability = 0.5
    new_population = population[:]
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities) #best chromosome 1
        y = random_pick(population, probabilities) #best chromosome 2
        child = reproduce(x, y) #creating two new chromosomes from the best 2 chromosomes
        # child = x
        if random.random() < mutation_probability:
            child = mutate(child)
        # print_chromosome(child)
        new_population.append(child)
        if fitness(child) == maxFitness: break
    new_population = sorted(new_population, key=lambda x: fitness(x), reverse=True)
    return new_population[:100]

def print_chromosome(chrom):
    print(f"Chromosome = {str(chrom)},  Fitness = {fitness(chrom)}")

def main():
    population = [random_chromosome(nq) for _ in range(100)]
    
    generation = 1

    start_time = time.time()
    while not maxFitness in [fitness(chrom) for chrom in population]:
        # print(f"=== Generation {generation} ===")
        population = genetic_queen(population, fitness)
        # print("")
        # print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1
        if time.time() - start_time >= 100:
            print(f"Go through {generation} Generations.")
            print("Minimum of Attacking queen pairs = {}".format(maxFitness - max([fitness(n) for n in population])))
            return
    chrom_out = []
    print("Solved in Generation {}!".format(generation-1))
    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("");
            print("One of the solutions: ")
            chrom_out = chrom
            print_chromosome(chrom)
            break

if __name__ == "__main__":
    main()
