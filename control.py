# -----------------------------------------------------------------------------------------------
# Nombre:       control.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       18 de Septiembre 2020
# Modificado:   16 de Noviembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------

"""
        Módulo principal:
           Importante instalar correctamente SQL Server con los datos importantes de este módulo
                               credenciales de acceso, tablas y datos de login

    Python 3.8.2
    PyQt 5.15.0

"""


from PyQt5.QtWidgets import QApplication
import sys

from sistemas.sistemas import appSistema
from generales.models_login import models_login 
from generales import variables

#Sistemas - con SQL Instalado
if __name__ == '__main__':

    #INICIO
    app = QApplication(sys.argv)

    # Conexión  a la BD
    models_login.conexion()

    # Sesión BD
    sesionBD = models_login()
    resultado = sesionBD.read("usuario2", "usuario2")
    
    if resultado:
        #Guardamos lo valores en las variables globales
        variables.usuarioIdCliente = resultado.getIdCliente()
        variables.usuarioNom = resultado.getUser()
        variables.usuarioPas = resultado.getPassword()
        variables.usuarioRol = resultado.getRol()

        # Se crea el objecto: appSistema
        objecto = appSistema(variables)
        # Muestra objeto creado
        objecto.show()
        
        sys.exit(app.exec_())
        
    else:
        print("revise la conexión a la BD")