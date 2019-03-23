def julio_eduardo(entrada):
#	diff = [ entrada[x] - entrada[x+1] for x in range(len(entrada))]	
#	cutpoints = [(elem == -1, index) for index, elem in enum(diff)]
#	cutpoints = filter()

	# 1 2 3 4 5   7 8 9
	# --------- | ------
    # T F F F F   T F F

	cutpoints = ((entrada[x] - entrada[x-1]) != 1
			     for x
                 in range(len(entrada)))
	result = []
	for value, _new in zip(entrada, cutpoints):
		if _new:
			result.append([value])
		else:
			result[-1] = [result[-1][0], value]
	return result

def tony(entrada):
	input = sorted(entrada)
	resultados = []
	while len(input) > 0:
		inicio = input.pop(0)
		ponteiro = inicio
		while input and input[0] - ponteiro == 1:
			ponteiro = input.pop(0)
		if inicio == ponteiro:
			resultado.append([inicio])
		else:
			resultado.append([inicio, ponteiro])
	return resultado
	
def grupo(entrada):
	prim = entrada[0]
	walker = prim	
	resultado = []
	interm = []
	interm.append(entrada[0])

	for elem in entrada[1:]:	
		
		if elem != walker+1:
			interm.append(walker)	
			resultado.append(interm)
			walker = elem
			interm =[elem]	
	
		else:
			walker = elem
		#print(elem)
	if len(interm) > 0:
		resultado.append(interm)
	#print(resultado)
	return sorted(resultado)
