# -----------------------------------------------------------------------------------------------
# Nombre:       sistemas.py
# Autor:        Gabriel F
# Creado:       18 de Septiembre 2020
# Modificado:   18 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------

"""
    sección sistemas
"""

from PyQt5.QtGui import QIcon, QFont 
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFileDialog, QGroupBox, QLineEdit, QPushButton, QLabel, QComboBox, QMessageBox, 
                            QRadioButton,QSpinBox, QDoubleSpinBox, QStatusBar, QAction, QTableWidget, QWidget,
                            QGridLayout, QTableWidgetItem, QAbstractItemView, QMenu )

import sys
from os import getcwd, makedirs

#Módulos creados
from generales.message import message, message1, message2
from generales.models_login import models_login
from sistemas.models_users import models_users
from sistemas.models_products import models_products

class appSistema(QMainWindow):
#Clase principal
  def __init__(self, variables, parent=None):#clase padre
    #Inicializa superclase, su metodo init
    super(appSistema, self).__init__(parent)
    #Ventana: Sistemas
    self.setWindowTitle(variables.nomSistema + " Sistemas")
    self.setWindowIcon(QIcon("generales/image/logo.png"))
    self.showMaximized()

    #Modulo recibido a manera parametro
    self.variables=variables

    self.prueba="prueba"

    #Inicializar metodo 
    self.initUI()

  def initUI(self):
  #Widgets: Menu Principal/Barra Tareas/Barra Estado----------------------
    
    """
    #Fuente
    font1 = QFont()
    font1.setFamily("Segoe UI")
    font1.setPointSize(12)
    font1.setBold(True)
    font1.setWeight(100)
    self.setFont(font1)
    #Color al momento de seleccionar: morado /color fondo: blanco
    self.setStyleSheet("selection-background-color: rgb(168, 97, 255);\n"
        "background-color: rgb(255, 255, 255);")

    """
    
    #Barra de estado
    self.statusBar().showMessage("Bievenid@")

    #Objeto barra menu
    menu=self.menuBar()

    #menu: Padres
    menuSistemas = menu.addMenu("&Sistemas")   
    menuCatalogo = menu.addMenu("&Catálogo")
    menuInventario = menu.addMenu("&Inventario")
    menuReportes = menu.addMenu("&Reportes")
    menuBaseDatos = menu.addMenu("&Base de Datos")
    menuAyuda = menu.addMenu("&Ayuda")

    #menu: Hijos
    menuUsuario=QAction(QIcon("generales/image/usuarios.jpg"),"&Usuarios", self)
    menuUsuario.setShortcut("Ctrl+1")#Atajo
    menuUsuario.setStatusTip("Usuari@")
    menuUsuario.triggered.connect(self.userWidget)#Método o función a ejecutar
    menuSistemas.addAction(menuUsuario)
    
    menuParametro=QAction(QIcon("generales/image/catalogo1.jpg"),"&Actualizar conexión", self)
    menuParametro.setShortcut("Ctrl+2")
    menuParametro.setStatusTip("Actualizar conexión")
    menuParametro.triggered.connect(self.updateconexion) 
    menuSistemas.addAction(menuParametro)
    
    menuEmpresa=QAction(QIcon("generales/image/empresa.jpg"),"&Empresa", self)
    menuEmpresa.setShortcut("Ctrl+3")
    menuEmpresa.setStatusTip("Empresa")
    menuEmpresa.triggered.connect(self.message) 
    menuSistemas.addAction(menuEmpresa)
    
    #Sepador
    menuSistemas.addSeparator()

    menuSalir=QAction(QIcon("generales/image/salir.jpg"),"&Salir", self)
    menuSalir.setShortcut("Ctrl+4")
    menuSalir.setStatusTip("Salir")
    menuSalir.triggered.connect(self.closewindow) 
    menuSistemas.addAction(menuSalir)

    menuProveedores=QAction(QIcon("generales/image/proveedores.png"),"&Proveedores", self)
    menuProveedores.setShortcut("Ctrl+5")
    menuProveedores.setStatusTip("Proveedores")
    menuProveedores.triggered.connect(self.message) 
    menuCatalogo.addAction(menuProveedores)

    menuProductos=QAction(QIcon("generales/image/productos.jpg"),"&Productos", self)
    menuProductos.setShortcut("Ctrl+6")
    menuProductos.setStatusTip("Productos")
    menuProductos.triggered.connect(self.productWidget) 
    menuCatalogo.addAction(menuProductos)

    menuClientes=QAction(QIcon("generales/image/clientes1.png"),"&Clientes", self)
    menuClientes.setShortcut("Ctrl+7")
    menuClientes.setStatusTip("Clientes")
    menuClientes.triggered.connect(self.message) 
    menuCatalogo.addAction(menuClientes)

    menuCompras=QAction(QIcon("generales/image/ventas.jpg"),"&Compras", self)
    menuCompras.setShortcut("Ctrl+8")
    menuCompras.setStatusTip("Compras")
    menuCompras.triggered.connect(self.message) 
    menuInventario.addAction(menuCompras)

    menuMovimientos=QAction(QIcon("generales/image/movimientos.png"),"&Movimientos", self)
    menuMovimientos.setShortcut("Ctrl+9")
    menuMovimientos.setStatusTip("Movimientos")
    menuMovimientos.triggered.connect(self.message) 
    menuInventario.addAction(menuMovimientos)

    menuVentas=QAction(QIcon("generales/image/ventas"),"&Ventas", self)
    menuVentas.setShortcut("Ctrl+0")
    menuVentas.setStatusTip("Ventas")
    menuVentas.triggered.connect(self.message)
    menuInventario.addAction(menuVentas)

    menuRptCompras=QAction(QIcon("generales/image/reportes4.jpg"),"&Compras", self)
    menuRptCompras.setShortcut("Alt+1")
    menuRptCompras.setStatusTip("Reportes Compras")
    menuRptCompras.triggered.connect(self.message)
    menuReportes.addAction(menuRptCompras)

    menuRptMovimientos=QAction(QIcon("generales/image/reportes3.jpg"),"&Movimientos", self)
    menuRptMovimientos.setShortcut("Alt+2")
    menuRptMovimientos.setStatusTip("Reportes Movimientos")
    menuRptMovimientos.triggered.connect(self.message)
    menuReportes.addAction(menuRptMovimientos)

    menuRptVentas=QAction(QIcon("generales/image/reportes2.png"),"&Ventas", self)
    menuRptVentas.setShortcut("Alt+3")
    menuRptVentas.setStatusTip("Reportes Ventas")
    menuRptVentas.triggered.connect(self.message)
    menuReportes.addAction(menuRptVentas)

    menuRptBitacora=QAction(QIcon("generales/image/reportes2.png"),"&Bitácora", self)
    menuRptBitacora.setShortcut("Alt+4")
    menuRptBitacora.setStatusTip("Reportes Bitácora")
    menuRptBitacora.triggered.connect(self.message)
    menuReportes.addAction(menuRptBitacora)

    menuRespaldo=QAction(QIcon("generales/image/bd.jpg"),"&Respaldo", self)
    menuRespaldo.setShortcut("Alt+5")
    menuRespaldo.setStatusTip("Respaldo")
    menuRespaldo.triggered.connect(self.message)
    menuBaseDatos.addAction(menuRespaldo)

    menuTutorial=QAction(QIcon("generales/image/tutorial.jpg"),"&Tutorial", self)
    menuTutorial.setShortcut("Alt+6")
    menuTutorial.setStatusTip("Tutorial")
    menuTutorial.triggered.connect(self.message)
    menuAyuda.addAction(menuTutorial)

    menuAcerca=QAction(QIcon("generales/image/sistema1.png"),"&Acerca de...", self)
    menuAcerca.setShortcut("Alt+7")
    menuAcerca.setStatusTip("Acerca de...")
    menuAcerca.triggered.connect(self.message)
    menuAyuda.addAction(menuAcerca)

    #Objeto: tooBar
    self.toolbar=self.addToolBar("Toolbar")
    self.toolbar.setMovable(False) #Estático
    self.toolbar.setIconSize(QSize(35, 35))#Tamaño de los iconos
    self.toolbar.setOrientation(Qt.Horizontal)#Orientación
    #Separador
    self.toolbar.addSeparator()

    #Asignar los menus al toolBar
    self.toolbar.addAction(menuUsuario)
    self.toolbar.addAction(menuParametro)
    self.toolbar.addAction(menuEmpresa)
    
    self.toolbar.addSeparator()
    
    self.toolbar.addAction(menuProveedores)
    self.toolbar.addAction(menuProductos)
    self.toolbar.addAction(menuClientes)
    
    self.toolbar.addSeparator()

    self.toolbar.addAction(menuCompras)
    self.toolbar.addAction(menuMovimientos)
    self.toolbar.addAction(menuVentas)
    
    self.toolbar.addSeparator()
    
    self.toolbar.addAction(menuRptCompras)
    self.toolbar.addAction(menuRptMovimientos)
    self.toolbar.addAction(menuRptVentas)
    self.toolbar.addAction(menuRptBitacora)
    
    self.toolbar.addSeparator()
    
    self.toolbar.addAction(menuRespaldo)
    self.toolbar.addSeparator()

    self.toolbar.addAction(menuTutorial)
    self.toolbar.addAction(menuAcerca)
    
    self.toolbar.addSeparator()
    self.toolbar.addAction(menuSalir)

    #--------Widgets principales:espacio trabajo--------------------------
    
    #Objeto: centralWidget1/#Asignar a la ventana
    self.centralWidget1=QWidget(self)
    self.setCentralWidget(self.centralWidget1)
    
    #Objeto Principal, estará cambiando dependiento del menu hijo (s) seleccionado (s)
    self.widgetPrincipal=QWidget(self.centralWidget1)
    
    #Objeto Qlabel
    self.label1=QLabel(self.widgetPrincipal)
    self.label1.move(550,250)
    self.label1.setText("Bienvenid@")

