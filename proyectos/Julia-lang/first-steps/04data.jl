# leer datos es simple es basicamente lo mismo que en otros lenguajes de programacion, donde lo unico que tienes que poner es el path del archivo. 

# los paquetes necesarios son 
# DelimitedFiles ExcelReaders # para csv text y excel 

# para trabajar con series temporales sin agrupar observaciones 
# no es tan simple por el momento, espero encontrar una libreria que me ayude

# primero definir la cantidad de observaciones temporales 

t = length(datos)

# ahora para ver el crecimiento economico  
g0 = datos[2:t, 1] - datos[1:t - 1, 1] # esto se refiere a la diff en R pero con la extraccion de l la primera columna aunque pueda ser redundante puede generar errore, no lo probe aun 

g1 = datos[1:t - 1, 1] # el componente de ahora 

# ahora para saber la tasa de crecimiento, dividir, pero 
# pero no se puede hacer facilmente sin el tupple dot 

g = g0 ./ g1 

# ahora se puede graficar, pero recordar que se perdio una observacion del tiempo asi que ahora es:
 

graf = plot(
    tiempo[2:t], g, 
    grid = true # todo lo demas es estilizacion
)

# como g es un vector se puede hacer las operaciones matematicas 

## para salvar informacion e espacio, es como el saveRds 


save("ubicacionynombre.jld", "nombre del elemento[i]", elemento-objeto[i] ) # la i asemeja a todo lo que uno quiera guardar

# se lee la data con 
using JLD 

d = load("jld") # ahora todo el entorno de trabajo gurdado esta en d

# para llamar elementos dentro de este solo se llama con

elemento = d["nombre del elemento[1]"]

# ahora esto se puede ordenar mas rapido !

# el modelo insumo producto se puede usar