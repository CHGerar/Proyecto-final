import random
import time

def mostrar_menu():
    print("Bienvenido a Forza Horizon 8  ")
    print("1 Elige tu auto y compite")
    print("2 Ver historial de carreras")
    print("3 Salir del juego")

def elegir_auto():
    autos = ["GTR35", "Honda NSX", "Toyota Supra", "Mazda rx7", "Nissan Godzilla"]
    
    print("Autos disponibles:")
    for i, auto in enumerate(autos, 1):
        print(f"{i}. {auto}")
    
    while True:
        try:
            eleccion = int(input(" Elige tu auto (1-5): "))
            if 1 <= eleccion <= 5:
                print(f"elegiste un {autos[eleccion - 1]}")
                return autos[eleccion - 1]
            else:
                print(" Por favor, elige un número válido entre 1 y 5.")
        except ValueError:
            print(" no válido intenta con un número.")

import random
import time

def simular_carrera(auto_usuario):
    autos = ["GTR35", "Honda NSX", "Toyota Supra", "Mazda rx7", "Nissan Godzilla"]
    velocidades = {auto: random.randint(200, 350) for auto in autos}

    print("Arranca la carrera")
    time.sleep(1)

    for auto, velocidad in velocidades.items():
        print(f"{auto} corre a {velocidad} km/h...")
        time.sleep(1)

    ganador = max(velocidades, key=velocidades.get)

    print("\nResultados finales\n")
    time.sleep(1)

    mensaje = (f" Ganaste con tu {auto_usuario} a {velocidades[auto_usuario]} km/h"
            if auto_usuario == ganador else
            f"Lo siento, el {ganador} ganó con {velocidades[ganador]} km/h. "
            f"Tu {auto_usuario} alcanzó {velocidades[auto_usuario]} km/h.")

    print(mensaje)
    return auto_usuario, velocidades[auto_usuario], ganador, velocidades[ganador]


def main():
    historial = []

    while True:
        mostrar_menu()
        opcion = input(" Elige una opción: ")

        if opcion == "1":
            auto_usuario = elegir_auto()
            resultado = simular_carrera(auto_usuario)
            historial.append(resultado)
        elif opcion == "2":
            if not historial:
                print(" No hay historial de carreras aún. ¡Compite para generar uno!")
            else:
                print(" Historial de carreras:")
                for i, (auto_usuario, velocidad_usuario, auto_ganador, velocidad_ganador) in enumerate(historial, 1):
                    print(f" Carrera {i}: Tú con {auto_usuario} a {velocidad_usuario} km/h | "
                        f"Ganador: {auto_ganador} a {velocidad_ganador} km/h")
        elif opcion == "3":
            print(" Gracias por jugar Nos vemos")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