#-------------------------Mensaje: No disponible------------------
  def message(self):
    message2(self)

#-------------------------MenuHijo: Usuarios------------------
  def userWidget(self):
  #Widgets para menu Hijo: Usuario
    
    #cerramos  primero, el widgetPrincipal
    self.widgetPrincipal.close()

    #Objeto: widgent1
    self.widget1=QWidget(self.centralWidget1)
    self.widget1.setGeometry(10,10,600,200)
    self.widget1.show()
    #Asignamos ahora el widget1, como Principal
    self.widgetPrincipal=self.widget1

    #Objeto: gridLayout1
    self.gridLayout1=QGridLayout(self.widget1)
    
    #Objeto: Qtable- número de columnas/registros
    self.table_user=QTableWidget(self.widget1)
    self.table_user.setColumnCount(4)
    self.table_user.setRowCount(0)

    #Campos de la tabla
    self.table_user.setHorizontalHeaderItem(0,QTableWidgetItem("Id Cliente"))
    self.table_user.setHorizontalHeaderItem(1,QTableWidgetItem("Usuario"))
    self.table_user.setHorizontalHeaderItem(2,QTableWidgetItem("Contraseña"))
    self.table_user.setHorizontalHeaderItem(3,QTableWidgetItem("Rol"))

    #QPushButton
    qPushButton1=QPushButton(self.widget1)
    qPushButton1.setText("Consultar Usuarios")
    qPushButton2=QPushButton(self.widget1)
    qPushButton2.setText("Agregar Usuario")
    qPushButton3=QPushButton(self.widget1)
    qPushButton3.setText("Modificar Usuario")
    qPushButton4=QPushButton(self.widget1)
    qPushButton4.setText("Eliminar Usuario")
    
    #tabla y QPushButton1 se agregan al gridLayout1: row, colum, anchorow, anchocolum
    self.gridLayout1.addWidget(self.table_user,0,0,4,1)
    self.gridLayout1.addWidget(qPushButton1,0,1,1,1)
    self.gridLayout1.addWidget(qPushButton2,1,1,1,1)
    self.gridLayout1.addWidget(qPushButton3,2,1,1,1)
    self.gridLayout1.addWidget(qPushButton4,3,1,1,1)

    #--------------Eventos PushButton----------------------------------------
    
    qPushButton1.clicked.connect(self.searchUser)
    qPushButton2.clicked.connect(self.addUser)
    qPushButton3.clicked.connect(self.updateUser)
    qPushButton4.clicked.connect(self.deleteUser)

  def searchUser(self):
  #Consulta Usuarios registrados en BD
    
    #Objeto a través del modulo: moduser /metod read
    consultaObjeto=models_users()
    resultado=consultaObjeto.read(self.variables, self.variables.usuarioIdCliente)

    if resultado:
      #guardamos los valores de la consulta en: listas
      user=resultado.getUser()
      password=resultado.getPassword()
      rol=resultado.getRol()

      #Cambiamos el número de filas en la tabla: numero de registros encontrados
      self.table_user.setRowCount(len(user))

      for row in range(len(user)):
      #Recorremos las listas y ejecutamos la función
         
        #Función, enviamos los valores en cada iteración
        self.adduser_in_table(row, user[row], password[row], rol[row])

    else:
      message("Aviso", "No encontramos ningún row")

  def adduser_in_table(self, row, user, password, rol):
  #Agrega los datos encontrados a la table_user
  
    #insertar los valores: row, colum
    self.table_user.setItem(row,0, QTableWidgetItem(str(self.variables.usuarioIdCliente)))
    self.table_user.setItem(row,1, QTableWidgetItem(user))
    self.table_user.setItem(row,2, QTableWidgetItem(password))
    self.table_user.setItem(row,3, QTableWidgetItem(rol))

  def addUser(self):
  #Ejecuta la clase: menu_user_ad

    menu_user_add(self.variables, self).exec_()
 
  def updateUser(self):
  #Ejecuta la clase: menu_user_update

    #Identificamos los usuarios en la BD, para después enviar como parámetro a la clase:menu_user_update
    #Creción del objeto, a través de: modelouusuario/ejecución metodo read
    objectUser=models_users()
    resultado=objectUser.read(self.variables, self.variables.usuarioIdCliente)

    if resultado:
    #si existe

      #Guardamos los valores: usuarios en variable lista
      user=resultado.getUser()
      
      #Ejecutamos la clase, enviadole el parametro
      menu_user_update(self.variables, user, self).exec_()

    else:
    #Si no existe: no se crea ningúna ventana de actualizar
      message("Advertencia", "No hay conexión a la red")

  def deleteUser(self):
  #Ejecuta la clase: menu_user_delete
    
    #Identificamos los usuarios en la BD, para después enviar como parametro a la clase:menu_user_update
    objeto=models_users()
    resultado=objeto.read(self.variables, self.variables.usuarioIdCliente)

    if resultado:
    
      user=resultado.getUser()
      """
      #Creación de objeto/ejecución objeto (ventana)
      ventanaUsuario=menu_user_delete(self.variables)
      ventanaUsuario.ventanEliminarUsuario(userEncontrados)
      ventanaUsuario.exec_()
      """
      #Ejecuta la clase
      menu_user_delete(self.variables, user, self).exec_()

    else:
    #Si no existe
      message("Advertencia", "No hay conexión a la red")

