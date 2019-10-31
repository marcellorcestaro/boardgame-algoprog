import random 

class Tabuleiro: 

    def __init__(self, posicoes):
        self.posicoes = posicoes
        self.lista = ['|__|'] * self.posicoes

    def mostrar(self):
        for i in range(self.posicoes):
            print(self.lista[i], end="")
        print('\n')

        # colunas = int(len(self.lista))
        # linhas = int(colunas ** (1/2))
        
        # for i in range(linhas):
        #     if i == 0:
        #         print('|', end="")
        #         print('X_|' * linhas)
        #         continue
        #     if i == linhas - 1:
        #         print('|', end="")
        #         print('__|' * linhas)
        #         continue
        #     print('|__|', end="")
        #     print('  ' * (linhas + 2), end="")
        #     print('|__|')
            

            
    def adicionarPersonagem(self, simbolo):
        if self.lista[0] == '|__|':
            self.lista[0] = '|' + str(simbolo) +'_|'

class Peca():

    def __init__(self, tabuleiro):
        self.posicao = 0
        self.tabuleiro = tabuleiro
    
    def avancar(self, casas):
        self.posicao += casas
    
    def retroceder(self, casas):
        
        self.posicao -= casas

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

    def fazerPergunta(self):

        print(self.pergunta)
        print('\ta) ' + self.a)
        print('\tb) ' + self.b)
        print('\tc) ' + self.c)
        print('\td) ' + self.d)

        resp_usuario = input("R: ")

        if resp_usuario == self.resp:
            return True
        else: 
            return False

    def todasQuestoes(self):
        return self.questoes

    def escolherQuestao(self):
        return random.choice(self.questoes)
    
tabuleiro = Tabuleiro(121)
tabuleiro.mostrar()
tabuleiro.adicionarPersonagem('X')
tabuleiro.mostrar()

# questao0 = Questao("Qual o meu nome? 1", "Marcello", "Joao", "Tiago", "Francielly", "a")
# questao1 = Questao("Qual o meu nome? 2", "Marcello", "Joao", "Tiago", "Francielly", "a")
# questao2 = Questao("Qual o meu nome? 3", "Marcello", "Joao", "Tiago", "Francielly", "a")
# questao3 = Questao("Qual o meu nome? 4", "Marcello", "Joao", "Tiago", "Francielly", "a")

# print(questao0.escolherQuestao())