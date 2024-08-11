from random import randint

matriz = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def mostrartab():
    print(f" {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} ")
    print("---+---+---")
    print(f" {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} ")
    print("---+---+---")
    print(f" {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} ")


def jogada(pos1, pos2, jogador):
    if matriz[pos1][pos2] == 'X' or matriz[pos1][pos2] == 'O':
        return '0'
    else:
        if jogador == 'X':
            matriz[pos1][pos2] = 'X'
        if jogador == 'O':
            matriz[pos1][pos2] = 'O'



while True:
    mostrartab()
    while True:
        jogador = 'X'
        pos1 = int(input('Escolha a linha: '))
        pos2 = int(input('Escolha a coluna: '))
        if jogada(pos1,pos2, jogador) == '0':
            print('Jogada invalida')
        else:
            break
    