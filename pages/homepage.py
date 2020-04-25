from PyQt5 import QtCore, QtGui, QtWidgets
from sites.walmart import Walmart
from sites.bestbuy import BestBuy
from pages.createdialog import CreateDialog
from utils import get_profile, get_proxy, BirdLogger, return_data, write_data, open_browser
import urllib.request,sys,platform,ssl
import settings
def no_abort(a, b, c):
    sys.__excepthook__(a, b, c)
sys.excepthook = no_abort
logger = BirdLogger()
class HomePage(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(HomePage, self).__init__(parent)
        self.setupUi(self)
        self.load_tasks()
    def setupUi(self, homepage):
        global tasks
        self.tasks = []
        tasks = self.tasks
        self.homepage = homepage
        self.homepage.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.homepage.setGeometry(QtCore.QRect(60, 0, 1041, 601))
        self.tasks_card = QtWidgets.QWidget(self.homepage)
        self.tasks_card.setGeometry(QtCore.QRect(30, 110, 991, 461))
        self.tasks_card.setStyleSheet("background-color: #232323;border-radius: 20px;border: 1px solid #2e2d2d;")
        self.scrollArea = QtWidgets.QScrollArea(self.tasks_card)
        self.scrollArea.setGeometry(QtCore.QRect(20, 30, 951, 421))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet("border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 951, 421))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.image_table_header = QtWidgets.QLabel(self.tasks_card)
        self.image_table_header.setGeometry(QtCore.QRect(40, 7, 51, 31))
        self.image_table_header.setText("Image")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15) if platform.system() == "Darwin" else font.setPointSize(15*.75)
        font.setBold(False)
        font.setWeight(50)
        self.image_table_header.setFont(font)
        self.image_table_header.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.product_table_header = QtWidgets.QLabel(self.tasks_card)
        self.product_table_header.setGeometry(QtCore.QRect(240, 7, 61, 31))
        self.product_table_header.setFont(font)
        self.product_table_header.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.product_table_header.setText("Product")
        self.profile_table_header = QtWidgets.QLabel(self.tasks_card)
        self.profile_table_header.setGeometry(QtCore.QRect(590, 7, 61, 31))
        self.profile_table_header.setFont(font)
        self.profile_table_header.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.profile_table_header.setText("Profile")
        self.status_table_header = QtWidgets.QLabel(self.tasks_card)
        self.status_table_header.setGeometry(QtCore.QRect(650, 7, 61, 31))
        self.status_table_header.setFont(font)
        self.status_table_header.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.status_table_header.setText("Status")
        self.actions_table_header = QtWidgets.QLabel(self.tasks_card)
        self.actions_table_header.setGeometry(QtCore.QRect(890, 7, 61, 31))
        self.actions_table_header.setFont(font)
        self.actions_table_header.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.actions_table_header.setText("Actions")
        self.site_table_header = QtWidgets.QLabel(self.tasks_card)
        self.site_table_header.setGeometry(QtCore.QRect(160, 7, 61, 31))
        self.site_table_header.setFont(font)
        self.site_table_header.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.site_table_header.setText("Site")
        self.id_header = QtWidgets.QLabel(self.tasks_card)
        self.id_header.setGeometry(QtCore.QRect(110, 7, 31, 31))
        self.id_header.setFont(font)
        self.id_header.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.id_header.setText("ID")
        self.tasks_header = QtWidgets.QLabel(self.homepage)
        self.tasks_header.setGeometry(QtCore.QRect(30, 10, 61, 31))
        self.tasks_header.setText("Tasks")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22) if platform.system() == "Darwin" else font.setPointSize(22*.75)
        font.setBold(False)
        font.setWeight(50)
        self.tasks_header.setFont(font)
        self.tasks_header.setStyleSheet("color: rgb(234, 239, 239);")
        self.checkouts_card = QtWidgets.QWidget(self.homepage)
        self.checkouts_card.setGeometry(QtCore.QRect(440, 45, 171, 51))
        self.checkouts_card.setStyleSheet("background-color: #232323;border-radius: 10px;border: 1px solid #2e2d2d;")
        self.checkouts_label = QtWidgets.QLabel(self.checkouts_card)
        self.checkouts_label.setGeometry(QtCore.QRect(78, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16) if platform.system() == "Darwin" else font.setPointSize(16*.75)
        font.setBold(False)
        font.setWeight(50)
        self.checkouts_label.setFont(font)
        self.checkouts_label.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.checkouts_label.setText("Checkouts")
        self.checkouts_icon = QtWidgets.QLabel(self.checkouts_card)
        self.checkouts_icon.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.checkouts_icon.setStyleSheet("border: none;")
        self.checkouts_icon.setText("")
        self.checkouts_icon.setPixmap(QtGui.QPixmap(":/images/success.png"))
        self.checkouts_icon.setScaledContents(True)
        global checkouts_count
        self.checkouts_count = QtWidgets.QLabel(self.checkouts_card)
        checkouts_count = self.checkouts_count
        self.checkouts_count.setGeometry(QtCore.QRect(43, 10, 31, 31))
        self.checkouts_count.setFont(font)
        self.checkouts_count.setStyleSheet("color: #34C693;border: none;")
        self.checkouts_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.checkouts_count.setText("0")
        self.tasks_total_card = QtWidgets.QWidget(self.homepage)
        self.tasks_total_card.setGeometry(QtCore.QRect(30, 45, 181, 51))
        self.tasks_total_card.setStyleSheet("background-color: #232323;border-radius: 10px;border: 1px solid #2e2d2d;")
        self.tasks_total_label = QtWidgets.QLabel(self.tasks_total_card)
        self.tasks_total_label.setGeometry(QtCore.QRect(80, 10, 91, 31))
        self.tasks_total_label.setFont(font)
        self.tasks_total_label.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.tasks_total_label.setText("Total Tasks")
        self.tasks_total_icon = QtWidgets.QLabel(self.tasks_total_card)
        self.tasks_total_icon.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.tasks_total_icon.setStyleSheet("border: none;")
        self.tasks_total_icon.setText("")
        self.tasks_total_icon.setPixmap(QtGui.QPixmap(":/images/tasks.png"))
        self.tasks_total_icon.setScaledContents(True)
        global tasks_total_count
        self.tasks_total_count = QtWidgets.QLabel(self.tasks_total_card)
        tasks_total_count = self.tasks_total_count
        self.tasks_total_count.setGeometry(QtCore.QRect(43, 10, 31, 31))
        self.tasks_total_count.setFont(font)
        self.tasks_total_count.setStyleSheet("color: #755FF6;border: none;")
        self.tasks_total_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tasks_total_count.setText("0")
        self.carted_card = QtWidgets.QWidget(self.homepage)
        self.carted_card.setGeometry(QtCore.QRect(240, 45, 171, 51))
        self.carted_card.setStyleSheet("background-color: #232323;border-radius: 10px;border: 1px solid #2e2d2d;")
        self.carted_label = QtWidgets.QLabel(self.carted_card)
        self.carted_label.setGeometry(QtCore.QRect(80, 10, 90, 31))
        self.carted_label.setFont(font)
        self.carted_label.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.carted_label.setText("Total Carts")
        self.carted_icon = QtWidgets.QLabel(self.carted_card)
        self.carted_icon.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.carted_icon.setStyleSheet("border: none;")
        self.carted_icon.setText("")
        self.carted_icon.setPixmap(QtGui.QPixmap(":/images/cart.png"))
        self.carted_icon.setScaledContents(True)
        global carted_count
        self.carted_count = QtWidgets.QLabel(self.carted_card)
        carted_count = self.carted_count
        self.carted_count.setGeometry(QtCore.QRect(43, 10, 31, 31))
        self.carted_count.setFont(font)
        self.carted_count.setStyleSheet("color: #F6905E;border: none;")
        self.carted_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.carted_count.setText("0")
        self.buttons_card = QtWidgets.QWidget(self.homepage)
        self.buttons_card.setGeometry(QtCore.QRect(640, 45, 381, 51))
        self.buttons_card.setStyleSheet("background-color: #232323;border-radius: 10px;border: 1px solid #2e2d2d;")
        self.startall_btn = QtWidgets.QPushButton(self.buttons_card)
        self.startall_btn.setGeometry(QtCore.QRect(103, 10, 86, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.startall_btn.setFont(font)
        self.startall_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startall_btn.setStyleSheet("color: #FFFFFF;background-color: #5D43FB;border: none;")
        self.startall_btn.setText("Start All")
        self.startall_btn.clicked.connect(self.start_all_tasks)
        self.stopall_btn = QtWidgets.QPushButton(self.buttons_card)
        self.stopall_btn.setGeometry(QtCore.QRect(197, 10, 81, 32))
        self.stopall_btn.setFont(font)
        self.stopall_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopall_btn.setStyleSheet("color: #FFFFFF;background-color: #5D43FB;border: none;")
        self.stopall_btn.setText("Stop All")
        self.stopall_btn.clicked.connect(self.stop_all_tasks)
        self.deleteall_btn = QtWidgets.QPushButton(self.buttons_card)
        self.deleteall_btn.setGeometry(QtCore.QRect(285, 10, 86, 32))
        self.deleteall_btn.setFont(font)
        self.deleteall_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteall_btn.setStyleSheet("color: #FFFFFF;background-color: #5D43FB;border: none;")
        self.deleteall_btn.setText("Delete All")
        self.deleteall_btn.clicked.connect(self.delete_all_tasks)
        self.newtask_btn = QtWidgets.QPushButton(self.buttons_card)
        self.newtask_btn.setGeometry(QtCore.QRect(10, 10, 86, 32))
        self.newtask_btn.setFont(font)
        self.newtask_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.newtask_btn.setStyleSheet("color: #FFFFFF;background-color: #5D43FB;border: none;")
        self.newtask_btn.setText("New Task")
        QtCore.QMetaObject.connectSlotsByName(homepage)

    def load_tasks(self):
        tasks_data = return_data("./data/tasks.json")
        write_data("./data/tasks.json",[])
        try:
            for task in tasks_data:
                tab = TaskTab(task["site"],task["product"],task["profile"],task["proxies"],task["monitor_delay"],task["error_delay"],task["max_price"],self.stop_all_tasks,self.scrollAreaWidgetContents)
                self.verticalLayout.takeAt(self.verticalLayout.count()-1)
                self.verticalLayout.addWidget(tab)
                spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem)
        except:
            pass

    def set_settings_data(self,settings_data):
        global settings
        settings = settings_data

    def start_all_tasks(self):
        for task in self.tasks:
            try:
                task.start(None)
            except:
                pass
    def stop_all_tasks(self):
        for task in self.tasks:
            try:
                task.stop(None)
            except:
                pass

    def delete_all_tasks(self):
        for task in self.tasks:
            try:
                task.delete(None)
            except:
                pass

class TaskTab(QtWidgets.QWidget):
    def __init__(self,site,product,profile,proxies,monitor_delay,error_delay,max_price,stop_all,parent=None):
        super(TaskTab, self).__init__(parent)
        self.task_id = str(int(tasks_total_count.text())+1)
        tasks_total_count.setText(self.task_id)
        self.site,self.product,self.profile,self.proxies,self.monitor_delay,self.error_delay,self.max_price,self.stop_all = site,product,profile,proxies,monitor_delay,error_delay,max_price,stop_all
        self.setupUi(self)
        tasks.append(self)
        tasks_data = return_data("./data/tasks.json")
        task_data = {"task_id": self.task_id,"site":self.site,"product": self.product,"profile": self.profile,"proxies": self.proxies,"monitor_delay": self.monitor_delay,"error_delay": self.error_delay,"max_price": self.max_price}
        tasks_data.append(task_data)
        write_data("./data/tasks.json",tasks_data)
    def setupUi(self,TaskTab):
        self.running = False

        self.TaskTab = TaskTab
        self.TaskTab.setMinimumSize(QtCore.QSize(0, 50))
        self.TaskTab.setMaximumSize(QtCore.QSize(16777215, 50))
        self.TaskTab.setStyleSheet("border-radius: none;")
        self.product_label = QtWidgets.QLabel(self.TaskTab)
        self.product_label.setGeometry(QtCore.QRect(222, 10, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setBold(False)
        font.setWeight(50)
        self.product_label.setFont(font)
        self.product_label.setStyleSheet("color: rgb(234, 239, 239);")
        self.profile_label = QtWidgets.QLabel(self.TaskTab)
        self.profile_label.setGeometry(QtCore.QRect(571, 10, 51, 31))
        self.profile_label.setFont(font)
        self.profile_label.setStyleSheet("color: rgb(234, 239, 239);")
        self.status_label = QtWidgets.QLabel(self.TaskTab)
        self.status_label.setGeometry(QtCore.QRect(632, 10, 231, 31))
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("color: rgb(234, 239, 239);")
        self.browser_label = QtWidgets.QLabel(self.TaskTab)
        self.browser_label.setGeometry(QtCore.QRect(632, 10, 231, 31))
        self.browser_label.setFont(font)
        self.browser_label.setStyleSheet("color: rgb(163, 149, 255);")
        self.browser_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browser_label.mousePressEvent = self.open_browser
        self.browser_label.hide()
        self.start_btn = QtWidgets.QLabel(self.TaskTab)
        self.start_btn.setGeometry(QtCore.QRect(870, 15, 16, 16))
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setPixmap(QtGui.QPixmap(":/images/play.png"))
        self.start_btn.setScaledContents(True)
        self.start_btn.mousePressEvent = self.start
        self.stop_btn = QtWidgets.QLabel(self.TaskTab)
        self.stop_btn.setGeometry(QtCore.QRect(870, 15, 16, 16))
        self.stop_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_btn.setPixmap(QtGui.QPixmap(":/images/stop.png"))
        self.stop_btn.setScaledContents(True)
        self.stop_btn.mousePressEvent = self.stop
        self.delete_btn = QtWidgets.QLabel(self.TaskTab)
        self.delete_btn.setGeometry(QtCore.QRect(920, 15, 16, 16))
        self.delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn.setPixmap(QtGui.QPixmap(":/images/trash.png"))
        self.delete_btn.setScaledContents(True)
        self.delete_btn.mousePressEvent = self.delete
        self.edit_btn = QtWidgets.QLabel(self.TaskTab)
        self.edit_btn.setGeometry(QtCore.QRect(895, 15, 16, 16))
        self.edit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_btn.setPixmap(QtGui.QPixmap(":/images/edit.png"))
        self.edit_btn.setScaledContents(True)
        self.edit_btn.mousePressEvent = self.edit
        self.image = QtWidgets.QLabel(self.TaskTab)
        self.image.setGeometry(QtCore.QRect(20, 0, 50, 50))
        self.image.setPixmap(QtGui.QPixmap(":/images/no_image.png"))
        self.image.setScaledContents(True)
        self.site_label = QtWidgets.QLabel(self.TaskTab)
        self.site_label.setGeometry(QtCore.QRect(140, 10, 61, 31))
        self.site_label.setFont(font)
        self.site_label.setStyleSheet("color: rgb(234, 239, 239);")
        self.id_label = QtWidgets.QLabel(self.TaskTab)
        self.id_label.setGeometry(QtCore.QRect(90, 10, 31, 31))
        self.id_label.setFont(font)
        self.id_label.setStyleSheet("color: rgb(234, 239, 239);")
        self.stop_btn.raise_()
        self.product_label.raise_()
        self.profile_label.raise_()
        self.browser_label.raise_()
        self.start_btn.raise_()
        self.delete_btn.raise_()
        self.image.raise_()
        self.site_label.raise_()
        self.monitor_delay_label = QtWidgets.QLabel(self.TaskTab)
        self.monitor_delay_label.hide()
        self.error_delay_label = QtWidgets.QLabel(self.TaskTab)
        self.error_delay_label.hide()
        self.max_price_label = QtWidgets.QLabel(self.TaskTab)
        self.max_price_label.hide()
        self.proxies_label = QtWidgets.QLabel(self.TaskTab)
        self.proxies_label.hide()
        self.load_labels()


    def load_labels(self):
        self.id_label.setText(self.task_id)
        self.product_label.setText(self.product)
        self.profile_label.setText(self.profile)
        self.proxies_label.setText(self.proxies)
        self.status_label.setText("Idle")
        self.browser_label.setText("Click To Open Browser")
        self.site_label.setText(self.site)
        self.monitor_delay_label.setText(self.monitor_delay)
        self.error_delay_label.setText(self.error_delay)
        self.max_price_label.setText(self.max_price)

    def update_status(self,msg):
        self.status_label.setText(msg["msg"])
        if msg["msg"] == "Browser Ready":
            self.browser_url,self.browser_cookies = msg["url"],msg["cookies"]
            self.running = False
            self.start_btn.raise_()
            self.browser_label.show()
            logger.alt(self.task_id,msg["msg"])
            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(1000, loop.quit)
            loop.exec_()
            self.task.stop()
            return
        if msg["status"] == "idle":
            self.status_label.setStyleSheet("color: rgb(255, 255, 255);")
            logger.normal(self.task_id,msg["msg"])
        elif msg["status"] == "normal":
            self.status_label.setStyleSheet("color: rgb(163, 149, 255);")
            logger.normal(self.task_id,msg["msg"])
        elif msg["status"] == "alt":
            self.status_label.setStyleSheet("color: rgb(242, 166, 137);")
            logger.alt(self.task_id,msg["msg"])
        elif msg["status"] == "error":
            self.status_label.setStyleSheet("color: rgb(252, 81, 81);")
            logger.error(self.task_id,msg["msg"])
        elif msg["status"] == "success":
            self.status_label.setStyleSheet("color: rgb(52, 198, 147);")
            logger.success(self.task_id,msg["msg"])
            self.running = False
            self.start_btn.raise_()
            if settings.buy_one:
                self.stop_all()
            checkouts_count.setText(str(int(checkouts_count.text())+1))
        elif msg["status"] == "carted":
            self.status_label.setStyleSheet("color: rgb(163, 149, 255);")
            logger.alt(self.task_id,msg["msg"])
            carted_count.setText(str(int(carted_count.text())+1))

    def update_image(self,image_url):
        self.image_thread = ImageThread(image_url)
        self.image_thread.finished_signal.connect(self.set_image)
        self.image_thread.start()

    def set_image(self,pixmap):
        self.image.setPixmap(pixmap)

    def start(self,event):
        if not self.running:
            self.browser_label.hide()
            self.task = TaskThread()
            self.task.status_signal.connect(self.update_status)
            self.task.image_signal.connect(self.update_image)
            self.task.set_data(
                self.task_id,
                self.site_label.text(),
                self.product_label.text(),
                self.profile_label.text(),
                self.proxies_label.text(),
                self.monitor_delay_label.text(),
                self.error_delay_label.text(),
                self.max_price_label.text()
            )
            self.task.start()
            self.running = True
            self.stop_btn.raise_()

    def stop(self,event):
        self.task.stop()
        self.running = False
        self.update_status({"msg":"Stopped","status":"idle"})
        self.start_btn.raise_()

    def edit(self,event):
        self.edit_dialog = CreateDialog()
        self.edit_dialog.addtask_btn.clicked.connect(self.update_task)
        self.edit_dialog.taskcount_spinbox.hide()
        self.edit_dialog.profile_box.clear()
        self.edit_dialog.proxies_box.clear()
        profile_combobox = self.parent().parent().parent().parent().parent().parent().parent().createdialog.profile_box
        for profile in [profile_combobox.itemText(i) for i in range(profile_combobox.count())]:
            self.edit_dialog.profile_box.addItem(profile)
        proxies_combobox = self.parent().parent().parent().parent().parent().parent().parent().createdialog.proxies_box
        for proxy in [proxies_combobox.itemText(i) for i in range(proxies_combobox.count())]:
            self.edit_dialog.proxies_box.addItem(proxy)
        self.edit_dialog.load_data(self)
        self.edit_dialog.show()

    def update_task(self):
        self.site=self.edit_dialog.site_box.currentText()
        self.product=self.edit_dialog.input_edit.text()
        self.profile=self.edit_dialog.profile_box.currentText()
        self.proxies=self.edit_dialog.proxies_box.currentText()
        self.monitor_delay=self.edit_dialog.monitor_edit.text()
        self.error_delay = self.edit_dialog.error_edit.text()
        self.max_price = self.edit_dialog.price_edit.text()
        self.load_labels()
        self.delete_json()
        tasks_data = return_data("./data/tasks.json")
        task_data = {"task_id": self.task_id, "site": self.site, "product": self.product, "profile": self.profile,
                     "proxies": self.proxies, "monitor_delay": self.monitor_delay, "error_delay": self.error_delay,
                     "max_price": self.max_price}
        tasks_data.append(task_data)
        write_data("./data/tasks.json",tasks_data)
        self.edit_dialog.deleteLater()

    def delete_json(self):
        tasks_data = return_data("./data/tasks.json")
        for task in tasks_data:
            if task["task_id"] == self.task_id:
                tasks_data.remove(task)
                break
        write_data("./data/tasks.json", tasks_data)

    def delete(self,event):
        tasks_total_count.setText(str(int(tasks_total_count.text()) - 1))
        self.delete_json()
        self.TaskTab.deleteLater()

    def open_browser(self,event):
        self.browser_thread = BrowserThread()
        self.browser_thread.set_data(
            self.browser_url,
            self.browser_cookies
        )
        self.browser_thread.start()
class TaskThread(QtCore.QThread):
    status_signal = QtCore.pyqtSignal("PyQt_PyObject")
    image_signal = QtCore.pyqtSignal("PyQt_PyObject")
    def __init__(self):
        QtCore.QThread.__init__(self)

    def set_data(self,task_id,site,product,profile,proxies,monitor_delay,error_delay,max_price):
        self.task_id,self.site,self.product,self.profile,self.proxies,self.monitor_delay,self.error_delay,self.max_price = task_id,site,product,profile,proxies,monitor_delay,error_delay,max_price

    def run(self):
        profile,proxy = get_profile(self.profile),get_proxy(self.proxies)
        if profile == None:
            self.status_signal.emit({"msg":"Invalid profile","status":"error"})
            return
        if proxy == None:
            self.status_signal.emit({"msg":"Invalid proxy list","status":"error"})
            return
        if self.site == "Walmart":
            Walmart(self.task_id,self.status_signal,self.image_signal,self.product,profile,proxy,self.monitor_delay,self.error_delay,self.max_price)
        elif self.site == "Bestbuy":
            BestBuy(self.task_id,self.status_signal,self.image_signal,self.product,profile,proxy,self.monitor_delay,self.error_delay)

    def stop(self):
        self.terminate()

class ImageThread(QtCore.QThread):
    finished_signal = QtCore.pyqtSignal("PyQt_PyObject")
    def __init__(self,image_url):
        self.image_url = image_url
        QtCore.QThread.__init__(self)

    def run(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        data = urllib.request.urlopen(self.image_url).read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(data)
        self.finished_signal.emit(pixmap)

class BrowserThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def set_data(self,url,cookies):
        self.url,self.cookies = url,cookies
    def run(self):
        open_browser(self.url,self.cookies)

