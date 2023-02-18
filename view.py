from PyQt6 import uic
from PyQt6.QtWidgets import QPushButton, QMainWindow, QTextEdit, QStatusBar, QTextBrowser


class View(QMainWindow):
    pb_reset: QPushButton
    pb_check: QPushButton
    result: QTextBrowser
    text: QTextEdit
    statusbar: QStatusBar

    def __init__(self, c):
        super().__init__()
        uic.loadUi("client.ui", self)
        self.pb_reset.clicked.connect(c.reset)
        self.pb_check.clicked.connect(c.execute)

    def reset(self):
        self.text.setText('')
        self.result.setText('')

    def get_text(self):
        return self.text

    def show_message_status(self, msg: str):
        self.statusbar.showMessage(msg)

    def change_result(self, r: str):
        curs = self.result.textCursor()
        curs.insertHtml(r)
