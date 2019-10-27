from random import randint

PG_WIDTH = 10
PG_HEIGHT = 10
ITERATION = 1


def init_playground(pg):  # начальное состояние поля
    for i in range(PG_WIDTH):
        for j in range(PG_HEIGHT):
            pg[i][j] = randint(0, 1)


def print_playground(pg):  # вывод поля
    print('Iteration', ITERATION)
    for row in pg:
        print(*row)
    print('\n')


def get_live_points(pg):  # количество живых клеток на поле
    points = 0
    for row in pg:
        for i in row:
            if i == 1:
                points += 1
    return points


def read_point_neighbors(nb, x, y):  # соседи клетки с координатами (x, y)
    k = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            nb[k][0] = i
            nb[k][1] = j
            k += 1


def get_live_neighbors(pg, x, y):  # количество живых соседей клетки с координатами (x, y)
    count = 0
    nb = [[0 for col in range(2)] for row in range(8)]
    read_point_neighbors(nb, x, y)
    for i in range(8):
        tmp_x = nb[i][0]
        tmp_y = nb[i][1]
        if tmp_x < 0 or tmp_y < 0:
            continue
        if tmp_x >= PG_WIDTH or tmp_y >= PG_HEIGHT:
            continue
        if pg[tmp_x][tmp_y] == 1:
            count += 1
    return count


def copy_playground(pg, pr_pg):  # копируем текущее состояние поля в предыдущее
    for i in range(PG_WIDTH):
        for j in range(PG_HEIGHT):
            pr_pg[i][j] = pg[i][j]


def next_generation(pg, pr_pg):  # следующая итерация => меняем состояние поля
    for i in range(PG_WIDTH):
        for j in range(PG_HEIGHT):
            tmp = pr_pg[i][j]
            live_nb = get_live_neighbors(pr_pg, i, j)
            if tmp == 0:
                if live_nb == 3:
                    pg[i][j] = 1
            else:
                if live_nb < 2 or live_nb > 3:
                    pg[i][j] = 0


def compare_pgs(pg1, pg2):  # сравниваем предыдущее и текущее состояния поля
    for i in range(PG_WIDTH):
        for j in range(PG_HEIGHT):
            if pg1[i][j] != pg2[i][j]:
                return -1
    return 0


playground = [[0 for col in range(PG_WIDTH)] for row in range(PG_HEIGHT)]  # поле
prev_pg = [[0 for col in range(PG_WIDTH)] for row in range(PG_HEIGHT)]  # предыдущее поле
init_playground(playground)  # задаем начальное состояние
live_points = -1  # количествое живых клеток
is_final = False  # достигнуто ли финальное состояние

while live_points != 0 and not is_final:  # цикл игры
    print_playground(playground)  # выводим поле игры
    ITERATION += 1  # переходим к следующей итерации
    copy_playground(playground, prev_pg)  # делаем копию поля
    next_generation(playground, prev_pg)  # обновляем поле
    is_final = compare_pgs(playground, prev_pg) == 0  # проверка на финальное состояние
    live_points = get_live_points(playground)  # проверка на кол-во живых клеток
    if is_final:
        print("Final configuration detected")
    if live_points == 0:
        print_playground(playground)
        print("All points died")
