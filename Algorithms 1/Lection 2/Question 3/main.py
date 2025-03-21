from typing import List


def find_closer(arr: List[int], number) -> int:
    closer: int = arr[0]
    min_difference: int = abs(number - arr[0])
    for elem in arr:
        if abs(number - elem) < min_difference:
            closer = elem
            min_difference = abs(number - elem)
    return closer


def main() -> None:
    n: int = int(input())
    arr: List[int] = list(map(int, input().split()))
    number: int = int(input())
    print(find_closer(arr, number))


if __name__ == "__main__":
    main()