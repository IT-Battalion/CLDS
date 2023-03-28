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
        req = requests.get('http://127.0.0.1:5000/lg', params={
            'id': text
        })
        if req.status_code == 200:
            parsed_json = json.loads(req.content)
            return preview_data(parsed_json)
        return "Error: " + req.reason + "(" + str(req.status_code) + ")"
