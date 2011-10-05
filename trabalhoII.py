f = open('part-00000', 'r')

lista = [['',0]]*11

contador = 0
minimo = 0

for line in f:
	contagem = line.split('\t')
	current_word = contagem[0]
	total_count = int(contagem[1].strip('\n'))
	
	if(current_word == 'love'):
		print current_word + "," + str(total_count)

	if(current_word == 'hate' ):
		print current_word + "," + str(total_count)	
	
	if(current_word == 'death' ):
		print current_word + "," + str(total_count)	
	
	if(current_word == 'be' ):
		print current_word + "," + str(total_count)	
	
	if(current_word == 'not' ):
		print current_word + "," + str(total_count)	
	if(current_word == 'life' ):
		print current_word + "," + str(total_count)	
	
	
	#Top Ten
	for x in range(10):
		if ((lista[x][1] <= lista[x+1][1]) & (lista[x][1] <= lista[minimo][1])):
			minimo = x			
	if lista[minimo][1] < total_count:
		lista[minimo] = [current_word,total_count]		

print lista
