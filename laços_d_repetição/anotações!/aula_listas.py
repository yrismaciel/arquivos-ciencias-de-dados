#Aula_lista.py

#iniciansdo uma lista vazia
listaVazia = []

#Iniciando uma lista de valores inteiros
listaInteiros = [2, 4, 5, 6, 9]
print('Lista de Inteiros: ', listaInteiros)

#Iniciando uma lista de valores reais
listaReais = [9.8, 6.5, 2.1, 3.02, 7.7]
print('Lista reais: ', listaReais)

#Iniciando uma lista de valores string
listaFrutas = ['Abacaxi', 'cupu', 'Ameixa', 'Castanha', 'Sapota']
print('lista de Frutas: ', listaFrutas)

#Adicionando valores a lista usando append
listaFrutas.append('Araçá')
print('lista de Frutas: ', listaFrutas)
listaFrutas.append('Camu-Camu')
print('lista de Frutas: ', listaFrutas)

#Para saber o tamanho dessa lista usansando o lenght de forma abreviada len
tamanholistaFrutas = len(listaFrutas)
print('A lista de frutas possui: ', tamanholistaFrutas)

#Mostrar o valor espercifico
print(listaFrutas[3])

#Alterar valor da lista com indice espercifico
listaFrutas[2] = 'Sapota'
print(listaFrutas)

#Excluindo um valor da lista
del listaFrutas[4]
print(listaFrutas)

#Manipulando lista com while
z = 0
tamanholistaFrutas = len(listaFrutas)

while z < tamanholistaFrutas:
    print('Valor na posição: ', z, 'é: ', listaFrutas[z])
    z = z + 1
#Manipulando lista com for
for fruta in listaFrutas:
    print('FOR> ', fruta)
    