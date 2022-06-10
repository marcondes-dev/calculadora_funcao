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