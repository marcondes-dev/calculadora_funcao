import math
a = 0
b = 0
c = 0

def calcula_delta(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    return delta

def funcao_grau2(a, b, delta):
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
    elif delta < 0:
        complex((-b, delta)/ (2 * a))

    return "A raiz 1 é:", x1, "A raiz 2 é:", x2

calculadora = True
while calculadora:
    escolha_usuario = int(input("Bem-vindo a nossa calculadora!\n"
          "Escolha qual cálculo gostaria de fazer:\n"
          "1 - Funções de segundo grau;\n"
          "2 - Funções exponenciais;\n"
          "3 - Matrizes:\n"
          "4 - Sair.\n"))
    if escolha_usuario == 1:
        print("Você escolheu calcular funções de 2º grau:")
        a = float(input("Informe o a:"))
        b = float(input("Informe o b:"))
        c = float(input("Informe o c:"))
        funcao = print(funcao_grau2(a, b, c))
    elif escolha_usuario == 2:
        """funcao_exponencial()"""
    elif escolha_usuario == 3:
        """cria_matriz()"""
    elif escolha_usuario == 4:
        break
    else:
        print("Escolha uma opção válida!")