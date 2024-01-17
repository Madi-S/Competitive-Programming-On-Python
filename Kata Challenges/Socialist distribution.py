from statistics import mean


def socialist_distribution(population, minimum):
    if mean(population) < minimum:
        return []

    while min(population) < minimum:
        rich_index = population.index(max(population))
        poor_index = population.index(min(population))
        population[rich_index] -= 1
        population[poor_index] += 1

    return population


res = socialist_distribution([5, 5, 5, 15, 70], 5)
print(res, [5, 5, 5, 15, 70], res == [5, 5, 5, 15, 70])
