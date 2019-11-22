import random
import sys
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

        if resp_usuario.lower() == self.resp:
            print('Correto!\n')
            return True
        else: 
            return False

    def todasQuestoes(self):
        return self.questoes

class Jogador:
    def __init__(self, simbolo, indice):
        self.simbolo = simbolo
        self.posicao = 0
        self.indice = indice

class Tabuleiro:
    def __init__(self, tamanho, jog1, jog2):
        self.tamanho = tamanho
        self.tabuleiro = []

        self.jogadorUm = jog1
        self.jogadorDois = jog2

        self.tabuleiro.insert(tamanho, 'F')
        
        casas = ['R', 'A', 'N']

        for i in range(tamanho-1):
            self.tabuleiro.insert(i, random.choice(casas))

    def mostrar(self):
        for i in range(len(self.tabuleiro)):
            if self.jogadorUm.posicao == i and self.jogadorDois.posicao == i:
                print(' |{'+self.jogadorUm.simbolo+' '+self.jogadorDois.simbolo+'}| ', end="")
            elif self.jogadorUm.posicao == i:
                print(' |{'+self.jogadorUm.simbolo+'}| ', end="")
            elif self.jogadorDois.posicao == i:
                print(' |{'+self.jogadorDois.simbolo+'}| ', end="")
            else:
                print('  |{ }|  ', end="")


        print('\n')

questoes = []

with open("perguntas.txt", mode="r", encoding="utf8") as f:
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

questoes_bckup = questoes

print('*~'*30)
print('TRIVIA - JOGO DE TABULEIRO (versão Python!)')
print('*~'*30)

print('\nRegras do jogo:')
print('\t- Este jogo é para dois jogadores')
print('\t- A cada turno, o jogador vai precisar responder uma pergunta para que depois possa se mover')
print('\t- Após avançar, você pode cair em três diferentes casas, com diferentes efeitos: Neutra, Avanço e Retrocesso')
print('\t\t- Neutra: não há movimento')
print('\t\t- Avanço: o jogador responde a pergunta. Se acertar, avançará mais algumas casas. Se não, se mantém parado')
print('\t\t- Retrocesso: o jogador responde a pergunta. Se acertar, se mantém parado. Se não, retrocede algumas casas.')
print('\n')
print('Está pronto(a) para jogar?')
resp = input('1) Sim\n2) Não\nR: ')
while resp != '1':
    print('Está pronto(a) para jogar?')
    resp = input('1) Sim\n2) Não\nR: ')

simUm = input('Qual o símbolo do jogador 1? (usar somente letras ou números unitários, sem frases) \nR: ')
simDois = input('Qual o símbolo do jogador 2? (usar somente letras ou números unitários, sem frases) \nR: ')

jogadorUm = Jogador(simUm, 1)
jogadorDois = Jogador(simDois, 2)

tabuleiro = Tabuleiro(22, jogadorUm, jogadorDois)

def casaFinal(player, avanco):
    tabuleiro.mostrar()

    print("Parabéns, jogador {}! Você está na reta final. Responda a próxima questão para ver se você conseguiu vencer desta vez!".format(player.indice))
    if escolherQuestao(questoes).fazerPergunta():
        print('*~'*30)
        print("Você venceu, jogador {}!! Parabéns!!!".format(player.indice))
        print('*~'*30)
        print("\nEspero que tenham gostado do jogo! :)")
        print("Créditos:\n\tFrancielly Ortiz\n\tJoão Victor Morais\n\tMarcello Cestaro")
        fim()
    else: 
        print("Vish, você errou! Volte para o lugar anterior! :(")
        player.posicao -= avanco
        if player.indice == 1: 
            turno(2)
        else:
            turno(1)

def fim():
    sys.exit()

def escolherQuestao(vetor):

    tam_vetor = len(vetor)
    indice = random.randint(0, tam_vetor - 1)

    if tam_vetor <= 0: 
        questoes = questoes_bckup

    elemento = vetor[indice]
    del vetor[indice]

    return elemento

def somenteMover(player, casas):
    if player.posicao + casas >= tabuleiro.tamanho - 1:
        player.posicao = tabuleiro.tamanho - 1
        casaFinal(player, casas)
    elif player.posicao + casas < 0:
        player.posicao = 0
    else: 
        player.posicao += casas


def casaAvanco(player):
    print('\n')
    print('Tabuleiro: ')
    tabuleiro.mostrar()
    print('Você caiu em uma casa de avanço! Responda a questão a seguir para avançar ainda mais!')
    if(escolherQuestao(questoes).fazerPergunta()):
        res = random.randint(1, 6)
        print("Você acertou!! Avance {} casas!".format(res))
        somenteMover(player, res)
        if player.indice == 1: 
            turno(2)
        else:
            turno(1)
    else: 
        print("Você errou :(")
        if player.indice == 1: 
            turno(2)
        else:
            turno(1)

def casaRetro(player):
    print('\n')
    print('Tabuleiro: ')
    tabuleiro.mostrar()
    print('Droga! Você caiu em uma casa de retrocesso! Se não quer sair perdendo, responda a pergunta a seguir!')
    if(escolherQuestao(questoes).fazerPergunta()):
        print('Ufa, você se safou! Pode continuar na mesma casa!')
        if player.indice == 1: 
            turno(2)
        else:
            turno(1)
    else: 
        res = random.randint(1, 6)
        print('Você errou! Volte {} casas!'.format(res))
        volta = res * -1
        somenteMover(player, volta)
        if player.indice == 1: 
            turno(2)
        else:
            turno(1)

def casaNeutra(player):
    print('Casa neutra! Vez passada.')

    if player.indice == 1: 
        turno(2)
    else:
        turno(1)

def mover(casas, player, tabuleiro):
    if player.posicao + casas >= tabuleiro.tamanho - 1:
        player.posicao = tabuleiro.tamanho - 1 
        casaFinal(player, casas)
    elif player.posicao + casas < 0:
        player.posicao = 0
    else: 
        player.posicao += casas

        if tabuleiro.tabuleiro[player.posicao] == 'R':
            casaRetro(player)
        elif tabuleiro.tabuleiro[player.posicao] == 'A':
            casaAvanco(player)
        elif tabuleiro.tabuleiro[player.posicao] == 'N':
            casaNeutra(player)

def turno(indice):
        print('=='*40)
        print('Tabuleiro: ')
        tabuleiro.mostrar()
        if indice == 1: 
            jogador = jogadorUm
        else: 
            jogador = jogadorDois
        print('=='* 40)
        print('Agora é a vez do jogador '+str(indice)+'!')
        print('Sua pergunta é: ')
        if(escolherQuestao(questoes).fazerPergunta()):
            print('Rolando o dado...')
            res = random.randint(1, 6)
            print("Dado:", res)
            mover(res, jogador, tabuleiro)
        else: 
            print('Ops! Resposta errada!')
            if indice == 1: 
                turno(2)
            else:
                turno(1)

# start

turno(1)
