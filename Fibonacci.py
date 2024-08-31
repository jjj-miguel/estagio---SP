#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número 
# informado pertence ou não a sequência.

n = int(input("Digite um número para calcular a sequência de Fibonacci: "))

def is_fibonacci(n): # def = função ( funçao verificando se n pertence a função Fibonacci)
    if n < 0:
        return False # definindo a função para que se o numero for menor que zero return false
    
    a, b = 0, 1 # definindo em linha o valor de a e b
    while a < n:
        temp = a # temporario para guardar o valor de a
        a = b
        b = temp + b
    return a == n # só retorna quando o valor for a == n

if is_fibonacci(n):
    print(f"{n} pertence à sequência de Fibonacci.")
else:
    print(f"{n} não pertence à sequência de Fibonacci.")   

