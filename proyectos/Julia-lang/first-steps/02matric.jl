# matrices en Julia 
# por el momento voy bien aun no cometo tantos erroes


# para crear matrices es simple como dejar un espacio y luego insertar un punto y coma para separar la fila

MOI = [1 2 3; 3 33 3; 12 12 12]

MOI'

# ahora entiendo por que no se permite '' estas comillas para crear string, ya que esta reservado para el uso de la transpuesta de la matriz

# para crear elementos y ahorrar espacio es tan facil como comas entre las variables las cuales se quiere asignar valores entre ellos un igual 

size(MOI) # este para saber las dimenciones

fila, columna = size(MOI)
fila
columna


## secuencias de elementos ordenados, por lo general no se puede cambiar el valor de los elementos dentro de este.


1:21 # por defecto de un en uno # para convertirlo en un arreglo modificable se usa collect(1:21)
a = collect(1:21)

a[21] = 12# se modifico !


b = 1:2:21
b |> collect
## Otra manera usar range, que en `R` es la funcion seq, solo que tiene mas caracteristicas

c = range(1, stop = 39, step = .2) # interesante para crear graficos con funciones
c |> collect

# Matrices especiales 
# aunque no se donde escuche o vi que la creacion de estas no tienen sentido

moi1 = zeros(3, 4) # siempre filas con columnas
moi2 = ones(3, 4)
moi3 = Matrix{Float64}(I, 2, 2) # no entiendo muy bien el significado de Float64, pero puedo asegurar que la `I` es la matriz identica, reservada osea que puedo probar si me genera error lo siguiente.

I = 12#nop pero, inmediatamente me salio un aviso de que hubo un crash
# abstenerme de usar esta variables

# valores aelatoris

y = rand(12, 2) # valores aelatorios, el primero para saber cuantos elementos crear, y el segundo como las columnas, 
# LOL recordar el orden de filas y columnas 

## algo muy curioso para generar valores de una distribusion tiene una sintaxis diferente a varios lenguajes de programacion 

moi4 = rand(12, 1) # Este significa que genera valores aelatorios de media 0 y sigma 1 es decir 0 + 1 * rand(12, 1)

# moi hace mas ejemplos 

## para una distribucion normal con media 3 y desviacion estandar de .4 
## recordar respetar la generacion de elementos coherentemente
moi5 = 3 * ones(3, 3) + .4*rand(3, 3)

## para hacer una distribucion uniforme en intervalos [a, b], se usa la siguiente forma: a + (b - a) * rand(y, x)

moi6 = 2*ones(2, 2) + (4 - 2)*rand(2, 2)


# Operaciones con matrices 
## lo de siempre de otros lenguajes de programacion senalare los que tienen una forma especial 

a = [1 2 3; 3 4 4; 8 9 00]

a*a == a^2 ## es lo mismo ahora la transpuesta tambien es con transpose

## inversa con inv(matrix)
inv(a)
## division izquierda `\` 

12 \ 2 # es como 2 entre 12


## ahora aparece un error mio  en el entendimiento el uso del .dot 
## hace que cada elemento se multiplique por el elemento que ocupe su misma posicion, pero no hace cumplir la regla de multiplicacion de matrices

## moi lo admite

a.^2 # esto es la multiplicacion filas por columnas
a.^2 == a*a
a.^2 == a.*a

# todo lo anterior para cumplir con esta regla debe ir antes un .

# Extraccion 


a
a[1, ] # no es como otros lenguajes que te recoje todos los elemento de la columna 1
# en julia es asi 
a[1, :] # con `:`

# si hay procesos en la extraccion de elementos, se puede hacer con vectores creados anteriormente


## concatenar matrices 

A = rand(3, 2); B  = rand(3, 2) # se pone coma al final porque no se quiere que se muestre lo que tiene dentro de las matrices

#juntar 
C = [A; B];

C # juntar por filas
# lo anterior resulta en una matriz 
#Ahora concatenar con la transpuesta

C1 = [A'B] # ahora juntar por columnas sea como cbind

