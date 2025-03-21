def count_goals(G11: int, G12: int, G21: int, G22: int, l: int) -> int:
    if l == 1:
        if G11 >= G12:
            if G21 > G22: return 0
            elif G21 <= G22: return G22 - G21 - G11 + G12 + 1
        elif G11 <= G12:
            if G21 > G22: return G12 - G11
            elif G21 <= G22: return G22 - G21 + G12 - G11
    elif l == 2:
        if G11 >= G12:
            if G21 > G22: return 0
            elif G21 <= G22: return G21 - G12
        elif G11 <= G12:
            if G21 > G22: return G11 - G12
            elif G21 <= G22: return G22 - G21 + 1


def main() -> None:
    G11, G12 = map(int, input().split(':'))
    G21, G22 = map(int, input().split(':'))
    l: int = int(input()) # 1 - первая команда дома, 2 - первая команда в гостях
    print(count_goals(G11, G12, G21, G22, l))



if __name__ == "__main__":
    main()