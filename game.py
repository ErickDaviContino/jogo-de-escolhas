from random import randrange
import os
import shutil

def main():
    CAMINHO_VERMELHO = 1
    CAMINHO_PRETO = 2
    tentativas = 7
    sala = 1
    tentativaFuga = False

    desenharSala(sala, tentativas, tentativaFuga)

    while (tentativas > 0 and sala != 9):

        escolha = int(input())

        if ((escolha == CAMINHO_VERMELHO and sala != 6) or (escolha == CAMINHO_PRETO and sala != 8)):
            sala += escolha
        elif sala == 8:
            sala = selecionaNumAleatorio(1, 6)
        else:
            tentativaFuga = True

        limpaTela()
        tentativas -= 1

        desenharSala(sala, tentativas, tentativaFuga)
        tentativaFuga = False

def desenharSala(sala, tentativas, fuga):

    desenharMensagem(sala, tentativas, fuga)
    desenharImagem(sala, tentativas)
    desenharVidas(tentativas)

def desenharMensagem(sala, tentativas, fuga):
    printFormatado(tipoFormatacao = "linhaCheia",
                   preenchimento = "=")

    if sala == 9:
        mensagem = [" Parabéns, bravo(a) guerreiro(a)! Você chegou ao final da masmorra. ",
                    " Leve este troféu e lembre-se de sua conquista "]
    elif tentativas == 0:
        mensagem = [" Apesar de seus esforços, suas chances se esgotaram. ",
                    " sua visão escurece, sua respiração pesa.. É O FIM! "]
    else:
        if fuga:
            mensagem = [" ESTÁ TENTANDO DESRESPEITAR AS REGRAS? NÃO VAI FUNCIONAR. ",
                        " -1 TENTATIVA PARA VOCÊ!! "]
        else:
            mensagem = [" Bravo(a) guerreiro(a), você está na {}ª sala ".format(sala),
                        " Escolha seu caminho, ou lamente eternamente "]
            if sala == 6:
                mensagem.append(" [2] - Caminho preto ")
            else:
                mensagem.append(" [1] - Caminho vermelho <-> [2] - Caminho preto ")

    printFormatado(tipoFormatacao = "alinhamento",
                   texto = mensagem,
                   alinhamento = "centralizado",
                   preenchimento = "=")
    
    printFormatado(tipoFormatacao = "linhaCheia",
                   preenchimento = "=")

def desenharImagem(sala, tentativas):
    imagem = ["@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
              "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"]

    if sala == 9:
        imagem.extend(["@@  |                                         |  @@",
                       "@@  |                                         |  @@",
                       "@@  |               ____________              |  @@",
                       "@@  |______________'._==_==_==_.'_____________|  @@",
                       "@@  /              .-\:       /-.             \  @@",
                       "@@ /              | (|:.      |) |             \ @@",
                       "@@/                '-|:.      |-'               \@@",
                       "@@                   \::.     /                  @@",
                       "@@                    '::.  .'                   @@",
                       "@@                      )  (                     @@",
                       "@@                    _.'  '._                   @@",
                       "@@                   '--------'                  @@",
                       "@@                                               @@",
                       "@@                                               @@"])

    elif tentativas == 0:
        imagem.extend(["@@               _________________               @@",
                       "@@           /  /                 \  \           @@",
                       "@@          / \/                   \/ \          @@",
                       "@@          \__|   XXX       XXX   |__/          @@",
                       "@@             |   XXXX     XXXX   |             @@",
                       "@@             |   XXXX     XXXX   |             @@",
                       "@@             \__       X       __/             @@",
                       "@@               |\     XXX     /|               @@",
                       "@@               | |           | |               @@",
                       "@@               | I I I I I I I |               @@",
                       "@@               |  I I I I I I  |               @@",
                       "@@               \_             _/               @@",
                       "@@                 \_         _/                 @@",
                       "@@                   \_______/                   @@"])

    else:
        if sala == 6:
            imagem.extend(["@@                 \____________/                @@",
                           "@@                  |          |                 @@",
                           "@@                  |   ____   |                 @@",
                           "@@                  |  /_   \  |                 @@",
                           "@@                  |   /   /  |                 @@",
                           "@@                  |  /   /_  |                 @@",
                           "@@                  |  \____/  |                 @@",
                           "@@                  |          |                 @@",
                           "@@                  |__________|                 @@",
                           "@@                  /          \                 @@",
                           "@@                 /            \                @@",
                           "@@                /              \               @@",
                           "@@               /                \              @@",
                           "@@              /                  \             @@"])
        else:
            imagem.extend(["@@ |    ___________               __________   | @@",
                           "@@ |   /           |             |          |  | @@",
                           "@@ |  |       _    |             |  ____    |  | @@",
                           "@@ |  |      / \    |            / /_   \   |  | @@",
                           "@@ | /       | |    |           |   /   /   |  | @@",
                           "@@ | |       | |    |  <===>    |  /   /_   |  | @@",
                           "@@ | |       \_/    |    |      |  \____/   |  | @@",
                           "@@ | |              |    |     /             | | @@",
                           "@@ |_|______________|____|____|______________|_| @@",
                           "@@ /  \__         /      |     \            /  \ @@",
                           "@@/     \         \      |     /          /     \@@",
                           "@@       \         \          /         _/       @@",
                           "@@        \         \________/         /         @@",
                           "@@         \                          /          @@"])
    
    imagem.extend(["@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
                   "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"])
               
            
    printFormatado(tipoFormatacao = "alinhamento",
                   texto = imagem,
                   alinhamento = "centralizado")

