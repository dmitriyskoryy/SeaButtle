import random

from board import Board
from ship import Ship
from display import Display



# функции get_around_points_ship и get_points_ship нужны для функции random_list_ship,
# для того чтобы корабли не налезали друг на друга и между ними был хотя бы один квадрат

#определяем точки корабля, а также точки вокруг корабля
def get_around_points_ship(list_):
    points_around_ship = set()
    row = list_[0]
    col = list_[1]
    p = list_[2]

    if list_[3] == 'v':
        for i in range(row - 1, row + p + 1):
            for j in range(col - 1, col + 2):
                points_around_ship.add(str(i) + str(j))
    else:
        for j_ in range(col - 1, col + p + 1):
            for i_ in range(row - 1, row + 2):
                points_around_ship.add(str(i_) + str(j_))

    return points_around_ship


#определяем точки корабля
def get_points_ship(list_):
    points_ship = set()
    row = list_[0]
    col = list_[1]
    p = list_[2]

    if list_[3] == 'v':
        for i in range(0, p):
            points_ship.add(str(row + i) + str(col))
    else:
        for j in range(0, p):
            points_ship.add(str(row) + str(col + j))

    return points_ship


# функция для создания рандомного списка корлей: одного трехпалубного, двух двупалубных, и четыре однопалубных
def random_list_ship():
    points_ships = set()

    orient_value = {0: 'v', 1: 'h'}

    for i in range(3000):
        test = Ship(random.randrange(1, 7, 1), random.randrange(1, 7, 1), 3, orient_value[random.randrange(0, 2, 1)])
        if test.ship is not False:
            points_ships = get_points_ship(test.ship)  # накапливаем точки только корабля, и точки вокруг не берем
            ship_list = [test.ship]
            break

    for i in range(2):
        for j in range(3000):
            test = Ship(random.randrange(1, 7, 1), random.randrange(1, 7, 1), 2,
                        orient_value[random.randrange(0, 2, 1)])
            if test.ship is not False:
                points_around_ship = get_around_points_ship(test.ship)  # получаем точки корабля и точки вокруг него
                if not points_around_ship.isdisjoint(points_ships):
                    continue
                else:
                    points_ships.update(get_points_ship(test.ship))  # накапливаем точки только корабля
                    ship_list.append(test.ship)
                    break

    for i in range(4):
        for j in range(3000):
            test = Ship(random.randrange(1, 7, 1), random.randrange(1, 7, 1), 1, 'h')
            if test.ship is not False:
                points_around_ship = get_around_points_ship(test.ship)  # получаем точки корабля и вокруг него
                if not points_around_ship.isdisjoint(points_ships):
                    continue
                else:
                    points_ships.update(get_points_ship(test.ship))  # накапливаем точки только корабля
                    ship_list.append(test.ship)
                    break

    if False in ship_list or len(ship_list) != 7:
        return -1
    else:
        return ship_list






def player_turn():
    while True:
        player_ = input('Нанесите сокрушительный удар по противнику! Передайте координаты огня: ')
        player_ = player_.replace(" ", "")

        if player_ == 'q':
            exit()

        if not player_.isdigit():
            print('Передай числовые координаты! Например: 43')
            print('Необходимо скорцентрироваться, враг ошибок допускать не будет!')
            continue

        if int(player_) // 10 < 1 or int(player_) // 10 > 6 and \
                int(player_) % 10 < 1 or int(player_) % 10 > 6 or \
                len(player_) != 2:
            print('Переданные координаты находятся за пределами зоны боевых действий!')
            print('Если так пойдет и дальше, враг разнесет нас в пух и прах!')
            continue
        else:
            row = int(player_) // 10 - 1
            col = int(player_) % 10 - 1

        cell = col + (row * 6) + 1


        if board_ai.get_board[cell] == 'O':
            board_ai.set_board(cell, 'T')
            board_ai_zero.set_board(cell, 'T')
            return 1
        elif board_ai.get_board[cell] == '\u25A0':
            board_ai.set_board(cell, 'X')
            board_ai_zero.set_board(cell, 'X')
            return 1
        else:
            print(f'Квадрат "{row + 1}{col + 1}" уже был атакован!')
            print('Необходимо скорцентрироваться, враг не будет допускать ошибок!')
            return 1



def ai_turn():
    while True:
        cell = random.randrange(0, 6, 1) + (random.randrange(0, 6, 1) * 6) + 1

        if board_player.get_board[cell] == 'O':
            board_player.set_board(cell, 'T')
            return 1
        elif board_player.get_board[cell] == '\u25A0':
            board_player.set_board(cell, 'X')
            return 1
        elif board_player.get_board[cell] == 'T':
            continue
        elif board_player.get_board[cell] == 'X':
            continue
        else:
            return -1




def game():
    while True:

        # проверка на выигрыш
        win = [i for i in board_ai.get_board if i == '\u25A0']
        if not win:
            print('Дым рассеялся... Было видно, как последний вражеский корабль пошел ко дну. Это победа!')
            exit()

        # проверка на проигрыш
        win = [i for i in board_player.get_board if i == '\u25A0']
        if not win:
            print('Координаты никто не принимает... Похоже, нашего флота больше нет... Это поражение!')
            exit()


        # ход игрока
        player_turn()
        # ход компьютера
        ai_turn()
        # вывод на экран
        display.display()






if __name__ == "__main__":
    print('Срочное донесение! Утром, враг вероломно напал на наши границы!')
    print('Настало время показать, кто тут главный.')
    print('Наноси удары по противнику, передавая координаты ударной группе (например: 46)')
    print('Вперед! Стране нужен настоящий герой, морской волк и дерзкий пират!\n')


    # создаем доску противника
    for _ in range(10):
        ships_ai = random_list_ship()
        if ships_ai != -1:
            board_ai = Board(ships_ai)
            board_ai.add_ship
            break


    # создаем доску противника с нулями, для отображения во время игры
    board_ai_zero = Board()
    board_ai_zero.new_board


    # создаем доску игрока
    for _ in range(10):
        ships_player = random_list_ship()
        if ships_player != -1:
            board_player = Board(ships_player)
            board_player.add_ship
            break


    # обработка исключения если не будет создан объект класса Board
    try:
        # создаем объект display, который будет выводить доски с результатами на экран
        display = Display(board_ai_zero.get_board, board_player.get_board)
        # выводим доски на экран
        display.display()
        # запускаем игру
        game()
    except NameError as e:
        s = str(e)
        if 'board_ai' in s:
            print(e)
            print('Так держать! Вражеская сторона решила урегулировать конфликт мирным путем, и просто не явилась на поле боя.')
        else:
            print(e)
            print('Еще донесение и еще срочнее! Наша сторона решила урегулировать конфликт мирным путем, и просто не явилась на поле боя.')







