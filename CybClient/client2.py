import sys
import os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QDialog
import requests
import socket
import json
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
            # Récupérer IP locale (optionnel si nécessaire)
            # ip = socket.gethostbyname(socket.gethostname())
            ip = '192.168.1.1'
            # Construire les données
            data = {
                'ip': ip,
                'action': 'autoriser'  # ou une autre action selon logique
            }

            response = requests.post(
                f"{SERVER_URL}/api/demander/",
                headers={'Content-Type': 'application/json'},
                data=json.dumps(data)
            )

            print(response.json())

        except Exception as e:
            print("Erreur de demande:", e)
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