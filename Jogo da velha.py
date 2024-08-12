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
        vencedor_x = True
        return 'vencedor x'
    if contador_bola == 3:
        vencedor_bola = True
        return 'vencedor bola'

    if matriz[2][0] == 'X' and matriz[1][1] == 'X' and matriz[0][2] == 'X':
        vencedor_x = True
        return 'vencedor x'
    if matriz[2][0] == 'O' and matriz[1][1] == 'O' and matriz[0][2] == 'O':
        vencedor_bola = True
        return 'vencedor bola'


def verificar_vencedor_vertical_horizontal():
    for i in range(3):
        contador_x = 0
        contador_bola = 0
        for j in range(3):
            if matriz[i][j] == 'X':
                contador_x += 1
            if matriz[i][j] == 'O':
                contador_bola += 1
        if contador_x == 3:
            return 'vencedor x' 
        if contador_bola == 3:
            return 'vencedor bola'
    
      
    for i in range(3):
        contador_x = 0
        contador_bola = 0  
        for j in range(3):
            if matriz[j][i] == 'X':
                contador_x += 1
            if matriz[j][i] == 'O':
                contador_bola += 1
        if contador_x == 3:
            return 'vencedor x'
        
        if contador_bola == 3:
            return 'vencedor bola'
    
                                
jogadores = ['humano', 'maquina']
jogador1 = random.choice(jogadores)
if jogador1 == 'humano':
    jogador2 = 'maquina'
if jogador1 == 'maquina':
    jogador2 = 'humano'

contador_de_jogadas = 0

while True:
    mostrar_tabuleiro()
    while True:
        if jogador1 == 'maquina':
            jogador = jogador1
            pos1, pos2 = jogada_maquina()
            jogada(pos1, pos2, jogador)
            contador_de_jogadas += 1
            break
        else:
            jogador = jogador1
            pos1 = int(input('Escolha a linha: '))
            pos2 = int(input('Escolha a coluna: '))
            if jogada(pos1,pos2, jogador) == False:
                print('Jogada invalida')
            else:
                contador_de_jogadas += 1
                break
    mostrar_tabuleiro()
    
    if contador_de_jogadas > 4:
        vencedor = verificar_vencedor_diagonal()
        vencedor2 = verificar_vencedor_vertical_horizontal()
        if vencedor == 'vencedor x' or vencedor2 == 'vencedor x':
            print('Humano venceu')
            break
        if vencedor == 'vencedor bola' or vencedor2 == 'vencedor bola':
            print('Computador venceu')
            break
    if contador_de_jogadas > 8:
        print('Ninguem venceu')
        break    
    while True:
        if jogador2 == 'maquina':
            jogador = jogador2
            pos1, pos2 = jogada_maquina()
            jogada(pos1, pos2, jogador)
            contador_de_jogadas += 1
            break
        else:
            jogador = jogador2
            pos1 = int(input('Escolha a linha: '))
            pos2 = int(input('Escolha a coluna: '))
            if jogada(pos1,pos2, jogador) == False:
                print('Jogada invalida')
            else:
                contador_de_jogadas += 1
                break
    
    if contador_de_jogadas > 4:
        vencedor = verificar_vencedor_diagonal()
        vencedor2 = verificar_vencedor_vertical_horizontal()
        if vencedor == 'vencedor x' or vencedor2 == 'vencedor x':
            print('Humano venceu')
            break
        if vencedor == 'vencedor bola' or vencedor2 == 'vencedor bola':
            print('Computador vencecu')
            break
    if contador_de_jogadas > 8:
        print('Ninguem venceu')
        break