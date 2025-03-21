def count_sequences(N: int) -> int:
    if N == 1:
        return 2
    elif N == 2:
        return 4
    elif N == 3:
        return 7

    dp = [0] * (N + 1)
    dp[1], dp[2], dp[3] = 2, 4, 7

    for i in range(4, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[N]


def main() -> None:
    N = int(input().strip())
    print(count_sequences(N))


if __name__ == '__main__':
    main()