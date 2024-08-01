# forma aprendida
dict_todos = {}
for i in range(1,11):
    dict_todos[i] = i**2
print('Todos numeros:', dict_todos)

# nova forma
dict_todos = {item: item**2 for item in range(1, 11)}
print('Todos numeros:', dict_todos)

# Com estrutura de condição na forma anterior
dict_impares = {}
for i in range(1, 11):
    if i % 2 != 0:
        dict_impares[i] = i**2
print('numeros impares:', dict_impares)

# nova forma
dict_impares = {item: item**2 for item in range(1,11) if item % 2 != 0}
print('numeros impares:', dict_impares)

# atividade 02 do desafio:
nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']

qtd_letras = {nome: len(nome) for nome in nomes}
print(qtd_letras)