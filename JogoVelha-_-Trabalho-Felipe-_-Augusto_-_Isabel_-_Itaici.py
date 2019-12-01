# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:24:43 2019

@author: Augusto A. Lima; Isabel Cristina; Itaici Oliveira; 
"""

import random, os, time

limpa = "os.system('cls' if os.name == 'nt' else '_clear_')"
jogando = 'X'
X = 0
O = 0
E = 0
V = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        
        ]

def cabecalho():
    print ("---------Jogo da velha----------")
    
    
def placar(): #Mostra quem é a vez de jogar
    print ("============================")
    print ("  Jogando "+str(jogando)+"     ")
    print ("                            ")

def velha(): #Andamento, números livres do jogo
    print ("==================================================================")
    print ("                                                                  ")
    print ("--------------------+--------------------+------------------------")
    print ("               "+str(V[0][0])+" |  "+str(V[0][1])+"  |  "+str(V[0][2])+"      ")
    print ("--------------------+--------------------+------------------------")
    print ("               "+str(V[1][0])+" |  "+str(V[1][1])+"  |  "+str(V[1][2])+"      ")
    print ("--------------------+--------------------+------------------------")
    print ("               "+str(V[2][0])+" |  "+str(V[2][1])+"  |  "+str(V[2][2])+"      ")
    print ("--------------------+--------------------+------------------------")
    print ("                                                                  ")
    print ("==================================================================")
    
def jogador(): #Escolha do Jogador
   return'X' if random.randint(1,2) == 1 else 'O'

def joga(msg): #Quem irá jogar
    while True:
        try: 
            jogada = input(msg)
            return int(jogada[0])
        except:
            print("Entre com um valor aceito.")
            

def mensagem(msg, erro="Escolha S para sim e N para não"): #perguntas para o usuario sobre continuar a partida/Jogi
    
    while True:
        try:
            resp = input(msg)
            if(resp[0] == 'S' or resp[0] == 's'):
                return True
            elif(resp[0] == 'N' or resp[0] == 'n'):
                return False
            else:
                print(erro)
        except:
            print("Entre com um valor aceito.")
 
#Conferir se ouve algum empate na partida
            
def empate():
    
    for i in range(3):
        for j in range(3):
            if str(V[i][j]).isdigit(): #verifica se em cada possição é numero na velha, caso seja digido,
            #é falso e ja fizeram todas as jogadas
                return False
    
    return True #define se o jogo foi empatado




Inicio = True

while Inicio:
    jogando = jogador()
    Go = True #Variavel de controle para inicio do jogo
    
    while Go:
        
        #Primeiro chama o cabeçalho do jogo
        eval(limpa); cabecalho(); placar(); velha() 
        
        jogada = joga("Coloque a posição desejada:  ")
        
        #validação da jogada
        
        JoAceita = False
        
        for i in range(3):
            for j in range(3):
                if jogada == V[i][j]:
                    V[i][j] = jogando
                    JoAceita = True
        if JoAceita:
            
            #Verificar se o jogo foi ganhado ou empatado, porem, so consegui implementar o empate
            
            if empate():
                print("O Jogo foi empatado!!!")
                time.sleep(5)
                E += 1
                
                Go = False
                
                Inicio = True if mensagem("Deseja iniciar um novo jogo [S/N]? ")else False
                    
            else:
                jogando = 'X' if jogando == 'O' else 'O'
        else:
            print ("OH OH!! Esta jogada foi invalida, tente outra vez!")
            time.sleep(5)
        
        if not mensagem("Deseja continuar?: "):
        
        
            Go = False
            Inicio = False