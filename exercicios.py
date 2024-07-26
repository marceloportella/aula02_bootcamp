import math
#numero01 =int(input("Digite o segundo numero "))
#numero02=int(input("Digite o segundo numero "))
#resultado = numero01 // numero02 # // divisao inteira

#print(resultado)


# raio = float(input("Digite o raio : "))
# area = math.pi * raio ** 2

# print (area)

#Datas separadas

# input("Insira uma data no formato dd/mm/aaaa: ")
data_user = "26/07/2024"
data_separate = data_user.split("/") 
print(data_separate) # Transforma em lista de elementos
print(f"O elemento 1 é o : {data_separate[1]}")