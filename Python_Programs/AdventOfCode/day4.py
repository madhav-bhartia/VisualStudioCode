def letter_search(letter, matrix, i, j, direction):
    length = len(matrix)

    new_i = i + direction[0]
    new_j = j + direction[1]

    if 0 <= new_i < length and 0 <= new_j < len(matrix[0]):
        if matrix[new_i][new_j] == letter:
            return True, new_i, new_j

    return False, -1, -1


def xmas_search(matrix, count = 0):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            if matrix[i][j] == 'X':
                for direction in directions:
                    M_Found, ai, aj = letter_search('M', matrix, i, j, direction)
                    if M_Found:
                        A_Found, si, sj = letter_search('A', matrix, ai, aj, direction)
                        if A_Found:
                            S_Found, _, _ = letter_search('S', matrix, si, sj, direction)
                            if S_Found:
                                count += 1

    return count


def x_mas_search(matrix, count = 0):
    


def main():
    matrix = []
    with open('AdventOfCode/day4.txt') as file:
        matrix = list(map(str.rstrip, file.readlines()))


    print(xmas_search(matrix))

main()