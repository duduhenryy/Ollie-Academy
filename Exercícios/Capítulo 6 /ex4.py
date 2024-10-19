# Desenvolva um programa em Python que use um loop for para imprimir os primeiros 10 números da sequência de Fibonacci. 
# A sequência de Fibonacci é aquela em que cada número é a soma dos dois anteriores (começando com 0 e 1). 
# Portanto, a sequência começa assim: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34…

a, b = 0, 1

for _ in range(10):
    print(a)
    a, b = b, a + b
