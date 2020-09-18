# -----------------------------------------------------------------------------------------------
# Nombre:       entlogin.py
# Autor:        Gabriel F
# Creado:       18 de Septiembre 2020
# Modificado:   18 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------


"""

           Entidad conexión BD: tabla usuario sql
           Utilizado en models_login

"""

class entlogin:

    def __init__(self):
        
        #Campos de la tabla BD: usuario, se declaran variables privadas
        self.__usuario=""
        self.__contrasena=""
        self.__rol=""
        self.__idCliente=""

    def setUser(self,user):
    #Se asigna el valor a la varibale privada: usuario
        self.__usuario=user
    
    def getUser(self):
    #Se obtiene el valor de la varible privado: usuario
        return self.__usuario

    def setPassword(self,password):
        self.__contrasena=password

    def getPassword(self):
        return self.__contrasena

    def setRol(self,rol):
        self.__rol=rol

    def getRol(self):
        return self.__rol
    
    def setIdCliente(self,idcliente):
    
        self.__idCliente=idcliente

    def getIdCliente(self):
        return self.__idCliente
