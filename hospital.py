### Inicializamos una farmacia donde trabajar ###
farmacia = Farmacia([], [], [], [], []) 

import funciones
import funciones2

### Bucle para el menu ###
condicion = True
while (condicion):
    print("")
        ### MENU ###
    print("[    MENU    ]")
    print("")
    print("1.- Menu medicos")
    print("2.- Menu pacientes")
    print("")
    print("[    MENU    ]")

    opcionMenu = input("Escribe un numero: ")
    ### MENU ###
    ### SUBMENU PACIENTE ###
    if (opcionMenu == 1):
        print("[    MENU PACIENTES    ]")
        print("")
        print("1.- ")
        print("2.- ")
        print("")
        print("[    MENU PACIENTES    ]")
    ### SUBMENU PACIENTE ###

    ### SUBMENU MEDICO ###
    elif (opcionMenu == 2):
        print("[    MENU MEDICO    ]")
        print("")
        print("1.- ")
        print("2.- ")
        print("")
        print("[    MENU MEDICO    ]")
    ### SUBMENU MEDICO ###



