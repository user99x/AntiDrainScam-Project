import psutil
import time
import tkinter as tk
import winsound
import pygetwindow as gw
from win10toast import ToastNotifier

# Liste des applications de communication 
CALL_APPS = ["Skype.exe", "Teams.exe", "Zoom.exe", "Discord.exe", "WhatsApp.exe"]

# Liste des applications / mots-clés sensibles
SENSITIVE_APPS = ["bank", "paypal", "crypto", "wallet", "finance"]

toaster = ToastNotifier()

def is_call_active():
    """ Vérifie si une application d'appel est en cours d'exécution """
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] in CALL_APPS:
            return True
    return False

def check_sensitive_activity():
    """ Vérifie si une application sensible est ouverte """
    windows = gw.getAllTitles()
    for win in windows:
        if any(keyword.lower() in win.lower() for keyword in SENSITIVE_APPS):
            return True
    return False

def show_fullscreen_alert():
    """ Affiche une alerte bloquante en plein écran et moderne """
    winsound.Beep(1000, 1000)  # Joue un bip pour attirer l'attention
    
    root = tk.Tk()
    root.title("⚠️ Alerte Sécurité ⚠️")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.focus_force()
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # Empêche la fermeture
    
    # Dégradé de fond avec canvas
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack()
    canvas.create_rectangle(0, 0, root.winfo_screenwidth(), root.winfo_screenheight(), fill="#ff6b6b", outline="")
    
    # Cadre central
    frame = tk.Frame(root, bg="white", padx=40, pady=30, relief="raised", bd=10)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    
    # Texte principal
    title = tk.Label(frame, text="⚠️ ATTENTION : POSSIBLE FRAUDE ⚠️", fg="#d32f2f", font=("Arial", 24, "bold"), bg="white")
    title.pack(pady=10)
    
    message = tk.Label(frame, text="Vous êtes en appel et utilisez une application sensible.\nVérifiez que ce n'est pas une arnaque !", 
                        font=("Arial", 16), fg="black", bg="white", justify="center")
    message.pack(pady=10)
    
    # Bouton stylisé avec effet
    def on_enter(e):
        button.config(bg="#d32f2f", fg="white")
    
    def on_leave(e):
        button.config(bg="white", fg="black")
    
    button = tk.Button(frame, text="J'AI COMPRIS", font=("Arial", 14, "bold"), bg="white", fg="black", 
                       padx=20, pady=10, relief="ridge", borderwidth=3, command=root.destroy)
    button.pack(pady=20)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    
    root.mainloop()

def main():
    print("Surveillance des appels et activités sensibles...")
    while True:
        if is_call_active() and check_sensitive_activity():
            show_fullscreen_alert()
        time.sleep(5)

if __name__ == "__main__":
    main()