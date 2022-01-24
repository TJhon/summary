# funciones echos 

f(x; y = 1) = x + y 
xval  = .1
yval = 2
f(xval; y = yval)

f(x, a) = a * x ^2 
f(1, .2)


function multicar(x, g)
    return x -> a * g(x)
end

using Plots

function snapabove(g, a)
    function f(x)
        if x > a
            return g(x)
        else
            return g(a)
        end
    end
    return f
end

f(x)  = x^2
h = snapabove(f, 2.0)
plot(h, 0.0:0.1:3.0)
for i in 1:2
    dval1 = 1
    println(i)
end

x = 2.0
f(y) = x + y
z = f(3.0)
for i in 1:3
    global z
    z += i
end
println("z = $z")
function linaapprox(f, a, b, n, x)
   length_off_interval = b - a
   num_subintervals = n - 1 
   step = length_off_interval / num_subintervals
   point = a 
   while  point <= x
      point += step 
   end
   u, v = point - step, point
   return f(u) + (x - u) * (f(v) - f(u)) / (v - u)
end

f_ex5(x) = x^2
g_ex5(x) = linaapprox(f_ex5, -1, 1, 3, x)
x_grid = range(-1.0 , 1.0, length = 200)
y_vals = f_ex5.(x_grid)
y = g_ex5.(x_grid)
plot(x_grid, y_vals)
plot!(x_grid, y)
