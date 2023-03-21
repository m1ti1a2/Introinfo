
# son 4 tipos de variables
# Cadena

nombre  =  "Cristóbal"
apellido  =  "Murillo"

# entero
identificación  =  113990099

# Flotar
efectivo  =  10.5

#Bool

activo  =  True


# Comparaciones de las variables
# Como verificar si el PIN ingresado por un usuario coincide con su PIN guardado

pin_entrado  =  5448
pin_esperado  =  5448

resultado  =  pin_entrado  ==  pin_esperado

print ( resultado )

# Comparaciones con desigualdad. Tenemos que usar el operador !=

resultado_1  =  2  !=  2
print ( resultado_1 )

uno  =  1
dos  =  ( "------------------------------" )
print ( uno  ==  dos )
print ( uno  !=  dos )


# Vamos a hacer un interruptor de luz inteligente que apague las luces si es de dia y las encienda si es de noche
print ( "------------------------------" )
es_dia  =  False
luces_encendidas  =  True 

print ("¿Durante el día?" )
print ( es_dia )

print ( "¿Luces encendidas?" )
print ( luces_encendidas )

# Con las comparaciones vamos a hacer un código que rastree los datos de ventas de una tienda de pantalones
print ( "------------------------------" )

existencias  =  600
vaqueros_vendidos  =  500
objetivo  =  500

target_hit  =  vaqueros_vendidos  ==  objetivo
print ( "Alcanzar el objetivo de venta de jeans: " )
print ( objetivo )

stock_actual  =  existencias  -  vaqueros_vendidos
en_existencias  =  existencias  !=  0
print ( "Jeans  " )
print ( existencias )
print ( stock_actual )


# Podemos usar comparaciones para verificar si un número es mayor o menor que otro número

print ( "------------------------------" )

print ( 2  <  200 )
print ( 2  >  200 )

print ( 201  <=  200 )
print ( 2  >=  200 )

print ( "------------------------------" )

# Comparaciones de cadenas de texto

mi_respuesta  =  "bajo"
solución  =  "bajo"

print ( mi_respuesta  ==  solución )
print ( mi_respuesta  !=  solución )

# practica: paciente que tiene frecuencia cardiaca y que si es preocupante

heart_rate = 77

too_low = heart_rate < 60
too_hight = heart_rate < 100

print("Heart rate low?")
print(too_low)

print("heart_rate hight?")
print(too_hight)

# combinaciones de suma o igual resta 

numero = 30
numero_2 = 10 
result = numero + numero_2
print(result)

#  la edad mayor de alguien

number = 25
edad = number  >= 18
print("mayor de edad")
print(edad)

# usemos comparaciones de string para etiquetar los datos adquiridos a a traves de la encuesta de usuarios de una aplicacion fitness
# verificamos las repuestas de la encuesta de los usuarios en respecto a la frecuecia e intensidad de la actividad, las etiquetiremos y mostraremos los resultados  

frecuencia = "una vez la semana" 
intensidad =  "baja"

activo = frecuencia == "diaria"

print("el usuario es activo?")
print(activo)

intenso = intensidad == "alta"
print("el usuario es intenso?")
print(intenso)

# poner un numero de whatsapp para un enlace que nos lleve a una pagina

numero_cualquiera = 8438-4857

print(numero_cualquiera)
print(f"https://wa.me/5068438-4857")


# practica, ejercicio 1, ejercicio 2, ejercicio 3

# ejercicio 1


Nombres= 3 
name3= "santi"  
name2= "b"
name1= "Mati"
print(name2)
print(name3) 
print(name1)
print(Nombres)
print( "Mati" +  "b" + "santi" )
input( Nombres ) 




