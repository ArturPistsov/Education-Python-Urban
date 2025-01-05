# Функция определения победителя (дописать строки условий)
def check_winner():
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'

    return '*'

# Функция вывода игрового поля
def draw_area():
    for i in area:
        print(*i)

area = [['*','*','*'],['*','*','*'],['*','*','*']]

for turn in range (1,10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_now = 'O'
        print('Ходит "O"')
    else:
        turn_now = 'X'
        print('Ходит "X"')
    row = int(input('Введите номер строки ')) - 1
    column = int(input('Введите номер столбца ')) - 1
    if area[row][column] == '*':
        area[row][column] = turn_now
    else:
        print('Ячейка уже занята, вы пропускаете ход')
        continue
    draw_area()
    print()
    if check_winner() == 'X':
        print('Победа "X"')
        break
    if check_winner() == 'O':
        print('Победа "O"')
        break
    if check_winner() == '*' and turn == 9:
        print('Ничья')