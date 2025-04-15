#calculo de media
#informe a altura de maria, juana e pedro,  em seguida calcule a media dessas alturas


NOMES = {
    'nome' :['Maria' , 'Juana' , 'Pedro'],'altura':[1.63, 1.45, 1.59]
}

for chave, valor in NOMES.items():
    print(chave, valor)
    
#imprimindo todos os produtos
NOMES = {
    'nome': ['Maria' , 'Juana' , 'Pedro'],
    'altura': [1.63, 1.45, 1.59],
}
for nome, altura, in zip (NOMES['nome'] , NOMES['altura'], ):
    print("nomes:", nome, "altura : ", altura, )










