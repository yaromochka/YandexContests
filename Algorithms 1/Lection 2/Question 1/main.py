from typing import List


def is_sorted(array: List[int]) -> str:
    for i in range(1, len(array)):
        if array[i] <= array[i - 1]: return 'NO'
    return 'YES'


def main() -> None:
    arr: List[int] = list(map(int, input().split()))
    print(is_sorted(arr))


if __name__ == '__main__':
    main()