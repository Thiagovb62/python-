#conjunto = {1,2,3,4,5}
#conjunto2={5,6,7,8,9}
#conjunto_un = conjunto.union(conjunto2)
#conjunto.add(5)
#conjunto.discard(2)
#print(conjunto_un)
#conjunto_inter=conjunto.intersection(conjunto2)
#print(conjunto_inter)
#conjunto_dif=conjunto.difference(conjunto2)
#print(conjunto_dif)#imprimir as difreças entre os dois conjuntos nesse caso 2 e 1
#conjunyo_diff_sime = conjunto.symetric_diferrence(conjunto2)#a diferença simetrica entre os dois ao mesmo tempo


conjunto_a={1,2,3}
conjunto_b={1,2,3,4,5}
conjunto_subset=conjunto_b.issubset(conjunto_a)#se o conjunto b esta  no a
print('{}'.format(conjunto_subset))
conjunto_superset=conjunto_b.issuperset(conjunto_a)#se pelo menos todo o conjunto a esta em b
print('{}'.format(conjunto_superset))


lista = ['cachorro','gato', 'elefante',]
conjunto_animais = set(lista)#converter pra conjunto
lista_animais= lista(conjunto_animais)
