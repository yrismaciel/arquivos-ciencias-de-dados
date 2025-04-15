#usando o laço while apresentar o total da soma obtida dos cem primeiros numeros inteiros
#(1+2+3+3+...+98+99+100)

##nicializando variáveis##
soma = 0
numero = 1

# Usando a somar dos números de 1 a 100
while numero <= 100:
    soma += numero
    numero += 1

# Exibindo o resultado
print("A soma dos cem primeiros números inteiros é:", soma)
