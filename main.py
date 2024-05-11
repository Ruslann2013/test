import random
a = {
    'player': 0,
    'computer': 0
}

def is_odd(n , n1):
    if n % 2 == 0 and n1 % 2 == 0:
        return False
    else:
        return True

while True:
    b = random.randint(10, 120)
    c = random.randint(10, 120)
    if not is_odd(b , c):
        continue
    op = random.choice(('+', '-'))
    if op == '-':
        ans = b - c
        user = input(f'{b} - {c} =')
    else:
        ans = b + c
        user = input(f'{b} + {c} =')
    if str(ans) == user:
        a['player'] += 2
        print('Всё правильно.')
    else:
        a['computer'] += 2
        print('Не все верно. Ты  ошибся')
    print(f'{a["computer"]}: {a["player"]}: ')