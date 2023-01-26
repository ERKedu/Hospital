class Hospital:
    def __init__(self, listaMedicos, listaPacientes, listaConsultas, listaHabitaciones, listaEnfermeros):
        self.listaMedicos = listaMedicos
        self.listaPacientes = listaPacientes
        self.listaConsultas = listaConsultas
        self.listaHabitaciones = listaHabitaciones
        self.listaEnfermeros = listaEnfermeros

class Paciente:
    def __init__(self, nombre, apellido1, apellido2, fechaNacimiento, numeroIdentificacion, historialMedico):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fechaNacimiento = fechaNacimiento
        self.numeroIdentificacion = numeroIdentificacion
        self.historialMedico = historialMedico

    def actualizarInformacion(self):
        print("[    DATOS     ]")
        self.nombre = input("Nombre: ")
        self.apellido1 = input("Primer Apellido: ")
        self.apellido2 = input("Segundo Apellido: ")
        self.fechaNacimiento = input("Fecha de nacimiento(DD/MM/YYYY): ")
        self.numeroIdentificacion = input("Numero Identificacion: ")
        print("[    DATOS CAMBIADOS     ]")
        print("")


    def obtenerInformacion(self):
        print("[    DATOS     ]")
        print("Nombre: ", self.nombre)
        print("Apellido 1: ", self.apellido1)
        print("Apellido 2: ", self.apellido2)
        print("Fecha de nacimiento: ", self.fechaNacimiento)
        print("Numero de identificacion: ", self.numeroIdentificacion)
        print("Historial medico:")
        print(self.historialMedico)


class Habitacion:
    def __init__(self, numero, tipo, pacientesAsignados, disponibilidad):
        self.numero = numero
        self.tipo = tipo
        self.pacientesAsignados = pacientesAsignados
        self.disponibilidad = disponibilidad

    def asignarPaciente(self, paciente):
        longitud = len(self.pacientesAsignados)
        if (longitud < 1 and self.tipo == "privada"):
            self.pacientesAsignados.append(paciente)
            self.disponibilidad = False

        elif (longitud < 2 and self.tipo == "compartida"):
            self.pacientesAsignados.append(paciente)

        if (len(self.pacientesAsignados) >= 2 and self.tipo == "compartida"):
            self.disponibilidad = False


    def liberarHabitacion(self, paciente):
        self.pacientesAsignados.remove(paciente)
        self.disponibilidad = True

    def verificarDisponibilidad(self):
        return self.disponibilidad

class Enfermero:
    def __init__(self, nombre, apellido1, apellido2, numeroIdentificacion, horarioTrabajo, pacientesAsignados):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.numeroIdentificacion = numeroIdentificacion
        self.horarioTrabajo = horarioTrabajo
        self.pacientesAsignados = pacientesAsignados

    def asignarPaciente(self, paciente):
        self.pacientesAsignados.append(paciente)


    def atenderPaciente(self, paciente):
        paciente.historialMedico.append(input("Actualize el historial del paciente "+paciente.nombre+" "))
        pass

    def actualizarInformacion(self):
        print("[    DATOS     ]")
        self.nombre = input("Nombre: ")
        self.apellido1 = input("Primer Apellido: ")
        self.apellido2 = input("Segundo Apellido: ")
        self.numeroIdentificacion = input("Numero Identificacion: ")
        self.horarioTrabajo = input("Horario trabajo: ")
        print("[    DATOS CAMBIADOS     ]")
        print("")
