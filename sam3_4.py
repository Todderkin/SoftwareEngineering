word = input('Введите предложение: ')
print('Длина предложения: ', len(word))
print('Предложение в нижнем регистре: ', word.lower())
glas = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in word:
    if i in glas:
        count += 1
print('Колличество гласных в предложении: ', count)
finish = len(word)-3

word = word.lower()


ugly = 'ugly'
beauty = 'beauty'
if ugly in word:
    print('Предложение с заменёнными словами: ', word.replace(ugly, beauty))



if (word[:3] == 'the') and (word[finish:] == 'end'):
    print('Да, предложение начинается с the и заканчивается на end')
else:
    print('Нет, предложение не начинается с the и заканчивается на end')