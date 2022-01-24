# Funciones 

## tratare de no complicarme mucho en la aplicacion de este 
## y estara enfocado a lo que normalmente uso 

## exp, log, log10, abs 
## en el orden 
## exp ^ a, logaritmo neperiano, logaritmo en  base 10, y valor absoluto

a = 3
b = exp(a)

log(a)
log10(a)

# ahora con el dot .

B = [1, 3]

exp1= exp.(B) # recordar que no se debe usar las expresiones regulares

## round, ceil, floor

round(1.31)
ceil(1.31)
floor(1.31)
sign.([1.31, -1.31])


# Funciones vectoriales 

## maximun, minimum, findmax, findmin
v = rand(6)
maximum(v)
minimum(v)
findmax(v) # la diferencia con lo anterior es que dice la posicion del elemento 
findmin(v)
## length 

length(v)

## sort, sortrows

sort(v)
sortrows(v) # no funciona o no esta definido 


## ahora a matrices

G = rand(5, 3)

maximum(G)
maximum(G, dims = 1)

## sum prod,  cumsum cumprod 
## suma producto, suma y producto acumulado

G_sum = sum(G)
G_cunsum = cumsum(G, dims = 1)

#### 

using Statistics

promedio = mean(G, dims = 1) # en r es como el colsum

promedio = mean(G, dims = 2) # promedio por filas

desviacion = std(G)
desviacion = std(G, dims = 1)
desviacion = std(G, dims = 2)

## covarianza 

a = rand(5)
b = rand(5)
covarianza = cov(a, b)



