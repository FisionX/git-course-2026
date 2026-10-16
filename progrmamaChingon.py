def sumar_numeros(a, b):
    return a + b

# Solicitar datos al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Llamar a la función y guardar el resultado
resultado = sumar_numeros(num1, num2)

# Mostrar el resultado
print(f"La suma de {num1} y {num2} es: {resultado}")