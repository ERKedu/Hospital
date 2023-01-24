class Medico: 
    def __init__(self, nombre, apellido1, apellido2, especialidad, numeroIdentificacion, horarioTrabajo, pacientesAsignados, consulta):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.especialidad=especialidad
        self.numeroIdentificacion=numeroIdentificacion
        self.horarioTrabajo=horarioTrabajo
        self.pacientesAsignados=pacientesAsignados
        self.consulta=consulta

    def asignarPaciente(self, numeroIdentificacion, listaPacientes): 
        for paciente in listaPacientes:
            if numeroIdentificacion == paciente.numeroIdentificacion:       
                self.pacientesAsignados.append(paciente)


    def atenderPaciente(self, paciente):
        print ("Visita del médico ", paciente.nombre)
        

    def actualizarInformacion(self):    
        nombre=input("Introduce el nombre: ")
        apellido1=input("Introduce el apellido1: ")
        apellido2=input("Introduce el apellido2: ")
        especialidad=input("Introduce la especialidad: ")
        numeroIdentificacion=input("Introduce el número de identificación: ")
        horarioTrabajo=input("Introduce el horario de trabajo: ")
        consulta=input("Introduce la consulta: ")
                    
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.especialidad=especialidad
        self.numeroIdentificacion=numeroIdentificacion
        self.horarioTrabajo=horarioTrabajo
        self.consulta=consulta

        print("Información actualizada")

class Consulta:
    def __init__(self, numero, medicoAsignado):
            self.numero=numero
            self.medicoAsignado=medicoAsignado

    def asignarMedico(self, Medico):
        self.medicoAsignado = Medico
        Medico.consulta = self

    def liberarConsulta(self, Medico):
        self.medicoAsignado = None
        Medico.consulta = None


class Farmacia:
    def __init__(self, medicamentosDisponibles):
        self.medicamentosDisponibles = medicamentosDisponibles

    def agregarMedicamento(self, medicamento):
        self.medicamentosDisponibles[medicamento] = 1
        

    def eliminarMedicamento():
        print("El medicamento no existe")
        

    def obtenerMedicamento():
        print("El medicamento no existe")
        
