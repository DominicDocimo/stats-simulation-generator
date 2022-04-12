import random

shots_per_season = 20
total_seasons = 25
categories = [[0, 1], [2, 3, 4, 5, 6, 7, 8, 9]]
stats = []
numbers = []

while total_seasons >= 1:
    season_shots = shots_per_season
    season_misses = 0
    season_hits = 0
    while season_shots >= 1:
        season_shots -= 1
        number = random.randint(1, 10)
        numbers.append(number)
        if number in categories[0]:
            season_misses += 1
        else:
            season_hits += 1
    total_seasons -= 1
    stats.append((season_hits, season_misses))

print(stats)
print(f"Total hits: {sum([x[0] for x in stats])}")
print(f"Total misses: {sum([x[1] for x in stats])}")
print(f"Accuracy: {(sum([x[0] for x in stats]) / (sum([x[0] for x in stats]) + sum([x[1] for x in stats])))*100}%")
print(f"Total times he missed more than 3 times: {sum([1 for x in stats if x[1] >= 3])}")
print(numbers)
