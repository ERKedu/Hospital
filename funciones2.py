class Medico: 
    def __init__(self, nombre, apellido1, apellido2, especialidad, numeroDeIdentificacion, horarioTrabajo, pacientesAsignados, consulta):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.especialidad=especialidad
        self.numeroDeIdentificacion=numeroDeIdentificacion
        self.horarioTrabajo=horarioTrabajo
        self.pacientesAsignados=pacientesAsignados
        self.consulta=consulta

    def asignarPaciente(self, numeroDeIdentificacion, ):          
        for paciente in listaPacientes:
            if numeroDeIdentificacion == paciente.numeroDeIdentificacion:
                pacientesAsignados.append(paciente)


    def atenderPaciente(self, numeroDeIdentificacion):
        for paciente in self.pacientesAsignados:
            if numeroDeIdentificacion == paciente.numeroDeIdentificacion:
                print ("Visita del médico ", nombre)
        

    def actualizarInformacion(self)    
        nombre=input("Introduce el nombre: ")
        apellido1=input("Introduce el apellido1: ")
        apellido2=input("Introduce el apellido2: ")
        especialidad=input("Introduce la especialidad: ")
        numeroDeIdentificacion=input("Introduce el número de identificación: ")
        horarioTrabajo=input("Introduce el horario de trabajo: ")
        consulta=input("Introduce la consulta: ")
                    
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.especialidad=especialidad
        self.numeroDeIdentificacion=numeroDeIdentificacion
        self.horarioTrabajo=horarioTrabajo
        self.pacientesAsignados=pacientesAsignados
        self.consulta=consulta

        print("Información actualizada")

class Consulta:
    def __init__(self, numero, medicoAsignado):
            self.numero=numero
            self.medicoAsignado=medicoAsignado

    def asignarMedico(self, Medico):
        self.medicoAsignado = Medico
        Medico.consulta = self

    def liberarConsulta(self, Medico, listaMedicos):
        self.medicoAsignado = None
        Medico.consulta = None
