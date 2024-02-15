from collections import OrderedDict
import json
import os
from lektor.project import Project
from lektor.utils import slugify

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT_PATH = os.path.dirname(HERE)

def extract_meetup_json(file):
    with open(file, "r", encoding="utf-8") as meetup_data:
        events = json.loads(meetup_data.read())
        return events

# TODO: Remove after migration is done
def attachments():
    project = Project.discover()
    env = project.make_env()
    pad = env.new_pad()
    eventos = pad.get('/eventos1/')
    return {evento["title"]: evento["attach"] for evento in eventos["body"].blocks[1]["body"].blocks[0]["anexos"].blocks}

def transform_event(event: dict):
    content = OrderedDict()
    content["title"] = event["name"]
    content["date_start"] = "{} {}".format(event["local_date"], event["local_time"])
    content["link"] = event["link"]
    content["information"] = event["description"]
    try:
        content["featured_photo"] = event["featured_photo"]["photo_link"]
    except KeyError:
        print("Key error: featured_photo on", event["name"])
    try:
        content["venue"] = event["venue"]["name"]
        content["address_1"] = event["venue"]["address_1"]
    except KeyError:
        print("Key error: venue on", event["name"])
    # TODO: remove when migration is complete
    content["talks"] = '\n\n#### talk ####\ntitle: {}\n----\nattach: {}'.format(event["name"], attachment_index.get(event["name"], ""))
    return content

def write_content(slug, fields):
    folderpath = os.path.join(PROJECT_ROOT_PATH, 'content', 'eventos', slug)
    if not os.path.isdir(folderpath):
        os.makedirs(folderpath)
    filepath = os.path.join(folderpath, 'contents.lr')
    items = ['{}: {}\n'.format(key, value) for key, value in fields.items()]

    if os.path.isfile(filepath):
        print("File for slug {} already exists, skipping".format(slug))
    else:
        with open(filepath, 'w') as fh:
            fh.write('---\n'.join(items))

def load_events(events):
    for event in events:
        write_content(event["date_start"][:10] + "-" + slugify(event["title"]), event)

events = extract_meetup_json("databags/meetup.json")
attachment_index = attachments()
transformed_events = [transform_event(event) for event in events["past_events"]]
load_events(transformed_events)
