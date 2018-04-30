

import logging
from collections import Counter
import maya.cmds as pm
import random as r
import time
import math


import os
import functools
from PySide import QtGui, QtCore, QtUiTools
from shiboken import wrapInstance
import maya.cmds as mc
import pymel.core as pm
from pymel.core.datatypes import Vector, Matrix, Point
from pymel.all import *
import maya.OpenMayaUI as omui

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


"""
to add a new path:
import sys
sys.path.append( 'palce path here', Ex: 'C:\Users\yourName\Documents/folderName' )

Otherwise, type this into the Script Editor:
import objectDuplicator as ob
reload(ob)
ob.run()
"""


def getMayaWindow():
    """ Pointer to the Maya Main Window 
    """

    ptr = omui.MQtUtil.mainWindow()
    if ptr:
        return wrapInstance(long(ptr), QtGui.QMainWindow)


def run():
    """ Builds the UI. Call This function to run the UI.
    """

    global win
    try:
        win.close()
    except:
        pass
    win = ObjectDuplicator(parent=getMayaWindow())
    win.show()


def stopwatch(func):
    """ Monitors the time it took to run each function.
        @return: float, total seconds
    """

    def timed(*args, **kwargs):

        timeStart = time.time()

        result = func(*args, **kwargs)

        timeEnd = time.time()
        elapsedTime = timeEnd - timeStart
        _logger.debug("%2.2f sec" % (elapsedTime))

        return result

    return timed


