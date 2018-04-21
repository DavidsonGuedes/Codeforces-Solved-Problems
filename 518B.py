string1 = map(str, input())
string2 = map(str, input())
match1_string1 = {}
match1_string2 = {}
match2_string1 = {}
match2_string2 = {}
match1 = 0
match2 = 0
for i in range(len(string1)):
	letra = string1[i]
	if letra in match1_string1:
		match1_string1[letra] += 1
	else:
		match1_string1[letra] = 1	
	if letra.lower() in match2_string1:
		match2_string1[letra.lower()] += 1
	else:
		match2_string1[letra.lower()] =	1				
for i in range(len(string2)):
	letra = string2[i]
	if letra in match1_string2:
		match1_string2[letra]+=1
	else:
		match1_string2[letra] = 1	
	if letra.lower() in match2_string2:
		match2_string2[letra.lower()] += 1
	else:
		match2_string2[letra.lower()] = 1
mindict = min(match1_string1,match1_string2)
maxdict = max(match1_string1,match1_string2)
mindict2 = min(match2_string1,match2_string2)
maxdict2 = max(match2_string1,match2_string2)			
for i in mindict:
	if i in maxdict:
		match1 += min(mindict[i],maxdict[i])
for i in mindict2:
		if i in maxdict2:
			match2 += min(mindict2[i],maxdict2[i])	
print(match1,match2-match1)
