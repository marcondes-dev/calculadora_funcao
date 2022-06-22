import math
import matplotlib.pyplot as plt
import numpy as np

global a
global b
global c

#funcoes 2 grau
def calcula_delta(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    return delta

def calcular_raizes(a, b, delta):
    x1 = 0
    x2 = 0
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2.0 * a)
        x2 = (-b - math.sqrt(delta)) / (2.0 * a)
    elif delta < 0:
        x1 = complex(-b, delta/ (2.0 * a))
        x2 = complex(-b, -delta / (2.0 * a))
    return f"A raiz 1 é: {x1} \n" \
           f"A raiz 2 é: {x2}"

def calcular_funcao(x):
    funcao = (a * pow(x, 2)) + (b * x) + c
    return f"x = {funcao}"

def calcular_vertice(a, b, delta):
    xv = 0
    yv = 0
    if a > 0:
        print("O ponto (Xv,Yv) é de mínimo.")
        xv = -b / (2 * a)
        yv = - delta / (4 * a)
    elif a < 0:
        print("O ponto (Xv,Yv) é de máximo.")
        xv = -b / (2 * a)
        yv = - delta / (4 * a)
    elif a == 0:
        print("O 'a' não pode ser zero.")
    return f"O vértice é ({xv},{yv})"

def parabola(x,a,b,c):
    y = a*x**2 + b*x + c
    return y

#funcoes exponenciais
def verificar_funcao(b):
    if (b > 1):
        return '\nA função é crescente!'
    else:
        return '\nA função é descrescente!'

def calcular_x_exp(a, b, x):
    funcao = a * (b ** x)
    return f"{x} = {funcao}"

#graficos
def gerar_grafico(funcao):
    if funcao == "exponencial":
        # Cria vetor de -7 a 7, aumentando de 0.1
        vetorX = np.arange(-7, 7, 0.1)
        print(vetorX)
        # Encontra os valores de y para cada valor de x vetory = [] # vetor y vazio
        vetorY = []  # vetor y vazio
        for x in vetorX:
            vetorY.append(a ** x)  # retorno da funcao vai para o vetory
        print(vetorY)
        # prepara para salvar o grafico
        fig = plt.figure(figsize=(5, 5))
        # Plota (desenha) o grafico
        plt.plot(vetorX, vetorY, label='Funcao Exponencial', color='g')
        plt.title('f(x) = a^x')
        # nome para o eixo x
        plt.xlabel('eixo x')
        # nome para o eixo y
        plt.ylabel('eixo y')
        # apresenta legenda do grafico
        plt.legend()
        # apresenta grade do plano cartesiano
        plt.grid(True, which='both')
        # destaca o eixo x em preto ('k')
        plt.axhline(y=0, color='k')
        # destaca o eixo y em preto ('k')
        plt.axvline(x=0, color='k')
        # mostra o grafico
        plt.show()
        fig.savefig('FExp.png')
    elif funcao == "quadratica":
        #calcula o delta
        delta = b ** 2 - 4 * a * c
        #verifica o delta e calcula raizes
        if delta > 0:
            x_1 = (-b + math.sqrt(delta)) / (2 * a)
            x_2 = (-b - math.sqrt(delta)) / (2 * a)
        if delta == 0:
            x_0 = -b / (2 * a)
        else:
            pass

        #calcula o vertice
        p = -b / (2 * a)
        q = -delta / (4 * a)

        # plot function
        x = np.linspace(int(p) - 5, int(p) + 5, 100)

        #parabola
        y = a * x ** 2 + b * x + c
        plt.plot(x, y)
        plt.axhline(y=0, color='black', linestyle='-')
        plt.axvline(x=0, color='black', linestyle='-')
        plt.text(p - 0.5, q - 3, '[' + str(round(p, 2)) + ',' + str(round(q, 2)) + ']', color='orange', fontsize=9)
        plt.plot(p, q, marker="o")

        if delta > 0:
            plt.plot(x_1, 0, marker="o", color='green')
            plt.text(x_1 - 0.5, 2, '[' + str(round(x_1, 2)) + ']', color='green', fontsize=9)
            plt.plot(x_2, 0, marker="o", color='green')
            plt.text(x_2 - 0.5, 2, '[' + str(round(x_2, 2)) + ']', color='green', fontsize=9)

        if delta == 0:
            plt.plot(x_0, 0, marker="o", color='green')
            plt.text(x_0 - 0.5, 2, '[' + str(round(x_0, 2)) + ']', color='green', fontsize=9)

        plt.show()

#matrizes
def gerar_matriz (linhas, colunas):
    matriz = []

    for i in range(linhas):
        matriz.append( [" "] * colunas )

    for linha in range(linhas):
        for coluna in range(colunas):
            print('Informe um elemento para:', linha, ';', coluna)
            matriz[linha][coluna] = int(input( ))

    return matriz

def multiplicar_matrizes(matriz, colunas_1, linhas_1):
    linhas_2 = int(input('Digite o numero de linhas da segunda matriz: '))
    colunas_2 = int(input('Digite o numero de colunas da segunda matriz: '))

    if(linhas_2 == colunas_1):
        matriz_2 = gerar_matriz(linhas_2, colunas_2)
        multiplicar(matriz, matriz_2, colunas_1, linhas_1, colunas_2)
    else:
        print('\nA operação não é possível pois o número de colunas da matriz 1 tem que ser igual ao número de linhas da matriz 2')

