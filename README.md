## Keylogger educativo en Python

Este proyecto es un **keylogger sencillo con interfaz gráfica en Tkinter**, pensado para fines **educativos** y de **pruebas locales**.  
Incluye:

- `keylogger.py`: aplica un listener de teclado con `pynput` y muestra el texto capturado en una ventana.
- `server.py`: script muy básico que actúa como servidor TCP para recibir logs (versión de pruebas, solo en `127.0.0.1`).

> **Aviso legal**: usar un keylogger para registrar las pulsaciones de otras personas sin su consentimiento es ilegal en muchos países.  
> Este código está pensado **solo para tu propio equipo y con fines de aprendizaje**.

---

### Requisitos

- Python 3.8 o superior.
- Paquetes:
  - `pynput`
  - `tkinter` (viene con la instalación estándar de Python en Windows).

Instala `pynput` con:

```bash
pip install pynput
```

---

### Estructura

- `keylogger.py`: interfaz Tkinter + lógica de captura de teclas.
- `server.py`: servidor muy simple que escucha en un puerto TCP y muestra por pantalla lo que recibe.
- `keylog.txt`: archivo donde se van guardando los logs locales (se crea automáticamente cuando se usa el keylogger).

Puedes añadir un `.gitignore` para evitar subir `keylog.txt` al repositorio:

```gitignore
keylog.txt
__pycache__/
*.log
```

---

### Uso

#### 1. Servidor (opcional, para pruebas de red)

En una terminal, ejecuta:

```bash
python server.py
```

El servidor quedará escuchando en `127.0.0.1:4443` (dirección local).

#### 2. Cliente / Keylogger

En otra terminal (o desde tu editor), ejecuta:

```bash
python keylogger.py
```

En la ventana:

1. Rellena `Server IP` y `Server Port` si quieres usar un servidor (por ejemplo `127.0.0.1` y `4443`).
2. Pulsa **"Start keylogger"** para empezar a capturar teclas.
3. Escribe en cualquier ventana; el texto aparecerá en el cuadro de texto del programa.
4. Pulsa **"Stop y guardar log"** para:
   - Detener la captura.
   - Guardar el contenido actual en `keylog.txt`.

> Nota: ahora mismo el ejemplo guarda el log en local. Puedes ampliar la lógica de `send_log` para enviar los datos al servidor usando sockets/SSL si lo necesitas.

---

### Notas técnicas

- El listener de teclado se implementa con `pynput.keyboard.Listener`.
- Se han tratado algunas teclas especiales:
  - `Backspace` borra el último carácter del log.
  - `Enter` añade un salto de línea.
  - `Shift`, `Ctrl`, `Alt` y similares se ignoran para no ensuciar el texto.
- El archivo `server.py` está pensado como **servidor de pruebas en local**, y no como solución segura/lista para producción.

---

### Seguridad y buenas prácticas

- **No incluyas IPs públicas reales ni contraseñas en el código** si vas a subirlo a GitHub.
- Si quieres usar IPs/puertos reales, es mejor cargarlos desde variables de entorno o desde un archivo `.env` que **no subas** al repositorio.
- Usa este proyecto solo en equipos donde tengas permiso explícito para hacerlo.

