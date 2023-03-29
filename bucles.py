# # # un bucle while repite su bucle de codigo mientras su rol es True
# # # crear una variable que detenga el bucle llamado control

control = True
while control == True:
    print("hola mundo")

    control = False

    print("se mostro una vez")

# Hacer el contador

contador = 1 

while contador < 10:
    print(contador)
    contador += 1 

# calculo de interes compuesto

cuenta = 1000

interes = 0.11

annos = 3

print("monto de inicio", cuenta)

contador = 1 

while contador<= annos:
    interes_compuesto= cuenta * interes
    cuenta += interes_compuesto
    print("ANO: ",contador,":",cuenta)
    contador += 1

# mate

n1 = 12
n2 = 14

suma = n1 + n2

print(suma)