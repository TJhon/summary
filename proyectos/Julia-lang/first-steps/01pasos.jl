# Primeros paso con Julia

pwd() # usar para sever el directorio actual 
cd() # establecer el directorioe

using Statistics


mean(1:20)
mean([1, missing, 20]) # mising es `NAsee`
mean(skipmissing([1, missing, 20])) # skipmissing es rm.na = T
# aunque este ultimo seria mejor si tuviese dentro de la funcion base

# variables

x = 23
# reconoce tamnbien complejos
α = 12

# String 

Y_1 = "moi"
parrafo = """
Este es un texto muy grande el cual deberia ser aceptado por Julia
probar la sintaxis siempre es bueno
ahora ver.
"""

# lo basico se hace con suma resta etc, 

## los caracteres no tan convencionales son:

# %  el cual muestra el residuo ideal para trabajar con series de tiempo

4 % 3 

# * la operacion es facil de enteder si se uso python es como el modulo + que sirve para concatenar String

"texto1" * "texto2"

# estructura de datos 
## con lo siguiente me puedo confundir mi ingles no es tan bueno

## tuplas: son secuencias ordenadas de elementos es como `factor`, 
## diccionarios: list 
## arreglos: los basicos dataframes

## tuplas con () y los elementos dentro de ellos no se pueden reasignar 

mitup = (1, 2, 3 ,4, "moi")

typeof(mitup)

# se puede extraer elemetos 
mitup[5]



## diccionarios usados como `=>`


notas = Dict(
"primer" => 12, 
"segundo" => 13
)

notas[2] # no funciona con el numero de elemento 
notas["segundo1"]

# para eliminar entradas en el diccionario usar pop!(variable, "dentro"1)
pop!(notas, "primer")
notas # bam se fue

# arreglos o arrays, vectores

elementos  = [
    "nombre", 
    1, 
    "nadie"
]
elementos

# al igual que en otros lengujes el uso es comun en []
# agregar elementos con push 

push!(elementos, 21)
pop!(elementos) # los elementos eliminados van desde el ultimo al Primero

# lo curioso de Julia `=`
# este significa que los cambios dentro de la variable se cambia tambien en la otra variables

x = 1:12 # esto no se puede editar los elemetos
x = [1, 2, 4, 4 , 0]
y = x
y[1] = 12
x
# usar copy()
y = copy(x)

# para definir dentro de una variable la cual hace valor de esta 
# es la asignacion de variable y prinln


moi = 1
println("referenciar a moi con $moi")

## grafico intuitivos 
## llamar a una libreria descargada 
## el problema, bueno en realidad no ha problema, cuando uno inicia en JUlia espera que sea rapido, por ser nativos de R Python ya que estos grafican rapido y llaman a las librerias rapido, en Julia tambien es asi solo que uno se debe acostumbrar a estar probando a cada rato para la flexivbiilidad de Julia
# al principio se demorara mucho pero poco a poco se vuelve mas rapido
using Plots

x = collect(0:pi/100:2*pi) # juntar por filas # juntar por filas
y = sin.(x) # aqui el punto sirve para evitar el error dot not include

grafico = plot(
    x, y,
    xlabel = "x", 
    ylabel = "f(x)", 
    title = "seno", 
    color = "red", 
    legend = false, 
    linewith = 2,  # juntar por filaslasatal7774575x 
    grid = true
)
x = range(-2 * pi, stop = 2 * pi, length = 50)
y1 = sin.(x)
y2 = cos.(x)

grafico2 = plot(
    x, 
    [y1, y2], # esto para determinar varios datos como excel
    color = [
        "red", "blue"
    ], 
    legend = true, 
    linewith = 2, 
    grid = true
)
# todo lo anterior por defecto una linea 
# ahora a modificar eso 


modi_gra = plot(
    x, 
    [y1, y2], 
    shape = [:circle :diamond], 
    line = [:dot :dash], 
    grid = true
)
# para guardar graficos esta funcion esta presente en casi todas las librerias de graficadoras, 
# savefig(nombre_guardado, "myplot")
savefig(modi_gra, "fig/ test.pdf")