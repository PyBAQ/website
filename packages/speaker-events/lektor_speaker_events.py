# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


class SpeakerEventsPlugin(Plugin):
    name = 'Speaker Events'
    description = u'Lektor plugin that adds a function to filter events by speaker.'

    def on_setup_env(self):
        def speaker_events(eventos, speaker):
            return [evento for evento in eventos if evento["talks"] and speaker in [talk["speaker"] for talk in evento["talks"].blocks]]

        self.env.jinja_env.filters["speakerevents"] = speaker_events
