"""
Этот код на питоне прошёл больше всего (11) тестов
Код на С++ проходит все тесты
Аналогичный код с С++ на пайтон проходит только 10 тестов
"""


from collections import deque


def count_odd(nums: deque[int]) -> str:
    f: int = nums.popleft()
    is_odd: bool = (f % 2 != 0)
    s: int = nums.popleft()
    result: deque[str] = deque()

    while nums or s is not None:
        if is_odd and s % 2 != 0:
            result.append('x')
            f *= s
        else:
            result.append('+')
            f += s
            if not is_odd and s % 2 == 0:
                is_odd = False
            else:
                is_odd = True
        s = nums.popleft() if nums else None
    return ''.join(result)


def main() -> None:
    n: int = int(input())
    nums: deque[int] = deque(map(int, input().split()))
    print(count_odd(nums))


if __name__ == "__main__":
    main()
