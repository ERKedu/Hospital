from funciones import *
from funciones2 import *
import time

### Inicializamos una hospital ###
hospital = Hospital([], [], [], [], []) 

### Creamos las habitaciones y las añadimos a la lista ###
disponibilidad = True

habitacion1 = Habitacion("1", "compartida", [], disponibilidad)
habitacion2 = Habitacion("2", "privada", [], disponibilidad)
hospital.listaHabitaciones.append(habitacion1)
hospital.listaHabitaciones.append(habitacion2)


### Creamos los pacientes y los añadimos a la lista de pacientes de la farmacia ###
paciente1 = Paciente("1", "1", "1", "1", "1", [])
paciente2 = Paciente("2", "2", "2", "2", "2", [])
paciente3 = Paciente("3", "3", "3", "3", "3", [])
hospital.listaPacientes.append(paciente1)
hospital.listaPacientes.append(paciente2)
hospital.listaPacientes.append(paciente3)



### Creamos los medicos y los añadimos a la lista de medicos del hosptial ###
medico1 = Medico("1", "1", "1", "1", "1", "1", [], "1")
medico2 = Medico("2", "2", "2", "2", "2", "2", [], "2")
hospital.listaMedicos.append(medico1)
hospital.listaMedicos.append(medico2)

### Creamos los enefremeros ###
enfermero1= Enfermero("Luisa", "Martinez", "Sanchez", "1", "9:00-17:00", [])
enfermero2= Enfermero("Carlos", "Esun", "Cohcebomba", "2", "17:00-9:00", [])
hospital.listaEnfermeros.append(enfermero1)
hospital.listaEnfermeros.append(enfermero2)


### Creamos las consultas ###
consulta1= Consulta("1","")
consulta2= Consulta("2","")
hospital.listaConsultas.append(consulta1)
hospital.listaConsultas.append(consulta2)