def multiplicar(matriz, matriz_2, colunas, linhas, colunas_2):
    matriz_multiplicada = []

    for linha in range(linhas):
        matriz_multiplicada.append([])
        for coluna in range(colunas_2):
            matriz_multiplicada[linha].append(0)
            for c in range(colunas):
                matriz_multiplicada[linha][coluna] += matriz[linha][c] * matriz_2[c][coluna]
    
    print('\nMatriz A:', matriz, 'x', matriz_2, 'resultou em\n', matriz_multiplicada)

def transpor_matriz(matriz, linhas, colunas):
    matriz_transposta = []
    for i in range(colunas):
        matriz_transposta.append( [" "] * linhas )

    for i in range (linhas): 
        for j in range (colunas): 
            matriz_transposta[j][i] = matriz[i][j] 
    print("Matriz Transposta") 
    for i in range (colunas): 
        print(matriz_transposta[i])

def verificar_matriz(linhas, colunas):
        if linhas == colunas:
            return 'A matriz é quadrada!'
        else:
            return 'A matriz não é quadrada!'

calculadora = True
while calculadora:
    escolha_usuario = int(input("\nBem-vindo a nossa calculadora!\n"
          "Escolha qual cálculo gostaria de fazer:\n"
          "1 - Funções de segundo grau;\n"
          "2 - Funções exponenciais;\n"
          "3 - Matrizes:\n"
          "4 - Sair.\n"))
    if escolha_usuario == 1:
        funcoes_2grau = True
        while funcoes_2grau:
            opcao_calculo = int(input("Você escolheu funções de 2º grau\n"
                                      "Escolha o que gostaria de calcular:\n"
                                      "1 - Calcular raízes;\n"
                                      "2 - Calcular função de x [f(x)];\n"
                                      "3 - Calcular vértice;\n"
                                      "4 - Gerar gráfico;\n"
                                      "5 - Sair\n"))
            if opcao_calculo < 5:
                a = float(input("Informe o a:"))
                b = float(input("Informe o b:"))
                c = float(input("Informe o c:"))
            delta_calculado = calcula_delta(a, b, c)
            match opcao_calculo:
                case 1:
                    print("1 - Calcular raízes;\n", calcular_raizes(a, b, delta_calculado))
                case 2:
                    print("2 - Calcular função de x [f(x)];\n", calcular_funcao(float(input("Informe o x:"))))
                case 3:
                    print("3 - Calcular vértice;\n", calcular_vertice(a, b, delta_calculado))
                case 4:
                    print("4 - Gerar gráfico;\n", gerar_grafico("quadratica"))
                case 5:
                    break
                case default:
                    print("Escolha uma opção válida!")


    elif escolha_usuario == 2:
        funcao_exp = True
        while funcao_exp:
            opcao_calculo = int(input('\nVocê escolheu funções exponenciais, digite de acordo com a ação que deseja:'
                                        '\n1 - Verificar se a funcão é crescente ou decrescente'
                                        '\n2 - Calcular função de x informado'
                                        '\n3 - Gerar gráfico'
                                        '\n4 - Sair '
                                        '\n'))
            match opcao_calculo:
                case 1:
                    print('1 - Verificar se a funcão é crescente ou decrescente\n')
                    b = float(input("Informe o b:"))
                    while b < 0:
                        print('\nO Valor de b tem que ser positivo.')
                        b = float(input('\nInforme o valor de b: '))
                    print(verificar_funcao(b))
                case 2:
                    print('2 - Calcular função de x informado')
                    b = int(input('\nInforme o valor de b: '))
                    while b < 0:
                        print('\nO Valor de b tem que ser positivo.')
                        b = int(input('\nInforme o valor de b: '))
                    print(calcular_x_exp(float(input("Informe o a:")),
                                         b,
                                         float(input('Informe um valor de x para calcular a função dele: \n'))))
                case 3:
                    print('3 - Gerar gráfico\n')
                    a = float(input("Informe o a:"))
                    x = float(input('\nInforme um valor de x para calcular a função dele:'))
                    gerar_grafico("exponencial")
                case 4:
                    break
                case default:
                    print("Escolha uma opção válida!")
    elif escolha_usuario == 3:
        matriz = True
        while matriz:
            opcao_calculo = int(input('\nVocê escolheu matrizes, digite de acordo com a ação que deseja:'
                                        '\n 1 - Verificar se a matriz é quadrada'
                                        '\n 2 - Multiplicar com outra matriz'
                                        '\n 3 - Transpor matriz'
                                        '\n 4 - Sair'
                                        '\n'))

            linhas = int(input('Digite o numero de linhas: '))
            colunas = int(input('Digite o numero de colunas: '))
            matriz = gerar_matriz(linhas, colunas)
            for i in range(linhas):
                print(matriz[i])

            match opcao_calculo:
                case 1:
                    print('1 - Verificar se a matriz é quadrada\n')
                    print(verificar_matriz(linhas, colunas))
                case 2:
                    print('2 - Multiplicar com outra matriz\n')
                    print(multiplicar_matrizes(matriz, colunas, linhas))
                case 3:
                    print('3 - Transpor matriz\n')
                    print(transpor_matriz(matriz, linhas, colunas))
                case 4:
                    break
                case default:
                    print("Escolha uma opção válida!")
    elif escolha_usuario == 4:
        break
    else:
        print("Escolha uma opção válida!")