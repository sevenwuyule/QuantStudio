# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Project\Python\QuantStudio\GUI\IDSetup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IDSetupDlg(object):
    def setupUi(self, IDSetupDlg):
        IDSetupDlg.setObjectName(_fromUtf8("IDSetupDlg"))
        IDSetupDlg.resize(700, 429)
        IDSetupDlg.setFocusPolicy(QtCore.Qt.ClickFocus)
        IDSetupDlg.setSizeGripEnabled(True)
        self.gridLayout_2 = QtGui.QGridLayout(IDSetupDlg)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(IDSetupDlg)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.DateEdit = QtGui.QLineEdit(IDSetupDlg)
        self.DateEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.DateEdit.setObjectName(_fromUtf8("DateEdit"))
        self.gridLayout_2.addWidget(self.DateEdit, 0, 1, 1, 2)
        self.ID1ListWidget = QtGui.QListWidget(IDSetupDlg)
        self.ID1ListWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ID1ListWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ID1ListWidget.setObjectName(_fromUtf8("ID1ListWidget"))
        self.gridLayout_2.addWidget(self.ID1ListWidget, 0, 4, 2, 1)
        self.label_7 = QtGui.QLabel(IDSetupDlg)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 6, 1, 1)
        self.IDNumEdit = QtGui.QLineEdit(IDSetupDlg)
        self.IDNumEdit.setReadOnly(True)
        self.IDNumEdit.setObjectName(_fromUtf8("IDNumEdit"))
        self.gridLayout_2.addWidget(self.IDNumEdit, 0, 7, 1, 1)
        self.DateCalendar = QtGui.QCalendarWidget(IDSetupDlg)
        self.DateCalendar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DateCalendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.DateCalendar.setGridVisible(False)
        self.DateCalendar.setObjectName(_fromUtf8("DateCalendar"))
        self.gridLayout_2.addWidget(self.DateCalendar, 1, 0, 1, 3)
        self.SelectID1Button = QtGui.QPushButton(IDSetupDlg)
        self.SelectID1Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SelectID1Button.setObjectName(_fromUtf8("SelectID1Button"))
        self.gridLayout_2.addWidget(self.SelectID1Button, 1, 3, 1, 1)
        self.IDToID1Button = QtGui.QPushButton(IDSetupDlg)
        self.IDToID1Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.IDToID1Button.setObjectName(_fromUtf8("IDToID1Button"))
        self.gridLayout_2.addWidget(self.IDToID1Button, 1, 5, 1, 1)
        self.IDListWidget = QtGui.QListWidget(IDSetupDlg)
        self.IDListWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.IDListWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.IDListWidget.setObjectName(_fromUtf8("IDListWidget"))
        self.gridLayout_2.addWidget(self.IDListWidget, 1, 6, 5, 2)
        self.CurrentRadioButton = QtGui.QRadioButton(IDSetupDlg)
        self.CurrentRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CurrentRadioButton.setObjectName(_fromUtf8("CurrentRadioButton"))
        self.gridLayout_2.addWidget(self.CurrentRadioButton, 2, 0, 1, 1)
        self.HistoryRadioButton = QtGui.QRadioButton(IDSetupDlg)
        self.HistoryRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.HistoryRadioButton.setChecked(True)
        self.HistoryRadioButton.setObjectName(_fromUtf8("HistoryRadioButton"))
        self.gridLayout_2.addWidget(self.HistoryRadioButton, 2, 2, 1, 1)
        self.CombineComboBox = QtGui.QComboBox(IDSetupDlg)
        self.CombineComboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CombineComboBox.setObjectName(_fromUtf8("CombineComboBox"))
        self.CombineComboBox.addItem(_fromUtf8(""))
        self.CombineComboBox.addItem(_fromUtf8(""))
        self.CombineComboBox.addItem(_fromUtf8(""))
        self.CombineComboBox.addItem(_fromUtf8(""))
        self.CombineComboBox.addItem(_fromUtf8(""))
        self.CombineComboBox.addItem(_fromUtf8(""))
        self.CombineComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.CombineComboBox, 2, 4, 2, 1)
        self.SelectIDButton = QtGui.QPushButton(IDSetupDlg)
        self.SelectIDButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SelectIDButton.setObjectName(_fromUtf8("SelectIDButton"))
        self.gridLayout_2.addWidget(self.SelectIDButton, 2, 5, 2, 1)
        self.label_2 = QtGui.QLabel(IDSetupDlg)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.IndexNameEdit = QtGui.QLineEdit(IDSetupDlg)
        self.IndexNameEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.IndexNameEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.IndexNameEdit.setObjectName(_fromUtf8("IndexNameEdit"))
        self.gridLayout_2.addWidget(self.IndexNameEdit, 3, 1, 1, 2)
        self.label_3 = QtGui.QLabel(IDSetupDlg)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.IndexIDEdit = QtGui.QLineEdit(IDSetupDlg)
        self.IndexIDEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.IndexIDEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.IndexIDEdit.setObjectName(_fromUtf8("IndexIDEdit"))
        self.gridLayout_2.addWidget(self.IndexIDEdit, 4, 1, 1, 2)
        self.SelectID2Button = QtGui.QPushButton(IDSetupDlg)
        self.SelectID2Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SelectID2Button.setObjectName(_fromUtf8("SelectID2Button"))
        self.gridLayout_2.addWidget(self.SelectID2Button, 4, 3, 1, 1)
        self.ID2ListWidget = QtGui.QListWidget(IDSetupDlg)
        self.ID2ListWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.ID2ListWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ID2ListWidget.setObjectName(_fromUtf8("ID2ListWidget"))
        self.gridLayout_2.addWidget(self.ID2ListWidget, 4, 4, 3, 1)
        self.groupBox = QtGui.QGroupBox(IDSetupDlg)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.FDBComboBox = QtGui.QComboBox(self.groupBox)
        self.FDBComboBox.setObjectName(_fromUtf8("FDBComboBox"))
        self.gridLayout.addWidget(self.FDBComboBox, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.FTComboBox = QtGui.QComboBox(self.groupBox)
        self.FTComboBox.setObjectName(_fromUtf8("FTComboBox"))
        self.gridLayout.addWidget(self.FTComboBox, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.FComboBox = QtGui.QComboBox(self.groupBox)
        self.FComboBox.setObjectName(_fromUtf8("FComboBox"))
        self.gridLayout.addWidget(self.FComboBox, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 5, 0, 1, 3)
        self.LocalSelectID2Button = QtGui.QPushButton(IDSetupDlg)
        self.LocalSelectID2Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LocalSelectID2Button.setObjectName(_fromUtf8("LocalSelectID2Button"))
        self.gridLayout_2.addWidget(self.LocalSelectID2Button, 5, 3, 1, 1)
        self.IDToID2Button = QtGui.QPushButton(IDSetupDlg)
        self.IDToID2Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.IDToID2Button.setObjectName(_fromUtf8("IDToID2Button"))
        self.gridLayout_2.addWidget(self.IDToID2Button, 5, 5, 1, 1)
        self.AcceptButton = QtGui.QPushButton(IDSetupDlg)
        self.AcceptButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AcceptButton.setObjectName(_fromUtf8("AcceptButton"))
        self.gridLayout_2.addWidget(self.AcceptButton, 6, 0, 1, 1)
        self.RejectButton = QtGui.QPushButton(IDSetupDlg)
        self.RejectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.RejectButton.setObjectName(_fromUtf8("RejectButton"))
        self.gridLayout_2.addWidget(self.RejectButton, 6, 1, 1, 1)
        self.IDInputEdit = QtGui.QLineEdit(IDSetupDlg)
        self.IDInputEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.IDInputEdit.setObjectName(_fromUtf8("IDInputEdit"))
        self.gridLayout_2.addWidget(self.IDInputEdit, 6, 6, 1, 2)
        self.label.setBuddy(self.DateEdit)
        self.label_2.setBuddy(self.IndexNameEdit)
        self.label_3.setBuddy(self.IndexIDEdit)

        self.retranslateUi(IDSetupDlg)
        QtCore.QMetaObject.connectSlotsByName(IDSetupDlg)
        IDSetupDlg.setTabOrder(self.DateEdit, self.CurrentRadioButton)
        IDSetupDlg.setTabOrder(self.CurrentRadioButton, self.HistoryRadioButton)
        IDSetupDlg.setTabOrder(self.HistoryRadioButton, self.IndexNameEdit)
        IDSetupDlg.setTabOrder(self.IndexNameEdit, self.IndexIDEdit)
        IDSetupDlg.setTabOrder(self.IndexIDEdit, self.SelectID1Button)
        IDSetupDlg.setTabOrder(self.SelectID1Button, self.ID1ListWidget)
        IDSetupDlg.setTabOrder(self.ID1ListWidget, self.DateCalendar)

    def retranslateUi(self, IDSetupDlg):
        IDSetupDlg.setWindowTitle(_translate("IDSetupDlg", "ID 设置", None))
        self.label.setText(_translate("IDSetupDlg", "<html><head/><body><p align=\"center\">给定日期</p></body></html>", None))
        self.label_7.setText(_translate("IDSetupDlg", "ID 数", None))
        self.IDNumEdit.setText(_translate("IDSetupDlg", "0", None))
        self.SelectID1Button.setText(_translate("IDSetupDlg", ">>", None))
        self.IDToID1Button.setText(_translate("IDSetupDlg", "<<", None))
        self.CurrentRadioButton.setText(_translate("IDSetupDlg", "当前", None))
        self.HistoryRadioButton.setText(_translate("IDSetupDlg", "历史", None))
        self.CombineComboBox.setItemText(0, _translate("IDSetupDlg", "并", None))
        self.CombineComboBox.setItemText(1, _translate("IDSetupDlg", "交", None))
        self.CombineComboBox.setItemText(2, _translate("IDSetupDlg", "上差下", None))
        self.CombineComboBox.setItemText(3, _translate("IDSetupDlg", "下差上", None))
        self.CombineComboBox.setItemText(4, _translate("IDSetupDlg", "对称差", None))
        self.CombineComboBox.setItemText(5, _translate("IDSetupDlg", "只取上", None))
        self.CombineComboBox.setItemText(6, _translate("IDSetupDlg", "只取下", None))
        self.SelectIDButton.setText(_translate("IDSetupDlg", ">>", None))
        self.label_2.setText(_translate("IDSetupDlg", "<html><head/><body><p align=\"center\">指数名称</p></body></html>", None))
        self.label_3.setText(_translate("IDSetupDlg", "<html><head/><body><p align=\"center\">指数代码</p></body></html>", None))
        self.SelectID2Button.setText(_translate("IDSetupDlg", ">>", None))
        self.groupBox.setTitle(_translate("IDSetupDlg", "本地因子库", None))
        self.label_4.setText(_translate("IDSetupDlg", "因子库", None))
        self.label_5.setText(_translate("IDSetupDlg", "因子表", None))
        self.label_6.setText(_translate("IDSetupDlg", "因子", None))
        self.LocalSelectID2Button.setText(_translate("IDSetupDlg", ">>", None))
        self.IDToID2Button.setText(_translate("IDSetupDlg", "<<", None))
        self.AcceptButton.setText(_translate("IDSetupDlg", "确定", None))
        self.RejectButton.setText(_translate("IDSetupDlg", "取消", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    IDSetupDlg = QtGui.QDialog()
    ui = Ui_IDSetupDlg()
    ui.setupUi(IDSetupDlg)
    IDSetupDlg.show()
    sys.exit(app.exec_())

