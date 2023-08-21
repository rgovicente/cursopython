# Concatenando vars

nome = "Adriano"
sobrenome = 'Silva'
idade = 34

# Forma 1 - Concatenando com +
print("Olá, me chamo " + nome + " " + sobrenome)

# Forma 2 - Concatenando com vírgula
print("Olá, me chamo", nome, sobrenome)

# Forma 3 - Format strings extensa
print("Olá, me chamo {} {} e tenho {} anos de idade".format(nome, sobrenome, idade))

# Forma 4 - Format string resumida
print(f"Olá, me chamo {nome} {sobrenome} e tenho {idade} anos de idade!")