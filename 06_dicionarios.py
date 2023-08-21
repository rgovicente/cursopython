# Dicionários são elementos que possuem chave: valor(Key: value)
dicionario = {
    'nome': 'Pythonildo',
    'idade': 18,
    'altura': 1.65
}

# Acessando o dado de um dicionário
print(dicionario['nome'])
print()

# Podemos usar o get para recuperar as informações
print(dicionario.get('nome'))
print()

# Caso não encontremos o dado, podemos definir um valor para mostrar o erro
print(dicionario.get('peso', 'Não foi possível localizar o que desejava'))
print()

# Listando as chaves
computador = {
  'Processador': 'I7',
  'RAM': '32GB',
  'SSD': '512GB'
}

print(computador.keys())
print()

# Listando os valores
materias = {
    'Português': 5,
    'Matemática': 6,
    'História': 10,
    'Inglês': 9
}

print(materias.values())
print()

# Percorrendo o Dicionário
computador = {
  'Processador': 'I7',
  'RAM': '32GB',
  'SSD': '512GB'
}

for chave in computador.keys():
    print(f"Item {chave} com valor de {computador[chave]}")

print()

# Usando o elemento items()
frutas = {
    'pera': 10,
    'manga': 12,
    'uva': 6
}

print(frutas.items())
print()

# Adicionando e atualizando itens
pessoa = {
    'nome': 'Pythonildo',
    'idade': 18,
    'altura': 1.65
}

print(pessoa)
print()

pessoa.update({'nome': 'Javonildo'})
pessoa.update({'idade': 32})
pessoa.update({'peso': 90})

print(pessoa)
print()

# Eliminando items
del pessoa['peso']
print(pessoa)
print()

# Eliminando último elemento
sacola = {'maça': 2, 'ovos': 6, 'farinha': 2}
print(sacola)
farinha = sacola.popitem()

print(farinha)
print(sacola)
print()

# Limpando o dicionário
dicio = {'nome': 'F9', 'motor': 'v8', 'ano': 2019}
dicio.clear()

print(dicio)
print()

# Criando dicionários a partir de listas
chaves = ['chave 1', 'chave 2', 'chave 3']
valor = 0

dicioList = dict.fromkeys(chaves, valor)
print(dicioList)

# Juntando Dicionários
regulagem = {'max': 10, 'min': 0, 'meio': 5}
extra = {'passo': 2}

dicioJuntinhos = {**regulagem, **extra}
print(dicioJuntinhos)
print()