def count_profit(n: int, k: int, d: int) -> str:
    for i in range(10):
        num = (n * 10 + i)
        if num % k == 0:
            break
    else:
        return "-1"
    return str(num) + "0" * (d - 1)


def main() -> None:
    n, k, d = map(int, input().split())
    ans = count_profit(n, k, d)
    print(ans)


if __name__ == "__main__":
    main()