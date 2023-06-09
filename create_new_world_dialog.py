# -*- coding: utf-8 -*-
#Author: Vodohleb04

# Form implementation generated from reading ui file 'createNewWorldDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ecosystem import EcoSystem
from typing import Dict
import configs


class NewWorldAcceptedSignals(QtCore.QObject):
    world_is_made_signal = QtCore.pyqtSignal(EcoSystem)
    world_is_made_message_signal = QtCore.pyqtSignal(str)
    game_is_running_signal = QtCore.pyqtSignal()


class CustomNewWorldDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        """creates CustomNewWorldDialog

        Custom dialog can emit signals about creation of new world (new data for ecosystem)
        """
        self.newWorldAcceptedSignals = NewWorldAcceptedSignals()
        QtWidgets.QWidget.__init__(self, parent)


class Ui_newWorldDialog(object):
    def setupUi(self, newWorldDialog: CustomNewWorldDialog, ecosystem: EcoSystem):
        """Adds elements to newWorldDialog"""
        newWorldDialog.setObjectName("newWorldDialog")
        newWorldDialog.resize(624, 345)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(configs.SERVICE_ICONS["gui_windows_icon"]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        newWorldDialog.setWindowIcon(icon)
        newWorldDialog.setStyleSheet("background-color: rgb(255, 242, 254);")
        newWorldDialog.setStyleSheet("QToolTip {background-color: white; color: black; border: black solid 1px}")
        self.gridLayout_2 = QtWidgets.QGridLayout(newWorldDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addedCreaturesTable = QtWidgets.QTableWidget(newWorldDialog)
        self.addedCreaturesTable.setEnabled(False)
        self.addedCreaturesTable.setStyleSheet("background-color: rgb(247, 255, 238);")
        self.addedCreaturesTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.addedCreaturesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.addedCreaturesTable.setObjectName("addedCreaturesTable")
        self.addedCreaturesTable.setColumnCount(2)
        self.addedCreaturesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.addedCreaturesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.addedCreaturesTable.setHorizontalHeaderItem(1, item)
        self.addedCreaturesTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.addedCreaturesTable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.gridLayout_2.addWidget(self.addedCreaturesTable, 5, 0, 1, 1)
        self.createWorldButtonBox = QtWidgets.QDialogButtonBox(newWorldDialog)
        self.createWorldButtonBox.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.createWorldButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.createWorldButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.createWorldButtonBox.setCenterButtons(True)
        self.createWorldButtonBox.setObjectName("createWorldButtonBox")
        self.gridLayout_2.addWidget(self.createWorldButtonBox, 7, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLengthSpinBox = QtWidgets.QSpinBox(newWorldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalLengthSpinBox.sizePolicy().hasHeightForWidth())
        self.verticalLengthSpinBox.setSizePolicy(sizePolicy)
        self.verticalLengthSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLengthSpinBox.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.verticalLengthSpinBox.setMinimum(4)
        self.verticalLengthSpinBox.setMaximum(14)
        self.verticalLengthSpinBox.setObjectName("verticalLengthSpinBox")
        self.gridLayout.addWidget(self.verticalLengthSpinBox, 3, 0, 1, 1)
        self.creatureTypeBox = QtWidgets.QComboBox(newWorldDialog)
        self.creatureTypeBox.setEnabled(False)
        self.creatureTypeBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.creatureTypeBox.setToolTip("")
        self.creatureTypeBox.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.creatureTypeBox.setObjectName("creatureTypeBox")
        for i in range(7):
                self.creatureTypeBox.addItem("")
        self.gridLayout.addWidget(self.creatureTypeBox, 8, 0, 1, 2)
        self.horizontalLengthSpinBox = QtWidgets.QSpinBox(newWorldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalLengthSpinBox.sizePolicy().hasHeightForWidth())
        self.horizontalLengthSpinBox.setSizePolicy(sizePolicy)
        self.horizontalLengthSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLengthSpinBox.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.horizontalLengthSpinBox.setFrame(True)
        self.horizontalLengthSpinBox.setProperty("showGroupSeparator", False)
        self.horizontalLengthSpinBox.setMinimum(4)
        self.horizontalLengthSpinBox.setMaximum(14)
        self.horizontalLengthSpinBox.setObjectName("horizontalLengthSpinBox")
        self.gridLayout.addWidget(self.horizontalLengthSpinBox, 3, 1, 1, 1)
        self.removeCreaturesButton = QtWidgets.QPushButton(newWorldDialog)
        icon.addPixmap(QtGui.QPixmap(configs.SERVICE_ICONS["minus_icon"]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeCreaturesButton.setIcon(icon)
        self.removeCreaturesButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeCreaturesButton.sizePolicy().hasHeightForWidth())
        self.removeCreaturesButton.setSizePolicy(sizePolicy)
        self.removeCreaturesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeCreaturesButton.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.removeCreaturesButton.setText("")
        self.removeCreaturesButton.setObjectName("removeCreaturesButton")
        self.gridLayout.addWidget(self.removeCreaturesButton, 8, 4, 1, 1)
        self.addCreatuersButton = QtWidgets.QPushButton(newWorldDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(configs.SERVICE_ICONS["add_icon"]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addCreatuersButton.setIcon(icon)
        self.addCreatuersButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addCreatuersButton.sizePolicy().hasHeightForWidth())
        self.addCreatuersButton.setSizePolicy(sizePolicy)
        self.addCreatuersButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addCreatuersButton.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.addCreatuersButton.setText("")
        self.addCreatuersButton.setObjectName("addCreatuersButton")
        self.gridLayout.addWidget(self.addCreatuersButton, 8, 3, 1, 1)
        self.worldNameEdit = QtWidgets.QLineEdit(newWorldDialog)
        self.worldNameEdit.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.worldNameEdit.setInputMask("")
        self.worldNameEdit.setDragEnabled(False)
        self.worldNameEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.worldNameEdit.setObjectName("worldNameEdit")
        self.gridLayout.addWidget(self.worldNameEdit, 1, 0, 1, 5)
        self.creaturesAmountSpinBox = QtWidgets.QSpinBox(newWorldDialog)
        self.creaturesAmountSpinBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creaturesAmountSpinBox.sizePolicy().hasHeightForWidth())
        self.creaturesAmountSpinBox.setSizePolicy(sizePolicy)
        self.creaturesAmountSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.creaturesAmountSpinBox.setStyleSheet("background-color: rgb(224, 224, 255);")
        self.creaturesAmountSpinBox.setMaximum(20)
        self.creaturesAmountSpinBox.setObjectName("creaturesAmountSpinBox")
        self.gridLayout.addWidget(self.creaturesAmountSpinBox, 8, 2, 1, 1)
        self.manualCreaturesAddingCheckBox = QtWidgets.QCheckBox(newWorldDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualCreaturesAddingCheckBox.sizePolicy().hasHeightForWidth())
        self.manualCreaturesAddingCheckBox.setSizePolicy(sizePolicy)
        self.manualCreaturesAddingCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.manualCreaturesAddingCheckBox.setTristate(False)
        self.manualCreaturesAddingCheckBox.setObjectName("manualCreaturesAddingCheckBox")
        self.gridLayout.addWidget(self.manualCreaturesAddingCheckBox, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self._world_name = self._get_world_autoname()

        self.retranslateUi(newWorldDialog)
        self.createWorldButtonBox.accepted.connect(
            lambda: self._make_ecosystem(ecosystem, newWorldDialog.newWorldAcceptedSignals))
        self.createWorldButtonBox.accepted.connect(newWorldDialog.newWorldAcceptedSignals.game_is_running_signal.emit)
        self.createWorldButtonBox.accepted.connect(newWorldDialog.accept)  # type: ignore
        self.createWorldButtonBox.rejected.connect(newWorldDialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(newWorldDialog)

        self.worldNameEdit.textChanged.connect(lambda: self.world_name_changed(newWorldDialog))
        self.manualCreaturesAddingCheckBox.clicked.connect(self._manual_mode_connection)
        self.addCreatuersButton.clicked.connect(self._add_creature)
        self.addedCreaturesTable.itemSelectionChanged.connect(self._activate_remove_button)
        self.removeCreaturesButton.clicked.connect(self._remove_added_element)

    def _make_general_params(self) -> Dict:
        """Makes dict with general parameters of ecosystem"""
        return {
            "forest_vertical_length": self.verticalLengthSpinBox.value(),
            "forest_horizontal_length": self.horizontalLengthSpinBox.value(),
            "deadly_worm_sleep_interval": 5
        }

    def _make_ecosystem(self, ecosystem: EcoSystem, newWorldAcceptedSignals: NewWorldAcceptedSignals) -> None:
        """Creates new data in ecosystem

        ecosystem - data controller of program
        newWorldAcceptedSignals - used to emit signals about creation of new data in ecosystem
        """
        filename = configs.BASIC_SAVES_DIR_LINUX_PATH + "/{}.json".format(self._world_name)
        world_params = self._make_general_params()
        for i in range(self.addedCreaturesTable.rowCount()):
            world_params[f"{ecosystem.define_creature_kind_from_russian(self.addedCreaturesTable.item(i, 0).text())}"
                         f"_amount"] = int(self.addedCreaturesTable.item(i, 1).text())
        ecosystem.__init__(filename, **world_params)
        newWorldAcceptedSignals.world_is_made_signal.emit(ecosystem)
        newWorldAcceptedSignals.world_is_made_message_signal.emit(self._world_name)

    def world_name_changed(self, newWorldDialog: CustomNewWorldDialog) -> None:
        """Changes title of dialog window if line edit changed (edit for name of world)"""
        newWorldDialog.setWindowTitle(configs.GuiMessages.NEW_WORLD_DIALOG_TITLE.value.format(
            self.worldNameEdit.text()))
        self._world_name = self.worldNameEdit.text()

    @staticmethod
    def _get_world_autoname() -> str:
        """Defines name for world if name isn't set by user"""
        import os
        import re
        regex = re.compile(configs.FileRegex.WORLD_AUTONAME_REGEX.value)
        filename_indexes = [int(regex.match(file).group(1)) for file in os.listdir(configs.BASIC_SAVES_DIR_LINUX_PATH)
                            if regex.match(file)]
        if not filename_indexes:
                filename_indexes.append(0)
        return f"new_world{max(filename_indexes) + 1}"

    def _manual_mode_connection(self) -> None:
        """Makes objects used to set creatures amount and types active/not active (define it automatically)"""
        if self.manualCreaturesAddingCheckBox.isChecked():
            self._activate_manual_creatures_addition()
        else:
            self._deactivate_manual_creatures_addition()

    def _activate_manual_creatures_addition(self) -> None:
        """Makes objects used to set creatures amount and types active"""
        self.addedCreaturesTable.setEnabled(True)
        self.creatureTypeBox.setEnabled(True)
        self.creaturesAmountSpinBox.setEnabled(True)
        self.addCreatuersButton.setEnabled(True)

    def _deactivate_manual_creatures_addition(self) -> None:
        """Makes objects used to set creatures amount and types not active"""
        self.addedCreaturesTable.setEnabled(False)
        self.creatureTypeBox.setEnabled(False)
        self.creaturesAmountSpinBox.setEnabled(False)
        self.addCreatuersButton.setEnabled(False)

    @staticmethod
    def _make_item(brush: QtCore.Qt.SolidPattern, text_to_set="") -> QtWidgets.QTableWidgetItem:
        """Makes item for QTableWidget

        brush - QtCore.Qt.SolidPattern (makes background color for item)
        text_to_set - text to emplace into item. Default - emplace empty string
        """
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(brush)
        item.setText(text_to_set)
        return item

    def _element_row_index(self, creature_type: str) -> int:
        """Defines index of row in addedTable

        creature_type - name of creature type from creaturesTypeBox
        returns amount of rows if creature_type is not in added_table
        """
        row_index = 0
        while row_index < self.addedCreaturesTable.rowCount():
            if self.addedCreaturesTable.item(row_index, 0).text() == creature_type:
                return row_index
            row_index += 1
        return row_index

    def _add_creature(self) -> None:
        """Adds creature to addedTable

        Emplace creature type to 0 column
        Emplace amount of creatures to 1 column
        """
        brush = QtGui.QBrush(QtGui.QColor(224, 224, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        if self._element_row_index(self.creatureTypeBox.currentText()) < self.addedCreaturesTable.rowCount():
            self.addedCreaturesTable.setItem(self._element_row_index(self.creatureTypeBox.currentText()), 1,
                                             self._make_item(brush, str(self.creaturesAmountSpinBox.value())))
        else:
            self.addedCreaturesTable.insertRow(self.addedCreaturesTable.rowCount())
            self.addedCreaturesTable.setItem(self.addedCreaturesTable.rowCount() - 1, 0,
                                             self._make_item(brush, self.creatureTypeBox.currentText()))
            self.addedCreaturesTable.setItem(self.addedCreaturesTable.rowCount() - 1, 1,
                                             self._make_item(brush, str(self.creaturesAmountSpinBox.value())))

    def _activate_remove_button(self) -> None:
        """Hides or shows self.removeButton (defines action automatically)"""
        if self.addedCreaturesTable.currentItem():
            self.removeCreaturesButton.setEnabled(True)
        else:
            self.removeCreaturesButton.setEnabled(False)

    def _remove_added_element(self) -> None:
        """Removes row in self.addedTable"""
        current_row = self.addedCreaturesTable.currentRow()
        self.addedCreaturesTable.removeRow(self.addedCreaturesTable.currentRow())
        current_row -= 0 if current_row == 0 else 1
        self.addedCreaturesTable.setCurrentCell(current_row, 0)

    def retranslateUi(self, newWorldDialog: CustomNewWorldDialog) -> None:
        """Set text, shortcuts and tooltips for newWorldDialog elements"""
        _translate = QtCore.QCoreApplication.translate
        newWorldDialog.setWindowTitle(
            _translate("newWorldDialog", configs.GuiMessages.NEW_WORLD_DIALOG_TITLE.value.format(self._world_name)))
        item = self.addedCreaturesTable.horizontalHeaderItem(0)
        item.setText(_translate("newWorldDialog", "Существо"))
        item = self.addedCreaturesTable.horizontalHeaderItem(1)
        item.setText(_translate("newWorldDialog", "Количество"))
        self.verticalLengthSpinBox.setToolTip(_translate("newWorldDialog", "Размер мира по вертикали"))
        self.verticalLengthSpinBox.setSpecialValueText(_translate("newWorldDialog", "Размер мира по вертикали"))
        self.creatureTypeBox.setItemText(0, _translate("newWorldDialog", configs.RussianCreaturesNames.BLUEBERRY.value))
        self.creatureTypeBox.setItemText(1, _translate("newWorldDialog", configs.RussianCreaturesNames.HAZEL.value))
        self.creatureTypeBox.setItemText(2, _translate("newWorldDialog", configs.RussianCreaturesNames.MAPLE.value))
        self.creatureTypeBox.setItemText(3, _translate("newWorldDialog", configs.RussianCreaturesNames.BOAR.value))
        self.creatureTypeBox.setItemText(4, _translate("newWorldDialog", configs.RussianCreaturesNames.ELK.value))
        self.creatureTypeBox.setItemText(5, _translate("newWorldDialog", configs.RussianCreaturesNames.WOLF.value))
        self.creatureTypeBox.setItemText(6, _translate("newWorldDialog", configs.RussianCreaturesNames.BEAR.value))
        self.horizontalLengthSpinBox.setToolTip(_translate("newWorldDialog", "Размер мира по горизонтали"))
        self.horizontalLengthSpinBox.setSpecialValueText(_translate("newWorldDialog", "Размер леса по горизонтали"))
        self.removeCreaturesButton.setShortcut(_translate("newWorldDialog", "-"))
        self.addCreatuersButton.setToolTip(_translate("newWorldDialog", "Добавить в мир существ, +"))
        self.addCreatuersButton.setShortcut(_translate("newWorldDialog", "+"))
        self.worldNameEdit.setPlaceholderText(_translate("newWorldDialog", "Введите имя нового мира..."))
        self.manualCreaturesAddingCheckBox.setToolTip(_translate("newWorldDialog", "Включает ручной выбор количества существ в мире"))
        self.manualCreaturesAddingCheckBox.setText(_translate("newWorldDialog", "Ручное заполнение существ"))

