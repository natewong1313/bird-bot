from PyQt5 import QtCore, QtGui, QtWidgets
from utils import return_data,write_data
import sys,platform
def no_abort(a, b, c):
    sys.__excepthook__(a, b, c)
sys.excepthook = no_abort

class ProxiesPage(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(ProxiesPage, self).__init__(parent)
        self.setupUi(self)
    def setupUi(self, proxiespage):
        self.proxiespage = proxiespage
        self.proxiespage.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.proxiespage.setGeometry(QtCore.QRect(60, 0, 1041, 601))
        self.proxiespage.setStyleSheet("QComboBox::drop-down {    border: 0px;}QComboBox::down-arrow {    image: url(:/images/down_icon.png);    width: 14px;    height: 14px;}QComboBox{    padding: 1px 0px 1px 3px;}QLineEdit:focus {   border: none;   outline: none;}")
        self.proxies_card = QtWidgets.QWidget(self.proxiespage)
        self.proxies_card.setGeometry(QtCore.QRect(30, 70, 981, 501))
        font = QtGui.QFont()
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setFamily("Arial")
        self.proxies_card.setFont(font)
        self.proxies_card.setStyleSheet("background-color: #232323;border-radius: 20px;border: 1px solid #2e2d2d;")
        self.listname_edit = QtWidgets.QLineEdit(self.proxies_card)
        self.listname_edit.setGeometry(QtCore.QRect(20, 50, 161, 21))
        self.listname_edit.setFont(font)
        self.listname_edit.setStyleSheet("outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);")
        self.listname_edit.setPlaceholderText("List Name")
        self.listname_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.editproxies_header = QtWidgets.QLabel(self.proxies_card)
        self.editproxies_header.setGeometry(QtCore.QRect(20, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18) if platform.system() == "Darwin" else font.setPointSize(18*.75)
        font.setWeight(50)
        self.editproxies_header.setFont(font)
        self.editproxies_header.setStyleSheet("color: rgb(212, 214, 214);border:  none;")
        self.editproxies_header.setText("Edit Proxies")
        self.loadlist_box = QtWidgets.QComboBox(self.proxies_card)
        self.loadlist_box.setGeometry(QtCore.QRect(210, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setFamily("Arial")
        self.loadlist_box.setFont(font)
        self.loadlist_box.setStyleSheet("outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);")
        self.loadlist_box.addItem("Load List")
        self.loadlist_box.currentTextChanged.connect(self.load_proxies)
        self.saveproxies_btn = QtWidgets.QPushButton(self.proxies_card)
        self.saveproxies_btn.setGeometry(QtCore.QRect(400, 450, 86, 32))
        self.saveproxies_btn.setFont(font)
        self.saveproxies_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveproxies_btn.setStyleSheet("color: #FFFFFF;background-color: #5D43FB;border-radius: 10px;border: 1px solid #2e2d2d;")
        self.saveproxies_btn.setText("Save")
        self.saveproxies_btn.clicked.connect(self.save_proxies)
        self.proxies_edit = QtWidgets.QTextEdit(self.proxies_card)
        self.proxies_edit.setGeometry(QtCore.QRect(20, 90, 941, 341))
        self.proxies_edit.setFont(font)
        self.proxies_edit.setStyleSheet("color: #FFFFFF;padding: 10px;")
        self.proxies_edit.setPlaceholderText("ip:port or ip:port:user:pass")
        self.proxies_edit.setAcceptRichText(False)
        self.deleteproxies_btn = QtWidgets.QPushButton(self.proxies_card)
        self.deleteproxies_btn.setGeometry(QtCore.QRect(500, 450, 86, 32))
        self.deleteproxies_btn.setFont(font)
        self.deleteproxies_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteproxies_btn.setStyleSheet("color: #FFFFFF;background-color: #5D43FB;border-radius: 10px;border: 1px solid #2e2d2d;")
        self.deleteproxies_btn.setText("Delete")
        self.deleteproxies_btn.clicked.connect(self.delete_proxies)
        self.proxies_header = QtWidgets.QLabel(self.proxiespage)
        self.proxies_header.setGeometry(QtCore.QRect(30, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22) if platform.system() == "Darwin" else font.setPointSize(22*.75)
        font.setWeight(50)
        self.proxies_header.setFont(font)
        self.proxies_header.setStyleSheet("color: rgb(234, 239, 239);")
        self.proxies_header.setText("Proxies")
        self.set_data()
        QtCore.QMetaObject.connectSlotsByName(proxiespage)
    
    def set_data(self):
        proxies = return_data("./data/proxies.json")
        for proxies_list in proxies:
            list_name = proxies_list["list_name"]
            self.loadlist_box.addItem(list_name)
            self.parent().parent().createdialog.proxies_box.addItem(list_name)

    def load_proxies(self):
        list_name = self.loadlist_box.currentText()
        if list_name !="Load Proxies":
            proxies = return_data("./data/proxies.json")
            for proxies_list in proxies:
                if proxies_list["list_name"] == list_name:
                    self.listname_edit.setText(list_name)
                    self.proxies_edit.setText(proxies_list["proxies"])

    def save_proxies(self):
        list_name = self.listname_edit.text()
        proxies = self.proxies_edit.toPlainText()
        if proxies != "" and list_name != "":
            for item in proxies.splitlines():
                if ":" not in item or item == "":
                    QtWidgets.QMessageBox.critical(self, "Bird Bot", "Incorrect Proxies")
                    return
            proxies_data = {
                "list_name": list_name,
                "proxies": self.proxies_edit.toPlainText()
            }
            proxies = return_data("./data/proxies.json")
            for p in proxies:
                if p["list_name"] == list_name:
                    proxies.remove(p)
                    break
            proxies.append(proxies_data)
            write_data("./data/proxies.json",proxies)
            if self.loadlist_box.findText(list_name) == -1:
                self.loadlist_box.addItem(list_name)
                self.parent().parent().createdialog.proxies_box.addItem(list_name)
            QtWidgets.QMessageBox.information(self, "Bird Bot", "Saved Proxies")
        else:
            QtWidgets.QMessageBox.critical(self, "Bird Bot", "Missing Fields")
    
    def delete_proxies(self):
        list_name = self.listname_edit.text()
        proxies = return_data("./data/proxies.json")
        for p in proxies:
            if p["list_name"] == list_name:
                proxies.remove(p)
                break
        write_data("./data/proxies.json",proxies)
        self.loadlist_box.removeItem(self.loadlist_box.findText(list_name))
        self.parent().parent().createdialog.proxies_box.removeItem(self.parent().parent().createdialog.proxies_box.findText(list_name))
        self.loadlist_box.setCurrentIndex(0)
        self.listname_edit.setText("")
        self.proxies_edit.setText("")
        QtWidgets.QMessageBox.information(self, "Bird Bot", "Deleted Proxy List")

