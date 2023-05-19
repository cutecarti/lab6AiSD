def cwr(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
#Часть 1


# #Функция генерирует все букеты длинной не больше N
def generate_bouquets(K, N):
    flowers = list(range(1, K+1))
    bouquets = []

    for num_flowers in range(1, N+1):
        for bouquet in cwr(flowers, num_flowers):
            bouquets.append(bouquet)
    return bouquets

#Часть 2


#Функция генерирует все букеты длинной не больше N, в которых один вид роз не встречается больше 2 раз
def generate_hardboquets(K,N):
    flowers = list(range(1, K+1))
    bouquets = []

    for num_flowers in range(1, N+1):
        for bouquet in cwr(flowers, num_flowers):
            if len(set(bouquet)) >= len(bouquet) - 1:
                bouquets.append(bouquet)
                most_expensive_bouquet(bouquet)
    return bouquets

max = 0
maxbouquet = tuple()
s = 0
pricelist = {1:100,2:58,3:44,4:87,5:154,6:118,7:65,8:29,9:95,10:299,11:43,12:59,13:999,14:32,15:29,16:51,17:240,18:178,19:44,20:74}

#Целевая функция ищет самый дорогой букет и его стоймость
def most_expensive_bouquet(list):
    global s
    global max
    global maxbouquet
    for i in list:
        s += pricelist.get(i)
    if s > max:
        max = s
        maxbouquet = tuple(list)
        s = 0


print('Выберите режим(0 - обычное исполнение,1 - усложненное):')
choise = input()
if choise == '0':
    print('Введите количество видов:')
    k = int(input())
    print('Введите максимальный размер букета:')
    n = int(input())
    print('Сгенерированные букеты:')
    for i in generate_bouquets(k,n):
        print(i)
elif choise == '1':
    print('Введите количество видов(Не больше 20):')
    k = int(input())
    print('Введите максимальный размер букета:')
    n = int(input())
    print('Сгенерированные букеты:')
    for i in generate_hardboquets(k,n):
        print(i)
    print('Самый дорогой букет: ',maxbouquet)
    print('Цена: ', max)

