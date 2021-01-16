def chotko(a):
    ''' Используя list comprehensions, напишите функцию,
    которая выводит все четные числа до числа, которое передано функции
    '''
    return [_ for _ in range(a) if _ % 2 == 0]


def vyvod(test):
    '''Вывод уникальных элементов списка, сохраняя порядок
    '''
    for i in test:
        if test.count(i) == 1:
            print(i)
