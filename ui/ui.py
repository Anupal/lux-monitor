from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QFrame,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsPixmapItem,
)


class MainView(QWidget):
    def __init__(self, button_callbacks={}):
        super(MainView, self).__init__()
        self.button_callbacks = button_callbacks
        self.init_ui()

        self.setup_callbacks()

    def setup_callbacks(self):
        if "settings" in self.button_callbacks:
            self.btnSettings.clicked.connect(self.button_callbacks["settings"])
        if "log" in self.button_callbacks:
            self.btnLog.clicked.connect(self.button_callbacks["log"])

    def init_ui(self):
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.setFont(font)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")

        # Todays' metrics
        self.txtToday = QLabel("TODAY")
        self.txtToday.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txtToday.setObjectName("txtToday")
        self.txtToday.setObjectName("txtToday")
        self.mainLayout.addWidget(
            self.txtToday, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.txtTodayValue = QLabel("0000")
        self.txtTodayValue.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(42)
        font.setBold(True)
        self.txtTodayValue.setFont(font)
        self.txtTodayValue.setObjectName("txtTodayValue")
        self.mainLayout.addWidget(
            self.txtTodayValue, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )

        # Weekly metrics
        self.txtWeekly = QLabel("WEEKLYs")
        self.txtWeekly.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txtWeekly.setObjectName("txtWeekly")
        self.mainLayout.addWidget(
            self.txtWeekly, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.txtWeeklyValue = QLabel("0000")
        self.txtWeeklyValue.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(42)
        font.setBold(True)
        self.txtWeeklyValue.setFont(font)
        self.txtWeeklyValue.setObjectName("txtWeeklyValue")
        self.mainLayout.addWidget(
            self.txtWeeklyValue, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )

        self.bottomButtonsLayout = QHBoxLayout()
        self.bottomButtonsLayout.setObjectName("bottomButtonsLayout")
        self.btnLog = QPushButton("LOG")
        self.btnLog.setObjectName("btnLog")
        self.btnLog.setFixedSize(100, 40)
        self.bottomButtonsLayout.addWidget(self.btnLog)
        spacerItem = QSpacerItem(
            40,
            20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )
        self.bottomButtonsLayout.addItem(spacerItem)
        self.btnSettings = QPushButton("SETTINGS")
        self.btnSettings.setObjectName("btnSettings")
        self.btnSettings.setFixedSize(100, 40)
        self.bottomButtonsLayout.addWidget(self.btnSettings)
        self.mainLayout.addLayout(self.bottomButtonsLayout)

        self.setLayout(self.mainLayout)


class LogItem(QWidget):
    def __init__(self, vitamin_d, time, time_duration):
        super(LogItem, self).__init__()
        self.vitamin_d = vitamin_d
        self.time = time
        self.time_duration = time_duration
        self.init_ui()

    def init_ui(self):
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.setFont(font)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setObjectName("mainLayout")

        self.labelTime = QLabel(self.time)
        self.labelTime.setObjectName("labelTime")

        self.labelTimeDuration = QLabel(self.time_duration)
        self.labelTimeDuration.setObjectName("labelTimeDuration")

        self.labelVitaminD = QLabel(self.vitamin_d)
        self.labelVitaminD.setObjectName("labelVitaminD")
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(24)
        font.setBold(True)
        self.labelVitaminD.setFont(font)

        spacerItem = QSpacerItem(
            40,
            20,
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Minimum,
        )

        layoutContainerFrame = QFrame()
        layoutContainerFrame.setObjectName("layoutContainerFrame")
        layoutContainer = QHBoxLayout()

        layoutContainer.addWidget(self.labelTime)
        layoutContainer.addWidget(self.labelTimeDuration)
        layoutContainer.addItem(spacerItem)
        layoutContainer.addWidget(self.labelVitaminD)
        layoutContainerFrame.setLayout(layoutContainer)
        layoutContainerFrame.setFixedSize(415, 80)

        self.mainLayout.addWidget(layoutContainerFrame)

        self.setLayout(self.mainLayout)


class BodyImageView(QWidget):
    def __init__(self, body_states=None):
        super().__init__()

        if body_states:
            self.body_states = body_states
        else:
            self.body_states = {
                "head": True,
                "neck": True,
                "left_arm_upper": True,
                "left_arm_lower": True,
                "left_palm": True,
                "right_arm_upper": True,
                "right_arm_lower": True,
                "right_palm": True,
                "torso": True,
                "left_leg_upper": True,
                "left_leg_lower": True,
                "left_feet": True,
                "right_leg_upper": True,
                "right_leg_lower": True,
                "right_feet": True,
            }
        self.init_ui()

    def init_ui(self):
        QtGui.QImageReader.setAllocationLimit(0)

        # Create a QGraphicsView and QGraphicsScene
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        # Load an image using QPixmap
        pixmap = QtGui.QPixmap("img/human_body.jpg")

        pixmap = pixmap.scaled(300, 700)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(pixmap_item)

        self.btn_dict = {
            "head": (QPushButton(), (135, 20)),
            "neck": (QPushButton(), (135, 75)),
            "left_arm_upper": (QPushButton(), (50, 150)),
            "left_arm_lower": (QPushButton(), (35, 250)),
            "left_palm": (QPushButton(), (25, 350)),
            "right_arm_upper": (QPushButton(), (225, 150)),
            "right_arm_lower": (QPushButton(), (240, 250)),
            "right_palm": (QPushButton(), (250, 350)),
            "torso": (QPushButton(), (135, 200)),
            "left_leg_upper": (QPushButton(), (95, 400)),
            "left_leg_lower": (QPushButton(), (80, 550)),
            "left_feet": (QPushButton(), (45, 650)),
            "right_leg_upper": (QPushButton(), (185, 400)),
            "right_leg_lower": (QPushButton(), (200, 550)),
            "right_feet": (QPushButton(), (235, 650)),
        }

        for btn_id, btn in self.btn_dict.items():
            btn[0].setFixedSize(30, 30)
            self.btn_dict[btn_id][0].setStyleSheet(
                "border : 2px solid #00008B; border-radius : 15px; background-color: transparent;"
            )
            # btn[0].setCheckable(True)
            # btn[0].setChecked(self.body_states[btn_id])
            btn[0].clicked.connect(lambda _, bid=btn_id: self.button_clicked(bid))
            btn_item = self.scene.addWidget(btn[0])
            btn[0].setObjectName("btnBody")
            btn_item.setPos(btn[1][0], btn[1][1])

        # Create a QVBoxLayout for the main widget
        layout = QVBoxLayout()
        layout.addWidget(self.view)

        # Set the layout for the main widget
        self.setLayout(layout)

    def button_clicked(self, btn_id):
        print(btn_id)
        self.btn_dict[btn_id][0].setStyleSheet(
            "border : 2px solid black; border-radius : 15px; background-color: blue;"
        )


class LogView(QWidget):
    def __init__(self, button_callbacks={}):
        super(LogView, self).__init__()
        self.button_callbacks = button_callbacks
        self.init_ui()

        self.setup_callbacks()

        self.add_log(("0000 IU", "14:00", "10 MIN"))
        self.add_log(("0000 IU", "13:00", "10 MIN"))

    def setup_callbacks(self):
        if "back" in self.button_callbacks:
            self.btnBack.clicked.connect(self.button_callbacks["back"])
        # if "log" in self.button_callbacks:
        #     self.btnLog.clicked.connect(self.button_callbacks["log"])

    def init_ui(self):
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.setFont(font)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setObjectName("mainLayout")

        # --- left layout --- #
        self.layoutLeft = QVBoxLayout()
        self.layoutLeft.setObjectName("layoutLeft")

        # Back button
        self.btnBack = QPushButton("BACK")
        self.btnBack.setObjectName("btnBack")
        self.btnBack.setFixedSize(100, 40)
        # self.btnBack.setMaximumSize(QtCore.QSize(100, 16777215))
        self.layoutLeft.addWidget(self.btnBack)

        # Day switcher
        self.layoutDayBar = QHBoxLayout()
        self.layoutDayBar.setObjectName("layoutDayBar")
        self.btnDayPrev = QPushButton("<")
        self.btnDayPrev.setObjectName("btnDay")
        self.btnDayPrev.setFixedSize(30, 30)
        self.layoutDayBar.addWidget(self.btnDayPrev)
        self.labelDay = QLabel("TODAY")
        self.labelDay.setObjectName("labelDay")
        self.layoutDayBar.addWidget(
            self.labelDay, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.btnDayNext = QPushButton(">")
        self.btnDayNext.setObjectName("btnDay")
        self.btnDayNext.setFixedSize(30, 30)
        self.layoutDayBar.addWidget(self.btnDayNext)
        layoutDayBarWidget = QWidget()
        layoutDayBarWidget.setLayout(self.layoutDayBar)
        layoutDayBarWidget.setFixedHeight(50)
        self.layoutLeft.addWidget(layoutDayBarWidget)
        self.txtDayValue = QLabel("0000")
        self.txtDayValue.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(42)
        font.setBold(True)
        self.txtDayValue.setFont(font)
        self.txtDayValue.setObjectName("txtDayValue")
        self.layoutLeft.addWidget(
            self.txtDayValue, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )

        # Placeholder for log list
        self.layoutLog = QVBoxLayout()
        self.layoutLog.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.layoutLog.setObjectName("layoutLog")
        layoutLogWidget = QWidget()
        layoutLogWidget.setLayout(self.layoutLog)
        # layoutLogWidget.setFixedHeight(420)
        self.layoutLeft.addWidget(layoutLogWidget)

        # Contain layout within widget and set max width
        layoutLeftWidget = QWidget()
        layoutLeftWidget.setLayout(self.layoutLeft)
        layoutLeftWidget.setMaximumSize(QtCore.QSize(480, 16777215))
        self.mainLayout.addWidget(layoutLeftWidget)

        self.btnAddLog = QPushButton("+")
        self.btnAddLog.setObjectName("btnAddLog")
        self.btnAddLog.setFixedSize(50, 50)
        self.layoutLeft.addWidget(
            self.btnAddLog, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter
        )

        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.mainLayout.addWidget(self.line)

        # --- right layout --- #
        self.layoutRight = QVBoxLayout()
        self.layoutRight.setObjectName("layoutRight")
        self.labelSkinExposure = QLabel("SKIN EXPOSURE")
        self.labelSkinExposure.setObjectName("labelSkinExposure")
        self.layoutRight.addWidget(
            self.labelSkinExposure, 0, QtCore.Qt.AlignmentFlag.AlignHCenter
        )
        self.bodyImageView = BodyImageView()
        self.layoutRight.addWidget(self.bodyImageView)

        # Contain layout within widget and set max width
        layoutRightWidget = QWidget()
        layoutRightWidget.setLayout(self.layoutRight)
        layoutRightWidget.setMaximumSize(QtCore.QSize(480, 16777215))
        self.mainLayout.addWidget(layoutRightWidget)

        self.setLayout(self.mainLayout)

    def add_log(self, log):
        self.layoutLog.addWidget(LogItem(log[0], log[1], log[2]))


class SettingsView(QWidget):
    def __init__(self, button_callbacks={}):
        super(SettingsView, self).__init__()
        self.button_callbacks = button_callbacks
