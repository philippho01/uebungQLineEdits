from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QTextBrowser, QLabel, QGridLayout, QLineEdit, QTextBrowser, \
    QPushButton, QTextEdit
from PyQt6.QtCore import pyqtSlot, Qt


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout(self)

        self.zahlen = QLineEdit(parent)
        self.hexa = QLineEdit(parent)
        self.binary = QLineEdit(parent)
        self.letters = QLineEdit(parent)
        self.letters1 = QLineEdit(parent)

        #self.button = QPushButton(parent)
        #self.button.setText("check")
        #self.button.clicked.connect(self.zahlen)

        layout.addWidget(QLabel("Dezimal:"), 1, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Hexadezimal:"), 2, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Binär:"), 3, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Buchstaben:"), 4, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Großbuchstaben:"), 5, 1, Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.zahlen, 1, 2)
        layout.addWidget(self.hexa, 2, 2)
        layout.addWidget(self.binary, 3, 2)
        layout.addWidget(self.letters, 4, 2)
        layout.addWidget(self.letters1, 5, 2)

        self.text_browser = QTextBrowser(self)
        layout.addWidget(self.text_browser, 6, 1, 3, 2)

        self.setLayout(layout)

        self.zahlen.setInputMask("9000")
        self.hexa.setInputMask("HHHHHH")
        self.binary.setInputMask("BBBbbbbbbb")
        self.letters.setMaxLength(-1)
        self.letters1.setInputMask(">A")

        #self.zahlen.textChanged.connect(self.text_changed)
        #self.zahlen.inputRejected.connect(self.text_rejected)

    @pyqtSlot(str)
    def text_changed(self):
        self.text_browser.append(self.binary, self.hexa)


    @pyqtSlot(str)
    def text_rejected(self, text_from_signal: str):
        self.text_browser.append(text_from_signal + "\t(rejected)")