#-------------------------MenuHijo: Actualizar conexión------------------

  def updateconexion(self):
  #Actualiza la conexion al servidor
    models_login.conexion()

#-------------------------MenuHijo: Salir------------------
  def closewindow(self):
  #Cierra la ventana en ejecución
    self.close()

#-------------------------MenuHijo: Productos------------------
  def productWidget(self):
  #widgets para menu Hijo: Productos
    
    #Cerrar el widget activo
    self.widgetPrincipal.close()
    
    #Objeto:
    widget2=QWidget(self.centralWidget1)
    widget2.move(20,20)
    widget2.resize(1300,570)#column, row
    widget2.show()
    
    #Se convierte el widget principal o activo
    self.widgetPrincipal=widget2

    #Objeto: gridLayout
    gridLayout2=QGridLayout(widget2)

    #Objeto Qtable
    self.tableProduct=QTableWidget(widget2)
    self.tableProduct.setEditTriggers(QAbstractItemView.NoEditTriggers)#Restringir edidición
    self.tableProduct.setAlternatingRowColors(True)#Colores alternados por fila
    self.tableProduct.setSelectionBehavior(QAbstractItemView.SelectRows)#Selecciona toda la fila
    self.tableProduct.setSelectionMode(QAbstractItemView.SingleSelection)#seleccionar una fila a la vez. O celda a la vez

    self.tableProduct.setColumnCount(12)
    self.tableProduct.setRowCount(0)

    #Campos de la tabla
    encabezado=["Id_cliente", "Id_producto","Categoría", "Subcategoría", "Marca", "Producto", "Sku",
                "Precio", "Descuento", "F. Registro", "Estatus", "Usuario"]
    # Establecer las etiquetas de encabezado horizontal usando etiquetas
    self.tableProduct.setHorizontalHeaderLabels(encabezado)
        
    #Qmenu  --QAccion
    #-------No utilizado--------
    menu1=QMenu()
    list1=("Categoría1", "Categorí2")
    for indice, columna in enumerate(list1, start=0):
      action1=QAction(columna, menu1)
      action1.setCheckable(True)
      action1.setChecked(True)
      action1.setData(indice)
      menu1.addAction(action1)


    menu2=QMenu()
    list2=("Buscar en la tabla", "Buscar en BD")
    for indice, columna in enumerate(list2, start=0):
      action2=QAction(columna, menu2)
      #action2.setCheckable(True)
      action2.setChecked(True)
      action2.setData(indice)
      menu2.addAction(action2)

    menu3=QMenu()
    list3=("excel", "Csv")
    for indice, columna in enumerate(list3, start=0):
      action3=QAction(columna, menu3)
      #action3.setCheckable(True)
      action3.setChecked(True)
      action3.setData(indice)
      menu3.addAction(action3)

    menu4=QMenu()
    list4=("excel", "Csv")
    for indice, columna in enumerate(list4, start=0):
      action4=QAction(columna, menu4)
      action4.setCheckable(True)
      action4.setChecked(True)
      action4.setData(indice)
      menu4.addAction(action4)

    #pushbutton
    pushbutton1=QPushButton(widget2)
    pushbutton1.setText("Mostrar Productos")
    #pushbutton1.setMenu(menu2)#menu
    pushbutton1.setFixedWidth(120)
    pushbutton1.setCursor(Qt.PointingHandCursor)#logo mano

    pushbutton2=QPushButton(widget2)
    pushbutton2.setText("Agregar Producto")
    pushbutton2.setFixedWidth(120)
    self.button_update=QPushButton(widget2)
    self.button_update.setText("Actualizar Producto")
    self.button_update.setEnabled(False)#Inhabilitar botón
    self.button_update.setFixedWidth(120)
    self.button_delete=QPushButton(widget2)
    self.button_delete.setText("Eliminar Producto")
    self.button_delete.setEnabled(False)#Inhabilitar botón
    self.button_delete.setFixedWidth(120)
    pushbutton5=QPushButton(widget2)
    pushbutton5.setText("Buscar producto")
    pushbutton5.setMenu(menu2)#menu
    pushbutton5.setFixedWidth(120)
    pushbutton6=QPushButton(widget2)
    pushbutton6.setText("Exportar datos")
    pushbutton6.setFixedWidth(120)
    pushbutton6.setMenu(menu3)#menu
    pushbutton7=QPushButton(widget2)
    pushbutton7.setText("Importar datos")
    pushbutton7.setFixedWidth(120)
    pushbutton7.setMenu(menu4)#Asignamos el menu

    #Qlabel
    qlabel1=QLabel(widget2)
    qlabel1.setText("Buscar por Sku")
    
    #QlineEdit
    qline1=QLineEdit(widget2)
    qline1.setFixedWidth(220)
    qline1.setPlaceholderText("Buscar por sku")

    #table,pushbutton1 asignando a gridLayput2: row, colum, anchorow, anchocolum
    gridLayout2.addWidget(pushbutton1,0,0,1,1)
    gridLayout2.addWidget(pushbutton2,0,1,1,1)
    gridLayout2.addWidget(self.button_update,0,2,1,1)
    gridLayout2.addWidget(self.button_delete,0,3,1,1)
    gridLayout2.addWidget(qlabel1, 0, 4,1,1)
    gridLayout2.addWidget(qline1, 0, 5,1,1)
    gridLayout2.addWidget(pushbutton5, 0, 6,1,1)
    gridLayout2.addWidget(pushbutton6, 0, 8,1,1)
    gridLayout2.addWidget(pushbutton7, 0, 9,1,1)
    gridLayout2.addWidget(self.tableProduct,1,0,1,10)
 
    #--------------------Eventos pushbutton-------------------------------
    pushbutton1.clicked.connect(self.searchProduct)
    pushbutton2.clicked.connect(self.addProduct)
    self.button_update.clicked.connect(self.updateProduct)
    self.button_delete.clicked.connect(self.deleteProduct)
    
    #Doble click en cualquier celda
    self.tableProduct.itemDoubleClicked.connect(self.doubleClick)
    menu3.triggered.connect(self.exportdocument)
    menu4.triggered.connect(self.importdocument)

  def searchProduct(self):
  #consulta los productos registrados en BD
    
    #Consulta en BD
    objetoConsulta=models_products()
    resultado=objetoConsulta.read(self.variables, self.variables.usuarioIdCliente)

    if resultado:
    #si existe el objeto

      #guardamos los resultados en variables listas
      id_producto=resultado.getIdProducto()
      categoria=resultado.getCategoria()
      subcategoria=resultado.getSubCategoria()
      marca=resultado.getMarca()
      producto=resultado.getProducto()
      sku=resultado.getSku()
      precio=resultado.getPrecio()

      #Limpiar tabla
      self.tableProduct.clearContents()
      
      #Insertar filas: cantidad de datos encontrados
      self.tableProduct.setRowCount(len(id_producto))    

      #Activación de botones
      self.button_update.setEnabled(True)
      self.button_delete.setEnabled(True)

      if len(id_producto)>=1:#la longitud es mayor a 1

        for row in range(len(id_producto)):
        #imprimimos los registros encontrados
          
          #Función, enviamos los valores en cada iteración
          
          self.addproduct_in_table(row,str(id_producto[row]),categoria[row], subcategoria[row], 
                                    marca[row], producto[row], str(sku[row]),str(precio[row]) )
        
    else:
      message("Aviso", "No encontramos ningún row")  

  def addproduct_in_table(self, row, id_producto, categoria, subcategoria, marca, producto, sku, precio):
  #Imprime los datos en la table_product
    
    #tableproduct: row, column
    self.tableProduct.setItem(row,0, QTableWidgetItem(str(self.variables.usuarioIdCliente)))
    self.tableProduct.setItem(row,1, QTableWidgetItem(id_producto))
    self.tableProduct.setItem(row,2, QTableWidgetItem(categoria))
    self.tableProduct.setItem(row,3, QTableWidgetItem(subcategoria))
    self.tableProduct.setItem(row,4, QTableWidgetItem(marca))
    self.tableProduct.setItem(row,5, QTableWidgetItem(producto))
    self.tableProduct.setItem(row,6, QTableWidgetItem(sku))
    self.tableProduct.setItem(row,7, QTableWidgetItem(precio))

  def addProduct(self):
  #Ejecuta la clase: menu_product_add
    
    menu_product_add(self).exec_()

  def updateProduct(self):
  #Ejecuta la clase: menu_product_update
    
    #si seleccionamos algún dato
    indices=self.tableProduct.selectedIndexes()

    if indices:

      #Accedemos los valores de la fila seleccionada, variable list
      self.select_row_product=[dato.text() for dato in self.tableProduct.selectedItems()]    

      """    
      filaseleccionada=self.tableProduct.selectedItems()
      texto= filaselecionada[1].text()#Valor de la posición 1
      """
      menu_product_update(self).exec_()

    else:
    #Fila no seleccionada
      message("Fila no seleccionada", "Seleccione la fila a actualizar")

  def deleteProduct(self):
  #Elimina productos

    #si seleccionamos algún dato
    indices=self.tableProduct.selectedIndexes()

    if indices:

      #Identificamos la fila seleccionada
      filaseleccionada=self.tableProduct.selectedItems()
        
      #Valores seleccionados
      id_producto=filaseleccionada[1].text()
      sku=filaseleccionada[6].text()


      resultado = QMessageBox.question(self, "Eliminar producto", 
                "¿Desea eliminar el producto:  {} ?".format(sku), QMessageBox.Yes | QMessageBox.No)
      
      if resultado==QMessageBox.Yes:

        #Eliminar producto en BD
        delete_producto=models_products()
        echo=delete_producto.delete(self.variables, self.variables.usuarioIdCliente, sku, id_producto)

        if echo:
          
          message("Eliminado", "Se eliminó correctamente de la BD")  
            
          #Eliminar producto seleccionado de la tabla
          #Fila seleccionada/eliminar de la tabla
          numero_fila=filaseleccionada[0].row()
          self.tableProduct.removeRow(numero_fila)
          self.tableProduct.clearSelection()
          
        else:
          message("No Eliminado", "El producto no fue eliminado")  
     
      else:
        pass

    else:
    #Fila no seleccionada
      message("Fila no seleccionada", "Seleccione la fila a eliminar")

  def exportdocument(self, seleccionado):
  #exportar documento
    
    #type: int 0,1
    datoseleccionado = seleccionado.data()

    if seleccionado.isChecked():  
    #Estatus inicial
      pass

    else:
    #Exportar datos a excel o csv

      if datoseleccionado==0:
      #Exportar a Excel
        
        #número de filas
        #num_row=self.tableProduct.rowCount()
        
        if self.tableProduct.rowCount()==0:
        #No hay datos
          QMessageBox.critical(self, "Advenrtencia", "No hay datos en la tabla",
                                 QMessageBox.Ok)
        
        else:
        #Si hay datos en la tabla

          nombreArchivo, opcion_seleccionado = QFileDialog.getSaveFileName(self, "Exportar a excel", 
                              "Listado de usuarios",  "Excel (*.xlsx);;All Files (*)",
                              options=QFileDialog.Options())

          #------------------Pendiente Sintaxis para crear archivo de excel----------

      
      else:
      #Exporta a csv
        pass

  def importdocument(self, seleccionado):
  #importar documento
    
    #type: int 0,1
    datoseleccionado = seleccionado.data()

    if seleccionado.isChecked():  
    #Estatus inicial
      pass

    else:
    #Exportar datos a excel o csv
      if datoseleccionado==1:
        #Sintaxis permite seleccionar un archivo
        imagen, extension = QFileDialog.getOpenFileName(self, "Seleccionar ", getcwd(),
                                                        "Archivo (*.xlsx *.csv)",
                                                        options=QFileDialog.Options())

  def doubleClick(self, celda_seleccionada):
  #Doble clik
    QMessageBox.warning(self, "Aviso", "Con los botones superiores de la tabla"
                            " seleccione que desea realizar con el dato {}.   ".format(celda_seleccionada.text()), QMessageBox.Ok)

  def closeEvent(self, event):
  #Cerrar ventana Sistemas

    close = QMessageBox(self)

    close.setWindowTitle("¿Salir de PRIME?")
    close.setIcon(QMessageBox.Question)
    close.setText("¿Estás seguro que desea salir Prime Sistemas?   ")
    botonSalir = close.addButton("Salir", QMessageBox.YesRole)
    botonCancelar = close.addButton("Cancelar", QMessageBox.NoRole)
            
    close.exec_()
            
    if close.clickedButton() == botonSalir:
      event.accept()
    else:
      event.ignore()


