; Script Inno Setup pour installer Retrosoft Navigateur
; https://jrsoftware.org/isinfo.php

[Setup]
AppName=Retrosoft Navigateur
AppVersion=1.0
DefaultDirName={userappdata}\RetrosoftNavigateur
DefaultGroupName=Retrosoft
OutputDir=.
OutputBaseFilename=RetrosoftNavigateurSetup
Compression=lzma
SolidCompression=yes

[Files]
Source: "retrosoft_navigateur.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "index.html"; DestDir: "{app}"; Flags: ignoreversion
Source: "update_retrosoft.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "retrosoft_icon_firefox_styled.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Retrosoft Navigateur"; Filename: "{app}\retrosoft_navigateur.exe"; IconFilename: "{app}\retrosoft_icon_firefox_styled.ico"
Name: "{group}\Mettre à jour Retrosoft"; Filename: "{app}\update_retrosoft.py"; IconFilename: "{app}\retrosoft_icon_firefox_styled.ico"

[Run]
Filename: "{app}\retrosoft_navigateur.exe"; Description: "Lancer Retrosoft Navigateur"; Flags: postinstall skipifsilent
