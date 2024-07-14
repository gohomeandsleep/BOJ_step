while True:
    try:
        n = int(input())
        lst = [1]
        cnt = 1
        while int(''.join(map(str, lst))) % n != 0:
            lst.append(1)
            cnt +=1
        print(cnt)
    except:
        break