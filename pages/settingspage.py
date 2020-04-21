from PyQt5 import QtCore, QtGui, QtWidgets
from utils import return_data,write_data
import sys,platform,settings
def no_abort(a, b, c):
    sys.__excepthook__(a, b, c)
sys.excepthook = no_abort

class SettingsPage(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(SettingsPage, self).__init__(parent)
        self.setupUi(self)
    def setupUi(self, settingspage):
        self.settingspage = settingspage
        self.settingspage.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.settingspage.setGeometry(QtCore.QRect(60, 0, 1041, 601))
        self.settingspage.setStyleSheet("QComboBox::drop-down {    border: 0px;}QComboBox::down-arrow {    image: url(:/images/down_icon.png);    width: 14px;    height: 14px;}QComboBox{    padding: 1px 0px 1px 3px;}QLineEdit:focus {   border: none;   outline: none;}")
        self.settings_card = QtWidgets.QWidget(self.settingspage)
        self.settings_card.setGeometry(QtCore.QRect(30, 70, 471, 501))
        font = QtGui.QFont()
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setFamily("Arial")
        self.settings_card.setFont(font)
        self.settings_card.setStyleSheet("background-color: #232323;border-radius: 20px;border: 1px solid #2e2d2d;")
        self.webhook_edit = QtWidgets.QLineEdit(self.settings_card)
        self.webhook_edit.setGeometry(QtCore.QRect(30, 50, 411, 21))
        self.webhook_edit.setFont(font)
        self.webhook_edit.setStyleSheet("outline: 0;border: 1px solid #5D43FB;border-width: 0 0 2px;color: rgb(234, 239, 239);")
        self.webhook_edit.setPlaceholderText("Webhook Link")
        self.webhook_edit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.webhook_header = QtWidgets.QLabel(self.settings_card)
        self.webhook_header.setGeometry(QtCore.QRect(20, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18) if platform.system() == "Darwin" else font.setPointSize(18*.75)
        font.setWeight(50)
        self.webhook_header.setFont(font)
        self.webhook_header.setStyleSheet("color: rgb(212, 214, 214);border:  none;")
        self.webhook_header.setText("Webhook")
        self.savesettings_btn = QtWidgets.QPushButton(self.settings_card)
        self.savesettings_btn.setGeometry(QtCore.QRect(190, 450, 86, 32))
        font = QtGui.QFont()
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setFamily("Arial")
        self.savesettings_btn.setFont(font)
        self.savesettings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.savesettings_btn.setStyleSheet("color: #FFFFFF;background-color: #5D43FB;border-radius: 10px;border: 1px solid #2e2d2d;")
        self.savesettings_btn.setText("Save")
        self.savesettings_btn.clicked.connect(self.save_settings)
        self.browser_checkbox = QtWidgets.QCheckBox(self.settings_card)
        self.browser_checkbox.setGeometry(QtCore.QRect(30, 90, 111, 20))
        self.browser_checkbox.setStyleSheet("color: #FFFFFF;border: none;")
        self.browser_checkbox.setText("Browser Opened")
        self.order_checkbox = QtWidgets.QCheckBox(self.settings_card)
        self.order_checkbox.setGeometry(QtCore.QRect(30, 120, 221, 20))
        self.order_checkbox.setStyleSheet("color: #FFFFFF;border: none;")
        self.order_checkbox.setText("Order Placed")
        self.paymentfailed_checkbox = QtWidgets.QCheckBox(self.settings_card)
        self.paymentfailed_checkbox.setGeometry(QtCore.QRect(30, 150, 121, 20))
        self.paymentfailed_checkbox.setStyleSheet("color: #FFFFFF;border: none;")
        self.paymentfailed_checkbox.setText("Payment Failed")
        self.general_header = QtWidgets.QLabel(self.settings_card)
        self.general_header.setGeometry(QtCore.QRect(20, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18) if platform.system() == "Darwin" else font.setPointSize(18*.75)
        font.setWeight(50)
        self.general_header.setFont(font)
        self.general_header.setStyleSheet("color: rgb(212, 214, 214);border:  none;")
        self.general_header.setText("General")
        self.onfailed_checkbox = QtWidgets.QCheckBox(self.settings_card)
        self.onfailed_checkbox.setGeometry(QtCore.QRect(30, 220, 221, 20))
        self.onfailed_checkbox.setStyleSheet("color: #FFFFFF;border: none;")
        self.onfailed_checkbox.setText("Open browser on payment failed")
        self.buy_one_checkbox = QtWidgets.QCheckBox(self.settings_card)
        self.buy_one_checkbox.setGeometry(QtCore.QRect(30, 250, 221, 20))
        self.buy_one_checkbox.setStyleSheet("color: #FFFFFF;border: none;")
        self.buy_one_checkbox.setText("Stop All after success")
        self.proxies_header = QtWidgets.QLabel(self.settingspage)
        self.proxies_header.setGeometry(QtCore.QRect(30, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22) if platform.system() == "Darwin" else font.setPointSize(22*.75)
        font.setWeight(50)
        self.proxies_header.setFont(font)
        self.proxies_header.setStyleSheet("color: rgb(234, 239, 239);")
        self.proxies_header.setText("Settings")
        self.set_data()
        QtCore.QMetaObject.connectSlotsByName(settingspage)

    def set_data(self):
        settings = return_data("./data/settings.json")
        self.webhook_edit.setText(settings["webhook"])
        if settings["webhookonbrowser"]:
            self.browser_checkbox.setChecked(True)
        if settings["webhookonorder"]:
            self.order_checkbox.setChecked(True)
        if settings["webhookonfailed"]:
            self.paymentfailed_checkbox.setChecked(True)
        if settings["browseronfailed"]:
            self.onfailed_checkbox.setChecked(True)
        if settings['onlybuyone']:
            self.buy_one_checkbox.setChecked(True)
        self.update_settings(settings)

    def save_settings(self):
        settings = {"webhook":self.webhook_edit.text(),
                    "webhookonbrowser":self.browser_checkbox.isChecked(),
                    "webhookonorder":self.order_checkbox.isChecked(),
                    "webhookonfailed":self.paymentfailed_checkbox.isChecked(),
                    "browseronfailed":self.onfailed_checkbox.isChecked(),
                    'onlybuyone':self.buy_one_checkbox.isChecked()}
        write_data("./data/settings.json",settings)
        self.update_settings(settings)
        QtWidgets.QMessageBox.information(self, "Bird Bot", "Saved Settings")

    def update_settings(self,settings_data):
        global webhook, webhook_on_browser, webhook_on_order, webhook_on_failed, browser_on_failed
        settings.webhook, settings.webhook_on_browser, settings.webhook_on_order, settings.webhook_on_failed, settings.browser_on_failed, settings.buy_one = settings_data["webhook"], settings_data["webhookonbrowser"], settings_data["webhookonorder"], settings_data["webhookonfailed"], settings_data["browseronfailed"], settings_data['onlybuyone']