### Creamos diccionario de medicamentos ###
file = open("medicamentos.txt", "r")
farmacia1 = Farmacia({file.read()})
file.close()

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

                if (pacienteEncontrado):
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

                if (pacienteEncontrado):
                    print("")
                    print("[    PACIENTE ENCONTRADO     ]")
                    print("")
                    paciente.obtenerInformacion()

                else:
                    print("")
                    print("[    PACIENTE NO ENCONTRADO   ]")
                    print("")

            ### Asignar paciente Habitaciones###
            elif (opcionSubmenu == "3"):
                numeroIdentificacion = input("Numero de identificacion del paciente: ")
                pacienteEncontrado = False
                for paciente in hospital.listaPacientes:
                    if (paciente.numeroIdentificacion == numeroIdentificacion):
                        pacienteEncontrado = True
                        break

                if (pacienteEncontrado):
                    print("")
                    print("[    PACIENTE ENCONTRADO     ]")
                    print("")
                    numero = input("Numero de habitacion: ")
                    habitacionEncontrada = False
                    for habitacion in hospital.listaHabitaciones:
                        if (habitacion.numero == numero):
                            habitacionEncontrada = True    
                            break

                    if (habitacionEncontrada):
                        print("")
                        print("[    HABITACION ENCONTRADA     ]")
                        print("")
                        longitud=len(habitacion.pacientesAsignados)
                        if (habitacion.tipo == "compartida" and longitud < 2):
                            habitacion.asignarPaciente(paciente)
                            print("[    HABITACION ASIGNADA       ]")


                        elif (habitacion.tipo == "privada" and longitud < 1):
                            habitacion.asignarPaciente(paciente)
                            print("[    HABITACION ASIGNADA       ]")

                        else:

                            print("[    HABITACION OCUPADA       ]")

                        print("")
                        print("En 2 segundos volveras al menu")
                        time.sleep(2)
                        
                    else:
                        print("")
                        print("[    HABITACION NO ENCONTRADA   ]")
                        print("")
                        print("En 2 segundos volveras al menu")
                        time.sleep(2)

                else:
                    print("")
                    print("[    PACIENTE NO ENCONTRADO   ]")
                    print("")
                    time.sleep(2)

            ### Liberar habitacion ###
            elif (opcionSubmenu == "4"):
                numero = input("Numero de habitacion: ")
                habitacionEncontrada = False
                for habitacion in hospital.listaHabitaciones:
                    if (habitacion.numero == numero):
                        habitacionEncontrada = True
                        break

                if (habitacionEncontrada):
                    print("")
                    print("[    HABITACION ENCONTRADA     ]")
                    print("")
                    for paciente in habitacion.pacientesAsignados:
                        habitacion.liberarHabitacion(paciente)
                        print("[    HABITACION LIBERADA     ]")
                        print("")
                        print("En 2 segundos volveras al menu")
                        time.sleep(2)
                    
                else:
                    print("")
                    print("[    PACIENTE NO ENCONTRADO   ]")
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

                if (habitacionEncontrada):
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
                    print("[    PACIENTE NO ENCONTRADO   ]")
                    print("")
                    print("En 2 segundos volveras al menu")
                    time.sleep(2)

            ### Asignar paciente Enfermero###
            elif (opcionSubmenu == "6"):
                numeroIdentificacion = input("Numero de identificacion del enfermero: ")
                enfermeroEncontrado = False
                for enfermero in hospital.listaEnfermeros:
                    if (enfermero.numeroIdentificacion == numeroIdentificacion):
                        enfermeroEncontrado = True
                        break

                if (enfermeroEncontrado):
                    print("")
                    print("[    ENFERMERO ENCONTRADO     ]")
                    print("")
                    pacienteEncontrado = False
                    numPaciente = input("Numero de identificacion del paciente: ")
                    for paciente in hospital.listaPacientes:
                        if (paciente.numeroIdentificacion == numPaciente):
                            pacienteEncontrado = True
                            break
                    if (pacienteEncontrado):
                        print("")
                        print("[    PACIENTE ENCONTRADO     ]")
                        print("")
                        enfermero.asignarPaciente(paciente)
                        print("")
                        print("[    PACIENTE ASIGNADO     ]")
                        print("")
                    else:
                        print("")
                        print("[    PACIENTE NO ENCONTRADO     ]")
                        print("")                        

                else:
                    print("")
                    print("[    ENFERMERO NO ENCONTRADO   ]")
                    print("")

                break

            ### Atender paciente ###
            elif (opcionSubmenu == "7"):
                numeroPaciente= input("Introduzca el numero del paciente: ")
                for paciente in hospital.listaPacientes:
                    if paciente.numeroIdentificacion == numeroPaciente:
                        print("")
                        print("[    PACIENTE ENCONTRADO     ]")
                        print("")
                        numeroEnfermero= input("Introduzca el numero del Enfermero: ")
                        for enfermero in hospital.listaEnfermeros:
                            if enfermero.numeroIdentificacion == numeroEnfermero:
                                print("")
                                print("[    ENFERMERO ENCONTRADO     ]")
                                print("")
                                enfermero.atenderPaciente(paciente)
                                break

                            else:
                                print("")
                                print("[    ENFERMERO no ENCONTRADO     ]")
                                print("")

                    else:
                        print("")
                        print("[    PACIENTE NO ENCONTRADO     ]")
                        print("")
                    break


            ### Actualizar informacion ###
            elif (opcionSubmenu == "8"):
                numeroIdentificacion = input("Numero de identificacion del enfermero: ")
                enfermeroEncontrado = False
                for enfermero in hospital.listaEnfermeros:
                    if (enfermero.numeroIdentificacion == numeroIdentificacion):
                        enfermeroEncontrado = True
                        break

                if (enfermeroEncontrado):
                    print("")
                    print("[    ENFERMERO ENCONTRADO     ]")
                    print("")
                    enfermero.actualizarInformacion()

                else:
                    print("")
                    print("[    ENFERMERO NO ENCONTRADO   ]")
                    print("")

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
            print("7.- Eliminar medicamento")
            print("8.- Obtener medicamento")
            print("")
            print("9.- Salir")
            opcionSubmenu = input("Introduce un numero: ")
            
            ### Asignar paciente ###
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
                            medicoEncontrado.asignarPaciente(paciente)
                            break
                else:
                    print("El medico no ha sido encontrado")
                     
            ### Atender paciente ###
            elif (opcionSubmenu == "2"):
                numeroIdentificacion = input("Numero de identificacion del medico: ")
                medicoEncontrado = False
                for medico in hospital.listaMedicos:
                    if (medico.numeroIdentificacion == numeroIdentificacion):
                        medicoEncontrado = True
                        break

                if (medicoEncontrado):
                    print("")
                    print("[    MEDICO ENCONTRADO     ]")
                    print("")
                    if (len(medico.pacientesAsignados) == 0):
                        print("El medico no tiene pacientes asignados")

                    else:
                        for paciente in medico.pacientesAsignados:
                            if numeroIdentificacion == paciente.numeroIdentificacion:
                                medico.atenderPaciente(paciente)
                                print("")
                                print("[    PACIENTE ATENDIDO     ]")
                                print("")
                                break

                else:
                    print("")
                    print("[    ENFERMERO NO ENCONTRADO   ]")
                    print("")

                break


            ### Actualizar informacion ###
            elif (opcionSubmenu == "3"):
                numeroIdentificacion=input("Introduce el numero de identificación del medico: ")
                for medico in hospital.listaMedicos:
                    if (medico.numeroIdentificacion == numeroIdentificacion):
                        medicoEncontrdo = True
                        medico.actualizarInformacion()
                        break
            
            ### Asignar medico ###
            elif (opcionSubmenu == "4"):
                numeroIdentificacion=input("Introduce el numero de identificación del medico: ")
                num=input("Introduce el numero de consulta:  ")

                for consulta in hospital.listaConsultas:
                    if (consulta.numero == num):
                        if (consulta.medicoAsignado == ""):
                            for medico in hospital.listaMedicos:
                                if (medico.numeroIdentificacion == numeroIdentificacion):
                                    consulta.asignarMedico(medico)
                                    break
                        else:
                            print ("Consulta ocupada")
                            break

            ### Liberar consulta ###
            elif (opcionSubmenu == "5"):
                num=input("Introduce el numero de consulta:  ")

                for consulta in hospital.listaConsultas:
                    if (consulta.numero == num):
                        for medico in hospital.listaMedicos:
                            if (medico.numeroIdentificacion == numeroIdentificacion):
                                consulta.liberarConsulta(medico)
                                break

            ### Agregar medicamento ###
            elif (opcionSubmenu == "6"):
                medicamento = input ("Introduce el nombre del medicamento: ")
            
                if (medicamento in farmacia1.medicamentosDisponibles):
                    farmacia1.medicamentosDisponibles[medicamento]+=1
                else:
                    farmacia1.agregarMedicamento(medicamento)
                break

            ### Eliminar medicamento ###
            elif (opcionSubmenu == "7"):
                medicamento = input ("Introduce el nombre del medicamento: ")
                
                if (medicamento in farmacia1.medicamentosDisponibles):
                    del farmacia1.medicamentosDisponibles[medicamento]
                else:
                    farmacia1.eliminarMedicamento()
                    break

            ### Obtener medicamento ###
            elif (opcionSubmenu == "8"):
                medicamento = input ("Introduce el nombre del medicamento: ")
                
                if (medicamento in farmacia1.medicamentosDisponibles and farmacia1.medicamentosDisponibles[medicamento]>0):
                    farmacia1.medicamentosDisponibles[medicamento]-=1
                else:
                    farmacia1.obtenerMedicamento()
                break

            elif (opcionSubmenu == "9"):
                condicion2 =  False
    ### SUBMENU MEDICO ###
    ### SALIR ###
    elif (opcionMenu == "3"):
        condicion =  False