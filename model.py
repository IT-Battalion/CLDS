import json

import requests as requests


def preview_data(json_input):
    return "reliable: " + ("yes" if json_input["reliable"] else "no") + "\n" + \
        "language: " + json_input["language"] + "\n" + \
        "probability: " + str(json_input["prob"]) + "%"


class LangResp:
    def __init__(self):
        pass

    def execute(self, text: str):
        req = requests.get('http://localhost:5000/lg', params={
            'id': text
        })
        parsed_json = json.loads(req.content)
        return preview_data(parsed_json)
