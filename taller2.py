print("Hola, Git")
x = 2 + 2
print(x)
x1 = x*2
print("A este archivo se agrega x1=", x1)
x2 = 3*(2*x1+1)
print("Se hace este cambio en esta rama x2=", x2)
x3 = x2**2+2*x1
print("Se hace este cambio para subir a Github: x3 =", x3)
prom = (x1+x2+x3)/3
print(f"Se modifica el archivo por el compañero en una rama. El promedio = {prom}")