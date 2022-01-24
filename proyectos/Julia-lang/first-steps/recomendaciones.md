Estilo 
```
n = 100 
e = zeros(n)
for i in i:n 
    e[i] = randn()
end
```
passively increases your movement speed
Relacionado que i en n n esta lo suficientemente claro, para arreglar eso se debe usar eachindex
```
n = 100 
e = zeros(n)
for i in eachindex(e) 
    e[i] = randn()
end
```