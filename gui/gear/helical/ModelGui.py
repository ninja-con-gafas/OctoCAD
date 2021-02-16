# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModelGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ModelGui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 470)
        Dialog.setMinimumSize(QtCore.QSize(600, 470))
        Dialog.setMaximumSize(QtCore.QSize(600, 470))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.profileLabel = QtWidgets.QLabel(Dialog)
        self.profileLabel.setObjectName("profileLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.profileLabel)
        self.profile = QtWidgets.QComboBox(Dialog)
        self.profile.setObjectName("profile")
        self.profile.addItem("")
        self.profile.addItem("")
        self.profile.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.profile)
        self.helixAngleLabel = QtWidgets.QLabel(Dialog)
        self.helixAngleLabel.setObjectName("helixAngleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.helixAngleLabel)
        self.helixAngle = QtWidgets.QDoubleSpinBox(Dialog)
        self.helixAngle.setMinimum(25.0)
        self.helixAngle.setMaximum(30.0)
        self.helixAngle.setSingleStep(0.25)
        self.helixAngle.setObjectName("helixAngle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.helixAngle)
        self.helixHandLabel = QtWidgets.QLabel(Dialog)
        self.helixHandLabel.setObjectName("helixHandLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.helixHandLabel)
        self.helixHand = QtWidgets.QComboBox(Dialog)
        self.helixHand.setObjectName("helixHand")
        self.helixHand.addItem("")
        self.helixHand.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.helixHand)
        self.moduleLabel = QtWidgets.QLabel(Dialog)
        self.moduleLabel.setObjectName("moduleLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.moduleLabel)
        self.module = QtWidgets.QDoubleSpinBox(Dialog)
        self.module.setMinimum(1.0)
        self.module.setMaximum(50.0)
        self.module.setSingleStep(0.25)
        self.module.setObjectName("module")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.module)
        self.teethLabel = QtWidgets.QLabel(Dialog)
        self.teethLabel.setObjectName("teethLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.teethLabel)
        self.teeth = QtWidgets.QSpinBox(Dialog)
        self.teeth.setMinimum(14)
        self.teeth.setMaximum(300)
        self.teeth.setObjectName("teeth")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.teeth)
        self.gearingLabel = QtWidgets.QLabel(Dialog)
        self.gearingLabel.setObjectName("gearingLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.gearingLabel)
        self.gearing = QtWidgets.QComboBox(Dialog)
        self.gearing.setObjectName("gearing")
        self.gearing.addItem("")
        self.gearing.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.gearing)
        self.faceWidthLabel = QtWidgets.QLabel(Dialog)
        self.faceWidthLabel.setObjectName("faceWidthLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.faceWidthLabel)
        self.faceWidth = QtWidgets.QDoubleSpinBox(Dialog)
        self.faceWidth.setMinimum(10.0)
        self.faceWidth.setMaximum(100.0)
        self.faceWidth.setSingleStep(0.5)
        self.faceWidth.setObjectName("faceWidth")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.faceWidth)
        self.clearanceLabel = QtWidgets.QLabel(Dialog)
        self.clearanceLabel.setObjectName("clearanceLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.clearanceLabel)
        self.clearance = QtWidgets.QDoubleSpinBox(Dialog)
        self.clearance.setMinimum(0.45)
        self.clearance.setMaximum(2.0)
        self.clearance.setSingleStep(0.01)
        self.clearance.setObjectName("clearance")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.clearance)
        self.filletLabel = QtWidgets.QLabel(Dialog)
        self.filletLabel.setObjectName("filletLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.filletLabel)
        self.fillet = QtWidgets.QDoubleSpinBox(Dialog)
        self.fillet.setMinimum(0.25)
        self.fillet.setMaximum(5.0)
        self.fillet.setSingleStep(0.05)
        self.fillet.setObjectName("fillet")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.fillet)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Model Data"))
        self.profileLabel.setText(_translate("Dialog", "Select type of gear pair"))
        self.profile.setItemText(0, _translate("Dialog", "14.5 degree full depth involute tooth"))
        self.profile.setItemText(1, _translate("Dialog", "20 degree full depth involute tooth"))
        self.profile.setItemText(2, _translate("Dialog", "20 degree stub involute tooth"))
        self.helixAngleLabel.setText(_translate("Dialog", "Enter helix angle"))
        self.helixHandLabel.setText(_translate("Dialog", "Select hand of helix"))
        self.helixHand.setItemText(0, _translate("Dialog", "Right hand"))
        self.helixHand.setItemText(1, _translate("Dialog", "Left hand"))
        self.moduleLabel.setText(_translate("Dialog", "Enter module"))
        self.teethLabel.setText(_translate("Dialog", "Enter number of teeth"))
        self.gearingLabel.setText(_translate("Dialog", "Select type of gearing"))
        # self.gearing.setItemText(0, _translate("Dialog", "Internal gearing"))
        self.gearing.setItemText(1, _translate("Dialog", "External gearing"))
        self.faceWidthLabel.setText(_translate("Dialog", "Enter face width in terms of module"))
        self.clearanceLabel.setText(_translate("Dialog", "Enter clearance in terms of module"))
        self.filletLabel.setText(_translate("Dialog", "Enter fillet radius in terms of module"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ModelGui()
    ui.setupUi(Dialog)
    Dialog.show()
    # sys.exit(app.exec_())
