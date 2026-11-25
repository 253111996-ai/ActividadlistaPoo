from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
#codigo oswaldo no pedir ala ia con dialog#

class ToDoList(QtWidgets.QMainWindow): 
    def __init__(self):
        super().__init__()
        uic.loadUi("ToDoList.ui",self)
        self.btnAgregar.clicked.connect(self.AgregarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)
        self.btnActualizar.clicked.connect(self.ActualizarTarea)
        self.lstTareas.itemClicked.connect(self.CargarTareaParaEditar)
        
    def AgregarTarea(self):
        tarea = self.edtTarea.text().strip()  
        if tarea == "":
            QMessageBox.warning(self, "Campo vacio", "escribe una tarea antes de agregar.")
            self.edtTarea.setFocus()
            return
        
        self.lstTareas.addItem(tarea)
        self.edtTarea.clear()
        self.edtTarea.setFocus()
    
    def EliminarTarea(self):
        inidceTareaBorrar = self.lstTareas.currentRow()
        self.lstTareas.takeItem(inidceTareaBorrar)
        
    def CargarTareaParaEditar(self, item):
        self.edtTarea.setText(item.text())
        self.edtTarea.setFocus()
        
    def ActualizarTarea(self):
        item_seleccionado=self.lstTareas.currentItem()
        nuevoTexto=self.edtTarea.text().strip()
        item_seleccionado.setText(nuevoTexto)
        self.edtTarea.clear()
        self.lstTareas.clearSelection()