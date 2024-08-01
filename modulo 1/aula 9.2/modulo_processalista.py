lista_teste = [0, 2, 5, 10, 15, 20, 21]

def maior_impar(lista):
    lista_impar = verificar_impar(lista)
    return max(lista_impar)

def menor_impar(lista):
    lista_impar = verificar_impar(lista)
    return min(lista_impar)

def menor_e_maior_par(lista):
    lista_par = [item for item in lista if item % 2 == 0]
    maior_e_menor = {'maior_par':max(lista_par), 'menor_par':min(lista_par)}
    return maior_e_menor

def verificar_impar(lista):
    return [item for item in lista if item % 2 != 0]

print('maior impar da lista:', maior_impar(lista_teste))
print('maior impar da lista:', menor_impar(lista_teste))
print('menor e maior par da lista:', menor_e_maior_par(lista_teste))