#-------------------------CLASES COLABORADORES-----------------
class menu_user_add(QDialog):
#menuHijo: Usuarios
  def __init__(self, variables, parent=None):#clase hijo
    super(menu_user_add, self).__init__()

    #Modulo recibido a manera parámetro
    self.variables=variables
    #Permite interactuar con la clase: Padre
    self.parent = parent
    
    self.setWindowTitle("Agregar Usuario")
    self.setWindowIcon(QIcon("generales/image/logo.png"))
    self.resize(469, 377)
    #Oculta los botones superiores y unicamente activa el boton close ventana
    self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
    

    self.initUI()

  def initUI(self):
  #Widgets
    label1 = QLabel(self)
    label1.setGeometry(QRect(100, 50, 141, 21))
    label1.setText("Ingrese el Usuario: ")
    label2 = QLabel(self)
    label2.setGeometry(QRect(100, 110, 141, 21))
    label2.setText("Ingrese el Password: ")
    label3 = QLabel(self)
    label3.setGeometry(QRect(100, 160, 141, 21))
    label3.setText("Seleccione el Rol: ")

    self.lineEdit1 = QLineEdit(self)
    self.lineEdit1.setGeometry(QRect(230, 50, 113, 20))
    self.lineEdit2 = QLineEdit(self)
    self.lineEdit2.setGeometry(QRect(230, 110, 113, 20))
    self.comboBox1 = QComboBox(self)
    self.comboBox1.setGeometry(QRect(230, 160, 111, 21))
    #Agregamos los elementos
    self.comboBox1.addItems(["","cajero","supervisor", "admin"])

    pushButton1 = QPushButton(self)
    pushButton1.setGeometry(QRect(270, 280, 75, 23))
    pushButton1.setText("Agregar")
    pushButton2 = QPushButton(self)
    pushButton2.setGeometry(QRect(100, 280, 75, 23))
    pushButton2.setText("Cancelar")

    #-------------------Funciones------------------------
    pushButton1.clicked.connect(self.verifyAdd)
    pushButton2.clicked.connect(self.closeWindow)

  def verifyAdd(self):
  #Valida y crea el usuario en la BD
    
    if self.lineEdit1.text()!="" and self.lineEdit2.text()!="" and self.comboBox1.currentText()!="":
    #Validación campos no vacios

      #Alacenar en variables
      user=self.lineEdit1.text()
      password=self.lineEdit2.text()
      rol=self.comboBox1.currentText()

      #objeto a traves del modulo: models_users
      objetoCreate=models_users()
      resultado=objetoCreate.create(self.variables, user, password, rol, self.variables.usuarioIdCliente)

      if resultado:
      #Validamos que se haya creado el usuario en BD

        message("Usuario Creado","El usuario fue creado exitosamente")
        #Realizamos consulta e imprimimos nuevamente: a través de la clase padre
        self.parent.searchUser()
        self.closeWindow()

      else:
        message("Usuario No creado","Las posibles razones: no hay conexión a la red o los campos superan los 10 caracteres permitidos")
        self.closeWindow()

    else:
    #Enviamos un message de advertencia
      message("IMPORTANTE","Favor de ingresar los datos solicitados")
  
  def closeWindow(self):
    self.close()

