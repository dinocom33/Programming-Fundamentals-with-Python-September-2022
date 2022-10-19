population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

is_distribution_possible = True

for current_wealth in population:
    wealth_needed = 0
    wealthiest = max(population)
    poorest = min(population)
    wealthiest_index = population.index(wealthiest)
    poorest_index = population.index(poorest)
    if sum(population) < minimum_wealth * (len(population)):
        print("No equal distribution possible")
        is_distribution_possible = False
        break
    if current_wealth < minimum_wealth:
        population[poorest_index] += (minimum_wealth - current_wealth)
#        population[current_wealth] = population[((minimum_wealth - current_wealth) + current_wealth)]
        population[wealthiest_index] -= minimum_wealth - current_wealth

if is_distribution_possible:
    print(population)
