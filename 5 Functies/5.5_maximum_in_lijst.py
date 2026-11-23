def vind_maximum(getallen):
	maximum = getallen[0]
	for getal in getallen:
		if getal > maximum:
			maximum = getal
	return maximum


getallen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(vind_maximum(getallen))
