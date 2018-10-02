# Página web comunidad python barranquilla

[![Build Status](https://travis-ci.org/PyBAQ/django-quilla-web.svg?branch=master)](https://travis-ci.org/PyBAQ/django-quilla-web)

## Instalación

Para poder ejecutar el proyecto localmente se requieren las siguientes dependencias:

- Python 2.7
- Imagemagick
- NodeJS 6
- [Lektor](https://www.getlektor.com/)

A continuación siga la guiá de instalación según su sistema operativo

### Windows

Para windows puede descargar python desde el siguiente enlace: https://www.python.org/downloads/

puede instalar imagemagick usando [chocolatey](https://chocolatey.org/), o descargar desde el siguiente enlace:

<http://www.imagemagick.org/>

Para instalar lektor puede usar el siguiente comando:

```powershell
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))" && SET PATH=%PATH%;%LocalAppData%\lektor-cli
```

Pero tambien puede ser ejecutado directamente en powershell:

```powershell
    iex ((new-object net.webclient).DownloadString('https://getlektor.com/install.ps1'))
```

### Windows 10: Windows Subsystem for Linux

Si quieres/debes mantener windows instalado, pero prefieres mantener este proyecto en linux, puedes usar el "Windows Subsystem for Linux" (subsistema de windows para linux).  La forma rápida de habilitarlo es por powershell en modo de Administrador, ten presente que necesitas reinicar tu PC:

```powershell
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Luego, en la tienda de microsoft encontrarás distintas distribuciones de ubuntu que podrás instalar, ten presente que esto solo te da acceso por linea de comandos. Podrás encontrar mas detalles en el siguiente vínculo: [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

De allí continua los pasos según el instructuvo para Linux.

### Linux

En ubuntu se pueden instalar las dependencias de lektor usando el comando:

    sudo apt-get install python-dev libssl-dev libffi-dev imagemagick

Luego puede instalar lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/install.sh | sh

### MacOS

En Mac OS si se tiene instalado homebrew se pueden instalar las dependencias de lektor usando el comando:

    brew install imagemagick

Luego puede instalar lektor usando el siguiente comando:

    curl -sf https://www.getlektor.com/install.sh | sh

### La discusión Python3

Ahora mismo Lektor **no provee** una forma confiable y sencilla de instalar la herramienta en Linux usando Python 3. Por esto no usamos esta versión de Python. Sin embargo todos los pasos anteriormente descritos en windows funcionan sin inconvenientes usando cualquier versión de Python 3.6+. Será, sin embargo, tu responsabilidad inspeccionar el código fuente de los plugins de Lektor para segurar su compatibilidad con Python 3. Recuerda que es codigo libre y no se trata de pedir las cosas sino de contribuir a las características que deseas.


## Ejecución del proyecto durante desarrollo

Para la ejecución del proyecto se debe ejecutar el comando

```bash
lektor server -f webpack
```

Si lektor logra ejecutar el proyecto sin errores, publicará la página construida en [http://localhost:5000/](http://localhost:5000/).

## Producción

Construye el proyecto en los artefactos finales

```bash
lektor build -f webpack
```

## Código de conducta

Los invitamos a leer el siguiente [repositorio con el código de conducta](https://github.com/PyBAQ/codigo-de-conducta) de la comunidad.

### Contribuciones

Necesitamos de tu ayuda para terminar este proyecto! **¿Cómo puedes contribuir?** Mira las normas que hemos redactado en el archivo [CONTRIBUTING.md] para organizarnos mejor en el desarrollo. Esperamos tus Pull Requests e Issues. Gracias por tu apoyo.

[CONTRIBUTING.md]: https://github.com/PyBAQ/django-quilla-web/blob/master/CONTRIBUTING.md
