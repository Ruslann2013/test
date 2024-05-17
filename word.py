import random
s = ['чашка', "кошка", "мышка", "кружка", "стол", "стул", "собака", "лев", "лопата"]
while True:
    a = random.choice(s)
    b = random.choice(s)
    d = input(f'{a} + {b} =')
    if d != a + b:
        print('Ты ошибся.Попробуй снова')
    else:
        print(' Ты оветил правильно. Попробуй вот это.')
    print(d)
