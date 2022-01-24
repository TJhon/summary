using DataFrames
df = DataFrame(
    a = 1:4, 
    B = ["M", "f", "f", "M"]
)
df

# aqui a diferencia de R se usa `.` en vez de `$`
df.a
df."a"
# todo esto es igual 

df.a == df[!, :a] == df[:, :a] == df[:, "a"] == df[!, "a"]
# call names

names(df)
propertynames(df)

df1 = DataFrame()
df.a = 1:8
df1.a = 1:8
df1.B = ["M", "F", "F", "M", "F", "M", "M", "F"]
df1

# dimencion de la base de datos

size(df1)

# agregando por filas 

df1
push!(df1, Dict(:B => "F", :a => 3))
using   CSV
CSV.write("data/01.csv", df1)

df = DataFrame(
    A = 1:2:1000,
    B = repeat(1:10, inner = 50),
    C = 1:500
)

# first y last como head y tail en R

first(df, 6)
last(df, 6)

df[1:3, :]
df[[1, 5, 10], :]
df[:, [:A, :B]]

# notar que df[!, [:A]], df[:, [:A]] son data Frames 
# df[!, :A] df[:, :A], son vectores

# seleccion de columnas con coincidencias, 

df = DataFrame(x1 = 1, x2= 2,y = 3)
df[!, r"x"] # retorna tolo que tiene x en su nombre

df[!, Not(:x1)] # es obvio


df.r = 12
df[:, All(r"x", :)] # All como si fuese everethin en r
df[:, All(Not(r"x"), :)] # los pasa al final de la columnas


# Transformacion de datos 

df = DataFrame(
    z1 = [1, 2], 
    z2 = [3, 4], 
    y = [5, 6]

)
select(df, Not(:z1))
select(df, r"z")
select(df, :z1 => :a1, :z2 => :a2) # rename
select(df, :z1, 
    :z2 => (x -> x .- minimum(x)) => :x2 #es un tanto logico aunque se complica mucho en la sintaxix
    ) 
select(
    df, :z2, :z2 => ByRow(sqrt) # hasta este momento aun se complica mucho
)
# para guardar los cambios en la base de datos original se usa select!

df
transform(
    df, All() => + # sumar todas las columnas+
)

using Random
Random.seed!(1) # semilla, para que la aelatoriedad sea la misma


df = DataFrame(rand(10, 3), [:a, :b, :c])

transform(
    df,
    AsTable(:) => ByRow(argmax) => :prediction
) # no se exactamente que hizo el comando, 
# ahora si compara por filas cual de los elementos de las filas es mayo y de acuerdo a eso imprime la columna donde este es

using   Statistics
df = DataFrame(
    x = [1, 2, missing], 
    y = [1, missing, missing]    
);
 # transform necesita una simbologia mas simple no encuentro la forma de insertar un dot.

df = DataFrame(A = 1:4, B = ["M", "F", "F", "M"])
describe(df)
iris = DataFrame(CSV.File(joinpath(dirname(pathof(DataFrames)), "../docs/src/assets/iris.csv")))