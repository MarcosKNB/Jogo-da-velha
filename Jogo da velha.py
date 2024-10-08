import random
terminar = False
matriz = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
contador_de_jogadas = 0

def mostrar_tabuleiro():
    for i in range(3):
        print(f' {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]} ')
        if i <= 1:
            print("---+---+---")
    print('============')
    
def jogada(jogador):
    global contador_de_jogadas
    if jogador == 'humano':
        while True:
            pos1 = int(input('Escolha a linha: ')) - 1
            pos2 = int(input('Escolha a coluna: ')) - 1
            if pos1 < 3 and pos1 > -1 and pos2 < 3 and pos2 > -1 and matriz[pos1][pos2] == ' ':
                matriz[pos1][pos2] = 'X'
                contador_de_jogadas += 1
                mostrar_tabuleiro()
                break
            else:
                print('Jogada invalida, por favor digite novamente.')
    else:
        while True:
            linha, coluna = random.randint(0, 2), random.randint(0,2)        
            if matriz[linha][coluna] == ' ':
                print('Minha vez de jogar.')
                print(f'Vou jogar na linha {linha+1} e coluna {coluna+1}.')
                matriz[linha][coluna] = 'O'
                contador_de_jogadas += 1
                mostrar_tabuleiro()
                break
                                 
def verifica_vencedor():
    for sinal in 'XO':
        diagonal_contraria = matriz[2][0] == sinal and matriz[1][1] == sinal and matriz[0][2] == sinal
        if diagonal_contraria:
            diagonal_contraria = True
        contador_diagonal = 0
        for i in range(3):
            contador_horizontal = 0
            contador_vertical = 0
            if matriz[i][i] == sinal:
                contador_diagonal += 1
            for j in range(3):
                if matriz[i][j] == sinal:
                    contador_horizontal += 1
                if matriz[j][i] == sinal:
                    contador_vertical += 1
            if contador_diagonal == 3 or contador_horizontal == 3 or contador_vertical == 3 or diagonal_contraria == True:
                if contador_de_jogadas > 4:
                    if sinal == 'X' :
                        print('Voce venceu. D:')
                        return True
                    elif sinal == 'O':
                        print('As máquinas venceram. :D') 
                        return True
        if contador_de_jogadas > 8:
            print('Ninguem venceu')
            return True                        

jogadores = ['humano', 'maquina']
jogador1 = random.choice(jogadores)
if jogador1 == 'humano':
    ordem = ['humano', 'maquina']
if jogador1 == 'maquina':
    ordem = ['maquina','humano']


print('Que o jogo comece!!!')    
mostrar_tabuleiro()
while True:    
    for i in ordem:
        jogada(i)
        if verifica_vencedor() == True:
            terminar = True
            break
    if terminar == True:
        break