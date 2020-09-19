# -----------------------------------------------------------------------------------------------
# Nombre:       models_products.py
# Autor:        Gabriel F
# Creado:       18 de Septiembre 2020
# Modificado:   19 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------

"""

           Modelo Productos: permite realizar CRUD en la tabla cat_producto
           El módulo es utilizado: sistemas

"""

import pyodbc


from main.sistemas.entproducts import entProduct

class models_products():
    
    def read(self, variables, idcliente):
        
        if variables.conexionBd:
            try:
                #With permite cerrar automáticamente el cursor, una vez finalizada el query
                with variables.conexionBd.cursor() as cursor:
                    
                    #Objeto a través del modulo entproducts
                    objetoConsulta=entProduct()
                    
                    query="SELECT id_producto, categoria, subcategoria, marca, producto, sku, precio,usuario FROM cat_producto WHERE id_cliente=?"
                    
                    cursor.execute(query,(idcliente))#idcliente, parámetro recibido

                    #La información consultada es una tupla dentro de una lista: [(val1, val2), (val1,va2)...]
                    #[(id_producto1, categoria1, ..., usuario), (id_producto2, categoria2, ...,usuario)]
                    datosObtenidos=cursor.fetchall()
                    
                    
                    if len(datosObtenidos)>=1:
                    #si la longitud de la lista es cero, significa que no hay ningún registro

                        for tupla in datosObtenidos:
                        #guardamos los registro encontrados, a través del objeto creado

                            objetoConsulta.setIdProducto(tupla[0])
                            objetoConsulta.setCategoria(tupla[1])
                            objetoConsulta.setSubCategoria(tupla[2])
                            objetoConsulta.setMarca(tupla[3])
                            objetoConsulta.setProducto(tupla[4])
                            objetoConsulta.setSku(tupla[5])
                            objetoConsulta.setPrecio(tupla[6])
                            objetoConsulta.setUsuario(tupla[7])
                            
                        return objetoConsulta

                    else:
                        return False
            except:
                return False
        else:
            return False
    
    def create(self, variables, cat, subcat, marca, prod, sku, precio, idcliente, usuario):
        if variables.conexionBd:
            try:
                #Utilizamos la variable global
                with variables.conexionBd.cursor() as cursor:
                    
                    #creamos la sintaxis
                    query="INSERT INTO cat_producto(categoria, subcategoria, marca, producto, sku, precio, id_cliente, usuario) VALUES (?,?,?,?,?,?,?,?)"    
                    #Ingresamos los valores
                    cursor.execute(query, (cat,subcat, marca, prod, sku, precio, idcliente, usuario))
                    
                    return True
            except:
                return False
        else:
            return False

    def update(self, variables, cat, subcat, marca, prod, sku, precio, idcliente, usuario, id_producto):
        
        if variables.conexionBd:
            try:

                with variables.conexionBd.cursor() as cursor:
                    
                    query="UPDATE cat_producto set categoria=?, subcategoria=?, marca=?, producto=?, sku=?, precio=? WHERE id_cliente=? and usuario=? and id_producto=?"
                    
                    #Ingresamos los valores
                    cursor.execute(query, (cat, subcat, marca, prod, sku, precio, idcliente, usuario, id_producto))
                    
                    variables.conexionBd.commit()
                    
                    return True

            except:
                return False
        else:
            return False

    def delete(self, variables, idcliente, sku, id_producto):
        if variables.conexionBd:
            try:

                with variables.conexionBd.cursor() as cursor:
                    
                    query="DELETE from cat_producto where id_cliente=? and sku=? and id_producto=?"    
                    
                    #Ingresamos los valores
                    cursor.execute(query, (idcliente, sku, id_producto))
                    
                    variables.conexionBd.commit()
                    
                    return True
                   
            except:
                return False
        else:
            return False

