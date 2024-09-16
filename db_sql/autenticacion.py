import sys
from PyQt5 import QtWidgets
import mysql.connector

class LoginApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Autenticación')
        
        # Crear campos y botón
        self.usuario_input = QtWidgets.QLineEdit(self)
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button = QtWidgets.QPushButton('Iniciar sesión', self)
        
        # Conectar el botón a la función de autenticación
        self.login_button.clicked.connect(self.authenticate)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.usuario_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def authenticate(self):
        usuario = self.usuario_input.text()
        password = self.password_input.text()

        # Conexión a la base de datos para verificar credenciales
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="segura_bd"
        )
        
        mycursor = mydb.cursor()
        
        sql = "SELECT * FROM USUARIOS WHERE usuario=%s AND password=%s"
        mycursor.execute(sql, (usuario, password))
        
        result = mycursor.fetchone()
        
        if result:
            QtWidgets.QMessageBox.information(self, 'Éxito', 'Autenticación exitosa')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Usuario o contraseña incorrectos')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = LoginApp()
    ex.show()
    sys.exit(app.exec_())
