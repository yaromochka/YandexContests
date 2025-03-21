from typing import List


def count_bigger_then_neighbors(arr: List[int]) -> int:
    counter: int = 0
    for index in range(1, len(arr) - 1):
        if arr[index] > arr[index + 1] and arr[index] > arr[index - 1]: counter += 1
    return counter


def main() -> None:
    arr: List[int] = list(map(int, input().split()))
    print(count_bigger_then_neighbors(arr))


if __name__ == '__main__':
    main()