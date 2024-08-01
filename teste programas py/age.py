# Programa que encontra o maior valor de uma lista

# ages = [18, 20, 45, 14, 27, 60]
# bigger_age = 0

# for age in ages:
#     for i in range(len(ages)):
#         if age > ages[i] and age > bigger_age:
#             bigger_age = age

# print(bigger_age)

# Programa aprimorado que pede os inputs do tamanho da lista e seus valores

ages = []
list_size = int(input('Digite a quantidade de idades que deseja comparar: '))

for i in range(list_size):
    valor = int(input('Digite o valor: '))
    ages.append(valor)

bigger_age = 0

for age in ages:
    for i in range(len(ages)):
        if age > ages[i] and age > bigger_age:
            bigger_age = age

print(bigger_age)
