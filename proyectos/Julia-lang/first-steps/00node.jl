# Motivacion

# Demanada q = .5^{-0.2} + .5p^{-.5}
## Funcion inversa de la demanda

p = 0.25
for i in 1:100
  deltap = (.5*p^-.2+.5*p^-.5-2)/(.1*p^-1.2 + .25*p^-1.5)
  p = p + deltap
  if abs(deltap) < 1.e-8
        break
  end
end 
println(p)

q = collect(0.5:0.1:2.2)
P = zeros(length(q))
for j=1:length(q)
    p = 0.25
    for i=1:100
        deltap = (.5*p^-.2+.5*p^-.5-q[j])/(.1*p^-1.2 + .25*p^-1.5)
        p = p + deltap
        if abs(deltap) < 1.e-8
            break
        end
    end 
    P[j] = p
end;

M = [q P]

using VegaLite