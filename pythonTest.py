# Ejercicio 1

from math import sqrt, ceil

punto1 = (2, 2)
punto2 = (4, 4)
punto3 = (6, 6)

def distancia_entre_3(p1, p2, p3):
	
    g=lambda p1,p2:sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    d1 = g(p1,p2)
    d2 = g(p1,p3)
    d3 = g(p2,p3)    
    return (d1 + d2 + d3)/ 3

print distancia_entre_3(punto1, punto2, punto3)

# Ejercicio 2

from collections import Counter

l1 = [34,31,34,77,82]
l2 = [22,101,102,101,102,525,88]
l3 = [66]
l4 = [14,14,2342,2342,2342]


def NumMasPopular(lst):
	mc = Counter(lst).most_common()	
	max_common = max(mc, key = lambda t: t[1])[1]	
	list_commons = filter(lambda x: x[1]== max_common, mc)	
	min_num_common = min(list_commons, key = lambda t: t[0])
	return min_num_common[0]

print NumMasPopular(l1)
print NumMasPopular(l2)
print NumMasPopular(l3)
print NumMasPopular(l4)

# Ejercicio 3
		
def IsCasiPalindromo(palabra):		
	reverse=palabra[::-1]		
	if  palabra == reverse:
		return True
	else:
		bad_chars = 0			
		for i, char in enumerate(palabra[:len(palabra)/2]):           
			if char != reverse[i]:				
				bad_chars += 1
				if bad_chars > 1:			
					return False		
		return True

print IsCasiPalindromo("abccba")
print IsCasiPalindromo("abccbx")
print IsCasiPalindromo("abccfg")
print IsCasiPalindromo("abcncbx")


	
