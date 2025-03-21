from typing import List


def max_place(arr: List[int]) -> int:
    first_place = 0
    for i in range(len(arr)):
        if arr[i] > arr[first_place]: first_place = i

    place: int = len(arr)
    for i in range(first_place, len(arr)):
        if arr[i] % 10 == 5 and arr[i] >= arr[i + 1]:
            place = min(place, i)


    if place != len(arr):
        result: int = 0
        for i in range(len(arr)):
            if arr[i] > arr[place]: result += 1
        return result + 1
    else: return 0


def main() -> None:
    n: int = int(input())
    arr: List[int] = list(map(int, input().split()))
    ans: int = max_place(arr)
    print(ans)



if __name__ == "__main__":
    main()