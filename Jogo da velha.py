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
            
            
def jogada_maquina():
    while True:
        linha = random.randint(1, 3)           
        coluna = random.randint(1, 3)
        if matriz[linha-1][coluna-1] == ' ':
            return linha, coluna
            break


def verificar_vencedor_diagonal():
    contador_x = 0
    contador_bola = 0
    for i in range(3):
        if matriz[i][i] == 'X':
            contador_x += 1
        if matriz[i][i] == 'O':
            contador_bola += 1
    if contador_x == 3:
        return 'humano venceu'
    if contador_bola == 3:
        return 'maquina venceu'
    contador_x = 0
    contador_bola = 0
    if matriz[2][0] == 'X' and matriz[1][1] == 'X' and matriz[0][2] == 'X':
        return 'humano venceu'
    if matriz[2][0] == 'O' and matriz[1][1] == 'O' and matriz[0][2] == 'O':
        return 'maquina venceu'
                
                                

jogadores = ['humano', 'maquina']
jogador1 = random.choice(jogadores)
if jogador1 == 'humano':
    jogador2 = 'maquina'
if jogador1 == 'maquina':
    jogador2 = 'humano'


while True:
    mostrar_tabuleiro()
    while True:
        if jogador1 == 'maquina':
            jogador = jogador1
            pos1, pos2 = jogada_maquina()
            jogada(pos1, pos2, jogador)
            break
        else:
            jogador = jogador1
            pos1 = int(input('Escolha a linha: '))
            pos2 = int(input('Escolha a coluna: '))
            if jogada(pos1,pos2, jogador) == False:
                print('Jogada invalida')
            else:
                break
    mostrar_tabuleiro()
    while True:
        if jogador2 == 'maquina':
            jogador = jogador2
            pos1, pos2 = jogada_maquina()
            jogada(pos1, pos2, jogador)
            break
        else:
            jogador = jogador2
            pos1 = int(input('Escolha a linha: '))
            pos2 = int(input('Escolha a coluna: '))
            if jogada(pos1,pos2, jogador) == False:
                print('Jogada invalida')
            else:
                break
    print(verificar_vencedor_diagonal())