# los programas inteligentes usan boleanos para tomar decisiones sobre si ejecutar lineas de codigo u omitirlas

activo = False

if activo == False:
    print("el usuario esta activo") 
    activo = True

cargado =  True
if cargado : 
    print("el cargador esata cargando")
else:
    print ("Conecte el celular")

nota = 80
if nota <= 80:
    print("pasaste")
else:
    print("no pasaste")

porcentaje = 65

if porcentaje > 75:
    print("pasaste")
elif porcentaje < 80 :
    print("reprobado")
else:
    print ("gano, fin")
