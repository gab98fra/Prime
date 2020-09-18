# -----------------------------------------------------------------------------------------------
# Nombre:       models_login.py
# Autor:        Gabriel F
# Creado:       18 de Septiembre 2020
# Modificado:   18 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------

"""

           Modelo: conexión al servidor bd utilizado en control.py

"""
import pyodbc

from generales import getdata
from generales import entlogin
from generales import variables 


class models_login:    
    
    def conexion():
    #Conexión al servidor
        
        
        if (getdata.archivoExiste(variables.nomArchivoxml)):  #si existe
            #obtenemos los datos del archivo: data.xml.
            servidor=getdata.obtenerDato(variables.nomArchivoxml,"servidor")
            database=getdata.obtenerDato(variables.nomArchivoxml,"database")
            usuario=getdata.obtenerDato(variables.nomArchivoxml,"usuario").rstrip()
            password=getdata.obtenerDato(variables.nomArchivoxml,"password")
        

        try:
        #si la conexión es exitosa
        
            variables.conexionBd=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
            servidor + ';DATABASE=' + database + ';UID='+ usuario + ';PWD='+password)
            return True
    
        except:
            return False
    
    def read(self, user, password):
    #Validación Inicio de Sesión

        if variables.conexionBd:#si hay conexión a la BD
            #Creamos el objeto: através del modulo entlogin
            obUsuario=entlogin.entlogin()

            try:
                #With permite cerrar automaticamente el cursor, una vez finalizada la query
                with variables.conexionBd.cursor() as cursor:

                    #Query
                    query="SELECT contrasena,rol,id_cliente FROM usuario WHERE usuario=?"
                    
                    cursor.execute(query,(user))#user es el parametro recibido

                    #La información consultada es una tupla dentro de una lista: [(val1, val2)]
                    datosObtenidos=cursor.fetchall()
        
                    #si la longitud de la lista es cero, significa que no hay ningun registro, por tanto no darle acceso
                    if len(datosObtenidos)>=1:
                        
                        #realizamos una comparacion con el pass que ingreso
                        if datosObtenidos[0][0]==password: #La primera tupla, y el primero valor corresponde a password

                            #La primera tupla, y segundo elemento de la tupla corresponde al rol: datosObtenidos[0][1]
                            #Ejecutamos el objeto y su metodo: setROl y le pasamos como parametro el elemento de la query
                            obUsuario.setRol(datosObtenidos[0][1]) 

                            #La primera tupla, y segundo elemento de la tupla corresponde al rol: datosObtenidos[0][2]    
                            obUsuario.setIdCliente(datosObtenidos[0][2])

                            obUsuario.setUser(user) 
                            obUsuario.setPassword(password)
                            
                            return obUsuario#retornamos el objeto creado
                        
                        else:
                            return obUsuario
                    
                    else:
                        return False
            except:
                return False

    def cerrarConexionBD():
    #cerramos la conexion al servidor BD
        variables.conexionBd.close()