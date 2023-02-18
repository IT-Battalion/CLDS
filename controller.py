from model import LangResp
from view import View


class Controller:
    def __init__(self):
        self.model = LangResp()
        self.view = View(self)
        self.view.show()

    def execute(self):
        text = self.view.get_text()
        res = self.model.execute(text)
        self.view.change_result(res)

    def reset(self):
        self.view.reset()
