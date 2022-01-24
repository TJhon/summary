# variables 
"string"
x = 12; y = 20
"string, referencia a x  = $x, y = $y"
## trabajando con string


s = "charlie don't surf"
split(s)
replace(s, "surf" => "none")

strip("   none   ") # elimina espacios innecesarios
match(r"(\d+)","Top 10")

## tuple , inumtable 

x = ("foor", "bar")

x = [10,20, 30, 40]
x[end]
x[end-1]
x[1:3]
"foobar"[3:end]

## diccionarios mutable
### loops 

for i in 1:3
    print(i)
end
## collect tambien arregla listas, es una funcion muy util
a = 1:5
for x in eachindex(a)
    println(a[x] * a[x])
end

## ziop, usado para hacer pasos consecutivos

paises = ("japor","korea", "china")
ciudades = ("tokyo", "seoul", "beijing")

for (paises, ciudades) in zip(paises, ciudades)
    println("la capital de $paises es $ciudades")
end

xs = 1:10000
f(x) = x^2
f_x = f.(x)
f_x2 = [f(x) for x in xs]
@show sum(f_x2)

x  = 1.0:1.0:5.0
y = [2.0, 4.0, 5.0, 6.0, 8.0]
z = similar(y)
z .= x .+ y .- sin.(x)
@. z = x + y - sin(x)
f(a, b) = a + b
a = [1 2 3]
b = [4 5 6]
@show f.(a, b)  
f.(a, b)


using  Plots
n = 100
f(x) = x ^ 2
x = randn(n)
plot(f.(x), label = "x2")
plot!(x, label = "x")
using Distributions
function histo(distri, n)
    e = rand(distri, n)
    histogram(e)
end
# 
lp = Laplace() # distribucion de laplace

histo(lp, 599)

function punto(f, iv, torance, maxiter)
    # algoritmo
    x = iv
    normdiff = Inf
    iter= 1
    while normdiff > torance && iter <= maxiter
        x_new = f(x)
        normdiff = norm(x_new - x)
        x = x_new
        iter = iter + 1
    end
    return(x, normdiff, iter)
end

p = 1.0
b = 0.9
f(v) = p + b*v
sol = punto(f, iv = 0.8, torance = 1.0E-8)


using Plots
gr(fmt = :png)
a = .9; n = 200; x = zeros(n + 1)
for t in 1:n
    x[t+1] = a * x[t] + randn()
end
plot(x)

αs = [0.0, 0.8, 0.98]
n = 200
p = plot() # naming a plot to add to
for α in αs
    x = zeros(n + 1)
    x[1] = 0.0
    for t in 1:n
        x[t+1] = α * x[t] + randn()
    end
    plot!(p, x, label = "alpha = $α") # add to plot p
end
p # display pl
