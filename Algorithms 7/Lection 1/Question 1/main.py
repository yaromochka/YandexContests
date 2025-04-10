def solve(N: int, M: int, X: list[int], Y: list[int]) -> None:
    groups: list[tuple] = sorted([(X[i] + 1, i) for i in range(N)])
    rooms: list[tuple] = sorted([(Y[j], j) for j in range(M)])

    used: list[bool] = [False] * M
    answer: list[int] = [0] * N
    assigned: int = 0

    for need, group_id in groups:
        for i in range(M):
            if not used[i] and rooms[i][0] >= need:
                used[i] = True
                answer[group_id] = rooms[i][1] + 1
                assigned += 1
                break

    print(assigned)
    print(*answer)


def main() -> None:
    N, M = map(int, input().split())
    X: list[int] = [int(x) for x in input().split()]
    Y: list[int] = [int(y) for y in input().split()]
    solve(N, M, X, Y)


if __name__ == "__main__":
    main()