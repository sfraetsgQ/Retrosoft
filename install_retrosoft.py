import os
import shutil
import sys
import subprocess

APP_NAME = "Retrosoft Navigateur"
INSTALL_DIR = os.path.join(os.environ["ProgramFiles"], "RetrosoftNavigateur")
FILES = ["retrosoft_navigateur.py", "index.html", "update_retrosoft.py"]

# Crée le dossier d'installation
os.makedirs(INSTALL_DIR, exist_ok=True)

# Copie les fichiers
for f in FILES:
    shutil.copy(f, INSTALL_DIR)

# Crée un raccourci sur le bureau (Windows)
def create_shortcut(name, target):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    shortcut = os.path.join(desktop, name + ".url")
    with open(shortcut, "w") as s:
        s.write(f"[InternetShortcut]\nURL=file:///{target}\n")

create_shortcut("Retrosoft Navigateur", os.path.join(INSTALL_DIR, "retrosoft_navigateur.py"))
create_shortcut("Mettre à jour Retrosoft", os.path.join(INSTALL_DIR, "update_retrosoft.py"))

# Ouvre l'application après installation
subprocess.Popen([sys.executable, os.path.join(INSTALL_DIR, "retrosoft_navigateur.py")])

print(f"{APP_NAME} installé dans {INSTALL_DIR}")
print("Raccourcis créés sur le bureau.")
print("Application lancée.")
