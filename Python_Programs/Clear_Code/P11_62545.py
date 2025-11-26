chess_board_fields = [[f'{char}{num}' for num in range(1, 8+1)] for char in 'ABCDEFGH'[::-1]]
for row in chess_board_fields:
    for elem in row:
        print(elem, end=' ')
    print()