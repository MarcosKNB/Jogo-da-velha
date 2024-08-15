import random

matriz = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
contador_de_jogadas = 0

def jogada(jogador):
    global contador_de_jogadas
    if jogador == 'humano':
        while True:
            pos1 = int(input('Escolha a linha: ')) - 1
            pos2 = int(input('Escolha a coluna: ')) - 1
            if pos1 < 3 and pos1 > -1 and pos2 < 3 and pos2 > -1 and matriz[pos1][pos2] == ' ':
                matriz[pos1][pos2] = 'X'
                contador_de_jogadas += 1
                break
            else:
                print('Jogada invalida')
    else:
        while True:
            linha, coluna = random.randint(0, 2), random.randint(0,2)        
            if matriz[linha][coluna] == ' ':
                matriz[linha][coluna] = 'O'
                contador_de_jogadas += 1
                break
            
def mostrar_tabuleiro():
    for i in range(3):
        print(f' {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]} ')
        if i <= 1:
            print("---+---+---")
    print('============')
                         
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

def executa_verificar_vencedor():
    if contador_de_jogadas > 4:
        if verificar_vencedor() == 'vencedor X' :
            print('Voce venceu')
            return True
        elif verificar_vencedor() == 'vencedor O':
            print('Computador venceu')
            return True
    if contador_de_jogadas > 8:
        print('Ninguem venceu')
        return True                        

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
            jogada('maquina')
            break
        else:
            jogada('humano')
            break
    mostrar_tabuleiro()
    
    if executa_verificar_vencedor() == True:
        break

    while True:
        if jogador2 == 'maquina':
            jogada('maquina')
            break
        else:
            jogada('humano')
            break
    
    if executa_verificar_vencedor() == True:
        break