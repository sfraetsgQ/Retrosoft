; NSIS Script pour Retrosoft Navigateur
; https://nsis.sourceforge.io/

Name "Retrosoft Navigateur"
OutFile "RetrosoftNavigateurSetup.exe"
InstallDir "$PROGRAMFILES\RetrosoftNavigateur"
ShowInstDetails show

Section "Installer Retrosoft Navigateur"
  SetOutPath "$INSTDIR"
  File "retrosoft_navigateur.py"
  File "index.html"
  File "update_retrosoft.py"

  ; Crée un raccourci pour lancer l'application
  CreateShortCut "$DESKTOP\Retrosoft Navigateur.lnk" "$INSTDIR\retrosoft_navigateur.py"
  CreateShortCut "$DESKTOP\Mettre à jour Retrosoft.lnk" "$INSTDIR\update_retrosoft.py"

SectionEnd

Section "Vérifier Git"
  ExecWait 'git --version'
SectionEnd

Section "Désinstaller"
  Delete "$INSTDIR\retrosoft_navigateur.py"
  Delete "$INSTDIR\index.html"
  Delete "$INSTDIR\update_retrosoft.py"
  Delete "$DESKTOP\Retrosoft Navigateur.lnk"
  Delete "$DESKTOP\Mettre à jour Retrosoft.lnk"
  RMDir "$INSTDIR"
SectionEnd
