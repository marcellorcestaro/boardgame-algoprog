import random
import re

class Jogador: 
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.posicao = 0

class Questao: 

    questoes = []

    def __init__(self, pergunta, a, b, c, d, resp): 

        self.pergunta = pergunta
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.resp = resp

        self.questoes.append(self)

    def mostrarPergunta(self):
        print(self.pergunta)
        print('\ta) ' + self.a)
        print('\tb) ' + self.b)
        print('\tc) ' + self.c)
        print('\td) ' + self.d)
        print('\tR: ' + self.resp)

    def fazerPergunta(self):

        print(self.pergunta)
        print('\ta) ' + self.a)
        print('\tb) ' + self.b)
        print('\tc) ' + self.c)
        print('\td) ' + self.d)

        resp_usuario = input("R: ")

        if resp_usuario == self.resp:
            print('Correto!\n')
            return True
        else: 
            return False

    def todasQuestoes(self):
        return self.questoes


def escolherQuestao(vetor):
    return random.choice(vetor)

def mostrarTabuleiro(tabuleiro, playerOne, playerTwo):
    for i in range(len(tabuleiro)):
        if playerOne['posicao'] == i and playerTwo['posicao'] == i:
            print('['+playerOne['simbolo']+playerTwo['simbolo']+']', end="")
        elif playerOne['posicao'] == i:
            print('['+playerOne['simbolo']+']', end="")
        elif playerTwo['posicao'] == i:
            print('['+playerTwo['simbolo']+']', end="")
        else:
            print('[ ]', end="")

with open("perguntas.txt") as f:
    questoes = []
    indice = 0
    questoes.insert(indice, Questao('teste', 'teste', 'teste', 'teste', 'teste', 'teste'))
    for line in f:
        if line != '\n':
            if line[0] == 'Q':
                questoes[indice].pergunta = line[2:]
            elif line[0] == 'a':
                questoes[indice].a = line[2:]
            elif line[0] == 'b':
                questoes[indice].b = line[2:]
            elif line[0] == 'c': 
                questoes[indice].c = line[2:]
            elif line[0] == 'd':
                questoes[indice].d = line[2:]
            elif line[0] == 'R': 
                questoes[indice].resp = line[3]
        else: 
            indice += 1
            questoes.insert(indice, Questao('teste', 'teste', 'teste', 'teste', 'teste', 'teste'))

print("Quantidade de questões carregadas:", len(questoes))

# escolherQuestao(questoes).fazerPergunta()
casas = ['N', 'A', 'R']

tabuleiro = []
tamanho_tabuleiro = 22
tabuleiro.insert(tamanho_tabuleiro, 'F')

for i in range(tamanho_tabuleiro-1):
    tabuleiro.insert(i, random.choice(casas))

print(tabuleiro)

playerOne = {
    'simbolo': 'X',
    'posicao': 0
    }

playerTwo = {
    'simbolo': 'Y',
    'posicao': 0
    }

mostrarTabuleiro(tabuleiro, playerOne, playerTwo)

vez = 1

win = 0

def checarWin(player):
    if player['posicao'] >= tamanho_tabuleiro:
        print('O jogador venceu!!')
        win = 1
        return True
    return False

def turno(player, indice):
        print('Agora é a vez do jogador '+str(indice)+'!')
        print('Sua pergunta é: ')
        if(escolherQuestao(questoes).fazerPergunta()):
            print('Rolando o dado...')
            res = random.randint(1, 6)
            print("Dado:", res)
            player['posicao'] += res
            if(checarWin(player) == False):
                print(tabuleiro[player['posicao']])
            return 

while win == 0:
    print('\n')
    if vez == 1:
        turno(playerOne, vez)
        mostrarTabuleiro(tabuleiro, playerOne, playerTwo)
        vez = 2
    elif vez == 2:
        turno(playerTwo, vez)
        mostrarTabuleiro(tabuleiro, playerOne, playerTwo)
        vez = 1
