import os
import subprocess

def update_app():
    app_dir = os.path.dirname(os.path.abspath(__file__))
    # URL du dépôt distant à personnaliser
    remote_url = 'https://github.com/RetrosoftApp/RetrosoftNavigateur.git'  # Remplacez par votre vrai dépôt
    # Vérifie si le dossier est un dépôt git
    if not os.path.exists(os.path.join(app_dir, '.git')):
        print('Ce dossier n\'est pas un dépôt git. Initialisation...')
        subprocess.run(['git', 'init'], cwd=app_dir)
        subprocess.run(['git', 'remote', 'add', 'origin', remote_url], cwd=app_dir)
    else:
        # Vérifie si le remote existe
        result = subprocess.run(['git', 'remote'], cwd=app_dir, capture_output=True, text=True)
        if 'origin' not in result.stdout:
            subprocess.run(['git', 'remote', 'add', 'origin', remote_url], cwd=app_dir)
    # Récupère les dernières modifications
    print('Mise à jour de l\'application...')
    subprocess.run(['git', 'pull', 'origin', 'main'], cwd=app_dir)

if __name__ == '__main__':
    update_app()
    print('Mise à jour terminée.')