class menu_user_update(QDialog):
#menuHijo: Usuarios
  def __init__(self, variables, user, parent=None):#clase hijo
    super(menu_user_update, self).__init__()
    self.setWindowTitle("Actualizar Usuario")
    self.setWindowIcon(QIcon("generales/image/logo.png"))
    self.resize(469, 377)
    self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
    
    #Modulos recibidos a manera parámetro
    self.variables=variables
    self.parent=parent
    
    self.initUI(user)

  def initUI(self, listacomboBox):
  #Widgets

    self.label1 = QLabel(self)
    self.label1.setGeometry(QRect(100, 50, 141, 21))
    self.label1.setText("Selecione el Usuario: ")
    self.label2 = QLabel(self)
    self.label2.setGeometry(QRect(100, 110, 141, 21))
    self.label2.setText("Ingrese el Usuario: ")
    self.label3 = QLabel(self)
    self.label3.setGeometry(QRect(100, 170, 141, 21))
    self.label3.setText("Ingrese el Password: ")
    self.label4 = QLabel(self)
    self.label4.setGeometry(QRect(100, 230, 141, 21))
    self.label4.setText("Seleccione el Rol: ")

    self.comboBox1 = QComboBox(self)
    self.comboBox1.setGeometry(QRect(230, 50, 111, 21))
    #Agregamos el primer elemento, 
    self.comboBox1.addItem("")

    #A través del parametro recibido, agregamos los usuarios
    for usuario in listacomboBox:
      #Agregamos uno a uno
      self.comboBox1.addItem(usuario)
    
    self.lineEdit1 = QLineEdit(self)
    self.lineEdit1.setGeometry(QRect(230, 110, 113, 20))
    self.lineEdit2 = QLineEdit(self)
    self.lineEdit2.setGeometry(QRect(230, 170, 113, 20))
    self.comboBox2 = QComboBox(self)
    self.comboBox2.setGeometry(QRect(230, 230, 111, 21))
    #Agregamos los elementos
    self.comboBox2.addItems(["","admin", "supervisor", "cajero"])

    self.pushButton1 = QPushButton(self)
    self.pushButton1.setGeometry(QRect(270, 300, 75, 23))
    self.pushButton1.setText("Modificar")
    self.pushButton2 = QPushButton(self)
    self.pushButton2.setGeometry(QRect(100, 300, 75, 23))
    self.pushButton2.setText("Cancelar")

    #-------------------Funciones------------------------
    self.pushButton1.clicked.connect(self.verifyUpdate)
    self.pushButton2.clicked.connect(self.closeWindow)
  
  def verifyUpdate(self):
  #Permite actualizar un usuario existente en la BD
    
    #validamos los campos no estén vacios, para posterior modificar el usuario BD
    if self.lineEdit1.text()!="" and self.lineEdit2.text()!="" and self.comboBox1.currentText()!="" and self.comboBox2.currentText()!="":

      
      if self.comboBox1.currentText()==self.variables.usuarioNom :
      #Si es el superUsuario
        #Tomar el nuevo pass
        password=self.lineEdit2.text()
        
        #Creamos el objeto/ejecutamos el metodo update enviandole parametros correspondientes
        objetoModificar=models_users()
        resultado=objetoModificar.update(self.variables, self.variables.usuarioNom, password, self.variables.usuarioRol, self.variables.usuarioIdCliente, self.variables.usuarioNom)

        #Si fue exitos
        if resultado:
          message("Modificado Exitosamente","Para la cuenta super-usuario, por seguridad unicamente se permite modficar el password. El usuario y rol son los mismos")
          
          #clase padre: permite mostrar los nuevos datos en table_user
          self.parent.searchUser()
          self.closeWindow()

        else:
          message("Aviso","El usuario no se actualizó, revise su conexión a la red")
          self.closeWindow()

      else:
      #Si es diferente al superUsuario

        user=self.comboBox1.currentText()

        userNew=self.lineEdit1.text()
        passwordNew=self.lineEdit2.text()
        rolNew=self.comboBox2.currentText()

        #Creamos el objeto/ejecutamos el metodo update enviandole paraetros correspondientes
        objetoModificar=models_users()
        resultado=objetoModificar.update(self.variables, userNew, passwordNew, rolNew, self.variables.usuarioIdCliente, user)

        #Se ejecuta el modulo, para actualizar el usuario en la BD
        if resultado:
          message("Aviso","El usuario fue actualizado exitosamente")
          
          #clase padre: permite mostrar los nuevos datos en table_user
          self.parent.searchUser()
          self.closeWindow()

        else:
          message("Aviso","En cada campo puede ingresar un máximo de 10 caracteres")
          self.closeWindow()

    else:
      #Enviamos un message de advertencia
      message("IMPORTANTE","Favor de ingresar los datos solicitados")
  
  def closeWindow(self):
    self.close()

