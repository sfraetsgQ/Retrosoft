import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading

import subprocess
import os

# Ouvre Google dans le navigateur par défaut
webbrowser.open('https://www.google.com')

# Mise à jour automatique via git
def auto_update():
    update_script = os.path.join(os.path.dirname(__file__), 'update_retrosoft.py')
    if os.path.exists(update_script):
        subprocess.run(['python', update_script])

auto_update()

# Serveur HTTP simple pour servir des fichiers HTML
class RetrosoftHandler(SimpleHTTPRequestHandler):
    pass

def start_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RetrosoftHandler)
    print('Retrosoft navigateur en cours sur http://localhost:8080')
    httpd.serve_forever()

if __name__ == '__main__':
    # Démarre le serveur dans un thread séparé
    threading.Thread(target=start_server, daemon=True).start()
    input('Appuyez sur Entrée pour quitter...')
