#Aluno Victor Fernandes - PUCPR - Matéria de Raciocínio Computacional - Análise e Desenvolvimento de Sistemas

#Utilizando print para exibir o nome do jogo e dar boas-vindas ao jogador
print ("ZOMBIE DICE (Prototipo Semana 4) ");
print ("Seja bem-vindo ao jogo Zombie Dice");

#Atribuição de valor 0 para váriavel numJogadores, para servir de parâmetro para linha abaixo
numJogadores = 0
#Esta linha verifica se o número de jogadores é menor que dois, enquanto for menor, o loop se repete
while (numJogadores < 2):
    #Linha para que o usário declare o número de jogadores
    numJogadores = int( input("Informe o número de jogadores: ") );
#Se o número declarado de jogadores for menor que dois, o aviso abaixo será exibido na tela e o loop reinicia
    if  (numJogadores < 2):
        print("AVISO: Você precisa de pelo menos 2 jogadores!\n");
#Iniciamos uma lista para armazenar o nome dos jogadores
listaJogadores = []
#Aqui criamos um parâmetro do tamanho do valor declarado no número de jogadores, ou seja, o range dele é proporcional ao valor do número de jogadores
for i in range (numJogadores):
    #Linha para que o usuário declare o nome do jogador e o associa a variável "nome"
    nome = input ("Informe o nome do jogador " + str(i + 1) + ": ");
#Append para conectar a váriavel "nome" com a lista de jogadores criada na linha 17
    listaJogadores.append(nome)
#Declarando as faces dos dados, C=Cerebro P=Passo T=Tiro
dadoVerde = "CPCTPC";
dadoAmarelo = "TPCTPC";
dadoVermelho = "TPTCPT";
#Lista contendo a quantidade de dados, afim de emular o copo de dados do jogo real
listaDados = [
    dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,
    dadoAmarelo,dadoAmarelo,dadoAmarelo,dadoAmarelo,
    dadoVermelho,dadoVermelho,dadoVermelho
]
#Print para dizer ao usuário que o jogo começou
print ("INICIANDO O JOGO!");
#Variável para controlar a posição do jogador na lista
jogadorAtual = 0;
#Contadores para declarar a quantidade de objetos que o jogador tem
tiros = 0;
cerebros = 0;
passos = 0;
#Lista para armazenamento dos dados já sorteados
dadosSorteados = []
#Enquanto verdadeiro, o jogo não para, declaração de loop infinito
while True:
#Mostrar ao usuário de qual jogador pertence o turno atual
    print ("TURNO DO JOGADOR", listaJogadores[jogadorAtual]);
#Dentro da lista de dados, serão sorteados três
    for i in range(0, 3):
#Import que aprendi no StackOverflow para poder utilizar o randint
        from random import randint
#randint irá selecionar aleatóriamente um número de 1 a 13
        numSorteado = randint(0, 12)
#O número que randint selecionar, será consultado na lista de dados
        dadoSorteado = listaDados[numSorteado];
#Mostra ao usuário qual a cor do dado cujo número foi selecionado pelo randint
        if dadoSorteado == 'CPCTPC':
            corDado = 'VERDE';
        elif dadoSorteado == 'TPCTPC':
            corDado = 'AMARELO';
        else:
             corDado = 'VERMELHO';
        print("Dado Sorteado: ", corDado);
#Append para armazenar quais dados foram sorteados
        dadosSorteados.append(dadoSorteado)
#Exibe na tela quais facetas do dado foram sorteadas
    print("As faces sorteadas foram: ")
#Cada item encontrado dentro da lista de dadosSorteados, será enviado para váriavel dadoSorteado
    for dadoSorteado in dadosSorteados:
#Em cada dado sorteado, será também sorteada uma das 6 facetas
        numFaceDado = randint(0, 5);
#Após o sorteio da faceta, o print irá exibir ao jogador qual faceta ele tirou
        if dadoSorteado[numFaceDado] == 'C':
            print("- CÉREBRO (Você comeu um cérebro)");
            cerebros = cerebros + 1;
        elif dadoSorteado[numFaceDado] == 'T':
            print("- TIRO(Você levou um tiro)");
            tiros = tiros + 1;
        else:
            print("- PASSOS (Uma vítima escapou)");
            passos = passos + 1;
#Após o termino do sorteio dos dados, irá ser exibido os dados atuais do jogador
    print("SCORE ATUAL: ");
    print("CÉREBROS: ", cerebros);
    print("TIROS: ", tiros);
#Exibe aviso na tela dando a opção de o jogador atual continuar rodando os dados
    continuarTurno = ( input ("AVISO: Você deseja continuar jogando dados? (s=sim / n=não):") );
#Caso selecione que não quer continuar, a vez passa para o próximo jogador
    if continuarTurno == "n":
        jogadorAtual = jogadorAtual + 1;
        dadosSorteados = [];
        tiros = 0;
        cerebros = 0;
        passos = 0;
#Função verifica se o player ganhou ou perdeu e exibe texto comemorativo
#Se o número de cerebros for maior que 12, o jogador atual ganha e o jogo exibe input para sair
    if (cerebros > 12):
        print("Mas que zumbi! você comeu 13 cérebros e ganhou :D !")
        while True:
            while True:
                fechar = input('Tchau Tchau, obrigado por jogar :D ! pressione enter para sair do jogo.')
                if not fechar:
                    print("Saindo do programa.")
                exit()
#Se o número de tiros for maior que 2, o jogador atual perde e o jogo exibe input para sair
    if (tiros > 2):
        print("Que pena! você levou três tiros e perdeu :C !")
        while True:
            while True:
                fechar = input('Tchau Tchau, obrigado por jogar :D ! pressione enter para sair do jogo.')
                if not fechar:
                    print("Saindo do programa.")
                exit()
#Se os jogadores decidirem por continuar rodando os dados, o jogo continua
    else:
        print("Iniciando mais uma rodada do turno atual");
        dadosSorteados = [];



