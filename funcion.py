def par(num, num2):
    suma = num + num2

    if suma % 2 == 0:
        return True
    else:
        return False

val = int(input("Ingresar primer número: "))
val2 = int(input("Ingresar segundo número: "))
resultado = par(val, val2)

print("¿La suma de", val, "y", val2, "es par?", resultado)