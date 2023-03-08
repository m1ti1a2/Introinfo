
# son 4 tipos de variables
# Cadena

nombre  =  "Cristóbal"
apellido  =  "Murillo"

# entero
identificación  =  113990099

# Flotar
efectivo  =  10.5

#Bool

activo  =  Verdadero

# Comparaciones de las variables
# Como verificar si el PIN ingresado por un usuario coincide con su PIN guardado

pin_entrado  =  5448
pin_esperado  =  5448

resultado  =  pin_entrado  ==  pin_esperado

imprimir ( resultado )

# Comparaciones con desigualdad. Tenemos que usar el operador !=

resultado_1  =  2  !=  2
imprimir ( resultado_1 )

uno  =  1
dos  =  2
imprimir ( "------------------------------" )
imprimir ( uno  ==  dos )
imprimir ( uno  ! =  dos )


# Vamos a hacer un interruptor de luz inteligente que apague las luces si es de dia y las encienda si es de noche
imprimir ( "------------------------------" )
es_dia  =  Falso
luces_encendidas  =  no_es_día

imprimir ("¿Durante el día?" )
imprimir ( es_dia )

imprimir ( "¿Luces encendidas?" )
imprimir ( luces_encendidas )

# Con las comparaciones vamos a hacer un código que rastree los datos de ventas de una tienda de pantalones
imprimir ( "------------------------------" )

existencias  =  600
vaqueros_vendidos  =  500
objetivo  =  500

target_hit  =  jeans_sold  ==  objetivo
print ( "Alcanzar el objetivo de venta de jeans: " )
imprimir ( objetivo_hit )

stock_actual  =  stock  -  vaqueros_vendidos
en_existencias  =  existencias_actuales  !=  0
print ( "Jeans en stock: " )
imprimir ( en_stock )
imprimir ( stock_actual )


# Podemos usar comparaciones para verificar si un número es mayor o menor que otro número

imprimir ( "------------------------------" )

imprimir ( 2  <  200 )
imprimir ( 2  >  200 )

imprimir ( 201  <=  200 )
imprimir ( 2  >=  200 )

imprimir ( "------------------------------" )

# Comparaciones de cadenas de texto

mi_respuesta  =  "bajo"
solución  =  "bajo"

imprimir ( mi_respuesta  ==  solución )
imprimir ( mi_respuesta  !=  solución )

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