class menu_user_delete(QDialog):
#menuHijo: Usuarios
  def __init__(self, variables, user, parent=None):
    super(menu_user_delete, self).__init__()#clase hijo
    self.setWindowTitle("Eliminar Usuario")
    self.setWindowIcon(QIcon("generales/image/logo.png"))
    self.resize(469, 377)
    #Oculta los botones superiores
    self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

    #Modulo recibido a manera parametro
    self.variables=variables
    self.parent=parent

    self.initUI(user)

  def initUI(self, listacomboBox):
  #Widgets
    label1 = QLabel(self,)
    label1.setGeometry(QRect(100, 50, 141, 21))
    label1.setText("Seleccione el Usuario: ")
    
    self.comboBox1 = QComboBox(self)
    self.comboBox1.setGeometry(QRect(230, 50, 111, 21))
    #Agregamos el primer elemento, en método usuarioCombox se agregan más elementos
    self.comboBox1.addItem("")
    #Agregamos los usuarios recibidos como parametro
    for user in range(len(listacomboBox)):
      if user==0:
        pass
        #Ignoramos el primero elemento, por ser admin
      else:
        #agregamos uno por uno
        self.comboBox1.addItem(listacomboBox[user])
    

    pushButton1 = QPushButton(self)
    pushButton1.setGeometry(QRect(270, 280, 75, 23))
    pushButton1.setText("Eliminar")
    pushButton2 = QPushButton(self)
    pushButton2.setGeometry(QRect(100, 280, 75, 23))
    pushButton2.setText("Cancelar")

    #-------------------Funciones------------------------
    pushButton1.clicked.connect(self.verifyDelete)
    pushButton2.clicked.connect(self.closewindow)

  def verifyDelete(self):
  #Permie eliminar el usuario indicado

    if self.comboBox1.currentText()!="":
    #No vacío
      
      #Mensaje de advertencia
      resultado=QMessageBox.question(self, "Eliminar...", "¿Seguro que desea eliminar el usuario?",QMessageBox.Yes | QMessageBox.No)

      #Si dice que sí, procedemos a eliminar
      if resultado==QMessageBox.Yes:
        
        #guardamos el usuario seleccionado
        user=self.comboBox1.currentText()

        #Creación de objeto/ejecución metodo delete
        objetoEliminar=models_users()
        resultado=objetoEliminar.delete(self.variables, self.variables.usuarioIdCliente,user)

        if resultado:
          message("Eliminado", "El usuario fue eliminado de la BD")
          
          #Actualizar tabla
          self.parent.searchUser()
          self.closewindow()

        else:
          message("No Eliminado", "El usuario no fue eliminado de la BD")
    
      else:
      #Cerramos la ventana 
        self.closewindow()
    else:
      message("Importante", "Tiene que seleccionar un usuario que desee eliminar")

  def closewindow(self):
    self.close()

