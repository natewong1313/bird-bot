from PyQt5 import QtCore, QtGui, QtWidgets
from sites.walmart import Walmart
from utils import get_profile
import urllib.request,sys,platform
def no_abort(a, b, c):
    sys.__excepthook__(a, b, c)
sys.excepthook = no_abort

class HomePage(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(HomePage, self).__init__(parent)
        self.setupUi(self)
    def setupUi(self, homepage):
        self.tasks = []
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
        self.image_table_header.setGeometry(QtCore.QRect(30, 7, 51, 31))
        self.image_table_header.setText("Image")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15) if platform.system() == "Darwin" else font.setPointSize(15*.75)
        font.setBold(False)
        font.setWeight(50)
        self.image_table_header.setFont(font)
        self.image_table_header.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.product_table_header = QtWidgets.QLabel(self.tasks_card)
        self.product_table_header.setGeometry(QtCore.QRect(190, 7, 61, 31))
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
        self.site_table_header.setGeometry(QtCore.QRect(110, 7, 61, 31))
        self.site_table_header.setFont(font)
        self.site_table_header.setStyleSheet("color: rgb(234, 239, 239);border: none;")
        self.site_table_header.setText("Site")
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
    def __init__(self,site,product,profile,monitor_delay,error_delay,max_price,parent=None):
        super(TaskTab, self).__init__(parent)
        tasks_total_count.setText(str(int(tasks_total_count.text())+1))
        self.site,self.product,self.profile,self.monitor_delay,self.error_delay,self.max_price = site,product,profile,monitor_delay,error_delay,max_price
        self.setupUi(self) 
    def setupUi(self,TaskTab):
        self.running = False

        self.TaskTab = TaskTab
        self.TaskTab.setMinimumSize(QtCore.QSize(0, 50))
        self.TaskTab.setMaximumSize(QtCore.QSize(16777215, 50))
        self.TaskTab.setStyleSheet("border-radius: none;")
        self.product_label = QtWidgets.QLabel(self.TaskTab)
        self.product_label.setGeometry(QtCore.QRect(172, 10, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setBold(False)
        font.setWeight(50)
        self.product_label.setFont(font)
        self.product_label.setStyleSheet("color: rgb(234, 239, 239);")
        self.profile_label = QtWidgets.QLabel(self.TaskTab)
        self.profile_label.setGeometry(QtCore.QRect(571, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setBold(False)
        font.setWeight(50)
        self.profile_label.setFont(font)
        self.profile_label.setStyleSheet("color: rgb(234, 239, 239);")
        self.status_label = QtWidgets.QLabel(self.TaskTab)
        self.status_label.setGeometry(QtCore.QRect(632, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setBold(False)
        font.setWeight(50)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("color: rgb(234, 239, 239);")
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
        self.delete_btn.setGeometry(QtCore.QRect(895, 15, 16, 16))
        self.delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_btn.setPixmap(QtGui.QPixmap(":/images/trash.png"))
        self.delete_btn.setScaledContents(True)
        self.delete_btn.mousePressEvent = self.delete
        self.image = QtWidgets.QLabel(self.TaskTab)
        self.image.setGeometry(QtCore.QRect(10, 0, 50, 50))
        self.image.setPixmap(QtGui.QPixmap(":/images/no_image.png"))
        self.image.setScaledContents(True)
        self.site_label = QtWidgets.QLabel(self.TaskTab)
        self.site_label.setGeometry(QtCore.QRect(90, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13) if platform.system() == "Darwin" else font.setPointSize(13*.75)
        font.setBold(False)
        font.setWeight(50)
        self.site_label.setFont(font)
        self.site_label.setStyleSheet("color: rgb(234, 239, 239);")
        self.stop_btn.raise_()
        self.product_label.raise_()
        self.profile_label.raise_()
        self.status_label.raise_()
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

        self.product_label.setText(self.product)
        self.profile_label.setText(self.profile)
        self.status_label.setText("Idle")
        self.site_label.setText(self.site)
        self.monitor_delay_label.setText(self.monitor_delay)
        self.error_delay_label.setText(self.error_delay)
        self.max_price_label.setText(self.max_price)
    
    def update_status(self,msg): 
        self.status_label.setText(msg["msg"])
        if msg["status"] == "idle":
            self.status_label.setStyleSheet("color: rgb(255, 255, 255);")
        elif msg["status"] == "normal":
            self.status_label.setStyleSheet("color: rgb(163, 149, 255);")
        elif msg["status"] == "alt":
            self.status_label.setStyleSheet("color: rgb(242, 166, 137);")
        elif msg["status"] == "error":
            self.status_label.setStyleSheet("color: rgb(252, 81, 81);")
        elif msg["status"] == "success":
            self.status_label.setStyleSheet("color: rgb(52, 198, 147);")
            self.running = False
            self.start_btn.raise_()
            checkouts_count.setText(str(int(checkouts_count.text())+1))
        elif msg["status"] == "carted":
            self.status_label.setStyleSheet("color: rgb(163, 149, 255);")
            carted_count.setText(str(int(carted_count.text())+1))
    
    def update_image(self,image_url):
        data = urllib.request.urlopen(image_url).read()
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(data)
        self.image.setPixmap(pixmap)
        
    def start(self,event):
        if not self.running:
            self.task = TaskThread()
            self.task.status_signal.connect(self.update_status)
            self.task.image_signal.connect(self.update_image)
            self.task.set_data(
                self.site_label.text(),
                self.product_label.text(),
                self.profile_label.text(),
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
    
    def delete(self,event):
        tasks_total_count.setText(str(int(tasks_total_count.text())-1))
        self.TaskTab.deleteLater()

class TaskThread(QtCore.QThread):
    status_signal = QtCore.pyqtSignal("PyQt_PyObject")
    image_signal = QtCore.pyqtSignal("PyQt_PyObject")
    def __init__(self):
        QtCore.QThread.__init__(self)

    def set_data(self,site,product,profile,monitor_delay,error_delay,max_price):
        self.site,self.product,self.profile,self.monitor_delay,self.error_delay,self.max_price = site,product,profile,monitor_delay,error_delay,max_price
    
    def run(self):
        profile = get_profile(self.profile)
        if profile == None:
            self.status_signal.emit({"msg":"Invalid profile","status":"error"})
            return
        if self.site == "Walmart":
            Walmart(self.status_signal,self.image_signal,self.product,profile,self.monitor_delay,self.error_delay,self.max_price)

    def stop(self):
        self.terminate()