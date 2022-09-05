import hashlib

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QLineEdit

class PW_GEN():
    def generator(self,txt):

        self.Hash = 'md5'
        length = 10

        text_encode = txt.encode('utf-8')
        result = hashlib.new(self.Hash)
        result.update(text_encode)

        self.pw = result.hexdigest()[:int(length)-1] + "!"
        print(self.pw)
        return self.pw

class MyApp(QWidget):
    global id
    id = ''
    global site
    site= ''

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel(self)
        self.lbl.move(100,120)
        self.lbl.setText("__")

        self.lbl1 = QLabel(self)
        self.lbl1.move(20,20)
        self.lbl1.setText("사이트 이름 ex)구글")

        self.lbl2 = QLabel(self)
        self.lbl2.move(20,80)
        self.lbl2.setText("아이디 이름 ex)abcd123")

        self.lbl3 = QLabel(self)
        self.lbl3.move(20,120)
        self.lbl3.setText("생성 결과")


        qle = QLineEdit(self)
        qle.move(160,20)
        qle.textChanged[str].connect(self.onChangeSite)

        qle2 = QLineEdit(self)
        qle2.move(160,80)
        qle2.textChanged[str].connect(self.onChangeID)


        self.setWindowTitle('PASSWORD GENERATOR')
        self.center()
        self.resize(400,200)
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onChangeSite(self, text=""):
        global site
        global id
        site = text
        self.onChange()

    def onChangeID(self, text=""):
        global site
        global id
        id = text
        self.onChange()

    def onChange(self):
        pw_gen = PW_GEN()
        text = site + id
        pw = pw_gen.generator(txt=text)
        self.lbl.setText(pw)
        self.lbl.adjustSize()    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


