import sys

def saludar():
    print("----------------------------------------")
    print("¡Hola desde el pipeline de GitHub Actions!")
    print(f"Versión de Python ejecutándose: {sys.version}")
    print("----------------------------------------")

if __name__ == "__main__":
    saludar()
