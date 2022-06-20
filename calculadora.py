import math
global a
global b
global c

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

def funcao_exponencial(a, b):
    n = 0
    a = int(input('\nInforme o valor de a: '))
    while n < 1:
        b = input('\nInforme o valor de b: ')
        if(b < 0):
            print('\nO Valor de b tem que ser positivo.')
            break
        else:
            calculos_exponencial(a, b)



    return n

def calculos_exponencial(a, b):
    n = 0
    while n < 1:
        escolha_usuario = int(input('\n Digite de acordo com a ação que deseja: 1 - Verificar se a funcão é crescente ou decrescente',
                                    '\n2 - Calcular função de x informado',
                                    '\n 3 - Gerar gráfico',
                                    '\n 4- Sair' ))
        if(escolha_usuario < 0 or escolha_usuario > 3):
            print('\nValor inválido')
            break
        elif escolha_usuario == 4:
            n =+ 1
        else:
            n += 1
            if(escolha_usuario == 1):
                if(b > 1):
                    print('\nA função é crescente!')
                else:
                    print('\nA função é descrescente!')
            elif(escolha_usuario == 2):
                x = int(input('\nInforme um valor de x para calcular a função dele.'))
                funcao = a * (b ** x)
                print('f(', x, ') = ', funcao)
            elif(escolha_usuario == 3):
                grafico(a, b)

def funcaoExponencial (a, b, x):
    return (a*b**x)   


def grafico(a, b):
    # Cria vetor de -7 a 7, aumentando de 0.1
    vetorX = np.arange(-7,7, 0.1)
    print (vetorX)
    # Coeficientes
    a = 2
    #Encontra os valores de y para cada valor de x
    vetorY = [] # vetor y vazio
    for x in vetorX:
        vetorY.append (funcaoExponencial(a, b, x)) # retorno da funcao vai para o vetory
        print(vetorY)
    #prepara para salvar o grafico
    fig = plt.figure (figsize=(5, 5))
    # Plota (desenha) o grafico
    plt.plot(vetorX, vetorY, label = 'Funcao Exponencial', color = 'g')
    plt.title ('f(x) = a^x')
    plt.xlabel('eixo x')
    # nome para o eixo x
    plt.ylabel('eixo y')
    # nome para o eixo y
    plt.legend()
    #apresenta legenda do grafico
    plt.grid(True, which ='both') # apresenta grade do plano cartesiano
    plt.axhline(y=0, color='k')
    # destaca o eixo x em preto ('k')
    plt.axvline(X = 0, color='k')
    # destaca o eixo y em preto ('k*)
    plt. show()
  


def matriz():
    n = 0
    while n < 1:
        linhas = int(input('Digite o numero delinhas'))
        colunas = int(input('Digite o numero de colunas'))

        matriz = [0] * linhas
        for coluna in range(colunas):
            matriz[coluna] = [0] * colunas

        for linha in range(linhas):
            for coluna in range(colunas):
                matriz[linha][coluna] = float(input('Digite um valor: '))

        for linha in linhas:
            for coluna in colunas:
                if(linhas == 2):
                    break

        escolha_usuario = int(input('\n Digite de acordo com a ação que deseja: 1 - Verificar se a funcão é crescente ou decrescente',
                                    '\n2 - Calcular função de x informado',
                                    '\n 3 - Gerar gráfico',
                                    '\n 4- Sair' ))
        if(escolha_usuario < 0 or escolha_usuario > 3):
            print('\nValor inválido')
            break
        elif escolha_usuario == 4:
            n =+ 1
        else:
            n += 1
            if(escolha_usuario == 1):
                if(b > 1):
                    print('\nA função é crescente!')
                else:
                    print('\nA função é descrescente!')
            elif(escolha_usuario == 2):
                x = int(input('\nInforme um valor de x para calcular a função dele.'))
                funcao = a * (b ** x)
                print('f(', x, ') = ', funcao)
            elif(escolha_usuario == 3):
                grafico(a, b)


calculadora = True
while calculadora:
    escolha_usuario = int(input("Bem-vindo a nossa calculadora!\n"
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
                                      "1 - Calular raízes;\n"
                                      "2 - Calcular função de x [f(x)];\n"
                                      "3 - Calcular vértice;\n"
                                      "4 - Gerar gráfico;\n"
                                      "5 - Sair\n"))
            a = float(input("Informe o a:"))
            b = float(input("Informe o b:"))
            c = float(input("Informe o c:"))
            delta_calculado = calcula_delta(a, b, c)
            if opcao_calculo == 1:
                raizes = print(calcular_raizes(a, b, delta_calculado))
            elif opcao_calculo == 2:
                x= float(input("Informe o x:"))
                fx = print(calcular_funcao(x))
            elif opcao_calculo == 3:
                vertice = print(calcular_vertice(a, b, delta_calculado))
            elif opcao_calculo == 4:
                break
            else:
                print("Escolha uma opção válida!")
    elif escolha_usuario == 2:
        """funcao_exponencial()"""
    elif escolha_usuario == 3:
        """cria_matriz()"""
    elif escolha_usuario == 4:
        break
    else:
        print("Escolha uma opção válida!")