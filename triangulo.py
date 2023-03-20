lado1 = float(input("Digite a 1º lado: "))
lado2 = float(input("Digite a 2º lado: "))
lado3 = float(input("Digite a 3º lado: "))

if lado1 == lado2 and lado2 == lado3:
    print(f"Triangulo equilátero")

elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
     print(f"Triangulo escaleno")

else:
    print(f"Triangulo isosceles")



