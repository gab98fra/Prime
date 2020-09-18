# -----------------------------------------------------------------------------------------------
# Nombre:       entproducts.py
# Autor:        Gabriel F
# Creado:       18 de Septiembre 2020
# Modificado:   18 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------

"""

           Entidad productos: Tabla cat_producto (sql server)
           El modulo es utilizado en: models_products


"""

class entProduct:

    def __init__(self):
        
        #Campos de la tabla BD: cat_producto, se declaran variables privadas y listas vacías
        self.__idproducto=[]
        self.__categoria=[]
        self.__subcategoria=[]
        self.__marca=[]
        self.__producto=[]
        self.__sku=[]
        self.__precio=[]
        self.__usuario=[]

    def setIdProducto(self,idproducto):
    
        self.__idproducto.append(idproducto)
    def getIdProducto(self):
    
        return self.__idproducto

    def setCategoria(self,cat):
    
        self.__categoria.append(cat)
    def getCategoria(self):
    
        return self.__categoria

    def setSubCategoria(self, sub):
    
        self.__subcategoria.append(sub)
    
    def getSubCategoria(self):
        return self.__subcategoria
    
    def setMarca(self, marca):
        self.__marca.append(marca)
    def getMarca(self):
        return self.__marca
    
    def setProducto(self, producto):
        self.__producto.append(producto)
    def getProducto(self):
        return self.__producto
    
    def setSku(self, sku):
        self.__sku.append(sku)
    def getSku(self):
        return self.__sku

    def setPrecio(self, precio):
        self.__precio.append(precio)
    def getPrecio(self):
        return self.__precio

    def setUsuario(self, usuario):
        self.__usuario.append(usuario)
    def getUsuario(self):
        return self.__usuario
