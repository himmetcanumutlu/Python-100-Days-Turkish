# Translated to Turkish by himmetcanumutlu

"""
Özyinelemeli geri izleme: deneme yöntemi olarak da adlandırılır; seçim ölçütüne göre ileri doğru arar,
bir adımda önceki seçimin iyi olmadığını veya hedefe ulaşamadığını fark edince bir adım geri dönüp yeniden seçer.
Klasik problem: şövalye devriyesi
"""
import os
import sys
import time

SIZE = 5
total = 0


def print_board(board):
    # os.system('clear')
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):
    if row >= 0 and row < SIZE and \
        col >= 0 and col < SIZE and \
        board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:
            global total
            total += 1
            print(f'{total}. yürüyüş biçimi: ')
            print_board(board)
        patrol(board, row - 2, col - 1, step + 1)
        patrol(board, row - 1, col - 2, step + 1)
        patrol(board, row + 1, col - 2, step + 1)
        patrol(board, row + 2, col - 1, step + 1)
        patrol(board, row + 2, col + 1, step + 1)
        patrol(board, row + 1, col + 2, step + 1)
        patrol(board, row - 1, col + 2, step + 1)
        patrol(board, row - 2, col + 1, step + 1)
        board[row][col] = 0


def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE - 1, SIZE - 1)


if __name__ == '__main__':
    main()