class menu_product_add(QDialog):
#menuHijo: Productos. También ejecutado desde la SECCION: COBRAR
  def __init__(self, parent=None):#clase hijo
    super(menu_product_add, self).__init__()
    self.setWindowTitle("Agregar Producto")
    self.setWindowIcon(QIcon("generales/image/logo.png"))
    self.resize(480, 220)#col, row
    self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

    #Interacción entre clase padre e hijo
    self.parent=parent

    #Métodos
    self.initUI()

  def initUI(self):
  #Widgets

    groupBox=QGroupBox(self)
    groupBox.move(20,20)
    groupBox.resize(450,160)
    groupBox.setTitle("Agregar productos")

    label1 = QLabel(groupBox)
    label1.setGeometry(QRect(30, 30, 70, 20))#col, row (x,y)
    label1.setText("Categoría: ")
    self.comboBox1 = QComboBox(groupBox)
    self.comboBox1.setGeometry(QRect(100, 30, 120, 20))
    self.comboBox1.addItems(["categoria 1", "categoria 2", "categoria 2"])

    label2 = QLabel(groupBox)
    label2.setGeometry(QRect(230, 30, 70, 20))
    label2.setText("Subcategoría: ")
    self.comboBox2 = QComboBox(groupBox)
    self.comboBox2.setGeometry(QRect(310, 30, 120, 20))
    self.comboBox2.addItems(["subcategoria 1", "subcategoria 2", "subcategoria 2"])

    label3 = QLabel(groupBox)
    label3.setGeometry(QRect(30, 70, 70, 20))
    label3.setText("Marca: ")
    self.comboBox3 = QComboBox(groupBox)
    self.comboBox3.setGeometry(QRect(100, 70, 120, 20))
    self.comboBox3.addItems(["marca1","marca2","marca3", "marca4"])
    
    label4 = QLabel(groupBox)
    label4.setGeometry(QRect(230, 70, 70, 20))
    label4.setText("Producto: ")
    self.lineEdit1=QLineEdit(groupBox)
    self.lineEdit1.setGeometry(QRect(310, 70, 120, 20))
    
    label5 = QLabel(groupBox)
    label5.setGeometry(QRect(30, 100, 70, 20))
    label5.setText("Sku: ")
    self.lineEdit2=QLineEdit(groupBox)
    self.lineEdit2.setGeometry(QRect(100, 100, 120, 20))

    label6 = QLabel(groupBox)
    label6.setGeometry(QRect(230, 100, 70, 20))
    label6.setText("Precio: ")
    self.doubleSpinBox1=QDoubleSpinBox(groupBox)
    self.doubleSpinBox1.setGeometry(QRect(310, 100, 120, 20))

    label7 = QLabel(groupBox)
    label7.setGeometry(QRect(30, 130, 70, 20))
    label7.setText("Descuento: ")
    self.lineEdit3=QLineEdit(groupBox)
    self.lineEdit3.setGeometry(QRect(100, 130, 120, 20))
    self.lineEdit3.setInputMethodHints(Qt.ImhDigitsOnly)

    label3 = QLabel(groupBox)
    label3.setGeometry(QRect(230, 130, 70, 20))
    label3.setText("Estatus: ")
    self.comboBox4 = QComboBox(groupBox)
    self.comboBox4.setGeometry(QRect(310, 130, 120, 20))
    self.comboBox4.addItems(["Activo","Baja"])
  
    pushButton1 = QPushButton(self)
    pushButton1.setGeometry(QRect(340, 190, 70, 20))
    pushButton1.setText("Agregar")
    pushButton2 = QPushButton(self)
    pushButton2.setGeometry(QRect(130, 190, 70, 20))
    pushButton2.setText("Cancelar")

    #-------------------Funciones------------------------
    pushButton1.clicked.connect(self.verifyAdd)
    pushButton2.clicked.connect(self.closewindow)

  def verifyAdd(self):
  #Validar y crear producto en BD

    if self.comboBox1.currentText()!="" and self.comboBox2.currentText()!="" and self.comboBox3.currentText()!="" and self.lineEdit1.text()!="" and self.lineEdit2.text()!="":
      
      #almacenamos los valores
      categoria=self.comboBox1.currentText()
      subcategoria=self.comboBox2.currentText()
      marca=self.comboBox3.currentText()
      producto=self.lineEdit1.text()
      sku=self.lineEdit2.text()
      precio=self.doubleSpinBox1.value()
      
      #Cread producto en BD
      objetoConsulta=models_products()
      resultado=objetoConsulta.create(self.parent.variables, categoria, subcategoria, marca, producto, sku, precio, self.parent.variables.usuarioIdCliente, self.parent.variables.usuarioNom)
      
      if resultado: 
        
        message("Aviso","El producto fue creado exitosamente")
        
        #Fila nueva al inicio de la tabla
        self.parent.tableProduct.insertRow(0)
    
        #Imprimir los valores en la fila nueva
        self.parent.addproduct_in_table(0,"pendiente", categoria, subcategoria, marca, producto, sku, str(precio))

        self.closewindow()

      else:
        message("Aviso","En cada campo puede ingresar un máximo de 10 caracteres")
        self.closewindow()

    else:
    #Mensaje de adventencia
      message("IMPORTANTE","Favor de ingresar los datos solicitados")
  
  def closewindow(self):
    self.close()

