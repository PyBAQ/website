# Página Web comunidad Python Barranquilla

![Desplegar pagina](https://github.com/pybaq/website/actions/workflows/deploy.yml/badge.svg)
![Probar páginas](https://github.com/pybaq/website/actions/workflows/test-e2e.yml/badge.svg)
![Actualizar eventos meetup](https://github.com/pybaq/website/actions/workflows/actualizar-eventos-meetup.yml/badge.svg)

Bienvenido al repositorio del sitio web de la comunidad python Barranquilla

## Código de conducta

Los invitamos a leer el siguiente [repositorio con el código de conducta](https://github.com/PyBAQ/codigo-de-conducta) de la comunidad.

## Contribuciones

Necesitamos de tu ayuda para terminar este proyecto! **¿Cómo puedes contribuir?** Mira las normas que hemos redactado en el archivo [CONTRIBUTING.md] para organizarnos mejor en el desarrollo. Esperamos tus Pull Requests e Issues. Gracias por tu apoyo.

[CONTRIBUTING.md]: https://github.com/PyBAQ/django-quilla-web/blob/master/CONTRIBUTING.md

Para este proyecto tenemos 2 guías en nuestro blog, y te invitamos a leerlas

- [Contribuir blog](https://pybaq.co/blog/contribuir-blog-python-barranquilla/)
- [Contribuir modo facil](https://pybaq.co/blog/contribuir-modo-facil/)

## Ejecución del proyecto

> Puedes dar esto por completado si estas usando Github CodeSpaces

Para poder visualizar este proyecto en tu maquina se requiere iniciar la ejecución de lektor y opcionalmente compilar los css

### Instalación de dependencias

Este proyecto requiere tener instalado python y nodejs
para hacerlo en tu maquina puedes usar esta [Guía](./install.md)

Para instalar las dependencias del proyecto ejecuta

    pipx install lektor

### Ejecucion de lektor server

Para la ejecución de lektor se debe ejecutar el comando:

    lektor server

Al ejecutar Lektor, verás una lista de procesos que tienen lugar antes de generar la página estática. Si en tu edición cometes algún error, aparecerá escrito en la consola. Si se genera con éxito la página, ésta estará disponible en [http://localhost:5000/](http://localhost:5000/).

### Compilar CSS

El proyecto actualmente usa Sass para los estilos en cascada si deseas modificarlos es necesario que tengas instalado Node.js.

para instalar con npm las dependencias ejecuta:

    npm install

Luego cada vez que actualices un estilo ejecuta:

    npm run build

## Tests

> Dependiendo de la configuración de CodeSpaces que escojas deberás ejecutar esta instalación

Instala los paquetes de pruebas con el comando

    pip install -r test-requirements.txt

### Validar HTML usando W3C validator

w3c se usa para validar la estructura de los archivos [HTML](https://validator.w3.org/) y [CSS](https://jigsaw.w3.org/css-validator/)

para validar los archivos html primero compila los fuentes en la carpeta build,
luego ejecuta el validador w3c_validator usando los comandos:

    lektor build --output-path ./build
    cd build
    w3c_validator $(find . -type f -name \*.html)

### Selenium

Para usar selenium se requiere tener ejecutándose un webdriver [instala el webdriver correspondiente a tu plataforma](https://selenium-python.readthedocs.io/installation.html#drivers)

Usando [docker compose](https://docs.docker.com/compose/install/) nos podemos ahorrar algo del tiempo de configuración de selenium hub e instalación de los diferentes drivers

para ejecutar los test ejecuta los siguientes comandos

    docker compose up
    python -m pytest

Por defecto los test corren en chrome, si deseas escoger el navegador que quieres ejecutar, crea una variable de entorno llamada `TEST_BROWSER` con el navegador que deseas usar, en estos momentos soportamos firefox y chrome.
La forma mas fácil de hacer esto es creando un archivo  `.env` con el siguiente contenido

    TEST_BROWSER=firefox

## Actualizar eventos

Para este proceso tenemos un [workflow](https://github.com/PyBAQ/website/actions/workflows/actualizar-eventos-meetup.yml) que nos crea un pull request con la actualización de los eventos

La actualización de eventos se hace a traves de 2 scripts, `scripts/events.py` que extrae la información de meetup y `scripts/create_events.py` que se encarga de crear los eventos

Para ejecutar localmente el script que extrae la información de meetup debes instalar el paquete requests con pip

    python scripts/events.py

El script crea o actualiza el archivo databags/meetup.json con los eventos actualizados. Recuerda adicionarlo al Pull Request con un commit.

> Por favor actualiza los eventos solo si lo consideras estrictamente necesario, entre los metadatos incluidos incluye la fecha de actualización en un timestamp (propenso a conflictos)

Para ejecutar localmente el script que genera los content.lr para cada uno de los eventos

    python scripts/create_events.py

Luego de esto puedes ir a los eventos creados con el admin de lektor y proceder con el respectivo pull request una vez finalices tus cambios
