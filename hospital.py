from funciones import *
from funciones2 import *
import time

### Inicializamos una farmacia ###
hospital = Hospital([], [], [], [], []) 

### Creamos las habitaciones y las añadimos a la lista ###
disponibilidad = True
habitacion1 = Habitacion("1", "Publica", [], disponibilidad)
habitacion2 = Habitacion("2", "Publica", [], disponibilidad)
hospital.listaHabitaciones.append(habitacion1)
hospital.listaHabitaciones.append(habitacion2)


### Creamos los pacientes y los añadimos a la lista de pacientes de la farmacia ###
paciente1 = Paciente("1", "1", "1", "1", "1", [])
paciente2 = Paciente("2", "2", "2", "2", "2", [])

hospital.listaPacientes.append(paciente1)
hospital.listaPacientes.append(paciente2)

### Creamos los medicos y los añadimos a la lista de medicos del hosptial ###
medico1 = Medico("1", "1", "1", "1", "1", "1", [], "1")
medico2 = Medico("2", "2", "2", "2", "2", "2", [], "2")
hospital.listaMedicos.append(medico1)
hospital.listaMedicos.append(medico2)

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

    ### SUBMENU PACIENTE ###
    if (opcionMenu == "1"):

        condicion2 = True
        while (condicion2):
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

            ### Actualizar informacion ###
            if (opcionSubmenu == "1"):
                numeroIdentificacion = input("Numero de identificacion del paciente: ")
                pacienteEncontrado = False
                for paciente in hospital.listaPacientes:
                    if (paciente.numeroIdentificacion == numeroIdentificacion):
                        pacienteEncontrado = True
                        break

                if (pacienteEncontrado == True):
                    print("")
                    print("[    PACIENTE ENCONTRADO     ]")
                    print("")
                    paciente.actualizarInformacion()

                else:
                    print("")
                    print("[    PACIENTE NO ENCONTRADO   ]")
                    print("")




            ### Obtener informacion ###
            elif (opcionSubmenu == "2"):
                numeroIdentificacion = input("Numero de identificacion del paciente: ")
                pacienteEncontrado = False
                for paciente in hospital.listaPacientes:
                    if (paciente.numeroIdentificacion == numeroIdentificacion):
                        pacienteEncontrado = True
                        break

                if (pacienteEncontrado == True):
                    print("")
                    print("[    PACIENTE ENCONTRADO     ]")
                    print("")
                    paciente.obtenerInformacion()

                else:
                    print("")
                    print("[    PACIENTE NO ENCONTRADO   ]")
                    print("")




            ### Asignar paciente ###
            elif (opcionSubmenu == "3"):
                numeroIdentificacion = input("Numero de identificacion del paciente: ")
                pacienteEncontrado = False
                for paciente in hospital.listaPacientes:
                    if (paciente.numeroIdentificacion == numeroIdentificacion):
                        pacienteEncontrado = True
                        break

                if (pacienteEncontrado == True):
                    print("")
                    print("[    PACIENTE ENCONTRADO     ]")
                    print("")
                    numero = input("Numero de habitacion: ")
                    habitacionEncontrada = False
                    for habitacion in hospital.listaHabitaciones:
                        if (habitacion.numero == numero):
                            habitacionEncontrada = True    
                            break

                    if (habitacionEncontrada == True):
                        print("")
                        print("[    HABITACION ENCONTRADA     ]")
                        print("")
                        habitacion.asignarPaciente(paciente)
                        print("[    HABITACION ASIGNADA     ]")
                        print("")
                        print("En 2 segundos volveras al menu")
                        time.sleep(2)
                        
                    else:
                        print("")
                        print("[    NO ENCONTRADO   ]")
                        print("")
                        print("En 2 segundos volveras al menu")
                        time.sleep(2)

                else:
                    print("")
                    print("[    PACIENTE NO ENCONTRADO   ]")
                    print("")

            ### Liberar habitacion ###
            elif (opcionSubmenu == "4"):
                numero = input("Numero de habitacion: ")
                habitacionEncontrada = False
                for habitacion in hospital.listaHabitaciones:
                    if (habitacion.numero == numero):
                        habitacionEncontrada = True
                        for paciente in habitacion.pacientesAsignados:
                            habitacion.liberarHabitacion(paciente)
                            break

                if (habitacionEncontrada == True):
                    print("")
                    print("[    HABITACION ENCONTRADA     ]")
                    print("")
                    habitacion.liberarHabitacion()
                    print("[    HABITACION LIBERADA     ]")
                    print("")
                    print("En 2 segundos volveras al menu")
                    time.sleep(2)
                    
                else:
                    print("")
                    print("[    NO ENCONTRADO   ]")
                    print("")
                    print("En 2 segundos volveras al menu")
                    time.sleep(2)


            ### Verificar disponibilidad ###
            elif (opcionSubmenu == "5"):
                numero = input("Numero de habitacion: ")
                habitacionEncontrada = False
                for habitacion in hospital.listaHabitaciones:
                    if (habitacion.numero == numero):
                        habitacionEncontrada = True
                        break

                if (habitacionEncontrada == True):
                    print("")
                    print("[    HABITACION ENCONTRADA     ]")
                    print("")
                    disponible = habitacion.verificarDisponibilidad()
                    if (disponible == True):
                        print("[    HABITACION DISPONIBLE     ]")
                        print("")
                        print("En 2 segundos volveras al menu")
                        time.sleep(2)
                    else:
                        print("[    HABITACION OCUPADA     ]")
                        print("")
                        print("En 2 segundos volveras al menu")
                        time.sleep(2)

                else:
                    print("")
                    print("[    NO ENCONTRADO   ]")
                    print("")
                    print("En 2 segundos volveras al menu")
                    time.sleep(2)

            ### Asignar paciente ###
            elif (opcionSubmenu == "6"):
                break

            ### Atender paciente ###
            elif (opcionSubmenu == "7"):
                break

            ### Actualizar informacion ###
            elif (opcionSubmenu == "8"):
                break

            ### Salir ###
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
            opcionSubmenu = input("Introduce un numero: ")
            
            if (opcionSubmenu == "1"):
                numeroIdentificacionMedico=input("Introduce el numero de identificación del medico: ")
                medicoEncontrado = ""
                for medico in hospital.listaMedicos:
                    if (medico.numeroIdentificacion == numeroIdentificacionMedico):
                        medicoEncontrado = medico
                        break
                
                if (medicoEncontrado!=""):
                    numeroIdentificacionPaciente=input("Introduce el numero de identificación del paciente: ")

                    for paciente in hospital.listaPacientes:
                        if (paciente.numeroIdentificacion == numeroIdentificacionPaciente):
                            medicoEncontrado.asignarPaciente(numeroIdentificacionPaciente, hospital.listaPacientes)
                            break
                else:
                    print("El medico no ha sido encontrado")
                     
            
            elif (opcionSubmenu == "2"):
                numeroIdentificacion=input("Introduce el numero de identificación: ")                
                for paciente in medico.pacientesAsignados:
                    if numeroIdentificacion == paciente.numeroIdentificacion:
                        medico.atenderPaciente(paciente)
                        break


            elif (opcionSubmenu == "3"):
                numeroIdentificacion=input("Introduce el numero de identificación del medico: ")
                for medico in hospital.listaMedicos:
                    if (medico.numeroIdentificacion == numeroIdentificacion):
                        medicoEncontrdo = True
                        medico.actualizarInformacion()
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
    ### SALIR ###
    elif (opcionMenu == "3"):
        condicion =  False