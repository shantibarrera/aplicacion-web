from math import sqrt

k = 9 * 10**9

def ingresar_carga(nombre_carga):
    # Pedir el signo y el valor de la carga
    valor_carga = float(input(f"Ingrese el valor de la {nombre_carga} carga (ej. -6.5 para -6.5 C): "))
    # Pedir la potencia de 10
    potencia = float(input(f"Ingrese la potencia de 10 para la {nombre_carga} carga (ej. -6 para 10^-6): "))
    return valor_carga * 10**potencia

def formato_cientifico(valor):
    # Convertir el valor a notación científica y formatearlo como "a x 10^b"
    a, b = f"{valor:.1e}".split("e")
    b = int(b)  # Convertir el exponente a entero
    return f"{a} x 10^{b}"

def calcular_fuerza():
    print("\n--- Calcular la fuerza entre dos cargas ---")
    carga1 = ingresar_carga("primera")
    carga2 = ingresar_carga("segunda")
    distancia = float(input("Ingrese la distancia entre las cargas (m): "))
    fuerza = (k * carga1 * carga2) / distancia**2
    print(f"La fuerza entre las cargas es: {formato_cientifico(abs(fuerza))} N\n")

def calcular_distancia():
    print("\n--- Calcular la distancia entre dos cargas ---")
    carga1 = ingresar_carga("primera")
    carga2 = ingresar_carga("segunda")
    fuerza = float(input("Ingrese la fuerza entre las cargas (N): "))
    distancia = sqrt((k * carga1 * carga2) / fuerza)
    print(f"La distancia entre las cargas es: {formato_cientifico(distancia)} m\n")

def calcular_valor_carga():
    print("\n--- Calcular el valor de una carga ---")
    carga1 = ingresar_carga("primera")
    fuerza = float(input("Ingrese la fuerza entre las cargas (N): "))
    distancia = float(input("Ingrese la distancia entre las cargas (m): "))
    carga2 = (fuerza * distancia**2) / (k * carga1)
    print(f"El valor de la segunda carga es: {formato_cientifico(carga2)} C\n")

def main():
    while True:
        print("BIENVENIDO A LA CALCULADORA DE COULOMB")
        print("1. Calcular la fuerza entre dos cargas.")
        print("2. Calcular la distancia entre dos cargas.")
        print("3. Calcular el valor de una carga.")
        print("4. Salir.")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            calcular_fuerza()
        elif opcion == 2:
            calcular_distancia()
        elif opcion == 3:
            calcular_valor_carga()
        elif opcion == 4:
            print("Gracias por usar la calculadora de Coulomb. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()