# -----------------------------------------------------------------------------------------------
# Nombre:       moduls_users.py
# Autor:        Gabriel F
# Creado:       18 de Septiembre 2020
# Modificado:   19 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------

"""


           Modelo Usuario: permite realizar CRUD en la tabla usuario sql
           Es utilizado en el módulo: sistemas.py


"""
import pyodbc

from main.sistemas.entusers import entUser

class models_users():
    def read(self, variables, idcliente):
        if variables.conexionBd:
            try:
                
                with variables.conexionBd.cursor() as cursor:

                    #Creamos un objeto, a través del módulo: entuser
                    objetoUsuario=entUser()

                    #realizamos la consulta en BD, para evitar inyeccion SQL usamos ?
                    consulta="SELECT usuario, contrasena,rol FROM usuario WHERE id_cliente=?"
                    
                    
                    cursor.execute(consulta,(idcliente))#idcliente, es el párametro recibido

                    datosObtenidos=cursor.fetchall()
                    #datosObtenidos ----> [(usuario1, contrasena1, rol1), (usuario2, contrasena2, rol2)]

                    #si la longitud de la lista es cero, significa que no hay ningún registro
                    if len(datosObtenidos)>=1:
                        
                        #guardamos los registro encontrados en el objeto: objetoUsuario
                        for dupla in datosObtenidos:
                        
            
                            #Utilizamos el objeto creado y le mandamos como párametro el usuario, [0]==user de la BD
                            objetoUsuario.setUser(dupla[0])
                            #asignamos el valor de password [1]==contraseña
                            objetoUsuario.setPassword(dupla[1])
                            #asignamos el valor de rol [2]==rol
                            objetoUsuario.setRol(dupla[2])  

                        #retornamos el objeto creado con sus valores
                        return objetoUsuario

                    else:
                        return False
            except:
                return False
        else:
            return False
    
    def create(self, variables, user, password, rol, idcliente):
        if variables.conexionBd:
            try:
                #Utilizamos la variable global
                with variables.conexionBd.cursor() as cursor:
                    #creamos la sintaxis
                    consulta="INSERT INTO usuario(usuario, contrasena,rol, id_cliente) VALUES (?,?,?,?)"    
                    #Ingresamos los valores
                    cursor.execute(consulta, (user, password,rol, idcliente))
                    return True
            except:
                return False
        else:
            return False

    def update(self,variables, userNew, passwordNew, rolNew, idcliente, user):
        if variables.conexionBd:
            try:
                #Utilizamos la variable global
                with variables.conexionBd.cursor() as cursor:
                    #creamos la sintaxis
                    consulta="UPDATE usuario set usuario=?, contrasena=?, rol=? WHERE id_cliente=? and usuario=?"    
                    #Ingresamos los valores
                    cursor.execute(consulta, (userNew, passwordNew, rolNew, idcliente, user))
                    
                    variables.conexionBd.commit()
                    return True

            except:
                return False
        else:
            return False

    def delete(self, variables, idcliente, user):
        if variables.conexionBd:
            try:
                #Utilizamos la variable global
                with variables.conexionBd.cursor() as cursor:
                    #creamos la sintaxis
                    consulta="DELETE from usuario where id_cliente=? and usuario=?"    
                    #Ingresamos los valores
                    cursor.execute(consulta, (idcliente,user))
                    
                    variables.conexionBd.commit()
                    return True      
            except:
                return False
        else:
            return False

