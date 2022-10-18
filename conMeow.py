i=2
x=int(input(" ingrese final columna = "))
y=x+1

for i in range(y):
    a=(f"=CONCATENAR(TRANSPONER(E{i}:F{i}))")
    print(a)
    if i == x:
        break