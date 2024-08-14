import random

matriz = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def jogada(pos1, pos2, jogador):
    if pos1 < 4 and pos1 > 0 and pos2 < 4 and pos2 > 0 and matriz[pos1-1][pos2-1] == ' ':
        if jogador == 'humano':
                matriz[pos1-1][pos2-1] = 'X'
        if jogador == 'maquina':
            matriz[pos1-1][pos2-1] = 'O'
    else:
        return False
            
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

def verificar_vencedor():
    contador_X = 0
    contador_O = 0
    for i in range(3):
        contador_X_horizontal = 0
        contador_O_horizontal = 0
        contador_X_vertical = 0
        contador_O_vertical = 0 
        if matriz[i][i] == 'X':
            contador_X += 1
        if matriz[i][i] == 'O':
            contador_O += 1
        for j in range(3):
            if matriz[j][i] == 'X':
                contador_X_vertical += 1
            if matriz[i][j] == 'X':
                contador_X_horizontal += 1
            if matriz[i][j] == 'O':
                contador_O_horizontal += 1
            if matriz[j][i] == 'O':
                contador_O_vertical += 1
            if contador_X == 3 or contador_X_vertical == 3 or contador_X_horizontal == 3:
                return 'vencedor X'
            if contador_O == 3 or contador_O_horizontal == 3 or contador_O_vertical == 3:
                return 'vencedor O'    
    for sinal in 'XO':
        diagonal_contraria = matriz[2][0] == sinal and matriz[1][1] == sinal and matriz[0][2] == sinal
        if diagonal_contraria:
            return (f'vencedor {sinal}')
                        
jogadores = ['humano', 'maquina']
jogador1 = random.choice(jogadores)
if jogador1 == 'humano':
    jogador2 = 'maquina'
if jogador1 == 'maquina':
    jogador2 = 'humano'

contador_de_jogadas = 0

while True:
    mostrar_tabuleiro()
    print('============')
    while True:
        if jogador1 == 'maquina':
            pos1, pos2 = jogada_maquina()
            jogada(pos1, pos2, jogador1)
            contador_de_jogadas += 1
            break
        else:
            pos1 = int(input('Escolha a linha: '))
            pos2 = int(input('Escolha a coluna: '))
            if jogada(pos1,pos2, jogador1) == False:
                print('Jogada invalida')
            else:
                contador_de_jogadas += 1
                break
    mostrar_tabuleiro()
    print('============')
    
    if contador_de_jogadas > 4:
        vencedor = verificar_vencedor()
        if vencedor == 'vencedor X':
            print('Voce venceu')
            break
        if vencedor == 'vencedor O':
            print('Computador venceu')
            break
    if contador_de_jogadas > 8:
        print('Ninguem venceu')
        break    

    while True:
        if jogador2 == 'maquina':
            pos1, pos2 = jogada_maquina()
            jogada(pos1, pos2, jogador2)
            contador_de_jogadas += 1
            break
        else:
            pos1 = int(input('Escolha a linha: '))
            pos2 = int(input('Escolha a coluna: '))
            if jogada(pos1,pos2, jogador2) == False:
                print('Jogada invalida')
            else:
                contador_de_jogadas += 1
                break
    
    if contador_de_jogadas > 4:
        vencedor = verificar_vencedor()
        if vencedor == 'vencedor X' :
            print('Voce venceu')
            break
        if vencedor == 'vencedor O':
            print('Computador vencecu')
            break
    if contador_de_jogadas > 8:
        print('Ninguem venceu')
        break