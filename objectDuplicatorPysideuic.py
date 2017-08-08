# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Marisa\Documents\objectDuplicator/objectDuplicator.ui'
#
# Created: Mon Aug 07 15:03:15 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_(object):
    def setupUi(self, ):

        .resize(867, 801)
        self.gridLayout = QtGui.QGridLayout()

        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.instructionsLabel = QtGui.QLabel()
        self.instructionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionsLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.instructionsLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)

        self.nameOfSurfaceLabel = QtGui.QLabel()

        self.horizontalLayout.addWidget(self.nameOfSurfaceLabel)
        self.nameOfSurfaceLineEdit = QtGui.QLineEdit()

        self.horizontalLayout.addWidget(self.nameOfSurfaceLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.percentageGeneratedLabel = QtGui.QLabel()

        self.horizontalLayout_2.addWidget(self.percentageGeneratedLabel)
        self.percentageGeneratedLineEdit = QtGui.QLineEdit()

        self.horizontalLayout_2.addWidget(self.percentageGeneratedLineEdit)
        self.percentageGeneratedHorizontalSlider = QtGui.QSlider()
        self.percentageGeneratedHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.percentageGeneratedHorizontalSlider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)

        self.scaleLabel = QtGui.QLabel()

        self.horizontalLayout_4.addWidget(self.scaleLabel)
        self.scaleLineEdit = QtGui.QLineEdit()

        self.horizontalLayout_4.addWidget(self.scaleLineEdit)
        self.scaleHorizontalSlider = QtGui.QSlider()
        self.scaleHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.scaleHorizontalSlider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)

        self.randomizeScaleCheckBox = QtGui.QCheckBox()

        self.horizontalLayout_7.addWidget(self.randomizeScaleCheckBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)

        self.minRandomizedScaleValueLabel = QtGui.QLabel()

        self.horizontalLayout_3.addWidget(self.minRandomizedScaleValueLabel)
        self.minRandomizedScaleLineEdit = QtGui.QLineEdit()

        self.horizontalLayout_3.addWidget(self.minRandomizedScaleLineEdit)
        self.minRandomizedScaleValueHorizontalSlider = QtGui.QSlider()
        self.minRandomizedScaleValueHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.minRandomizedScaleValueHorizontalSlider)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)

        self.maxRandomizedScaleValueLabel = QtGui.QLabel()

        self.horizontalLayout_6.addWidget(self.maxRandomizedScaleValueLabel)
        self.maxRandomizedScaleLineEdit = QtGui.QLineEdit()

        self.horizontalLayout_6.addWidget(self.maxRandomizedScaleLineEdit)
        self.maxRandomizedScaleValueHorizontalSlider = QtGui.QSlider()
        self.maxRandomizedScaleValueHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.maxRandomizedScaleValueHorizontalSlider)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)

        self.checkBox_4 = QtGui.QCheckBox()

        self.horizontalLayout_8.addWidget(self.checkBox_4)
        self.checkBox_3 = QtGui.QCheckBox()

        self.horizontalLayout_8.addWidget(self.checkBox_3)
        self.checkBox_2 = QtGui.QCheckBox()

        self.horizontalLayout_8.addWidget(self.checkBox_2)
        self.checkBox = QtGui.QCheckBox()

        self.horizontalLayout_8.addWidget(self.checkBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)

        self.label = QtGui.QLabel()

        self.horizontalLayout_5.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit()

        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.horizontalSlider = QtGui.QSlider()
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)

        self.label_2 = QtGui.QLabel()

        self.horizontalLayout_9.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit()

        self.horizontalLayout_9.addWidget(self.lineEdit_2)
        self.horizontalSlider_2 = QtGui.QSlider()
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.horizontalSlider_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.createGeometryPushButton = QtGui.QPushButton()

        self.verticalLayout.addWidget(self.createGeometryPushButton)
        self.deleteLocatorsPushButton = QtGui.QPushButton()

        self.verticalLayout.addWidget(self.deleteLocatorsPushButton)
        self.emptyScenePushButton = QtGui.QPushButton()

        self.verticalLayout.addWidget(self.emptyScenePushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.importLabel = QtGui.QLabel()
        self.importLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.importLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.importLabel)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)

        self.browsePushButton = QtGui.QPushButton()

        self.horizontalLayout_10.addWidget(self.browsePushButton)
        self.lineEdit_3 = QtGui.QLineEdit()

        self.horizontalLayout_10.addWidget(self.lineEdit_3)
        self.importPushButton = QtGui.QPushButton()

        self.horizontalLayout_10.addWidget(self.importPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self, ):
        .setWindowTitle(QtGui.QApplication.translate("", "", None, QtGui.QApplication.UnicodeUTF8))
        self.instructionsLabel.setText(QtGui.QApplication.translate("", "To use tool, enter name of surface you want objects duplicated on below and then select objects to duplicated. Press button to create geometry.", None, QtGui.QApplication.UnicodeUTF8))
        self.nameOfSurfaceLabel.setText(QtGui.QApplication.translate("", "Name of Surface: ", None, QtGui.QApplication.UnicodeUTF8))
        self.percentageGeneratedLabel.setText(QtGui.QApplication.translate("", "Percentage Generated (must be between 1 and 10): ", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleLabel.setText(QtGui.QApplication.translate("", "Scale (must be between 1 and 10):", None, QtGui.QApplication.UnicodeUTF8))
        self.randomizeScaleCheckBox.setText(QtGui.QApplication.translate("", "Randomize Scale Between Minimum and Maximum", None, QtGui.QApplication.UnicodeUTF8))
        self.minRandomizedScaleValueLabel.setText(QtGui.QApplication.translate("", "Minimum Scale:", None, QtGui.QApplication.UnicodeUTF8))
        self.maxRandomizedScaleValueLabel.setText(QtGui.QApplication.translate("", "Maximum Scale:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.createGeometryPushButton.setText(QtGui.QApplication.translate("", "Create Locators and Geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteLocatorsPushButton.setText(QtGui.QApplication.translate("", "Delete Locators", None, QtGui.QApplication.UnicodeUTF8))
        self.emptyScenePushButton.setText(QtGui.QApplication.translate("", "Empty Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.importLabel.setText(QtGui.QApplication.translate("", "Import Geometry/Nurbs to be Duplicated:", None, QtGui.QApplication.UnicodeUTF8))
        self.browsePushButton.setText(QtGui.QApplication.translate("", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.importPushButton.setText(QtGui.QApplication.translate("", "Import", None, QtGui.QApplication.UnicodeUTF8))

