# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatusGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class StatusGui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setMinimumSize(QtCore.QSize(400, 300))
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.status = QtWidgets.QPlainTextEdit(Dialog)
        self.status.setReadOnly(True)
        self.status.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.status.setBackgroundVisible(False)
        self.status.setCenterOnScroll(False)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 0, 0, 1, 2)
        self.timeLapsedLabel = QtWidgets.QLabel(Dialog)
        self.timeLapsedLabel.setObjectName("timeLapsedLabel")
        self.gridLayout.addWidget(self.timeLapsedLabel, 1, 0, 1, 1)
        self.timeLapsed = QtWidgets.QLCDNumber(Dialog)
        self.timeLapsed.setObjectName("timeLapsed")
        self.gridLayout.addWidget(self.timeLapsed, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OctoCAD©"))
        self.timeLapsedLabel.setText(_translate("Dialog", "Time lapsed in second"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = StatusGui()
    ui.setupUi(Dialog)
    Dialog.show()
    # sys.exit(app.exec_())
