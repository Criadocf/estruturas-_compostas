#conjunto nao repete os elementos e tambem a ordem dos elementos sempre
# e aleatoria.
#set nao aceita lista elemento.

conjunto = {1993,"kleber", True, 1.85, 1.85,  ('kaleb', 1.10)}

print(conjunto)

print(len(conjunto))

conjunto.add('Vasco')

print(conjunto)
print(len(conjunto))
print(conjunto)

print(conjunto)

#é assim que acesso a um elemento do conjunto, ''arranco'' ele do conjunto
#com pop(), estranho ne, mas é assim mesmo.
elemento = conjunto.pop()


print('POP')
print(elemento)

print(conjunto)

#Ou entao, se eu quiser acessar a um elemento do conjunto sem precisar
#"arrancar" ele do conjunto, eu transformo esse conjunto em uma lista.
novo_conjunto = list(conjunto)

print(novo_conjunto)

del novo_conjunto[-1]

print(novo_conjunto)