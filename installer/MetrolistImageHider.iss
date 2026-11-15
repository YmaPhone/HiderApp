#ifndef AppVersion
  #define AppVersion "14.0.0"
#endif

[Setup]
AppId={{2C623F9A-DA75-4B98-88EF-2C7DD2417A18}
AppName=Metrolist Image Hider
AppVersion={#AppVersion}
AppPublisher=YmaPhone
DefaultDirName={localappdata}\Programs\Metrolist
DefaultGroupName=Metrolist
DisableProgramGroupPage=yes
OutputDir=..\upstream\dist
OutputBaseFilename=Metrolist-Image-Hider-Setup-{#AppVersion}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
UninstallDisplayIcon={app}\Metrolist.exe

[Languages]
Name: "hebrew"; MessagesFile: "compiler:Languages\Hebrew.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create desktop shortcuts"; GroupDescription: "Additional shortcuts:"

[Files]
Source: "..\stage\Metrolist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\Metrolist"; Filename: "{app}\Metrolist.exe"
Name: "{autoprograms}\Metrolist Image Hider"; Filename: "{app}\Metrolist Image Hider.exe"
Name: "{autodesktop}\Metrolist"; Filename: "{app}\Metrolist.exe"; Tasks: desktopicon
Name: "{autodesktop}\Metrolist Image Hider"; Filename: "{app}\Metrolist Image Hider.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Metrolist.exe"; Description: "Launch Metrolist"; Flags: postinstall nowait skipifsilent unchecked
