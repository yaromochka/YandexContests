# TODO: доделать задачу т.к. она оч странная в плане реализации


def count_rounds(x: int, y: int, p: int) -> int:
    level: int = 0
    soldiers: int = 0 # солдаты врага
    while (y > 0 or soldiers > 0) and x > 0:
        # print(f'lvl: {level}, y: {y}, soldiers: {soldiers}, x: {x}')
        damage: int = x # наносимый в каждом раунде урон
        if y + p <= damage * 1.618:
            if y > 0:
                damage -= y
                y = 0
                soldiers -= damage
            else:
                soldiers -= damage
        else:
            if soldiers >= damage:
                if y >= 0:
                    damage -= y
                    y = 0
                    soldiers -= damage
                else:
                    y -= damage
            else:
                damage -= soldiers
                soldiers = 0
                y -= damage
        x -= soldiers
        level += 1
        if y > 0:
            soldiers += p
    # print(f'lvl: {level}, y: {y}, soldiers: {soldiers}, x: {x}')
    return level if x > 0 else -1


def main() -> None:
    x: int = int(input()) # количество солдат
    y: int = int(input()) # здоровье казармы
    p: int = int(input()) # производимые солдаты
    print(count_rounds(x, y, p))


if __name__ == "__main__":
    main()