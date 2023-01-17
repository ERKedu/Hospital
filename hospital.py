from funciones import *
###from funciones2 import *

### Inicializamos una farmacia donde trabajar ###
farmacia = Farmacia([], [], [], [], []) 


### Bucle para el menu ###
condicion = True
while (condicion):
    print("")
    ### MENU ###
    print("[    MENU    ]")
    print("")
    print("1.- Menu pacientes")
    print("2.- Menu medico")
    print("3.- Salir")
    print("")
    ### MENU ###

    opcionMenu = input("Escribe un numero: ")

    if (opcionMenu == "1"):
        condicion2 = True
        while (condicion2):
        ### SUBMENU PACIENTE ###
            if (opcionMenu == "1"):
                print("[    MENU PACIENTES    ]")
                print("")
                print("[    PACIENTE    ]")
                print("1.- Actualizar informacion")
                print("2.- Obtener informacion")
                print("")
                print("[    HABITACION    ]")
                print("3.- Asignar paciente")
                print("4.- Liberar habitacion")
                print("5.- Verificar disponibilidad")
                print("")
                print("[    ENFERMERO    ]")
                print("6.- Asignar paciente")
                print("7.- Atender paciente")
                print("8.- Actualizar informacion")
                print("")
                print("9.- Salir")
                opcionSubmenu = input("Introduce un numero: ")

            if (opcionSubmenu == "1"):
                break
            elif (opcionSubmenu == "2"):
                break
            elif (opcionSubmenu == "3"):
                break
            elif (opcionSubmenu == "4"):
                break
            elif (opcionSubmenu == "5"):
                break
            elif (opcionSubmenu == "6"):
                break
            elif (opcionSubmenu == "7"):
                break
            elif (opcionSubmenu == "8"):
                break
            elif (opcionSubmenu == "9"):
                condicion2 = False
        ### SUBMENU PACIENTE ###

    ### SUBMENU MEDICO ###
    elif (opcionMenu == "2"):
        condicion2 = True
        while (condicion2):
            print("[    MENU MEDICO    ]")
            print("")
            print("[    MEDICO    ]")
            print("1.- Asignar paciente")
            print("2.- Atender paciente")
            print("3.- Actualizar informacion")
            print("")
            print("[    CONSULTA    ]")
            print("4.- Asignar medico")
            print("5.- Liberar consulta")
            print("")
            print("[    FARMACIA    ]")
            print("6.- Agregar medicamento")
            print("7.- ELiminar medicamento")
            print("8.- Obtener medicamento")
            print("")
            print("9.- Salir")
            opconSubmenu = input("Introduce un numero: ")
            if (opcionSubmenu == "1"):
                break
            elif (opcionSubmenu == "2"):
                break
            elif (opcionSubmenu == "3"):
                break
            elif (opcionSubmenu == "4"):
                break
            elif (opcionSubmenu == "5"):
                break
            elif (opcionSubmenu == "6"):
                break
            elif (opcionSubmenu == "7"):
                break
            elif (opcionSubmenu == "8"):
                break
            elif (opcionSubmenu == "9"):
                condicion2 =  False
    ### SUBENU MEDICO ###
    elif (opcionMenu == "3"):
        condicion =  False