def count_time(L: int, x1: int, v1: int, x2: int, v2: int) -> int:
    ans: int = 10 ** 30
    for rotation in range(2):
        deltax: int = (x2 - x1 + L) % L
        deltav: int = (v1 - v2)
        if deltav < 0:
            deltav *= -1
            deltax = -deltax % L
        if deltax == 0:
            ans = 0
        if deltav != 0:
            ans = min(ans, deltax / deltav)
        x2 = -x2 % L
        v2 = -v2
    if ans == 10 ** 30: return -1
    return ans


def main() -> None:
    L, x1, v1, x2, v2 = map(int, input().split())
    t: int = count_time(L, x1, v1, x2, v2)
    if t == -1: print('NO')
    else: print('YES', f'{t:.10f}', sep='\n')


if __name__ == "__main__":
    main()