import random
a = {
    'player':0,
    'computer':0
}
while True:
    b = random.randint(10, 90)
    c = random.randint(10, 90)
    op = random.choice(('+', '-'))
    if op =='+':
        ans = b + c
        user = input(f'{b} + {c} =')
    else:
        ans = b - c
        user = input(f'{b} - {c} =')
    if str(ans) == user:
        a['player'] += 1
        print('Всё верно')
    else:
        a['computer'] += 1
        print('Не все верноxrj. Ты где-то ошибся')
    print(f'{a["computer"]}: {a["player"]}: ')