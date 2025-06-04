import sys
import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QDialog
import requests
class conDial(QDialog):
    def __init__(self):
        super(conDial,self).__init__()
        basedir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(basedir, "conex.ui")
        loadUi(ui_file,self)
        self.activer.clicked.connect(self.connexion)
    def connexion(self):
        SERVER_URL = "http://127.0.0.1:8000"
        try:
            requests.post(
                f"{SERVER_URL}/api/demander/",
                headers={'Content-Type':'application/json'}
            )
            print(requests.post)
        except Exception as e:
            print("Erreur de demande:",e)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Résoudre le chemin absolu vers pan.ui
        basedir = os.path.dirname(os.path.abspath(__file__))
        ui_file = os.path.join(basedir, "pan.ui")
        loadUi(ui_file, self)

        # Connexion du bouton

    def mousePressEvent(self, event):
        dialog = conDial()
        dialog.exec_()
    
    def show_alert(self):
        QMessageBox.information(self, "Alerte", "Tu as cliqué !")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())