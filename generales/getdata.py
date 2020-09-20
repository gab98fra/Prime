# -----------------------------------------------------------------------------------------------
# Nombre:       getdata.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       18 de Septiembre 2020
# Modificado:   20 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------


"""

           Algoritmo: permite leer archivos XML: especificamente: data.xml
           Es utilizado en el modulo: modconexbd.py


"""

import os.path

from xml.dom import minidom


#Funcion para verificar si un archivo existe
def archivoExiste(archivo):
    #verificamos si existe el archivo
    return os.path.isfile(archivo)

#obtener datos del archivo: data.xml
def obtenerDato(archivoxml, dato):
    
    #Obtener acceso al documento
    docXML=minidom.parse(archivoxml)

    #Obtiene el dato, obtenemos la linea de xml según sDato, y en posición 0
    dato=docXML.getElementsByTagName(dato)[0]

    return dato.firstChild.data
