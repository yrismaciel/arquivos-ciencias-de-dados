#Usando o laço while apresentar os resultados de uma tabuada de multiplicar (de 1 ate 10) de um
#numero qualquer

##Solicitando um número##
numero = int(input("Digite um número para ver sua tabuada: "))

# Iniciando a variável para o laço
contador =1

# Laço while para calcular e exibir a tabuada
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador +=1

