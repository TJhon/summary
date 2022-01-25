using LinearAlgebra
A = rand(3, 3)
x = fill(1, (3,))
b = A * x

Alu = lu(A)

typeof(Alu)

Alu.P

Alu.L

Alu.U

A\b

Alu\b

det(A) ≈ det(Alu)

Aqr = qr(A)

Aqr.Q

Aqr.R

Asym = A + A'
AsymEig = eigen(Asym)

AsymEig.values

AsymEig.vectors

inv(AsymEig)*Asym

n = 1000
A = randn(n,n);

Asym = A + A'
issymmetric(Asym)

Asym_noisy = copy(Asym)
Asym_noisy[1,2] += 5eps()

issymmetric(Asym_noisy)

Asym_explicit = Symmetric(Asym_noisy);

@time eigvals(Asym);

@time eigvals(Asym_noisy);

@time eigvals(Asym_explicit);

n = 1_000_000;
A = SymTridiagonal(randn(n), randn(n-1));
@time eigmax(A)

1//2

Arational = Matrix{Rational{BigInt}}(rand(1:10, 3, 3))/10

x = fill(1, 3)
b = Arational*x

Arational\b

lu(Arational)

using LinearAlgebra

@assert A_eigv ==  [-128.49322764802145, -55.887784553056875, 42.7521672793189, 87.16111477514521, 542.4677301466143]

@assert A_diag ==  [-128.493    0.0      0.0      0.0       0.0;
    0.0    -55.8878   0.0      0.0       0.0;
    0.0      0.0     42.7522   0.0       0.0;
    0.0      0.0      0.0     87.1611    0.0;
    0.0 0.0      0.0      0.0     542.468]
# #### 11.3
# Create a `LowerTriangular` matrix from `A` and store it in `A_lowertri`
@assert A_lowertri ==  [140    0    0    0   0;
  97  106    0    0   0;
  74   89  152    0   0;
 168  131  144   54   0;
 131   36   71  142  36]
