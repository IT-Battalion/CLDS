import json

import requests as requests


def preview_data(json_input):
    return "reliable: " + ("<b>yes</b>" if json_input["reliable"] else "no") + "<br>" + \
        "language: <b>" + json_input["language"] + "</b><br>" + \
        "probability: <b>" + str(json_input["prob"]) + "%</b>"


class LangResp:
    def __init__(self):
        pass

    def execute(self, text: str):
        req = requests.get('http://localhost:5000/lg', params={
            'id': text
        })
        parsed_json = json.loads(req.content)
        return preview_data(parsed_json)
