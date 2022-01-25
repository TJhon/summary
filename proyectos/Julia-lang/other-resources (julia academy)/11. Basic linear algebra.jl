A = rand(1:4,3,3)

x = fill(1.0, (3,)) # = fill(1.0, 3)

b = A*x

A'

transpose(A)

A'A

A\b

Atall = rand(3, 2)

Atall\b

v = rand(3)
rankdef = hcat(v, v)

rankdef\b

bshort = rand(2)
Ashort = rand(2, 3)

Ashort\bshort

v = [1,2,3]



@assert dot_v == 14



@assert outer_v == [1 2 3
                    2 4 6
                    3 6 9]

@assert cross_v == [0, 0, 0]
