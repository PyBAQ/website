## Instalación

Primero haz un Fork del proyecto en GitHub y luego clonalo en tu computador así:

  SSH: git clone git@github.com:PyBAQ/django-quilla-web.git

  HTTPS: git clone https://github.com/PyBAQ/django-quilla-web.git

Para poder ejecutar el proyecto localmente se requieren las siguientes dependencias:

- Python 3
- ImageMagick
- [Lektor](https://www.getlektor.com/docs/installation/)

A continuación siga la guía de instalación según su sistema operativo

### Windows

Para Windows puedes descargar Python desde el siguiente enlace: https://www.python.org/downloads/windows/

Puedes instalar ImageMagick desde el siguiente enlace: <https://imagemagick.org/>

o usar [chocolatey](https://chocolatey.org/) y ejecutar

    choco install imagemagick

Para instalar Lektor puedes usar el siguiente comando:

    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))" && SET PATH=%PATH%;%LocalAppData%\lektor-cli

Pero también puede ser ejecutado directamente en powershell:

    iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))

### Windows 10: Windows Subsystem for Linux

Si quieres/debes mantener Windows instalado, pero prefieres mantener este proyecto en Linux, puedes usar el "Windows Subsystem for Linux" (subsistema de Windows para Linux).  La forma rápida de habilitarlo es por powershell en modo de Administrador, ten presente que necesitas reinicar tu PC:

    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

Luego, en la tienda de Microsoft encontrarás distintas distribuciones de Ubuntu que podrás instalar, ten presente que esto solo te da acceso por linea de comandos. Podrás encontrar mas detalles en el siguiente vínculo: [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

De allí continua los pasos según el instructivo para Linux.

### Linux

En Ubuntu se pueden instalar las dependencias de Lektor usando el comando:

    sudo apt install python3-dev libssl-dev libffi-dev imagemagick

Luego puedes instalar Lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/installer.py | python3

### MacOS

En Mac OS si se tiene instalado [homebrew](https://brew.sh/) se pueden instalar las dependencias de Lektor usando el comando:

    brew install imagemagick

Luego puede instalar Lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/installer.py | python3

Verificar que las variables de entorno del formato UTF-8 en sus respectivos idiomas esten definidas en el
archivo ~/.bash_profile de su sistema y en caso de no estar definidas agregarlas.

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8
