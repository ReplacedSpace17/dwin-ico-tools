# Autor original: https://github.com/b-pub/dwin-ico-tools

# Esta versión es una versión modificada de la propuesta pór el autor original, mismo que se hace referencia más arriba.
# GitHub: ReplacedSpace17

from splitIco import SplitIco
from makeIco import MakeIco

opcion=0
def info():
    print("\nMakeIco te ayudará a generar un archivo .ico a partir de una carpeta con .jpg\nSplitIco te ayudará a descomprimir un archivo .ico en una carpeta con .jpg")


def menu():
    info()
    print("\nBienvenid@ ingresa el numero correspondiente a una  opción: \n\nSplitIco(1)\nMakeIco (2)\nSalir(3)")
    opcion= input()
    opcion=int(opcion)

    split = SplitIco()
    make = MakeIco()

    match opcion:
        case 1:
           print("Ingresa el nombre de tu archivo .ICO sin la extensión (.ICO). ")
           archivo= input()
           archivo=archivo+".ICO"
           print("Ingresa el nombre como se llamará la carpeta de destino(NO HACE FALTA CREARLA): ")
           destino= input()

           split.init(archivo, destino)
            

        case 2:
           print("Ingresa el nombre de tu carpeta que contiene los iconos: ")
           carpeta= input()
    
           print("¿Cómo se llamará tu archivo .ICO?")
           archivo= input()
           archivo=archivo+".ICO"
           make.init(archivo, carpeta)


        case 3:
            print("")
        case _:
            print("\n\nPor favor ingresa un numero del 1 al 3...")
    return opcion
    

if __name__ == '__main__':
    do = True

while do:
    opcion=menu()
    if opcion == 3:
        do = False


