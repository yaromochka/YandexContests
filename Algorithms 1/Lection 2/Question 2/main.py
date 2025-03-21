from typing import List

def sequence_type() -> str:
    IS_CONSTANT = True
    IS_ASCENDING = True
    IS_WEAKLY_ASCENDING = True
    IS_DESCENDING = True
    IS_WEAKLY_DESCENDING = True

    prev: int = int(input())
    arr: List[int] = []
    while prev != -2 * 10 ** 9:
        arr.append(prev)
        prev = int(input())

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]: IS_CONSTANT = False
        if arr[i] > arr[i - 1]:
            IS_DESCENDING = False
            IS_WEAKLY_DESCENDING = False
        if arr[i] < arr[i - 1]:
            IS_ASCENDING = False
            IS_WEAKLY_ASCENDING = False
        if arr[i] == arr[i - 1]:
            IS_ASCENDING = False
            IS_DESCENDING = False
    if IS_CONSTANT: return "CONSTANT"
    elif IS_DESCENDING: return "DESCENDING"
    elif IS_ASCENDING: return "ASCENDING"
    elif IS_WEAKLY_DESCENDING: return "WEAKLY DESCENDING"
    elif IS_WEAKLY_ASCENDING: return "WEAKLY ASCENDING"
    else: return "RANDOM"


def main() -> None:
    print(sequence_type())


if __name__ == "__main__":
    main()