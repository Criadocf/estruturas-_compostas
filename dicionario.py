dicionario = {'nome':'kajota', 'idade':32}

print(dicionario)

#retorna as chaves do dicionario
print(dicionario.keys())

#retorna os valores do dicionario.
print(dicionario.values())

#retorna as as chaves e os valores.
print(dicionario.items())

###
transition = ['televisao', 1.86, 'vivo']
# To get the class (type) of a variable, use the 'type()' function.
print(type(transition))

david = tuple(transition)
print(type(david))

conjunto = set(david)
print(type(conjunto))

#O python é inteligente o suficiente pra transfomar um par de chave-valor
#em um dicionário!
dicionario_entendido = dict((['nome', 'kleber'], ['idade', 0]))

print(dicionario_entendido)




