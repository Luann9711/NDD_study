def robin_queue(n, m, c):
    pizza = [(i + 1, int(c[i])) for i in range(m)]
    # 오븐에 들어간 피자
    pizza_oven = pizza[:n]
    # 남은 피자
    pizza_left = pizza[n:]

    while len(pizza_oven) != 1:
        num, cheese = pizza_oven.pop(0)
        cheese //= 2

        if cheese:
            pizza_oven.append((num, cheese))
        else:
            if pizza_left:
                pizza_oven.append(pizza_left.pop(0))
            

    return pizza_oven.pop()



# 테스트 케이스 입력
try:
    test_case = int(input('테스트 케이스 입력 : '))
except ValueError:
    print('ValueError : Wrong Number!!')
if not(1 <= test_case <= 50):
    raise ValueError


for t in range(1, test_case + 1):
    n, m = map(int, input('화덕 크기 n 과 피자 개수 m 을 입력하시오 : ').split())
    c = list(map(int, input('피자에 뿌려진 치즈의 양을 입력하시오 : ').split()))
    
    pizza_num = robin_queue(n, m, c)

    print(f'#{t} {pizza_num[0]}')