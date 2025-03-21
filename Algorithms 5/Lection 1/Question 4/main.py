from typing import List

def count_safety(chess: List[List[str]]) -> int:
    ans: int = 64
    for i in range(len(chess)):
        for j in range(len(chess)):
            if chess[i][j] == 'R':
                while chess[i][j] != 'R':
                    pass
    return ans


def main() -> None:
    chess: List[List[str]] = [[ch for ch in input()] for _ in range(8)]
    print(count_safety(chess))


if __name__ == "__main__":
    main()