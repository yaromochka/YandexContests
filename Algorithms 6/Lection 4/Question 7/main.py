import sys

sys.setrecursionlimit(10 ** 6)


def dfs(v, graph, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)


def solve():
    # Чтение входных данных
    N, M, K = map(int, input().split())

    # Граф, в котором храним связи между дятлами
    graph = [[] for _ in range(N + 1)]

    # Считываем связи между дятлами
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # Массив, чтобы отслеживать посещенные вершины
    visited = [False] * (N + 1)

    # Количество компонент связности
    components_count = 0

    # Проходим по всем вершинам и считаем количество компонент связности
    for i in range(1, N + 1):
        if not visited[i]:
            # Для каждой новой компоненты запускаем dfs
            dfs(i, graph, visited)
            components_count += 1

    # Количество способов размещения дятлов
    result = pow(2, components_count, K)

    # Выводим результат
    print(result)


# Вызов функции решения
solve()
