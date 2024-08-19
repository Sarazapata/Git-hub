class Paciente:
    def __init__(self):
        self.__nombre=""
        self.__cedula= 0
        self.__genero= ""
        self.__servicio= ""
        print("hola")
    
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
