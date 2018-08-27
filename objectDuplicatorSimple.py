

import logging
from collections import Counter
import random as r
import time
import math


import os
import functools
from PySide2 import QtGui, QtCore, QtUiTools, QtWidgets
from shiboken2 import wrapInstance
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
        return wrapInstance(long(ptr), QtWidgets.QMainWindow)


def run():
    """ Builds the UI. Call This function to run the UI
    """

    global win
    try:
        win.close()
    except:
        pass
    win = ObjectDuplicator(parent=getMayaWindow())
    win.show()


def stopwatch(func):
    """ Monitors the time it took to run each function
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


class ObjectDuplicator(QtWidgets.QMainWindow):
    """ Main Class of this Module
    """

    def __init__(self, parent=None):
        super(ObjectDuplicator, self).__init__(parent)

        self.generatedValue = 1.0
        self.allDupGroups = []

        self.setCentralWidget(QtWidgets.QWidget(self))
        self.gridLayout = QtWidgets.QGridLayout()

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.instructionsLabel = QtWidgets.QLabel(
            "To use tool, enter name of surface you want objects duplicated on"
            " below and then select objects to duplicated."
            " A group will be created with all duplicated objects,"
            " enter name of group otherwise a default name will be given."
            "\nPress button to create geometry.")
        self.instructionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionsLabel.setWordWrap(True)
        self.verticalLayout_2.addWidget(self.instructionsLabel)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)

        self.nameOfSurfaceLabel = QtWidgets.QLabel("Name of Surface: ")
        self.horizontalLayout.addWidget(self.nameOfSurfaceLabel)

        self.nameOfSurfaceLineEdit = QtWidgets.QLineEdit()
        self.horizontalLayout.addWidget(self.nameOfSurfaceLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)

        self.nameOfGroupLabel = QtWidgets.QLabel("Name of Group: ")
        self.horizontalLayout_11.addWidget(self.nameOfGroupLabel)

        self.nameOfGroupLineEdit = QtWidgets.QLineEdit()
        self.horizontalLayout_11.addWidget(self.nameOfGroupLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.percentageGeneratedLabel = QtWidgets.QLabel(
            "Percentage Generated: ")
        self.horizontalLayout_2.addWidget(self.percentageGeneratedLabel)
        self.percentageGeneratedLineEdit = QtWidgets.QLineEdit("1")
        self.horizontalLayout_2.addWidget(self.percentageGeneratedLineEdit)

        self.percentageGeneratedHorizontalSlider = QtWidgets.QSlider()
        self.percentageGeneratedHorizontalSlider.setMinimum(1)
        self.percentageGeneratedHorizontalSlider.setMaximum(100)
        self.percentageGeneratedHorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.horizontalLayout_2.addWidget(
            self.percentageGeneratedHorizontalSlider)

        self.setRotationToNormals = QtWidgets.QCheckBox(
            "Set Rotation to Surface")
        self.horizontalLayout_2.addWidget(
            self.setRotationToNormals)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.createGeometryPushButton = QtWidgets.QPushButton("Create Objects")
        self.verticalLayout.addWidget(self.createGeometryPushButton)

        self.deleteObjectsPushButton = QtWidgets.QPushButton(
            "Delete Duplicated Objects Group")
        self.verticalLayout.addWidget(self.deleteObjectsPushButton)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.importLabel = QtWidgets.QLabel(
            "Import Geometry/Nurbs to be Duplicated:")
        self.importLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.importLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.importLabel)

        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)

        self.browsePushButton = QtWidgets.QPushButton("...")
        self.horizontalLayout_10.addWidget(self.browsePushButton)

        self.fileNameLineEdit = QtWidgets.QLineEdit()
        self.horizontalLayout_10.addWidget(self.fileNameLineEdit)

        self.importPushButton = QtWidgets.QPushButton("Import")
        self.horizontalLayout_10.addWidget(self.importPushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        
        self.initStateOfUI()
        self.makeConnections()
        self.setWindowTitle("Object Duplicator")
        self.centralWidget().setLayout(self.gridLayout)
        self.show()

    def initStateOfUI(self):
        """ Sets the initial state of the UI before anything is done
        """

        self.nameOfSurfaceLineEdit.setPlaceholderText("Name of Geometry Here")
        self.nameOfGroupLineEdit.setPlaceholderText("Name of Group Here")
        self.percentageGeneratedHorizontalSlider.setValue(self.generatedValue)
        self.fileNameLineEdit.setPlaceholderText("File Name Here")

    def makeConnections(self):
        """ All functions to make the UI work
        """

        self.percentageGeneratedHorizontalSlider.valueChanged[int].connect(
            self.percentageChange)
        self.percentageGeneratedLineEdit.editingFinished.connect(
            self.manualPercentageEnteredEvent)

        self.createGeometryPushButton.clicked.connect(
            functools.partial(self.createGeometry))

        self.deleteObjectsPushButton.clicked.connect(
            functools.partial(self.deleteObjects))

        self.browsePushButton.clicked.connect(self.findFile)

        self.importPushButton.clicked.connect(self.importFile)

    def percentageChange(self, value):
        """ Changes the percentage number to mirror the slider
            @param value: numbers 1-100
        """

        floatValue = int(value)
        self.percentageGeneratedLineEdit.setText(str(floatValue))
        self.generatedValue = floatValue

    def manualPercentageEnteredEvent(self):
        """ Forces the slider to mirror the value when a manual percentage is entered
        """

        userInputScale = float(self.percentageGeneratedLineEdit.text())

        if userInputScale < 1.0:
            self.generatedValue = 1.0
        elif userInputScale > 100.0:
            self.generatedValue = 100.0
        else:
            self.generatedValue = userInputScale

        self.percentageGeneratedHorizontalSlider.setValue(self.generatedValue)

    def createGeometry(self):
        """ Calls main function to create objects at various vertices and locators
        """

        name = self.nameOfSurfaceLineEdit.text()
        numberToGenerate = float(self.percentageGeneratedLineEdit.text())/100.0

        if self.setRotationToNormals.isChecked():
            setToNormals = True
        else:
            setToNormals = False

        if self.nameOfSurfaceLineEdit.text() == "":
            _logger.debug(
                "Please enter the name of the surface"
                " you want objects duplicated on.")
        elif len(pm.ls(sl=True)) < 1:
            _logger.debug(
                "Please select the object you want duplicated.")
        else:
            self.makeLocators(
                numberToGenerate, name, setToNormals)

    def deleteObjects(self):
        pm.select(cl=True)
        pm.delete(self.allDupGroups)

    def findFile(self):
        """ Opens browser to find a file
        """

        fileName = None
        dialog = QtWidgets.QFileDialog(directory=os.path.dirname(__file__))

        if dialog.exec_():
            fileName = dialog.selectedFiles()

        if fileName:
            self.fileNameLineEdit.setText(fileName[0])

    def importFile(self):
        """ Imports selected file
        """

        fileToImport = self.fileNameLineEdit.text()
        mc.file(fileToImport, i=True, iv=True, mnc=False)

    @stopwatch
    def makeLocators(self, num=None, nameOfSurface=None, setToNormals=None):

        """ Populates a given surface with objects.
            @param num: int, percentage of geometry to be covered
            @param nameOfsurface: str, name of surface
            @param nameOfsurface: str, name given by user to determine
                                       the surface
        """

        selectedObject = pm.ls(sl=True)
        pm.select(nameOfSurface)
        pm.select(selectedObject, add=True)
        if self.nameOfGroupLineEdit.text() == "":
            duplicateGroup = pm.group(n="duplicatedObjectsGrp{0}".format(1), em=True)
        else:
            duplicateGroup = pm.group(n=self.nameOfGroupLineEdit.text(), em=True)
        self.allDupGroups.append(duplicateGroup)

        def vertLocators():
            """ Iterates through vertices on surface, attaches locators and objects
            """

            aimLoc = pm.spaceLocator(n="aimLoc")

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
                    vertLoc = pm.spaceLocator(
                        n="vertexLoc{0}".format(1), p=(v[0], v[1], v[2]))
                    pm.xform(centerPivots=True)
                    pm.delete(pm.aimConstraint(
                        aimLoc, vertLoc,
                        aimVector=[0, -1, 0], upVector=[0, 1, 0],
                        worldUpVector=[0, 1, 0]))
                    duplicatedObject = pm.instance(selectedObject, lf=True)
                    rotVal = pm.getAttr(vertLoc + '.rotate')
                    pm.setAttr(
                        duplicatedObject[0] + '.translate', v[0], v[1], v[2])
                    pm.setAttr(
                        duplicatedObject[0] + '.rotate', rotVal[0], rotVal[1], rotVal[2])

                    if setToNormals is False:
                        pm.setAttr(
                            duplicatedObject[0] + '.rotate', 0, 0, 0)
                        pm.setAttr(
                            vertLoc + '.rotate', 0, 0, 0)

                    pm.parent(vertLoc, duplicatedObject[0], duplicateGroup)
                    vertLocCount += 1

            pm.delete(aimLoc)
            totalVerts = round(float(vertLocCount)/vs*100.0, 2)
            _logger.debug("Generated " + str(vertLocCount) + " locators at vertices for " + str(vs) + " possible vertices. (" + str(totalVerts) + "%) ")

        def faceLocators():
            """ Iterates through faces on surface, attaches locators and objects
            """

            # Selects all faces, puts average center coordinates in a list
            pm.select(nameOfSurface)
            fc = pm.polyEvaluate(face=True)
            faceLocCount = 0
            for x in range(0, fc):
                numGen = r.random()
                bBox = pm.xform(
                    nameOfSurface + '.f['+str(x)+']',
                    ws=True, q=True, bb=True)
                transX = (bBox[0] + bBox[3])/2
                transY = (bBox[1] + bBox[4])/2
                transZ = (bBox[2] + bBox[5])/2

                # Creates locators
                if (numGen <= num):
                    pm.spaceLocator(
                        n="faceLoc{0}".format(1), p=(transX, transY, transZ))
                    duplicatedObject = pm.instance(selectedObject, leaf=True)
                    pm.setAttr(
                        duplicatedObject[0] + '.translate',
                        transX, transY, transZ)

                    if setToNormals is True:
                        pm.delete(
                            pm.aimConstraint(
                                selectedObject, duplicatedObject[0],
                                aimVector=[0, -1, 0], upVector=[0, 1, 0],
                                worldUpVector=[0, 1, 0]))

                    faceLocCount += 1

            totalFace = round(float(faceLocCount)/fc*100.0, 2)
            _logger.debug("Generated " + str(faceLocCount) + " locators at faces for " + str(fc) + " possible surfaces.(" + str(totalFace) + "%) ")

        if (num < 0.01 or num > 10.0):
            _logger.error("Error. Please input a number between 1 and 100")
        elif (pm.objExists(nameOfSurface) is False):
            _logger.error(
                "Error. Enter a name of a plane that exists in your scene.")
        else:
            vertLocators()
            # faceLocators()
            pm.select(cl=True)
