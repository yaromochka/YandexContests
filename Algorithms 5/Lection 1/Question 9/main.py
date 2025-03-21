result = 0
while True :
    try :
        n = int(input('Введите число'))
        if n == 0 :
            break
        result += n
    except :
        continue
print(result)