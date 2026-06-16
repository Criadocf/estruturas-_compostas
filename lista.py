#dentro da lista posso usar todos os tipos de variaveis, inclusive listas.

lista = [1.85, 32, 'kleber', 1993, ['elsie',10], 79, 57, True]

print(lista[4])

#acessar o ultimo elemento sem saber quantos elementos tem na lista (lista[-1])

print(lista[-1])


#adicionar um elemento na lista.
lista.append(2000)
lista.append(1923)

print(lista)

#deletar um item da lista
del lista[-1]
print(lista)

lista.remove(2000) #usando o metodo 'remove' passamos entre parenteses o item
#queremos remover e nao a posição entre colchetes.
print(lista)

#substituir item da lista. atribuimos outros valor.
lista[2] = 'Kajota'

print(lista)

#saber o tamanho de uma lista, quantos elementos há nela. Usamos
#a função len.
len(lista)

#as strings se comportam como lista, ou seja posso acessar
#qualquer individuualmente qualquer caractere dessa string

texto = 'pangloss'

print(texto[4])

