class Empresa:
    def __init__(self) -> None:
        self.__nit=0
        self.__ubicacion= ""
        self.__contaminantes=""
        self.__registro_contaminantes:0
    
    def asignarNit(self,n):
        self.__nit=n
    def asignarUbicacion(self,u):
        self.__ubicacion = u
    def asignarcontaminantes(self,c):
        self.__contaminantes = c
    def asignarRegistro(self,r):
        self.__registro_contaminantes= r
    
    def verNit(self):
        return self.__nit
    def verUbicacion(self):
        return self.__ubicacion
    def verContaminantes(self):
        return self.__contaminantes
    def verRegistro(self):
        return self.__registro_contaminantes
    

class Sistema:
    def __init__(self) -> None:
        self.__lista_empresas=[]
    
    def verificarEmpresa(self,n):
        for e in self.__lista_empresas:
            if n == e.verNit():
                return True
        return False


    def verDatosEmpresa(self,n):
        if self.verificarEmpresa==True:
            return None
        for p in self.__lista_empresas:
            if n == p.verNit():
                return p
    def ingresarEmpresa(self,em):
        self.__lista_empresas.append(em)

def main():
    sisCalidad= Sistema()

    while True:
        opcion=int(input("""Ingrese la opcion deseada: 
                         1)Agregar nueva empresa
                         2)Buscar empresa por NIT
                         3)Salir"""))
        
        if opcion ==1:
            nit=int(input("Ingrese el NIT de la empresa: "))
            ubicacion= input("Ingrese la ubicacion de la empresa: ")
            conta=input("Ingrese los contaminantes que genera la empresa: ")
            registro=int(input("Ingrese el registro de contaminacion de la empresa: "))

            em=Empresa()
            em.asignarNit(nit)
            em.asignarUbicacion(ubicacion)
            em.asignarcontaminantes(conta)
            em.asignarRegistro(registro)

            resultado= sisCalidad.verificarEmpresa(em)
            if resultado==True:
                return "Ya existe esta empresa"
            else:
                sisCalidad.ingresarEmpresa(em)
                return "Se ha ingresado empresa con exito"
        
        elif opcion==2:
            op=int(input("Ingrese el NIT de la empresa a buscar: "))

            ob= sisCalidad.verificarEmpresa(op)
            if ob ==True:

                h=sisCalidad.verDatosEmpresa(op)
                print("NIT: " + str( h.verNit()))
                print("Ubicacion: " + h.verUbicacion())
                print("Contaminantes: " + h.verContaminantes())
                print("Registro de contaminantes: " + str( h.verRegistro()))
        
        elif opcion ==3:
            print("Se ha cerrado seccion")
            break
        else:
            print("opción invalida")
    
if __name__== "__main__":
    main()






            

