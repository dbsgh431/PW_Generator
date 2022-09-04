import hashlib
from re import L
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QLineEdit

class PW_GEN():
    def generator(self,txt):
        self.Hash = 'md5'

        site = txt
        id = "kim"
        length= 10
        text = site+id
        text_encode = text.encode('utf-8')
        result = hashlib.new(self.Hash)
        result.update(text_encode)

        self.pw = result.hexdigest()[:int(length)-1] + "!"
        print(self.pw)
        return self.pw

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60,40)
        qle = QLineEdit(self)
        qle.move(60,100)
        qle.textChanged[str].connect(self.onChange)

        self.setWindowTitle('PASSWORD GENERATOR')
        self.center()
        self.resize(400,200)
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onChange(self, text):
        pw_gen = PW_GEN()
        pw = pw_gen.generator(txt=text)
        self.lbl.setText(pw)
        self.lbl.adjustSize()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


