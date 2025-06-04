# agent_client.py
import tkinter as tk
import requests
import time
import threading

class AgentClient:
    def __init__(self, server_url, poste):
        self.server_url = server_url
        self.poste = poste
        self.root = tk.Tk()
        self.root.title(f"Poste {poste} - Verrouillé")
        self.root.geometry("500x250")
        self.root.configure(bg="#2c3e50")

        self.label = tk.Label(self.root, text="Poste verrouillé. Demandez connexion.", font=("Arial", 14), bg="#2c3e50", fg="white")
        self.label.pack(pady=30)

        self.btn = tk.Button(self.root, text="Demander Connexion", font=("Arial", 12), bg="#27ae60", fg="white", command=self.demander_connexion)
        self.btn.pack(ipadx=10, ipady=5)

    def demander_connexion(self):
        requests.post(f"{self.server_url}/api/demande-connexion/", json={"poste": self.poste})
        self.label.config(text="Demande envoyée. En attente d'autorisation...")
        self.btn.config(state="disabled")
        threading.Thread(target=self.verifier_autorisation).start()

    def verifier_autorisation(self):
        while True:
            r = requests.get(f"{self.server_url}/api/statut-poste/{self.poste}/")
            data = r.json()
            if data.get("statut") == "refuse":
                self.label.config(text="Connexion refusée par l'admin.")
                break
            if data.get("autorise"):
                self.root.destroy()
                AgentSession(self.server_url, self.poste).start()
                break
            time.sleep(3)

    def start(self):
        self.root.mainloop()

class AgentSession:
    def __init__(self, server_url, poste):
        self.server_url = server_url
        self.poste = poste
        self.root = tk.Tk()
        self.root.title("Session en cours")
        self.root.geometry("500x300")
        self.root.configure(bg="#34495e")

        self.label = tk.Label(self.root, text="Session en cours...", font=("Arial", 16), bg="#34495e", fg="white")
        self.label.pack(pady=20)

        self.timer_label = tk.Label(self.root, text="00:00", font=("Courier", 20, "bold"), bg="#34495e", fg="#f1c40f")
        self.timer_label.pack(pady=10)

        self.btn = tk.Button(self.root, text="Terminer", font=("Arial", 14), bg="#e74c3c", fg="white", command=self.terminer)
        self.btn.pack(pady=30, ipadx=10, ipady=5)

        self.start_time = time.time()
        self.running = True
        threading.Thread(target=self.update_timer).start()

    def update_timer(self):
        while self.running:
            elapsed = int(time.time() - self.start_time)
            minutes, seconds = divmod(elapsed, 60)
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            time.sleep(1)

    def terminer(self):
        self.running = False
        r = requests.post(f"{self.server_url}/api/terminer-session/", json={"poste": self.poste})
        tarif = r.json().get("tarif", 0)
        self.label.config(text=f"Session terminée. Tarif: {tarif} Ar")
        self.btn.config(state="disabled")

    def start(self):
        self.root.mainloop()

# Exemple d'exécution client
if __name__ == "__main__":
    client = AgentClient("http://localhost:8000", "PC1")
    client.start()