class menu_product_update(QDialog):
#menuHijo: Productos
  def __init__(self, parent=None):#clase hijo
    super(menu_product_update, self).__init__()
    self.setWindowTitle("Agregar Producto")
    self.setWindowIcon(QIcon("generales/image/logo.png"))
    self.resize(480, 220)#col, row
    self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

    self.parent=parent

    self.initUI()

  def initUI(self):
  #Widgets

    #Datos de la fila seleccionada--variable de clase padre
    categoria=self.parent.select_row_product[2]
    subcategoria=self.parent.select_row_product[3]
    marca=self.parent.select_row_product[4]
    producto=self.parent.select_row_product[5]
    sku=self.parent.select_row_product[6]
    

    groupBox=QGroupBox(self)
    groupBox.move(20,20)
    groupBox.resize(450,160)
    groupBox.setTitle("Agregar productos")


    label1 = QLabel(groupBox)
    label1.setGeometry(QRect(30, 30, 70, 20))#col, row (x,y)
    label1.setText("Categoría: ")
    self.cb_categoria = QComboBox(groupBox)
    self.cb_categoria.setGeometry(QRect(100, 30, 120, 20))
    self.cb_categoria.addItems([categoria])#seleccionado en tabla

    label2 = QLabel(groupBox)
    label2.setGeometry(QRect(230, 30, 70, 20))
    label2.setText("Subcategoría: ")
    self.cb_subcategoria = QComboBox(groupBox)
    self.cb_subcategoria.setGeometry(QRect(310, 30, 120, 20))
    self.cb_subcategoria.addItems([subcategoria])#seleccionado en tabla

    label3 = QLabel(groupBox)
    label3.setGeometry(QRect(30, 70, 70, 20))
    label3.setText("Marca: ")
    self.cb_marca = QComboBox(groupBox)
    self.cb_marca.setGeometry(QRect(100, 70, 120, 20))
    self.cb_marca.addItems([marca])
    
    label4 = QLabel(groupBox)
    label4.setGeometry(QRect(230, 70, 70, 20))
    label4.setText("Producto: ")
    self.le_producto=QLineEdit(groupBox)
    self.le_producto.setGeometry(QRect(310, 70, 120, 20))
    self.le_producto.setText(producto)
    
    label5 = QLabel(groupBox)
    label5.setGeometry(QRect(30, 100, 70, 20))
    label5.setText("Sku: ")
    self.le_sku=QLineEdit(groupBox)
    self.le_sku.setGeometry(QRect(100, 100, 120, 20))
    self.le_sku.setText(sku)

    label6 = QLabel(groupBox)
    label6.setGeometry(QRect(230, 100, 70, 20))
    label6.setText("Precio: ")
    self.ds_precio=QDoubleSpinBox(groupBox)
    self.ds_precio.setGeometry(QRect(310, 100, 120, 20))

    label7 = QLabel(groupBox)
    label7.setGeometry(QRect(30, 130, 70, 20))
    label7.setText("Descuento: ")
    self.le_descuento=QLineEdit(groupBox)
    self.le_descuento.setGeometry(QRect(100, 130, 120, 20))
    self.le_descuento.setInputMethodHints(Qt.ImhDigitsOnly)

    label3 = QLabel(groupBox)
    label3.setGeometry(QRect(230, 130, 70, 20))
    label3.setText("Estatus: ")
    self.cb_estatus = QComboBox(groupBox)
    self.cb_estatus.setGeometry(QRect(310, 130, 120, 20))
    self.cb_estatus.addItems(["Activo","Baja"])
  
    pushButton1 = QPushButton(self)
    pushButton1.setGeometry(QRect(340, 190, 70, 20))
    pushButton1.setText("Actualizar")
    pushButton2 = QPushButton(self)
    pushButton2.setGeometry(QRect(130, 190, 70, 20))
    pushButton2.setText("Cancelar")

    #-------------------Funciones------------------------
    pushButton1.clicked.connect(self.verifyAdd)
    pushButton2.clicked.connect(self.closewindow)

  def verifyAdd(self):
  #Validar y actualizar en la BD

    if (self.cb_categoria.currentText()!="" and self.cb_subcategoria.currentText()!="" and 
        
        self.cb_marca.currentText()!="" and self.le_producto.text()!="" and self.le_sku.text()!=""):
      
      #almacenamos los valores
      id_producto=self.parent.select_row_product[1]#variable clase padre
      categoria=self.cb_categoria.currentText()
      subcategoria=self.cb_subcategoria.currentText()
      marca=self.cb_marca.currentText()
      producto=self.le_producto.text()
      sku=self.le_sku.text()
      precio=self.ds_precio.value()

      #Actualizar producto
      objetoConsulta=models_products()
      resultado=objetoConsulta.update(self.parent.variables, categoria, subcategoria, marca, producto, sku, precio, self.parent.variables.usuarioIdCliente, self.parent.variables.usuarioNom, id_producto)
      
      if resultado: 
      #si es True
        message("Aviso","Se actualizó correctamente el producto")
        
        self.parent.searchProduct()
        self.closewindow()

      else:
        message("Error","El producto no fue actualizado")
        self.closewindow()

    else:
    #Adventencia

      message("IMPORTANTE","Favor de ingresar los datos solicitados")
  
  def closewindow(self):
    self.close()
