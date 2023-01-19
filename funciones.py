class Farmacia:
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

    def asignarPaciente(self, numeroIdentificacion):
        if self.disponibilidad== True:
            self.pacientesAsignados= numeroIdentificacion
            self.disponibilidad== False

        else:
            print("Habitación ocupada")


    def liberarHabitacion(self):
        pass

    def verificarDisponibilidad(self):
        pass