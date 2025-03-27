import psutil
import time
import tkinter as tk
import winsound
import pygetwindow as gw
from win10toast import ToastNotifier

# Liste des applications de communication
CALL_APPS = ["Skype.exe", "Teams.exe", "Zoom.exe", "Discord.exe", "WhatsApp.exe"]

# Liste des applications / mots-clés sensibles
SENSITIVE_APPS = ["bank", "paypal", "crypto", "wallet", "finance", "banque", "cryptomonnaie", "paiement", "payment", "Allianz", "AXA", "Banque Accord", "Banque Casino", "Banque de Savoie",
    "Banque Fédérale Mutualiste", "Barclays", "BNP Paribas", "BRED",
    "Caisse d'Epargne", "Carrefour Banque", "CCSO", "Cetelem", "CIC",
    "Crédit Agricole", "Crédit Coopératif", "Crédit du Nord", "Crédit Foncier",
    "Crédit Mutuel", "FLOA Bank", "Fortis", "Groupama Banque", "HSBC",
    "Institut pour le Financement du Cinéma", "La Banque Postale", "LCL",
    "RCI Banque", "Société Générale", "VTB Bank", "American Express","binance", "coinbase", "crypto.com", "kraken", "bitfinex", "bitstamp",
    "bitget", "bybit", "okx", "kucoin", "gate.io", "bitmart", "blockchain.com",
    "metamask", "trust wallet", "ledger", "trezor", "phantom wallet",
    "coinomi", "exodus", "safepal", "rain", "luno", "payeer", "binance wallet",
    "coinbase wallet", "crypto wallet", "nexo", "zengo", "brd wallet",
    "token pocket", "xdefi", "argent", "walletconnect"]

toaster = ToastNotifier()

def is_call_active():
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] in CALL_APPS:
            print(f"[DEBUG] Appel détecté via : {process.info['name']}")
            return True
    return False

def check_sensitive_activity():
    windows = gw.getAllTitles()
    for win in windows:
        for keyword in SENSITIVE_APPS:
            if keyword.lower() in win.lower():
                print(f"[DEBUG] Mot-clé sensible détecté dans fenêtre : \"{win}\"")
                return True
    return False


import tkinter as tk
import winsound

def show_fullscreen_alert():
    """ Affiche une alerte bloquante en plein écran et moderne façon Windows """

    # Joue un bip sonore pour alerter
    winsound.Beep(1000, 1000)

    root = tk.Tk()
    root.title("⚠️ Alerte Sécurité ⚠️")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Empêche fermeture
    root.configure(bg="black")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Canvas pour créer un fond avec dégradé rouge vers orange
    canvas = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack()

    r1, g1, b1 = (255, 50, 50)   # Rouge vif
    r2, g2, b2 = (255, 160, 90)  # Orange clair
    steps = screen_height
    for i in range(steps):
        r = int(r1 + (r2 - r1) * i / steps)
        g = int(g1 + (g2 - g1) * i / steps)
        b = int(b1 + (b2 - b1) * i / steps)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, screen_width, i, fill=color)

    # Simule une ombre portée derrière le cadre central
    shadow = tk.Frame(root, bg="#000000", width=500, height=300)
    shadow.place(relx=0.5, rely=0.5, anchor="center", x=6, y=6)

    # Cadre central esthétique
    frame = tk.Frame(root, bg="white", padx=40, pady=30)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Titre fort
    title = tk.Label(frame, text="⚠️ ATTENTION : RISQUE DE FRAUDE ⚠️",
                     fg="#b71c1c", font=("Segoe UI", 28, "bold"), bg="white")
    title.pack(pady=(0, 20))

    # Message d'alerte
    message = tk.Label(frame,
                       text="Vous êtes en appel et utilisez une application sensible.\n"
                            "Vérifiez que ce n'est pas une tentative de fraude.",
                       font=("Segoe UI", 16), fg="black", bg="white", justify="center")
    message.pack(pady=(0, 20))

    # Bouton stylé à la Windows
    def on_enter(e):
        button.config(bg="#d32f2f", fg="white")

    def on_leave(e):
        button.config(bg="white", fg="black")

    button = tk.Button(frame, text="J'AI COMPRIS", font=("Segoe UI", 14, "bold"), bg="white", fg="black",
                       padx=30, pady=12, relief="solid", bd=2, command=root.destroy,
                       activebackground="#d32f2f", activeforeground="white", cursor="hand2")
    button.pack(pady=(10, 0))
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    root.mainloop()


def main():
    print("Surveillance des appels et activités sensibles...")
    while True:
        call_active = is_call_active()
        sensitive_active = check_sensitive_activity()

        print(f"[DEBUG] Appel actif ? {call_active}")
        print(f"[DEBUG] Activité sensible détectée ? {sensitive_active}")

        if call_active and sensitive_active:
            print("[DEBUG] CONDITIONS REMPLIES → Affichage de l'alerte")
            show_fullscreen_alert()

        time.sleep(5)


if __name__ == "__main__":
    main()
