# funções anônimas (funções lambda)

# Exemplo de função explícita (tradicional)
def area_quadrado(lado):
    return  lado * lado

print(area_quadrado(5))

# Transformando em uma função anônima
area_quad = lambda lado: lado * lado
print(area_quad(4))

# outro exemplo com mais de um parâmetro
area_triangulo = lambda base, altura: (base * altura) / 2
print(area_triangulo(4,2))

print(type(area_triangulo), type(area_quad), type(area_quadrado))

# novo recurso - map - para exemplo de utilização da função lambda
triplo = lambda valor: valor * 3
lista = [1,2,3,4,5]
print(list(map(triplo, lista)))

# criando a função anônima diretamente no chamada do map
print(list(map(lambda valor: valor * 2, lista)))
# ou
print(list(map(lambda valor: valor * 2, [6,7,8,9,10])))

# atividade 04 do desafio
def area_circulo(raio, pi = 3.14159265359):
    return pi * raio**2
print(area_circulo(2))

area_circ = lambda raio, pi = 3.14159265359: pi * raio**2
print(area_circ(2))