
class Display:


    def __init__(self, field_ai, field_player):
        self.field_player = field_player
        self.field_ai = field_ai


    def display(self):
        field_player = self.finish_view(self.field_player)
        field_ai = self.finish_view(self.field_ai)
        if field_player != -1 or field_ai != -1:
            print('Расположение кораблей противника            Расположение наших кораблей')
            print('  | 1 | 2 | 3 | 4 | 5 | 6 |                   | 1 | 2 | 3 | 4 | 5 | 6 |')
            r = ' 1 2 3 4 5 6 '
            for row_p, row_ai, i in zip(field_player, field_ai, r.split()):
                print(f"{i} | {' | '.join(str(j) for j in row_ai)} |                 {i} | {' | '.join(str(j_) for j_ in row_p)} |")

            print('\n')
        else:
            print('Список кораблей не создан')

    def finish_view(self, field):
        result = []
        result.append(field[1:7])
        result.append(field[7:13])
        result.append(field[13:19])
        result.append(field[19:25])
        result.append(field[25:31])
        result.append(field[31:])
        return result

