# para iniciar
# si existe funciones creadas nuestra para el uso posterior o llamado de paquetes ateriore
# es facil precargalr con 

#como comentario porque no tengo la funcoininclude("moi.jl") # donde moi.jl tiene todo lo anterior mencionado

# ahora definir funciones, tener en cuenta que para este fin es para reducir trabajo o simplificar acciones repetidas

# el que todos deberian conocer 
"""
Esto se conoce como la documentacion de la funcion que estamos creando 
facil para no perderse que queremos lograr con la siguiente funcion

aqui se escribe lo que uno desee.
"""
function estadisticos(x)
   n = length(x) 
   using Statistics
   promedio = mean(x)
   sd = 12 # me olvide la funcion estadistica aqui
end

# ahora para funciones rapidas se usa 

mi_funcion(x) = 2*x - 5
mi_otra_funcion = x -> 2*x - 5 # aqui se uso con -> que significa asiganacion creo yo 

# for loops


n = 8
x = rand(n)
suma = zeros(n) # esto porque me genero erroes cuando lo deje en blanco

for i = 2:n
    suma[1] = suma[i-1] + x[1]
end

print(sumx)# lo anterior como la suma acumulada de x en el orde que establece

# mi favorito y como entedi los for loops 

clase = ["a", "b", "c"]
for i in clase
    println("curso es: $i")
end

for i = clase
    println("curos es: $i")
end # resultan en lo mismo 


#  algo mas sencillo para simplicar los for loops 


x = [3.0, 6.0, 9.0, 8.0, 3.0]
sqrx = [i^2 for i in x]

# ahora julia tienen purrr de R por defecto 

fun(x) = x^2
expt = map(fun, x)

# de la otra forma de asignar funciones 

expt = map(y -> y^2, x)

# while loops 
# probar con mas

none = 1
println(none)
while none > 0.05
    global none
    none /= 2
    return none
end # me sale un error de que delta no esta definido 
## se corrige con global para que evalue valores fuera del entorno de la funccion booleada

m = 3
n = 2
H = zeros(m,n)

for i = 1:m
    for j = 1:n 
        H[i, j] = 1/(i+j-1)
    end
end

H
# simplificas con 
H2 = zeros(m, n)
for i in 1:m, j in 1:n
    H2[i, j] = 1 / (i + j -1)
end
H2

mas = [1 / (i + j -1) for i in 1:m, j in 1:n]

# ifelse

A = rand()
if A > 0
    "break"
elseif A == 0 
    "continue"
else
    print("none")
end

# Matrices logicas  

A = [1, 4, 7, 2, 8, 5, 2, 7, 9]
B = [2, 5, 1, 4, 8, 0, 3, 4, 3]

dummy = A.>B


## lo que se usa 

## normal < > <= >= == != !
!true
# | `o` ver dadero si al menos una es verdadero
# || `o` lo anterior, no evalua la segunda si la primera condicion es verdadero 
# & `y` verdader si todos son verdaderos 
# && `y` lo anterior solo qe no evalua si una es falsa

# any vverdadero si el elemeno booleado es verdadero 
# all si todo los elementos son verdader
# isnan detecta valores NaN en una matriz 
# isempty detecta si es una matriz vacia