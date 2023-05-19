from itertools import combinations_with_replacement
def generate_bouquets(K, N):
    flowers = list(range(1, K+1))
    bouquets = []

    for num_flowers in range(1, N+1):
        for bouquet in combinations_with_replacement(flowers, num_flowers):
            bouquets.append(bouquet)
    return bouquets
K = int(input("Введите количество видов роз: "))
N = int(input("Введите максимальное количество цветов в букете: "))

all_bouquets = generate_bouquets(K, N)

print("Все возможные варианты букетов:")
for bouquet in all_bouquets:
    print(bouquet)
