# -----------------------------------------------------------------------------------------------
# Nombre:       message.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       18 de Septiembre 2020
# Modificado:   20 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# -----------------------------------------------------------------------------------------------


from PyQt5.QtWidgets import QMessageBox


def message(message, information):
#Mensaje imperativa
    
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setInformativeText(information)
    msg.setWindowTitle("Mensaje de Advertencia")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

    return True


def message1(message, information):
#Advertencia interrogativa, no utilizado
    
    # Mensaje de advertencia, los parametros son de tipo String
    resultado = QMessageBox.question(
        self, message, information, QMessageBox.Yes | QMessageBox.No)
    return resultado


def message2(self):
# Mensaje de adventencia no utilizado

    message = QMessageBox(self)
    message.setWindowTitle("Mensaje")
    message.setText("Por el momento no se encuentra DISPONIBLE")
    message.move(self.pos().x()+33, self.pos().y()+150)
    message.exec_()
