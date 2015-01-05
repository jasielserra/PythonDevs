def crivo(n):
	lista = [2]
	lista.extend(range(3,n+1,2))
	primos = lista[:1]
	while len(lista) > 0:
		primo = primos[-1]
		lista = [numero for numero in lista if numero % primo != 0 ]
                          if lista:
                            primos.append(lista[0])
	return primos

