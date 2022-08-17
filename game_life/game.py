import numpy as np
import copy
import matplotlib.pyplot as plt
import random


def make_random_ocean(size, num_fish, num_shrimps, num_rocks):
    if num_fish + num_shrimps + num_rocks > size**2:
        raise ValueError('элементов больше, чем поле')
    global n
    n = size
    ocean = np.zeros((size, size), dtype=complex)
    for _ in range(num_fish):
        set_to_random_pos(ocean, 1 + 0j)
    for _ in range(num_shrimps):
        set_to_random_pos(ocean, 0 + 1j)
    for _ in range(num_rocks):
        set_to_random_pos(ocean, 10 + 0j)
    return ocean


def set_to_random_pos(mas, elem):
    i = random.randint(0, len(mas) - 1)
    k = random.randint(0, len(mas) - 1)
    while mas[i][k] != 0:
        i = random.randint(0, len(mas) - 1)
        k = random.randint(0, len(mas) - 1)
    mas[i][k] = elem


def find(i, k, pole):
    if pole[i][k] != 10 + 0j: # если это не скала
        now = find_sum_around(i, k, pole)
        if pole[i][k] == 1 + 0j: # если это рыба
            if now.real % 10 >= 4 or now.real % 10 < 2:
                return 0 + 0j
            else:
                return 1 + 0j
        elif pole[i][k] == 0 + 1j: # если это креветка
            if now.imag >= 4 or now.imag < 2:
                return 0 + 0j
            else:
                return 0 + 1j
        elif pole[i][k] == 0 + 0j: # проверка, пустая ли ячейка
            if now.real % 10 == 3: # рождение новой рыбы
                return 1 + 0j
            elif now.imag == 3: # рождение новой креветки
                return 0 + 1j
            else:
                return 0 + 0j
    else:
        return 10 + 0j


def find_sum_around(i, k, pole):
    if i == 0 and k == 0: # левый верхний
        return pole[0][1] + pole[1][0] + pole[1][1]
    elif i == n - 1 and k == 0: # левый нижний
        return pole[n - 2][0] + pole[n - 1][1] + pole[n - 2][1]
    elif i == 0 and k == n - 1: # правый верхний
        return pole[0][n - 2] + pole[1][n - 1] + pole[1][n - 2]
    elif i == n - 1 and k == n - 1: # правый нижний
        return pole[n - 1][n - 2] + pole[n - 2][n - 1]+ pole[n - 2][n - 2]
    elif i == n - 1: # нижняя граница
        return pole[n - 1][k + 1] + pole[n - 1][k - 1] + pole[n - 2][k] + pole[n - 2][k - 1] + pole[n - 2][k + 1]
    elif k == n - 1: # правая граница
        return pole[i - 1][n - 1] + pole[i + 1][n - 1] + pole[i][n - 2] + pole[i - 1][n - 2] + pole[i + 1][n - 2]
    elif i == 0: # верхняя граница
        return pole[0][k + 1] + pole[0][k - 1] + pole[1][k] + pole[1][k - 1] + pole[1][k + 1]
    elif k == 0: # левая граница
        return pole[i - 1][0] + pole[i + 1][0] + pole[i][1] + pole[i - 1][1] + pole[i + 1][1]
    else: # штука в центре
        return pole[i - 1][k - 1] + pole[i + 1][k + 1] + pole[i + 1][k] + pole[i - 1][k] +\
               + pole[i][k + 1] + pole[i][k - 1] + pole[i - 1][k + 1] + pole[i + 1][k - 1]


def draw_graphics(pole, time=1.):
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            if pole[i][j] == 1 + 0j:
                col = 'grey'
            elif pole[i][j] == 0 + 1j:
                col = 'pink'
            elif pole[i][j] == 10 + 0j:
                col = 'black'
            elif pole[i][j] == 0 + 0j:
                col = 'blue'
            plt.plot(j, n - i, '-s', color=col)
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    plt.draw()
    plt.pause(time)


# рыба - 1
# креветка - 1j
# скала - 10
# ничего - 0


pole = make_random_ocean(5, 10, 9, 5)
plt.ion()
draw_graphics(pole, time=0.5)
while True:
    pole_new = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for k in range(n):
            pole_new[i][k] = find(i, k, pole)
    if np.array_equiv(pole, pole_new):
        plt.text(1.3, 3, "Ocean is fixed", fontsize=15)
        break
    pole = copy.deepcopy(pole_new)
    draw_graphics(pole, time=0.5)
plt.ioff()
plt.show()