def desenharVidas(tentativas):

    printFormatado(tipoFormatacao = "linhaCheia",
                   preenchimento = "=")

    printFormatado(tipoFormatacao = "alinhamento",
                   texto = ["Vidas:"],
                   alinhamento = "centralizado")
    if tentativas > 0:            
        vidas = [listParaString(["<3 "] * tentativas)]
    else:
        vidas = ["X_X"]

    printFormatado(tipoFormatacao = "alinhamento",
                   texto = vidas,
                   alinhamento = "centralizado")
    
    printFormatado(tipoFormatacao = "linhaCheia",
                   preenchimento = "=")

def limpaTela():
    os.system("CLS")

def selecionaNumAleatorio(numInicio, numFim):
    return randrange(numInicio, numFim)

def stringParaList(stringParaConversao):
    comprimentoString = len(stringParaConversao)
    listFinal = [None] * comprimentoString
    posicaoAtual = 0
    while posicaoAtual < comprimentoString:
        listFinal[posicaoAtual] = stringParaConversao[posicaoAtual]
        posicaoAtual += 1
    return listFinal

def listParaString(listParaConversao):
    return "".join(listParaConversao)

def printFormatado(tipoFormatacao, texto = None, alinhamento = None, preenchimento = None):

    if preenchimento == None or preenchimento == "":
        caracteresPreenchimento = [" "]
    else:
        caracteresPreenchimento = stringParaList(preenchimento)

    if texto == None:
        textoFormatado = [" "]
    else:
        textoFormatado = [None] * len(texto)
    cont = 0

    if tipoFormatacao == "alinhamento":
        for linha in texto:
            linha = stringParaList(linha)
            textoFormatado[cont] = alinharConteudo(texto = linha,
                                                   tipoAlinhamento = alinhamento,  
                                                   preenchimento = caracteresPreenchimento)
            cont += 1

    elif tipoFormatacao == "linhaCheia":
        larguraTerminal = shutil.get_terminal_size()[0]
        textoFormatado[0] = preencherLinha(tipoPreenchimento = "direita",
                                           tamanhoPreenchimento = larguraTerminal,
                                           preenchimento = caracteresPreenchimento)
    
    for linhaFormatada in textoFormatado:
        print(listParaString(linhaFormatada), end = "")

def preencherLinha(tipoPreenchimento, tamanhoPreenchimento, preenchimento, linha = None):
    if linha == None:
        linha = [""]
    cont = 1
    caracterAtual = 0
    while cont <= tamanhoPreenchimento:
        if tipoPreenchimento == "esquerda":
            linha.insert(0, preenchimento[caracterAtual])
        elif tipoPreenchimento == "direita":
            linha.append(preenchimento[caracterAtual])
        cont += 1
        caracterAtual += 1
        if caracterAtual >= len(preenchimento):
            caracterAtual = 0
    return linha

def alinharConteudo(texto, tipoAlinhamento, preenchimento):
    larguraTerminal = shutil.get_terminal_size()[0]
    totalCaracteres = len(texto)
    if totalCaracteres < larguraTerminal:
        espacamentoTotal = larguraTerminal - totalCaracteres
        espacamentoEsquerdo = 0
        espacamentoDireito = 0
        cont = 1
        linhaFormatada = texto
        
        if tipoAlinhamento == "centralizado":
            espacamentoEsquerdo = espacamentoTotal // 2
            if espacamentoTotal % 2 == 0:
                espacamentoDireito = espacamentoTotal / 2
            else:
                espacamentoDireito = espacamentoTotal // 2 + 1
        elif tipoAlinhamento == "direita":
            espacamentoEsquerdo = espacamentoTotal
        elif tipoAlinhamento == "esquerda":
            espacamentoDireito = espacamentoTotal
        
        if tipoAlinhamento == "centralizado" or tipoAlinhamento == "direita":
            linhaFormatada = preencherLinha(tipoPreenchimento = "esquerda",
                                            tamanhoPreenchimento = espacamentoEsquerdo,
                                            preenchimento = preenchimento,
                                            linha = linhaFormatada)
        
        if tipoAlinhamento == "centralizado" or tipoAlinhamento == "esquerda":
            linhaFormatada = preencherLinha(tipoPreenchimento = "direita",
                                            tamanhoPreenchimento = espacamentoDireito,
                                            preenchimento = preenchimento,
                                            linha = linhaFormatada)

        return linhaFormatada
    else:
        return texto

if __name__ == "__main__":
    main()
