# definindo variáveis
palavra = input().lower()

# algoritmo
vogais = "aeiouy"
nova_palavra = ""
for i in palavra:
        if i not in vogais:
                nova_palavra += "." + i
print(nova_palavra)
