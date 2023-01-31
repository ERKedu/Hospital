class Medico:
    ### Constructor de la clase Medico ###
    def __init__(self, nombre, apellido1, apellido2, especialidad, numeroIdentificacion, horarioTrabajo, pacientesAsignados, consulta):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.especialidad=especialidad
        self.numeroIdentificacion=numeroIdentificacion
        self.horarioTrabajo=horarioTrabajo
        self.pacientesAsignados=pacientesAsignados
        self.consulta=consulta

    ### Funcion para asigna un paciente al mdeico ###
    def asignarPaciente(self, paciente):      
        self.pacientesAsignados.append(paciente)

    ### Funcion para atender a un paciente ###
    def atenderPaciente(self, paciente):
        mensaje = "El enfermero/a '" + self.nombre + "' ha visitado a '" + paciente.nombre + "'"
        paciente.historialMedico.append(mensaje)
        print(mensaje)
        print("")
        print("[     HISTORIAL ACTUALIZADO     ]")
        print("")        

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
    ### Constructor de la clase Consulta ###
    def __init__(self, numero, medicoAsignado):
            self.numero=numero
            self.medicoAsignado=medicoAsignado

    ### Funcion que asigna un médico a la consulta ###
    def asignarMedico(self, Medico):
        self.medicoAsignado = Medico
        Medico.consulta = self

    ### Funcion para liberer una consulta ###
    def liberarConsulta(self, Medico):
        self.medicoAsignado = None
        Medico.consulta = None


class Farmacia:
    ### Constructor de la clase Farmacia ###
    def __init__(self, medicamentosDisponibles):
        self.medicamentosDisponibles = medicamentosDisponibles

    ### Funcion para agregar un medicamento a la lista de medicamentos ###
    def agregarMedicamento(self, medicamento):
        self.medicamentosDisponibles[medicamento] = 1
        
    ### Funcion para elimimnar un medicamento de la lista de medicamentos ###
    def eliminarMedicamento(self):
        print("El medicamento no existe")
        
    ### Funcion para obtener un medicamento de la lista de medicamentos, restando 1 a la cantidad ###
    def obtenerMedicamento(self):
        print("El medicamento no existe")
        