class ObjectDuplicator(QtGui.QDialog):
    """ Main Class of this Module
    """

    def __init__(self, parent=None):
        super(ObjectDuplicator, self).__init__(parent)

        self.scaleValue = 1.0
        self.randomizedScale = False
        self.setRotationToNormals = False
        self.randomizedRotation = False
        self.randomizeX = False
        self.randomizeY = False
        self.randomizeZ = False

        self.gridLayout = QtGui.QGridLayout()

        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.instructionsLabel = QtGui.QLabel(
            "To use tool, enter name of surface you want objects duplicated on below and then select objects to duplicated. Press button to create geometry.")
        self.instructionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionsLabel.setWordWrap(True)
        self.verticalLayout_2.addWidget(self.instructionsLabel)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)

        self.nameOfSurfaceLabel = QtGui.QLabel("Name of Surface: ")
        self.horizontalLayout.addWidget(self.nameOfSurfaceLabel)

        self.nameOfSurfaceLineEdit = QtGui.QLineEdit()
        self.horizontalLayout.addWidget(self.nameOfSurfaceLineEdit)

        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.percentageGeneratedLabel = QtGui.QLabel("Percentage Generated: ")
        self.horizontalLayout_2.addWidget(self.percentageGeneratedLabel)
        self.percentageGeneratedLineEdit = QtGui.QLineEdit("1.0")
        self.horizontalLayout_2.addWidget(self.percentageGeneratedLineEdit)

        self.percentageGeneratedHorizontalSlider = QtGui.QSlider()
        self.percentageGeneratedHorizontalSlider.setMinimum(1)
        self.percentageGeneratedHorizontalSlider.setMaximum(100)
        self.percentageGeneratedHorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.horizontalLayout_2.addWidget(
            self.percentageGeneratedHorizontalSlider)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)

        self.scaleLabel = QtGui.QLabel("Scale:")
        self.horizontalLayout_4.addWidget(self.scaleLabel)

        self.scaleLineEdit = QtGui.QLineEdit("1.0")
        self.horizontalLayout_4.addWidget(self.scaleLineEdit)

        self.scaleHorizontalSlider = QtGui.QSlider()
        self.scaleHorizontalSlider.setMinimum(1)
        self.scaleHorizontalSlider.setMaximum(100)
        self.scaleHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalLayout_4.addWidget(self.scaleHorizontalSlider)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)

        self.randomizeScaleCheckBox = QtGui.QCheckBox("Randomize Scale")
        self.horizontalLayout_7.addWidget(self.randomizeScaleCheckBox)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)

        self.minRandomizedScaleValueLabel = QtGui.QLabel("Minimum Scale:")
        self.horizontalLayout_3.addWidget(self.minRandomizedScaleValueLabel)

        self.minRandomizedScaleLineEdit = QtGui.QLineEdit("1.0")
        self.horizontalLayout_3.addWidget(self.minRandomizedScaleLineEdit)

        self.minRandomizedScaleValueHorizontalSlider = QtGui.QSlider()
        self.minRandomizedScaleValueHorizontalSlider.setMinimum(1)
        self.minRandomizedScaleValueHorizontalSlider.setMaximum(100)
        self.minRandomizedScaleValueHorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.horizontalLayout_3.addWidget(
            self.minRandomizedScaleValueHorizontalSlider)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)

        self.maxRandomizedScaleValueLabel = QtGui.QLabel("Maximum Scale:")
        self.horizontalLayout_6.addWidget(self.maxRandomizedScaleValueLabel)

        self.maxRandomizedScaleLineEdit = QtGui.QLineEdit("2.0")
        self.horizontalLayout_6.addWidget(self.maxRandomizedScaleLineEdit)

        self.maxRandomizedScaleValueHorizontalSlider = QtGui.QSlider()
        self.maxRandomizedScaleValueHorizontalSlider.setMinimum(1)
        self.maxRandomizedScaleValueHorizontalSlider.setMaximum(100)
        self.maxRandomizedScaleValueHorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.horizontalLayout_6.addWidget(
            self.maxRandomizedScaleValueHorizontalSlider)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)

        self.setRotationToNormals = QtGui.QCheckBox(
            "Set Rotation to Surface Normals")
        self.horizontalLayout_8.addWidget(self.setRotationToNormals)

        self.randomizeAllRotationCheckBox = QtGui.QCheckBox(
            "Randomize Rotation")
        self.horizontalLayout_8.addWidget(self.randomizeAllRotationCheckBox)

        self.randomizeRotateXCheckBox = QtGui.QCheckBox("Randomize X")
        self.horizontalLayout_8.addWidget(self.randomizeRotateXCheckBox)

        self.randomizeRotateYCheckBox = QtGui.QCheckBox("Randomize Y")
        self.horizontalLayout_8.addWidget(self.randomizeRotateYCheckBox)

        self.randomizeRotateZCheckBox = QtGui.QCheckBox("Randomize Z")
        self.horizontalLayout_8.addWidget(self.randomizeRotateZCheckBox)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)

        self.minRandomizedRotationLabel = QtGui.QLabel("Minimum Rotation: ")
        self.horizontalLayout_5.addWidget(self.minRandomizedRotationLabel)

        self.minRandomizedRotationLineEdit = QtGui.QLineEdit("0.0")
        self.horizontalLayout_5.addWidget(self.minRandomizedRotationLineEdit)

        self.minRandomizedRotationHorizontalSlider = QtGui.QSlider()
        self.minRandomizedRotationHorizontalSlider.setMinimum(-100)
        self.minRandomizedRotationHorizontalSlider.setMaximum(100)
        self.minRandomizedRotationHorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.horizontalLayout_5.addWidget(
            self.minRandomizedRotationHorizontalSlider)

        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)

        self.maxRandomizedRotationLabel = QtGui.QLabel("Maximum Rotation: ")
        self.horizontalLayout_9.addWidget(self.maxRandomizedRotationLabel)

        self.maxRandomizedRotationLineEdit = QtGui.QLineEdit("1.0")
        self.horizontalLayout_9.addWidget(self.maxRandomizedRotationLineEdit)

        self.maxRandomizedRotationHorizontalSlider = QtGui.QSlider()
        self.maxRandomizedRotationHorizontalSlider.setMinimum(-100)
        self.maxRandomizedRotationHorizontalSlider.setMaximum(100)
        self.maxRandomizedRotationHorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.horizontalLayout_9.addWidget(
            self.maxRandomizedRotationHorizontalSlider)

        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.createGeometryPushButton = QtGui.QPushButton("Create Objects")
        self.verticalLayout.addWidget(self.createGeometryPushButton)

        self.deleteLocatorsPushButton = QtGui.QPushButton("Delete Locators")
        self.verticalLayout.addWidget(self.deleteLocatorsPushButton)

        self.deleteObjectsPushButton = QtGui.QPushButton("Delete Duplicated Objects")
        self.verticalLayout.addWidget(self.deleteObjectsPushButton)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.importLabel = QtGui.QLabel(
            "Import Geometry/Nurbs to be Duplicated:")
        self.importLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.importLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.importLabel)

        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)

        self.browsePushButton = QtGui.QPushButton("...")
        self.horizontalLayout_10.addWidget(self.browsePushButton)

        self.fileNameLineEdit = QtGui.QLineEdit()
        self.horizontalLayout_10.addWidget(self.fileNameLineEdit)

        self.importPushButton = QtGui.QPushButton("Import")
        self.horizontalLayout_10.addWidget(self.importPushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        
        self.makeConnections()
        self.initStateOfUI()
        self.setWindowTitle("Object Duplicator")
        self.setLayout(self.gridLayout)
        self.show()

    def initStateOfUI(self):
        """ Sets the initial state of the UI before anything is done.
        """

        self.nameOfSurfaceLineEdit.setPlaceholderText("Name of Geometry Here")
        self.percentageGeneratedHorizontalSlider.setValue(self.scaleValue)
        self.minScaleValue = int(round(float(
            self.minRandomizedScaleLineEdit.text())))
        self.maxScaleValue = int(round(float(
            self.maxRandomizedScaleLineEdit.text())))
        self.minRotationValue = int(round(float(
            self.minRandomizedRotationLineEdit.text())))
        self.maxRotationValue = int(round(float(
            self.maxRandomizedRotationLineEdit.text())))
        self.fileNameLineEdit.setPlaceholderText("File Name Here")

    def makeConnections(self):
        """ All functions to make the UI work.
        """

        self.percentageGeneratedHorizontalSlider.valueChanged[int].connect(
            self.percentageChange)
        self.percentageGeneratedLineEdit.editingFinished.connect(
            self.manualPercentageEnteredEvent)

        self.scaleHorizontalSlider.valueChanged[int].connect(self.scaleChange)
        self.scaleLineEdit.editingFinished.connect(
            self.manualScaleEnteredEvent)
        self.randomizeScaleCheckBox.stateChanged.connect(
            self.disableMainScaleSlider)

        self.minRandomizedScaleValueHorizontalSlider.valueChanged[int].connect(
            self.minRandomizedScaleChange)
        self.minRandomizedScaleLineEdit.editingFinished.connect(
            self.manualMinScaleEnteredEvent)
        self.maxRandomizedScaleValueHorizontalSlider.valueChanged[int].connect(
            self.maxRandomizedScaleChange)
        self.maxRandomizedScaleLineEdit.editingFinished.connect(
            self.manualMaxScaleEnteredEvent)

        self.setRotationToNormals.stateChanged.connect(
            self.disableRotationCheckBoxes)

        self.setRotationToNormals.stateChanged.connect(
            self.checkNormalsRotationBoxesState)

        self.randomizeAllRotationCheckBox.stateChanged.connect(
            self.checkAllRotationBoxState)

        self.minRandomizedRotationHorizontalSlider.valueChanged[int].connect(
            self.minRandomizedRotationChange)
        self.minRandomizedRotationLineEdit.editingFinished.connect(
            self.manualMinRotationEnteredEvent)
        self.maxRandomizedRotationHorizontalSlider.valueChanged[int].connect(
            self.maxRandomizedRotationChange)
        self.maxRandomizedRotationLineEdit.editingFinished.connect(
            self.manualMaxRotationEnteredEvent)

        self.createGeometryPushButton.clicked.connect(
            functools.partial(self.createGeometry))

        self.deleteLocatorsPushButton.clicked.connect(
            functools.partial(self.deleteLocators))

        self.browsePushButton.clicked.connect(self.findFile)

        self.importPushButton.clicked.connect(self.importFile)

    def percentageChange(self, value):
        """ Changes the percentage number to mirror the slider.
            @param value: numbers 1-100
        """

        floatValue = float(value)
        self.percentageGeneratedLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def manualPercentageEnteredEvent(self):
        """ Forces the slider to mirror the value when a manual percentage is entered.
        """

        userInputScale = float(self.percentageGeneratedLineEdit.text())

        if userInputScale < 1.0:
            self.scaleValue = 1.0
        elif userInputScale > 100.0:
            self.scaleValue = 100.0
        else:
            self.scaleValue = userInputScale
        
        self.percentageGeneratedHorizontalSlider.setValue(self.scaleValue)

    def scaleChange(self, value):
        """ Changes the scale number to mirror the slider.
        """

        floatValue = float(value)
        self.scaleLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def manualScaleEnteredEvent(self):
        """ Forces the slider to mirror the value when a manual scale is entered.
        """
        
        userInputScale = float(self.scaleLineEdit.text())

        if userInputScale < 1.0:
            self.scaleValue = 1.0
        elif userInputScale > 100.0:
            self.scaleValue = 100.0
        else:
            self.scaleValue = userInputScale
        
        self.scaleHorizontalSlider.setValue(self.scaleValue)

    def checkScaleBoxState(self):
        """ Activates minimum and maximum scales if the user wants to randomize scale.
        """

        if self.randomizeScaleCheckBox.isChecked():
            self.randomizedScale = True
            self.setScaleMinMaxValues()
        else:
            self.randomizedScale = False

    def disableMainScaleSlider(self):
        """ Disables main scale slider.
        """

        if self.randomizeScaleCheckBox.isChecked():
            self.scaleLineEdit.setDisabled(True)
            self.scaleHorizontalSlider.setDisabled(True)
        else:
            self.scaleLineEdit.setDisabled(False)
            self.scaleHorizontalSlider.setDisabled(False)

    def minRandomizedScaleChange(self, value):
        """ Changes the minimum scale number to mirror the slider.
        """

        floatValue = float(value)
        self.minRandomizedScaleLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def maxRandomizedScaleChange(self, value):
        """ Changes the maximum scale number to mirror the slider.
        """
        floatValue = float(value)
        self.maxRandomizedScaleLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def manualMinScaleEnteredEvent(self):
        """ Forces the slider to mirror the value when a manual minimum scale is entered.
        """

        userInputScale = float(self.minRandomizedScaleLineEdit.text())

        if userInputScale < 1.0:
            self.scaleValue = 1.0
        elif userInputScale > 100.0:
            self.scaleValue = 100.0
        else:
            self.scaleValue = userInputScale

        self.minRandomizedScaleValueHorizontalSlider.setValue(self.scaleValue)

    def manualMaxScaleEnteredEvent(self):
        """" Forces the slider to mirror the value when a manual maximum scale is entered.
        """

        userInputScale = float(self.maxRandomizedScaleLineEdit.text())

        if userInputScale < 1.0:
            self.scaleValue = 1.0
        elif userInputScale > 100.0:
            self.scaleValue = 100.0
        else:
            self.scaleValue = userInputScale

        self.maxRandomizedScaleValueHorizontalSlider.setValue(self.scaleValue)

    def setScaleMinMaxValues(self):
        """ Captures minimum and maximum scale values.
        """
        self.minScaleValue = int(round(float(
            self.minRandomizedScaleLineEdit.text())))
        self.maxScaleValue = int(round(float(
            self.maxRandomizedScaleLineEdit.text())))
        if (self.minScaleValue >= self.maxScaleValue):
            _logger.error("Minimum value must be smaller than maximum value.")
            return

    def disableRotationCheckBoxes(self):
        """ Disables rotation check boxes if set
            to normals is on.
        """

        if self.setRotationToNormals.isChecked():
            self.randomizeAllRotationCheckBox.setDisabled(True)
            self.randomizeRotateXCheckBox.setDisabled(True)
            self.randomizeRotateYCheckBox.setDisabled(True)
            self.randomizeRotateZCheckBox.setDisabled(True)
            self.minRandomizedRotationLineEdit.setDisabled(True)
            self.minRandomizedRotationHorizontalSlider.setDisabled(True)
            self.maxRandomizedRotationLineEdit.setDisabled(True)
            self.maxRandomizedRotationHorizontalSlider.setDisabled(True)
        else:
            self.randomizeAllRotationCheckBox.setDisabled(False)
            self.randomizeRotateXCheckBox.setDisabled(False)
            self.randomizeRotateYCheckBox.setDisabled(False)
            self.randomizeRotateZCheckBox.setDisabled(False)
            self.minRandomizedRotationLineEdit.setDisabled.setDisabled(False)
            self.minRandomizedRotationHorizontalSlider.setDisabled(False)
            self.maxRandomizedRotationLineEdit.setDisabled(False)
            self.maxRandomizedRotationHorizontalSlider.setDisabled(False)

    def checkNormalsRotationBoxesState(self):
        if self.setRotationToNormals.isChecked():
            self.setRotationToNormals = True

    def checkAllRotationBoxState(self):
        """ Automatically checks all other rotation boxes if master rotation box is on
        """

        if self.randomizeAllRotationCheckBox.isChecked():
            self.randomizeRotateXCheckBox.click()
            self.randomizeRotateYCheckBox.click()
            self.randomizeRotateZCheckBox.click()

    def checkRotationBoxesStates(self):
        """ Activates various rotations if checked.
        """

        if self.randomizeAllRotationCheckBox.isChecked():
            self.randomizedRotation = True
            self.setMinMaxRotationValues()

        if self.randomizeRotateXCheckBox.isChecked():
            self.randomizeX = True
            self.setMinMaxRotationValues()

        if self.randomizeRotateYCheckBox.isChecked():
            self.randomizeY = True
            self.setMinMaxRotationValues()

        if self.randomizeRotateZCheckBox.isChecked():
            self.randomizeZ = True
            self.setMinMaxRotationValues()

    def minRandomizedRotationChange(self, value):
        """ Changes the minimum rotation number to mirror the slider.
        """

        floatValue = float(value)
        self.minRandomizedRotationLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def maxRandomizedRotationChange(self, value):
        """ Changes the maximum rotation number to mirror the slider.
        """
        floatValue = float(value)
        self.maxRandomizedRotationLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def manualMinRotationEnteredEvent(self):
        """ Forces the slider to mirror the value
            when a manual minimum rotation is entered.
        """

        userInputScale = float(self.minRandomizedRotationLineEdit.text())

        if userInputScale < -100.0:
            self.scaleValue = -100.0
        elif userInputScale > 100.0:
            self.scaleValue = 100.0
        else:
            self.scaleValue = userInputScale

        self.minRandomizedRotationHorizontalSlider.setValue(self.scaleValue)

    def manualMaxRotationEnteredEvent(self):
        """" Forces the slider to mirror the value when a
             manual maximum rotation is entered.
        """

        userInputScale = float(self.maxRandomizedRotationLineEdit.text())

        if userInputScale < -100:
            self.scaleValue = -100.0
        elif userInputScale > 100.0:
            self.scaleValue = 100.0
        else:
            self.scaleValue = userInputScale
        
        self.maxRandomizedRotationHorizontalSlider.setValue(self.scaleValue)

    def setMinMaxRotationValues(self):
        """ Capture minimum and maximum rotation values from user
        """

        self.minRotationValue = int(round(float(
            self.minRandomizedRotationLineEdit.text())))
        self.maxRotationValue = int(round(float(
            self.maxRandomizedRotationLineEdit.text())))
        if (self.minRotationValue >= self.maxRotationValue):
            _logger.error("Minimum value must be smaller than maximum value.")
            return

    def createGeometry(self):
        """ Calls main function to create objects at various vertices and locators.
        """

        name = self.nameOfSurfaceLineEdit.text()
        numberGenerated = float(self.percentageGeneratedLineEdit.text())/100.0
        scaleValue = float(self.scaleLineEdit.text())
        self.checkScaleBoxState()
        self.checkRotationBoxesStates()
        
        self.makeLocators(
            numberGenerated, name, scaleValue, self.randomizedScale,
            self.minScaleValue, self.maxScaleValue,
            self.setRotationToNormals, self.randomizedRotation,
            self.randomizeX, self.randomizeY,
            self.randomizeZ, self.minRotationValue, self.maxRotationValue)

    def deleteLocators(self):
        """ Deleted all locators made from UI.
        """

        allVertexLocs = pm.ls('vertexLoc*')
        allFaceLocs = pm.ls('faceLoc*')
        pm.delete(allVertexLocs, allFaceLocs)

    def findFile(self):
        """ Opens browser to find a file.
        """

        fileName = None
        dialog = QtGui.QFileDialog(directory=os.path.dirname(__file__))

        if dialog.exec_():
            fileName = dialog.selectedFiles()

        if fileName:
            self.fileNameLineEdit.setText(fileName[0])

    def importFile(self):
        """ Imports selected file.
        """

        fileToImport = self.fileNameLineEdit.text()
        mc.file(fileToImport, i=True, iv=True, mnc=False)

    @stopwatch
    def makeLocators(
        self, num=None, nameOfSurface=None, scaleOfItems=None,
        randomScale=None, minRandomScale=None, maxRandomScale=None,
        setToNormals=None, randomRotation=None, randomX=None, randomY=None,
            randomZ=None, minRandomRotation=None, maxRandomRotation=None):

        """ Populates a given surface with objects.
            @param num: fl, percentage of geometry to be covered
            @param nameOfsurface: str, name given by user to determine the surface
            @param scaleOfItems: int, scale of items being duplicated
            @param randomScale: bool, randomizes scale between a range of minimum and maximum values
            @param minRandomScale: int, minimum scale of object
            @param maxRandomScale: int, maximum scale of object
            @param randomRotation: bool, randomizes rotation between a range of minimum and maximum values
            @param randomX: bool, randomizes the X rotation between a range of minimum and maximum values
            @param randomY: bool, randomizes the Y rotation between a range of minimum and maximum values
            @param randomZ: bool, randomizes the Z rotation between a range of minimum and maximum values
            @param minRandomRotation: int, minimum rotation of object
            @param maxRandomRotation: int, maximum rotation of object
        """

        selectedObject = pm.ls(sl=True)
        sizeOfSelectedObject = int(pm.getAttr(selectedObject[0] + '.scaleY'))
        boundingBox = pm.exactWorldBoundingBox(selectedObject)
        bottom = [(boundingBox[0] + boundingBox[3])/2, boundingBox[1], (boundingBox[2] + boundingBox[5])/2]
        pm.xform(selectedObject, piv=bottom, ws=True)
        pm.select(nameOfSurface)
        pm.select(selectedObject, add=True)
        pm.parentConstraint(nameOfSurface, selectedObject, mo=False)
        pm.delete(selectedObject, cn=True)

        def vertLocators():
            """ Iterates through vertices on surface, attaches locators and objects
            """

            # Selects all vertices, puts all vertice coordinates in a list
            pm.select(nameOfSurface)
            vs = pm.polyEvaluate(v=True)
            verts = []
            vertLocCount = 0
            for i in range(0, vs):
                verts += (pm.pointPosition(nameOfSurface + '.vtx[' + str(i) + ']'), )

            # Creates locators
            for v in verts:
                numGen = r.random() 
                if (numGen <= num):
                    pm.spaceLocator(n="vertexLoc{0}".format(1), p=(v[0], v[1], v[2]))
                    duplicatedObject = pm.instance(selectedObject, leaf=True)
                    pm.setAttr(duplicatedObject[0] + '.translate', (v[0], v[1], v[2]))
                    randomScaleNumber = r.randrange(minRandomScale, maxRandomScale)
                    randomRotationNumber = r.randrange(minRandomRotation, maxRandomRotation)

                    if randomScale is True:
                        pm.setAttr(duplicatedObject[0] + '.scale', randomScaleNumber, randomScaleNumber, randomScaleNumber)

                    if setToNormals is True:
                        poly = PyNode(nameOfSurface)
                        pos = [v[0], v[1], v[2]]
                        count = 0
                        for point in poly.getPoints('world'):
                            if dt.Vector(point) == dt.Vector(pos):
                                poly = PyNode(nameOfSurface + '.vtx[' + str(count) + ']')
                                normalVector = poly.getNormal()
                                rotationAngles = getRotationAxis(normalVector)
                            count += 1

                    if randomRotation is True:
                        pm.setAttr(duplicatedObject[0] + '.rotate', randomRotationNumber, randomRotationNumber, randomRotationNumber)

                    if randomX is True:
                        pm.setAttr(duplicatedObject[0] + '.rotateX', randomRotationNumber)

                    if randomY is True:
                        pm.setAttr(duplicatedObject[0] + '.rotateY', randomRotationNumber)

                    if randomZ is True:
                        pm.setAttr(duplicatedObject[0] + '.rotateZ', randomRotationNumber)

                    vertLocCount += 1

            totalVerts = round(float(vertLocCount)/vs*100.0, 2)
            _logger.debug("Generated " + str(vertLocCount) + " locators at vertices for " + str(vs) + " possible vertices. (" + str(totalVerts) + "%) ")

        def getRotationAxis(normalVector):
            yVector = Vector(normalVector)
            if pm.upAxis(q=True, axis=True) == 'y':
                upVector = Vector(0, 1, 0)
            else:
                upVector = Vector(0, 0, 1)

            xVector = Vector.cross(yVector, upVector)
            zVector = Vector.cross(xVector, yVector)

            rotationMatrix = Matrix(
                xVector.x, xVector.y, xVector.z,
                yVector.x, yVector.y, yVector.z,
                zVector.x, zVector.y, zVector.z)

            # rotX = math.arcta

        def faceLocators():
            """ Iterates through faces on surface, attaches locators and objects
            """

            # Selects all faces, puts average center coordinates in a list
            pm.select(nameOfSurface)
            fc = pm.polyEvaluate(face=True)
            faceLocCount = 0
            for x in range(0, fc):
                numGen = r.random()
                bBox = pm.xform(nameOfSurface + '.f['+str(x)+']', ws=True, q=True, bb=True)
                transX = (bBox[0] + bBox[3])/2
                transY = (bBox[1] + bBox[4])/2
                transZ = (bBox[2] + bBox[5])/2

                # Creates locators
                if (numGen <= num):
                    pm.spaceLocator(n="faceLoc{0}".format(1), p=(transX, transY, transZ))
                    duplicatedObject = pm.instance(selectedObject, leaf=True)
                    pm.setAttr(duplicatedObject[0] + '.translate', transX, transY, transZ)
                    randomScaleNumber = r.randrange(minRandomScale, maxRandomScale)
                    randomRotationNumber = r.randrange(minRandomRotation, maxRandomRotation)

                    if randomScale is True:
                        pm.setAttr(duplicatedObject[0] + '.scale', randomScaleNumber, randomScaleNumber, randomScaleNumber)

                    if setToNormals is True:
                        poly = PyNode(nameOfSurface + '.f[' + str(x) + ']')
                        normalVector = poly.getNormal()
                        rotationMatrix = getRotationAxis(Vector(normalVector))

                    if randomRotation is True:
                        pm.setAttr(duplicatedObject[0] + '.rotate', randomRotationNumber, randomRotationNumber, randomRotationNumber)

                    if randomX is True:
                        pm.setAttr(duplicatedObject[0] + '.rotateX', randomRotationNumber)

                    if randomY is True:
                        pm.setAttr(duplicatedObject[0] + '.rotateY', randomRotationNumber)

                    if randomZ is True:
                        pm.setAttr(duplicatedObject[0] + '.rotateZ', randomRotationNumber)

                    faceLocCount += 1

            totalFace = round(float(faceLocCount)/fc*100.0, 2)
            _logger.debug("Generated " + str(faceLocCount) + " locators at faces for " + str(fc) + " possible surfaces.(" + str(totalFace) + "%) ")

        if (num < 0.01 or num > 10.0):
            _logger.error("Error. Please input a number between 1 and 100")
        elif (pm.objExists(nameOfSurface) is False):
            _logger.error("Error. Enter a name of a plane that exists in your project.")
        else:
            vertLocators()
            faceLocators()
