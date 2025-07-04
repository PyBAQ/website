"""
Este script procesa eventos de un archivo JSON de Meetup y los transforma
para ser almacenados en el sistema de contenido.
"""

import json
import os
from collections import OrderedDict

from lektor.utils import slugify
from datetime import datetime

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT_PATH = os.path.dirname(HERE)


def extract_meetup_json(file):
    """
    Lee el archivo JSON proporcionado y devuelve una lista de eventos.

    Args:
        file (str): Ruta al archivo JSON de Meetup.

    Returns:
        list: Lista de eventos obtenidos del archivo JSON.
    """
    with open(file, "r", encoding="utf-8") as meetup_data:
        events = json.loads(meetup_data.read())
        return events


def transform_event(event_node: dict):
    """
    Transforma un evento de Meetup en un diccionario ordenado con los campos necesarios.

    Args:
        event (dict): Diccionario con los datos del evento de Meetup.

    Returns:
        OrderedDict: Diccionario ordenado con los campos transformados.
    """
    event = event_node['node']
    content = OrderedDict()
    content["title"] = event["title"]
    dt = datetime.fromisoformat(event['dateTime'].replace('Z', '+00:00'))
    content["date_start"] = dt.strftime('%Y-%m-%d %H:%M')
    content["link"] = event["eventUrl"]
    content["information"] = event["description"]
    if event["featuredEventPhoto"]:
        content["featured_photo"] = event["featuredEventPhoto"]["standardUrl"]
    if event["venues"] and len(event["venues"])>0:
        content["venue"] = event["venues"][0]["name"]
        content["address_1"] = event["venues"][0]["address"]
    return content


def write_content(slug, fields):
    """
    Escribe el contenido del evento en un archivo con formato específico.

    Args:
        slug (str): Slug único del evento.
        fields (OrderedDict): Campos del evento a escribir en el archivo.
    """
    folderpath = os.path.join(PROJECT_ROOT_PATH, "content", "eventos", slug)
    if not os.path.isdir(folderpath):
        os.makedirs(folderpath)
    filepath = os.path.join(folderpath, "contents.lr")
    items = [f"{key}: {value}\n" for key, value in fields.items()]

    if os.path.isfile(filepath):
        print(f"File for slug {slug} already exists, skipping")
    else:
        print(f"Creating file for slug {slug}")
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write("---\n".join(items))


def load_events(event_list):
    """
    Carga y guarda eventos transformados.

    Args:
        event_list (list): Lista de eventos transformados.
    """
    for event in event_list:
        slug = event["date_start"][:10] + "-" + slugify(event["title"])
        write_content(slug, event)


if __name__ == "__main__":
    event_data = extract_meetup_json("databags/meetup_gql.json")
    transformed_events = [
        transform_event(event)
        for event in event_data["data"]["groupByUrlname"]["past_events"]["edges"]
    ]
    load_events(transformed_events)
