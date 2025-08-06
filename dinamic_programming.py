""" Lession - Dinamic programming """


def backpack(W, wt, val, n):
    """ Task backpack """
    dp = [[0 for x in range(W +1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 and w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

val = [10, 100, 1000]
wt = [5, 50, 500]
W = 20
n = len(val)
print(f'Рюкзак: {backpack(W=W, wt=wt, val=val, n=n)}')

def length_tow_strong(text1: str, text2: str) -> int:
    """length 2 string"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

test_one = "Lorem ipsum dolor sit amet"
test_tow = "Nulla porta lectus in nulla iaculis tristique"

print(f'\nДлина наибольшей общей подпоследовательности: {length_tow_strong(text1=test_one, text2=test_tow)}')

test_one = "Suspendisse fringilla magna eget ligula fermentum posuere"
test_tow = "In ac nibh eget quam pharetra tincidunt sed id massa"

print(f'Длина наибольшей общей подпоследовательности: {length_tow_strong(text1=test_one, text2=test_tow)}')


def number_splitting(n: int) -> int:
    """ number splitting """
    dp = [0] * (n + 1)
    dp[0] = 1 
    for num in range(1, n + 1):
        for i in range(num, n + 1):
            dp[i] += dp[i - num]
    return dp[n]

print(f"\nРазбитие числа 5 :{number_splitting(5)}")

print(f"Разбитие числа 23 :{number_splitting(23)}")


def floyd_warshall(adj_matrix):
    """floyd warshall"""
    n = len(adj_matrix)
    dist = [row[:] for row in adj_matrix]  # Создаем копию матрицы
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


INF = float('inf')

adj_matrix = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

shortest_paths = floyd_warshall(adj_matrix)

print("\nКратчайшие пути между всеми парами вершин:")
for row in shortest_paths:
    print(row)
