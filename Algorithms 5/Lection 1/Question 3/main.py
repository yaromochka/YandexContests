from typing import List


def count_press(spaces: List[int]) -> int:
    ans: int = 0
    for space in spaces:
        ans += space // 4
        if space % 4 == 1 or space % 4 == 2:
            ans += space % 4
        if space % 4 == 3:
            ans += 2
    return ans


def main() -> None:
    n: int = int(input())
    spaces: List[int] = [int(input()) for _ in range(n)]
    print(count_press(spaces))


if __name__ == "__main__":
    main()