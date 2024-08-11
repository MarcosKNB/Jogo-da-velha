import random

matriz = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def jogada(pos1, pos2, jogador):
    if pos1 > 3 or pos1 < 1 or pos2 > 3 or pos2 < 1:
        return False
    else:
        if matriz[pos1-1][pos2-1] == 'X' or matriz[pos1-1][pos2-1] == 'O':
            return False
        else:
            if jogador == 'humano':
                matriz[pos1-1][pos2-1] = 'X'
            if jogador == 'maquina':
                matriz[pos1-1][pos2-1] = 'O'

def mostrar_tabuleiro():
    for i in range(3):
        print(f' {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]} ')
        if i <= 1:
            print("---+---+---")
        
jogadores = ['humano', 'maquina']
jogador1 = random.choice(jogadores)
if jogador1 == 'humano':
    jogador2 = 'maquina'
if jogador1 == 'maquina':
    jogador2 = 'humano'

while True:
    mostrar_tabuleiro()
    while True:
        jogador = jogador1
        pos1 = int(input('Escolha a linha: '))
        pos2 = int(input('Escolha a coluna: '))
        if jogada(pos1,pos2, jogador) == False:
            print('Jogada invalida')
        else:
            break
    mostrar_tabuleiro()
    while True:
        jogador = jogador2
        pos1 = int(input('Escolha a linha: '))
        pos2 = int(input('Escolha a coluna: '))
        if jogada(pos1,pos2, jogador) == False:
            print('Jogada invalida')
        else:
            break
    