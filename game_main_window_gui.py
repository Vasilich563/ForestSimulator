# -*- coding: utf-8 -*-
# Author: Vodohleb04

# Form implementation generated from reading ui file 'mainGameWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class modExitMainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/bimer.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(icon)
        self.resize(300, 100)

    def closeEvent(self, event) -> None:
        result = QtWidgets.QMessageBox.question(
            self,
            "Подтверждение закрытия окна",
            "Вы действительно хотите закрыть окно?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Save,
            QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            event.accept()
            QtWidgets.QWidget.closeEvent(self, event)
        elif result == QtWidgets.QMessageBox.Save:
            # TODO Save world
            event.accept()
            QtWidgets.QWidget.closeEvent(self, event)
        else:
            event.ignore()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1158, 579)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("appdata/icons/bimer.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 242, 254);")
        MainWindow.setStyleSheet("""QToolTip {background-color: white; 
                                              color: black; 
                                              border: black solid 1px}""")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 250, 230);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.wakeDeadlyWordButton = QtWidgets.QPushButton(self.centralwidget)
        self.wakeDeadlyWordButton.setBaseSize(QtCore.QSize(108, 32))
        self.wakeDeadlyWordButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wakeDeadlyWordButton.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.wakeDeadlyWordButton.setObjectName("wakeDeadlyWordButton")
        self.gridLayout.addWidget(self.wakeDeadlyWordButton, 2, 5, 1, 1)
        self.periodButton = QtWidgets.QPushButton(self.centralwidget)
        self.periodButton.setBaseSize(QtCore.QSize(108, 32))
        self.periodButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.periodButton.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.periodButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("appdata/icons/doubleR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.periodButton.setIcon(icon1)
        self.periodButton.setCheckable(False)
        self.periodButton.setObjectName("periodButton")
        self.gridLayout.addWidget(self.periodButton, 2, 1, 1, 1)
        self.reduceAutoSpeedButton = QtWidgets.QPushButton(self.centralwidget)
        self.reduceAutoSpeedButton.setEnabled(False)
        self.reduceAutoSpeedButton.setBaseSize(QtCore.QSize(108, 32))
        self.reduceAutoSpeedButton.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.reduceAutoSpeedButton.setObjectName("reduceAutoSpeedButton")
        self.gridLayout.addWidget(self.reduceAutoSpeedButton, 2, 2, 1, 1)
        self.autoPeriodButton = QtWidgets.QPushButton(self.centralwidget)
        self.autoPeriodButton.setBaseSize(QtCore.QSize(108, 32))
        self.autoPeriodButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.autoPeriodButton.setStatusTip("")
        self.autoPeriodButton.setWhatsThis("")
        self.autoPeriodButton.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.autoPeriodButton.setIconSize(QtCore.QSize(16, 16))
        self.autoPeriodButton.setCheckable(True)
        self.autoPeriodButton.setObjectName("autoPeriodButton")
        self.gridLayout.addWidget(self.autoPeriodButton, 2, 3, 1, 1)
        self.worldMapTable = QtWidgets.QTableWidget(self.centralwidget)
        self.worldMapTable.setStyleSheet("background-color: rgb(247, 255, 238);")
        self.worldMapTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.worldMapTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.worldMapTable.setAutoScroll(False)
        self.worldMapTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.worldMapTable.setDragEnabled(False)
        self.worldMapTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.worldMapTable.setGridStyle(QtCore.Qt.SolidLine)
        self.worldMapTable.setCornerButtonEnabled(False)
        self.worldMapTable.setObjectName("worldMapTable")
        self.worldMapTable.setColumnCount(2)
        self.worldMapTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 242, 254))
        self.worldMapTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.worldMapTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        item.setBackground(QtGui.QColor(255, 242, 254))
        self.worldMapTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.worldMapTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(224, 224, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.worldMapTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.worldMapTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.worldMapTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.worldMapTable.setItem(1, 1, item)
        self.gridLayout.addWidget(self.worldMapTable, 0, 1, 2, 6)
        self.cellDataListWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cellDataListWidget.sizePolicy().hasHeightForWidth())
        self.cellDataListWidget.setSizePolicy(sizePolicy)
        self.cellDataListWidget.setStyleSheet("background-color: rgb(247, 255, 238);")
        self.cellDataListWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.cellDataListWidget.setObjectName("cellDataListWidget")
        item = QtWidgets.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(244, 224, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.cellDataListWidget.addItem(item)
        self.gridLayout.addWidget(self.cellDataListWidget, 0, 0, 3, 1)
        self.increaseAutoSpeedButton = QtWidgets.QPushButton(self.centralwidget)
        self.increaseAutoSpeedButton.setEnabled(False)
        self.increaseAutoSpeedButton.setBaseSize(QtCore.QSize(108, 32))
        self.increaseAutoSpeedButton.setStatusTip("")
        self.increaseAutoSpeedButton.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.increaseAutoSpeedButton.setObjectName("increaseAutoSpeedButton")
        self.gridLayout.addWidget(self.increaseAutoSpeedButton, 2, 4, 1, 1)
        self.appocalipseButton = QtWidgets.QPushButton(self.centralwidget)
        self.appocalipseButton.setBaseSize(QtCore.QSize(108, 32))
        self.appocalipseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.appocalipseButton.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.appocalipseButton.setObjectName("appocalipseButton")
        self.gridLayout.addWidget(self.appocalipseButton, 2, 6, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea)
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.newWorldAction = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("appdata/icons/addIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newWorldAction.setIcon(icon2)
        self.newWorldAction.setIconVisibleInMenu(True)
        self.newWorldAction.setObjectName("newWorldAction")
        self.loadWorldAction = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("appdata/icons/loadIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadWorldAction.setIcon(icon3)
        self.loadWorldAction.setObjectName("loadWorldAction")
        self.leaveWorldAction = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("appdata/icons/exitIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leaveWorldAction.setIcon(icon4)
        self.leaveWorldAction.setObjectName("leaveWorldAction")
        self.exitGameAction = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("appdata/icons/linuxIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitGameAction.setIcon(icon5)
        self.exitGameAction.setObjectName("exitGameAction")
        self.saveWorldAction = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("appdata/icons/saveIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveWorldAction.setIcon(icon6)
        self.saveWorldAction.setObjectName("saveWorldAction")
        self.helpAction = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("appdata/icons/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpAction.setIcon(icon7)
        self.helpAction.setObjectName("helpAction")
        self.toolBar.addAction(self.newWorldAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.saveWorldAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.loadWorldAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.helpAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.leaveWorldAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.exitGameAction)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Forest Simulator 2.0"))
        self.wakeDeadlyWordButton.setToolTip(_translate("MainWindow", "Пробудить смерточервя"))
        self.wakeDeadlyWordButton.setText(_translate("MainWindow", "Смерточервь"))
        self.wakeDeadlyWordButton.setShortcut(_translate("MainWindow", "W"))
        self.periodButton.setToolTip(_translate("MainWindow", "Сменить временной период"))
        self.periodButton.setShortcut(_translate("MainWindow", "N"))
        self.reduceAutoSpeedButton.setToolTip(_translate("MainWindow", "Замедлить течение времени (работает при при включенном автоматическом режиме)"))
        self.reduceAutoSpeedButton.setText(_translate("MainWindow", "Замедлить"))
        self.reduceAutoSpeedButton.setShortcut(_translate("MainWindow", "<"))
        self.autoPeriodButton.setToolTip(_translate("MainWindow", "Режим автоматической смены времени"))
        self.autoPeriodButton.setText(_translate("MainWindow", "Авто"))
        self.autoPeriodButton.setShortcut(_translate("MainWindow", "A"))
        item = self.worldMapTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "str"))
        item = self.worldMapTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Новая строка"))
        item = self.worldMapTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "col"))
        item = self.worldMapTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Новый столбец"))
        __sortingEnabled = self.worldMapTable.isSortingEnabled()
        self.worldMapTable.setSortingEnabled(False)
        item = self.worldMapTable.item(0, 0)
        item.setText(_translate("MainWindow", "sdff"))
        item = self.worldMapTable.item(0, 1)
        item.setText(_translate("MainWindow", "wefsrdvgv"))
        item = self.worldMapTable.item(1, 0)
        item.setText(_translate("MainWindow", "ewrfvdgrewdqedscf"))
        item = self.worldMapTable.item(1, 1)
        item.setText(_translate("MainWindow", "qdwerfdtgrewdqsaedcfv"))
        self.worldMapTable.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.cellDataListWidget.isSortingEnabled()
        self.cellDataListWidget.setSortingEnabled(False)
        item = self.cellDataListWidget.item(0)
        item.setText(_translate("MainWindow", "creature"))
        self.cellDataListWidget.setSortingEnabled(__sortingEnabled)
        self.increaseAutoSpeedButton.setToolTip(_translate("MainWindow", "Ускорить течение времени (работает при при включенном автоматическом режиме)"))
        self.increaseAutoSpeedButton.setText(_translate("MainWindow", "Ускорить"))
        self.increaseAutoSpeedButton.setShortcut(_translate("MainWindow", ">"))
        self.appocalipseButton.setToolTip(_translate("MainWindow", "Вызвать апокалипсис"))
        self.appocalipseButton.setText(_translate("MainWindow", "Апокалипсис"))
        self.appocalipseButton.setShortcut(_translate("MainWindow", "Del"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.newWorldAction.setText(_translate("MainWindow", "Создать новый мир"))
        self.loadWorldAction.setText(_translate("MainWindow", "Загрузить мир"))
        self.loadWorldAction.setToolTip(_translate("MainWindow", "Загрузить мир F9"))
        self.loadWorldAction.setShortcut(_translate("MainWindow", "F9"))
        self.leaveWorldAction.setText(_translate("MainWindow", "Покинуть мир"))
        self.exitGameAction.setText(_translate("MainWindow", "Выйти на рабочий стол"))
        self.saveWorldAction.setText(_translate("MainWindow", "Сохранить мир"))
        self.saveWorldAction.setToolTip(_translate("MainWindow", "Сохранить мир F5"))
        self.saveWorldAction.setShortcut(_translate("MainWindow", "F5"))
        self.helpAction.setText(_translate("MainWindow", "Помощь"))
        self.helpAction.setToolTip(_translate("MainWindow", "Помощь F11"))
        self.helpAction.setShortcut(_translate("MainWindow", "F11"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = modExitMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())