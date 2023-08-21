# Listas são basicamente vars que podem receber múltiplos valores, de todos os tipos de dados.
lista = ['abc', 'def', 123, 456, True, False]

# Imprimindo a lista inteira
print(lista)

# Imprimindo um item específico da lista
print(lista[0])

# Imprimindo um intervalo da lista
print(lista[1:4])

# Imprimindo tudo até uma posição específica
print(lista[:4])

# Imprimindo todos os itens a partir de uma posição
print(lista[1:])

# Imprimindo o último item da lista
print(lista[-1])

# Adicionando itens a lista
lista.append("2023")
print(lista)

# Adicionando múltiplos itens a lista
novosElementos = ['maio', 'agosto']
lista.extend(novosElementos)
print(lista)

# Removendo itens da lista
lista.remove('maio')
print(lista)

# Verificando o tamanho da lista(Quantidade de Itens)
print(len(lista))

# Atualizando um item em uma posição específica
lista[3] = "456"
print(lista)