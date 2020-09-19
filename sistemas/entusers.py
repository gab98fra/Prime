# -----------------------------------------------------------------------------------------------
# Nombre:       entusers.py
# Autor:        Gabriel F
# Creado:       18 de Septiembre 2020
# Modificado:   19 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------

"""

           Entidad usuarios: Tabla usuario (sql server)
           El módulo es utilizado en: models_users

"""

class entUser:

    def __init__(self):
        
        #Campos de la tabla BD: usuario, se declaran variables privadas y listas vacías
        self.__usuario=[]
        self.__contrasena=[]
        self.__rol=[]
        self.__idCliente=[]

    def setUser(self,user):
    
        self.__usuario.append(user)
    
    def getUser(self):
        
        return self.__usuario

    def setPassword(self,password):
        
        self.__contrasena.append(password)

    def getPassword(self):
        
        return self.__contrasena

    def setRol(self,rol):
        
        self.__rol.append(rol)

    def getRol(self):
        
        return self.__rol
    
    def setIdCliente(self,idcliente):
    
        self.__idCliente.append(idcliente)

    def getIdCliente(self):
        
        return self.__idCliente

