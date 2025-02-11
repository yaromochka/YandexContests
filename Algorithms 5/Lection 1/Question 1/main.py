def count_paint(P: int, V: int, Q: int, M: int) -> int:
    minv, maxv = P - V, P + V
    minm, maxm = Q - M, Q + M
    if max(minv, minm) <= min(maxv, maxm):
        return max(maxv, maxm) - min(minv, minm) + 1
    else:
        return (maxv - minv + 1) + (maxm - minm + 1)


def main() -> None:
    P, V = map(int, input().split())
    Q, M = map(int, input().split())
    print(count_paint(P, V, Q, M))


if __name__ == "__main__":
    main()