def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:

	# Return the element-wise sum of vectors 'a' and 'b'.
	dizi=[]
	if len(a) == len(b):
		for i in range (len(a)):
			dizi.append(a[i]+b[i])
		return dizi
	else:
		return -1
		
	