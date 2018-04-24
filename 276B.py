entrada = raw_input()

#Subtrai do ord(a) para substituir na posição, ex b = 98 a = 97, logo o array será alfabeto = [0, 1, 0....0].
alfabeto = [0]*26
for i in range(len(entrada)):
	alfabeto[ord(entrada[i]) - ord('a')] += 1

#Verifica a quantidade de ocorrências ímpares do array, pois no fim é a única coisa que importa.	
contador = 0
for j in range(26):
	if alfabeto[j] % 2 == 1:
		contador += 1
if contador == 0 or contador % 2 == 1:
	print 'First'
else:
	print 'Second'
