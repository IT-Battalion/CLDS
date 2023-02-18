from flask import Flask, request, jsonify
from iso639 import languages
from langdetect import detect_langs

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/lg')
def lg():
    print("Start")
    search = request.args.get("id")
    print("Detect")
    rep = detect_lang(search).serialize()
    print(rep)
    return jsonify(rep)


def detect_lang(search):
    result = detect_langs(search)
    best = result[0]
    prob = round(best.prob * 100, 2)
    short = best.lang
    is_reliable = best.prob > 0.5
    long = languages.get(part1=short).name
    ret = Resp(is_reliable, long, short, prob)
    return ret


class Resp:
    def __init__(self, reliable: bool, language: str, short: str, prob: float):
        self.reliable = reliable
        self.language = language
        self.short = short
        self.prob = prob

    def serialize(self):
        return {"reliable": str(self.reliable),
                "language": self.language,
                "short": self.short,
                "prob": str(self.prob)}


if __name__ == '__main__':
    app.run(debug=False)
