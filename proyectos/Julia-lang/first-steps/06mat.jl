using Calculus
using Plots
# A 
# # V+1 = "mostasa"
#     I-2 = "blanco"
# B 
#     V-2 = "rosado"
#     I = 'Verde"

## A53 B48 A56 B53 
## A54 B46 A54 B53 
## A53 B46 A54 B51 
##  

fxy(x) = x[1] * exp(-x[1]^2 - x[2]^2)
fc = fxy([1, 1])
df = Calculus.gradient(fxy, [1, 1])
fx = df[1]
fy = df[2]
fxyapox(x) = fc - fx - fy + fx*x[1] + fy*x[2]
x = collect(range(.5, stop = 1.5, step = .1))
n = length(x)
forig = faprox = X = zeros(n, n)

for i in 1:n, j in 1:n
    forig[i, j] = fxy([x[i], x[j]])
    faprox[i, j] = fxyapox([x[i], x[j]])
    X[i, j] = x[j]
end

plot(
    x, x, forig, 
    st = :surface
)

plot(x, x, forig, st=:surface, legend=false, color=cgrad([:red,:blue]), grid = true)
plot(x, x, faprox, st=:surface, legend=false, color=cgrad([:red,:blue]), grid = true)

function courtno(q, c, eta)
   neq = length(q) 
   fval = zeros(neq, 1)
   q1 = q[1]
   q2 = q[2]
   c1 = c[1]
   c2 = c[2]
  for i in 1:2
    fval[i] = (q1 - q2) ^(-1/eta) - (1/eta)*((q1 + q2) ^(-1/eta - 1)) * q[i] - c[i]*q[i]
  end 
end

