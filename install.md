## Instalación

Primero haz un Fork del proyecto en GitHub y luego clonalo en tu computador así:

  SSH: git clone git@github.com:PyBAQ/django-quilla-web.git

  HTTPS: git clone https://github.com/PyBAQ/django-quilla-web.git

Para poder ejecutar el proyecto localmente se requieren las siguientes dependencias:

- Python 3 (3.12 o superior)
- ImageMagick (para procesamiento de imágenes)
- [uv](https://docs.astral.sh/uv/)

Una vez tengas estas dependencias instaladas en tu sistema operativo, ejecuta `uv sync` desde la carpeta del proyecto para instalar todas las dependencias de Python incluyendo Lektor.

A continuación siga la guía de instalación según su sistema operativo

### Windows

Descarga Python desde: https://www.python.org/downloads/windows/

Para ImageMagick puedes descargar desde <https://imagemagick.org/> o usar [chocolatey](https://chocolatey.org/):

    choco install imagemagick

Para instalar uv, ejecuta en PowerShell:

    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

O descarga el instalador desde https://docs.astral.sh/uv/getting-started/installation/

### Windows 10: Windows Subsystem for Linux

Si quieres/debes mantener Windows instalado, pero prefieres mantener este proyecto en Linux, puedes usar el "Windows Subsystem for Linux" (subsistema de Windows para Linux).  La forma rápida de habilitarlo es por powershell en modo de Administrador, ten presente que necesitas reinicar tu PC:

    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

Luego, en la tienda de Microsoft encontrarás distintas distribuciones de Ubuntu que podrás instalar, ten presente que esto solo te da acceso por linea de comandos. Podrás encontrar mas detalles en el siguiente vínculo: [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

De allí continua los pasos según el instructivo para Linux.

## Después de instalar las dependencias del sistema

Una vez tengas Python, ImageMagick y uv instalados, navega a la carpeta del proyecto y ejecuta:

    uv sync

Esto instalará Lektor y todas las demás dependencias de Python necesarias para el proyecto.

### Linux

En Ubuntu instala las dependencias del sistema:

    sudo apt install python3 imagemagick

Luego instala uv:

    curl -LsSf https://astral.sh/uv/install.sh | sh

Y sigue las instrucciones para agregar uv a tu PATH si es necesario

### MacOS

Con [homebrew](https://brew.sh/) instala las dependencias del sistema:

    brew install python imagemagick

Luego instala uv:

    curl -LsSf https://astral.sh/uv/install.sh | sh

(Opcional en macOS) Verifica que las variables de entorno UTF-8 estén definidas en `~/.bash_profile` (o `~/.zprofile` si usas zsh):

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8
