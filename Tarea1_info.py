class Paciente:
    def __init__(self):
        self.__nombre=""
        self.__cedula= 0
        self.__genero= ""
        self.__servicio= ""
        #print("hola")

    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula

    def asignarNombre (self,n):
        self.__nombre=n
    def asignarServicio (self,s):
        self.__servicio= s
    def asignarGenero (self,g):
        self.__genero=g
    def asignarCedula (self,c):
        self.__cedula= c

class Sistema:
    def __init__(self):
        self.__lista_pacientes=[]
        self.__numero_pacientes= len(self.__lista_pacientes)
    def ingresarPaciente(self):
        nombre=input("Ingrese el nombre: ")
        cedula=int(input("Ingrese la cedula: "))
        genero= input("Ingrese el genero: ")
        servicio= input("Ingrese el servicio: ")

        p= Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        self.__lista_pacientes.append(p)
        self.__numero_pacientes=len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPaciente (self):
        cedula= int(input("Ingrese cedula del paciente a buscar: "))
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print ("Nombre: " + paciente.verNombre())
                print ("Cedula: " + str(paciente.verCedula()))
                print ("Genero: " + paciente.verGenero())
                print ("Servicio: " + paciente.verServicio())
    
mi_sistema= Sistema()

while True:
    opcion= int(input("""Ingrese la opcion deseada
                      1) Nuevo paciente
                      2) Numero de pacientes
                      3) Datos del paciente
                      4) Salir
                      """))
    if opcion==1:
        mi_sistema.ingresarPaciente()
    elif opcion==2:
        print("En este momento el numero de personas que hay es:" + str(mi_sistema.verNumeroPacientes()))
    elif opcion==3:
        mi_sistema.verDatosPaciente()
    elif opcion== 4:
        break
    else:
        print("Opcion invalida")
