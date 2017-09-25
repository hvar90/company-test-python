from math import sqrt, ceil

punto1 = (2, 2)
punto2 = (4, 4)
punto3 = (6, 6)

def distancia_entre_3(p1, p2, p3):

    d1 = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    d2 = sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2)
    d3 = sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)

    return (d1 + d2 + d3)/ 3
    
def distancia_entre_32(p1, p2, p3):
	
    g=lambda p1,p2:sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    d1 = g(p1,p2)
    d2 = g(p1,p3)
    d3 = g(p2,p3)
    
    return (d1 + d2 + d3)/ 3

print distancia_entre_3(punto1, punto2, punto3)

print distancia_entre_32(punto1, punto2, punto3)

# Ejercicio 2

from collections import Counter

l1 = [34,31,34,77,82]
l2 = [22,101,102,101,102,525,88]
l3 = [66]
l4 = [14,14,2342,2342,2342]

# la longitud del arreglo no es necesaria, la incluyo solo 
# para cumplir con el planteamiento del problema

def NumMasPopular(lst, long):
	mc = Counter(lst).most_common()
	print mc
	max_reps = max(mc, key = lambda t: t[1])[1]
	print max_reps
	mr = filter(lambda x: x[1]== max_reps, mc)
	print mr
	mrc = min(mr, key = lambda t: t[0])
	print mrc
	return mrc[0]

print NumMasPopular(l1, len(l1))
print NumMasPopular(l2, len(l2))
print NumMasPopular(l3, len(l3))
print NumMasPopular(l4, len(l4))

# Ejercicio 3

def IsCasiPalindromo(palabra):    
    def _isPal(palabra):
        if str(palabra) == str(palabra)[::-1]:
            return True

    if _isPal(palabra):
        return True
    else:
        mod_char = 0

        length = len(palabra)

        chars = []

        for i, char in enumerate(palabra[:length/2],1):           
            if char == palabra[length - i]:
                chars.append(char)
            else:
                chars.append(palabra[length - i])
                mod_char += 1
        if mod_char > 1:
            return False
        return True
        
def IsCasiPalindromo2(palabra):	
	
	reverse=palabra[::-1]	
	
	if  palabra == reverse:
		return True
	else:
		mod_char = 0
		length = len(palabra)
		chars = []		
		for i, char in enumerate(palabra[:len(palabra)/2]):           
			if char == reverse[i]:
				chars.append(char)
			else:
				chars.append(reverse[i])
				mod_char += 1
		if mod_char > 1:			
			return False		
		return True
		
def IsCasiPalindromo3(palabra):	
	
	reverse=palabra[::-1]	
	
	if  palabra == reverse:
		return True
	else:
		mod_char = 0
		length = len(palabra)
		chars = []		
		for i, char in enumerate(palabra[:len(palabra)/2]):           
			if char != reverse[i]:
				chars.append(reverse[i])
				mod_char += 1
				if mod_char > 1:			
					return False		
		return True
		
print "abccba"[:4]
print IsCasiPalindromo3("abccba")
print IsCasiPalindromo3("abccbx")
print IsCasiPalindromo3("abccfg")
print IsCasiPalindromo3("abcncbx")

print list(set([(0, 'a'), (4, 'e'), (1, 'b'), (2, 'c'), (5, 'f'), (3, 'd')]))
print set([(0, 'a'), (4, 'e'), (1, 'b'), (4, 'e'), (5, 'f'), (3, 'd')])

