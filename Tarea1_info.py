class Paciente:
    def __init__(self):
        self.__nombre=""
        self.__apellido=""
        self.__cedula= 0
        self.__genero= ""
        self.__servicio= ""
        #print("hola")

    def verNombre(self):
        return self.__nombre
    def verApellido(self):
        return self.__apellido
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula

    def asignarNombre (self,n):
        self.__nombre=n
    def asignarApellido(self,a):
        self.__apellido=a
    def asignarServicio (self,s):
        self.__servicio= s
    def asignarGenero (self,g):
        self.__genero=g
    def asignarCedula (self,c):
        self.__cedula= c

class Sistema (object): 
    def __init__(self):
        self.__lista_pacientes=[]
        # self.__numero_pacientes= 

    def verificar_paciente(self,cedula):
        for v in self.__lista_pacientes:
            if cedula == v.verCedula():
                print("Paciente Encontrado")
                return True 
        
        return False

    def ingresarPaciente(self, pac):
        if self.verificar_paciente(pac.verCedula()):
            return True
        
        self.__lista_pacientes.append(pac)
        
        return False
    
        # nombre=input("Ingrese el nombre: ")
        # cedula=int(input("Ingrese la cedula: "))
        # genero= input("Ingrese el genero: ")
        # servicio= input("Ingrese el servicio: ")

        # p= Paciente()
        # p.asignarNombre(nombre)
        # p.asignarCedula(cedula)
        # p.asignarGenero(genero)
        # p.asignarServicio(servicio)

        # self.__lista_pacientes.append(p)


        
    def verNumeroPacientes(self):
        return  len(self.__lista_pacientes)

    
    def verDatosPaciente (self,c):
        if self.verificar_paciente(c) ==  False:
            return None
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
    
def main():
    sis=Sistema()


    while True:
        opcion= int(input("""Ingrese la opcion deseada
                        1) Nuevo paciente
                        2) Numero de pacientes
                        3) Datos del paciente
                        4) Salir
                        """))
        if opcion==1:
            print("a continuación se solicitaran los datos")

            nombre=input("Ingrese el nombre: ")
            apellido=input("Ingrese el apellido: ")
            cedula=int(input("Ingrese la cedula: "))
            genero= input("Ingrese el genero: ")
            servicio= input("Ingrese el servicio: ")

            pac= Paciente()
            pac.asignarNombre(nombre)
            pac.asignarApellido(apellido)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)

            resultado= sis.verificar_paciente(pac)

            if resultado == True:
                print("Ya existe un paciente con esa cédula")
            else:
                resultado= sis.ingresarPaciente(pac)

                print("Paciente ingresado")


        elif opcion==2:
            print("En este momento el numero de personas que hay es:" + str(sis.verNumeroPacientes()))

        elif opcion==3:
            ce= int(input("Ingrese cedula del paciente a buscar: "))
            
            h= sis.verDatosPaciente(ce)
            

            # for paciente in self.__lista_pacientes:
            #     if cedula == paciente.verCedula():
        # cedula= int(input("Ingrese cedula del paciente a buscar: "))
        # for paciente in self.__lista_pacientes:
        #     if cedula == paciente.verCedula():
        #         print ("Nombre: " + paciente.verNombre())
        #         print ("Cedula: " + str(paciente.verCedula()))
        #         print ("Genero: " + paciente.verGenero())
        #         print ("Servicio: " + paciente.verServicio())
            print ("Nombre: " + h.verNombre())
            print ("Apellido: " + h.verApellido())
            print ("Cedula: " + str(h.verCedula()))
            print ("Genero: " + h.verGenero())
            print ("Servicio: " + h.verServicio())
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")

if __name__=="__main__":
    main()



# mi_sistema= Sistema()
