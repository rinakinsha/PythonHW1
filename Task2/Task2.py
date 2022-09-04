"Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат."


def ListCompletion(a):  # функция для заполнения списка
    xyz = []
    for i in range(a):
        xyz.append(input(f'Введите {i+1} число: '))
    return xyz


def ConditionCheck(list):  # функия для проверки истинности утверждения
    first = not (list[0] or list[1] or list[2])
    second = not list[0] and not list[1] and not list[2]
    result = first == second
    return result


newlist = ListCompletion(3)

if ConditionCheck(newlist) == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')