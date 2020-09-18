# -----------------------------------------------------------------------------------------------
# Nombre:       variables.py
# Autor:        Gabriel F
# Creado:       18 de Septiembre 2020
# Modificado:   18 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------

"""

           Es utilizado en los modulos: control y sistemas

"""


#------------------------------Constantes:----------------------------------------
#Nombre del sistema
nomSistema="Prime " 
#Archivo xml, datos de acceso al servidor BD
nomArchivoxml="generales/data.xml"


#------------------------------Variables Globales--------------------------------
usuarioIdCliente=0 #Id_cliente
usuarioNom="Unknow" #Nombre del usuario
usuarioPas="Unknow" #password del usuario
usuarioRol="Unknow" #Rol del Usuario
conexionBd=False #Conexión a la BD
accesoconcedido=False #Variable que indica si el usuario tiene acceso al sistema: Ventana Principal
