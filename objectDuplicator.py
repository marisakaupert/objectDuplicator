

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
# import pyside_dynamic
import maya.cmds as mc
import pymel.core as pm
import maya.OpenMayaUI as omui 


_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


def getMayaWindow():
    """ pointer to the maya main window  
    """
    ptr = omui.MQtUtil.mainWindow()
    if ptr :
        return wrapInstance(long(ptr), QtGui.QMainWindow)


def run():
    """  builds our UI
    """
    global win
    if win:
        win.close()
    win = ObjectDuplicator(parent=getMayaWindow())
    win.show()

def stopwatch(func):

    def timed (*args, **kwargs):

        timeStart = time.time()

        result = func(*args, **kwargs)

        timeEnd = time.time()
        elapsedTime = timeEnd - timeStart
        _logger.debug("%2.2f sec" %(elapsedTime))

        return result

    return timed




class ObjectDuplicator(QtGui.QDialog):
    """ This is the main class of this module """

    def __init__(self, parent=None):
        super(ObjectDuplicator,self).__init__(parent)

        self.scaleValue = 1.0
        self.randomizedScale = False
        self.randomizedRotation = False
        self.randomizeX = False
        self.randomizeY = False
        self.randomizeZ = False




        # from pysideuic--------------------------------------------


        self.gridLayout = QtGui.QGridLayout()

        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.instructionsLabel = QtGui.QLabel("To use tool, enter name of surface you want objects duplicated on below and then select objects to duplicated. Press button to create geometry.")
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
        self.percentageGeneratedHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.percentageGeneratedHorizontalSlider)
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
        self.minRandomizedScaleValueHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.minRandomizedScaleValueHorizontalSlider)
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
        self.maxRandomizedScaleValueHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.maxRandomizedScaleValueHorizontalSlider)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)

        self.randomizeAllRotationCheckBox = QtGui.QCheckBox("Randomize Rotation")

        self.horizontalLayout_8.addWidget(self.randomizeAllRotationCheckBox)
        self.randomizeRotateXCheckBox = QtGui.QCheckBox("Randomize Rotate X")

        self.horizontalLayout_8.addWidget(self.randomizeRotateXCheckBox)
        self.randomizeRotateYCheckBox = QtGui.QCheckBox("Randomize Rotate Y")

        self.horizontalLayout_8.addWidget(self.randomizeRotateYCheckBox)
        self.randomizeRotateZCheckBox = QtGui.QCheckBox("Randomize Rotate Z")

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
        self.minRandomizedRotationHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.minRandomizedRotationHorizontalSlider)
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
        self.maxRandomizedRotationHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.maxRandomizedRotationHorizontalSlider)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.createGeometryPushButton = QtGui.QPushButton("Create Objects")

        self.verticalLayout.addWidget(self.createGeometryPushButton)
        self.deleteLocatorsPushButton = QtGui.QPushButton("Delete Locators")

        self.verticalLayout.addWidget(self.deleteLocatorsPushButton)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.importLabel = QtGui.QLabel("Import Geometry/Nurbs to be Duplicated:")
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

    def makeConnections(self):

        self.percentageGeneratedHorizontalSlider.valueChanged[int].connect(self.percentageChange)
        self.scaleHorizontalSlider.valueChanged[int].connect(self.scaleChange)
        self.minRandomizedScaleValueHorizontalSlider.valueChanged[int].connect(self.minRandomizedScaleChange)
        self.maxRandomizedScaleValueHorizontalSlider.valueChanged[int].connect(self.maxRandomizedScaleChange)
        self.minRandomizedRotationHorizontalSlider.valueChanged[int].connect(self.minRandomizedRotationChange)
        self.maxRandomizedRotationHorizontalSlider.valueChanged[int].connect(self.maxRandomizedRotationChange)

        self.randomizeAllRotationCheckBox.stateChanged.connect(
            self.checkAllRotationBoxState)

        #create geometry button
        self.createGeometryPushButton.clicked.connect(
            functools.partial(self.createGeometry))

        self.deleteLocatorsPushButton.clicked.connect(
            functools.partial(self.deleteLocators))

        self.browsePushButton.clicked.connect(self.findFile)

        self.importPushButton.clicked.connect(self.importFile)

    def initStateOfUI(self):
        self.nameOfSurfaceLineEdit.setPlaceholderText("Name of Geometry Here")
        self.percentageGeneratedHorizontalSlider.setValue(self.scaleValue)
        self.minScaleValue = int(round(float(self.minRandomizedScaleLineEdit.text())))
        self.maxScaleValue = int(round(float(self.maxRandomizedScaleLineEdit.text())))
        self.minRotationValue = int(round(float(self.minRandomizedRotationLineEdit.text())))
        self.maxRotationValue = int(round(float(self.maxRandomizedRotationLineEdit.text())))
        self.fileNameLineEdit.setPlaceholderText("Import File")

    def percentageChange(self, value):
        floatValue = float(value)
        self.percentageGeneratedLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def scaleChange(self, value):
        floatValue = float(value)
        self.scaleLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def minRandomizedScaleChange(self, value):
        floatValue = float(value)
        self.minRandomizedScaleLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def maxRandomizedScaleChange(self, value):
        floatValue = float(value)
        self.maxRandomizedScaleLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def minRandomizedRotationChange(self, value):
        floatValue = float(value)
        self.minRandomizedRotationLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue

    def maxRandomizedRotationChange(self, value):
        floatValue = float(value)
        self.maxRandomizedRotationLineEdit.setText(str(floatValue))
        self.scaleValue = floatValue


    def checkAllRotationBoxState(self):
        if self.randomizeAllRotationCheckBox.isChecked():
            self.randomizeRotateXCheckBox.click()
            self.randomizeRotateYCheckBox.click()
            self.randomizeRotateZCheckBox.click()


    def checkScaleBoxState(self):
        if self.randomizeScaleCheckBox.isChecked():
            self.randomizedScale = True
            self.setScaleMinMaxValues()
        else:
            self.randomizedScale = False
            

    def setScaleMinMaxValues(self):
        self.minScaleValue = int(round(float(self.minRandomizedScaleLineEdit.text())))
        self.maxScaleValue = int(round(float(self.maxRandomizedScaleLineEdit.text())))
        if (self.minScaleValue >= self.maxScaleValue):
            _logger.error("Minimum value must be smaller than maximum value.")
            return


    def checkRotationBoxesStates(self):
        if self.randomizeAllRotationCheckBox.isChecked():
            self.randomizedRotation = True
            self.setMinMaxRotationValues()

        elif self.randomizeRotateXCheckBox.isChecked():
            self.randomizeX = True
            self.setMinMaxRotationValues()

        elif self.randomizeRotateYCheckBox.isChecked():
            self.randomizeY = True
            self.setMinMaxRotationValues()

        elif self.randomizeRotateZCheckBox.isChecked():
            self.randomizeZ = True
            self.setMinMaxRotationValues()
            
        else:
            self.randomizedRotation = False
            self.randomizeX = False
            self.randomizeY = False
            self.randomizeZ = False


    def setMinMaxRotationValues(self):
        self.minRotationValue = int(round(float(self.minRandomizedRotationLineEdit.text())))
        self.maxRotationValue = int(round(float(self.maxRandomizedRotationLineEdit.text())))
        if (self.minRotationValue >= self.maxRotationValue):
            _logger.error("Minimum value must be smaller than maximum value.")
            return



    def createGeometry(self):
        name = self.nameOfSurfaceLineEdit.text()
        numberGenerated = float(self.percentageGeneratedLineEdit.text())/100.0
        scaleValue = float(self.scaleLineEdit.text())
        self.checkScaleBoxState()
        self.checkRotationBoxesStates()
        
        self.makeLocators(numberGenerated, name, scaleValue, self.randomizedScale, self.minScaleValue, self.maxScaleValue, 
            self.randomizedRotation, self.randomizeX, self.randomizeY, self.randomizeZ, self.minRotationValue, self.maxRotationValue)

    def deleteLocators(self):
        allVertexLocs = pm.ls('vertexLoc*')
        allFaceLocs = pm.ls('faceLoc*')
        pm.delete(allVertexLocs, allFaceLocs)


    def emptyScene(self):
        leafs = pm.ls(lf=True)
        pm.delete(leafs)


    def findFile(self):
        """ Browse to find a file """
        fileName = None
        dialog = QtGui.QFileDialog(directory = os.path.dirname(__file__))

        if dialog.exec_():
            fileName = dialog.selectedFiles()

        if fileName:
            self.fileNameLineEdit.setText(fileName[0])



    def importFile(self):
        fileToImport = self.fileNameLineEdit.text()
        mc.file(fileToImport, i=True, iv=True, mnc=False)


    @stopwatch
    def makeLocators(self, num= None, nameOfSurface = None, scaleOfItems = None, randomScale = None, minRandomScale = None, 
        maxRandomScale = None, randomRotation = None, randomX = None, randomY = None, 
        randomZ = None, minRandomRotation = None, maxRandomRotation = None):
        
        """ Function to place random locators on a given name
        
        makeLocators() takes 2 arguments- 
            num = a percentage between 0.0 and 1 for relative density of locators
            nameOfSurface = name of surface in the open Project, input as a String 
        Example Usage: makeLocators(0.1, "geo") <-- places locator over 
            surface "geo", with a 10% density
        
        """
        
        #Puts all geometry in the scene into a list
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
            """ Iterates through vertices on surface, attaches Locators 
            """
            
            #Selects all vertices, puts all vertice coordinates in a list
            pm.select(nameOfSurface)
            vs = pm.polyEvaluate(v=True)
            verts = [] 
            vertLocCount = 0 
            for i in range(0,vs):
                verts += (pm.pointPosition(nameOfSurface + '.vtx['+ str(i) + ']'))
            
            #Creates locators
            for v in verts: 
                numGen = r.random()
                if (numGen <= num):
                    vertsLocsNames = pm.spaceLocator(n="vertexLoc{0}".format(1), p=(v[0],v[1],v[2]))
                    duplicatedObject = pm.instance(selectedObject, leaf = True)
                    pm.setAttr(duplicatedObject[0] + '.translate', v[0], v[1] + scaleOfItems, v[2])
                    randomScaleNumber = r.randrange(minRandomScale, maxRandomScale)
                    randomRotationNumber = r.randrange(minRandomRotation, maxRandomRotation)
                    _logger.debug("random rotaion number: {0}".format(randomRotationNumber))

                    if randomScale == True:
                        pm.setAttr(duplicatedObject[0] + '.scale', (scaleOfItems * randomScaleNumber), (scaleOfItems * randomScaleNumber), (scaleOfItems * randomScaleNumber))

                    elif randomRotation == True:      
                        pm.setAttr(duplicatedObject[0] + '.rotate', randomRotationNumber, randomRotationNumber, randomRotationNumber)

                    elif randomX == True:
                        pm.setAttr(duplicatedObject[0] + '.rotateX', randomRotationNumber)

                    elif randomY == True:
                        pm.setAttr(duplicatedObject[0] + '.rotateY', randomRotationNumber)

                    elif randomZ == True:
                        pm.setAttr(duplicatedObject[0] + '.rotateZ', randomRotationNumber)
                    else:
                        pm.setAttr(duplicatedObject[0] + '.scale', scaleOfItems, scaleOfItems, scaleOfItems)
                        pm.setAttr(duplicatedObject[0] + '.rotate', 0,0,0)
                    
                    


                    vertLocCount += 1

            # pm.group(vertsLocsNames,duplicatedObject)

            totalVerts = round(float(vertLocCount)/vs*100.0, 2)
            _logger.debug("Generated " + str(vertLocCount) + " locators at vertices for " + str(vs) + " possible vertices. (" + str(totalVerts) + "%) ")
        
        
        def faceLocators():
            """ Iterates through faces on surface, attaches Locators 
            """
            
            #Selects all faces, puts average center coordinates in a list
            pm.select(nameOfSurface)
            fc = pm.polyEvaluate(face=True)
            faces = [] 
            faceLocCount=0
            for x in range(0, fc):
                numGen = r.random()
                bBox = pm.xform(nameOfSurface + '.f['+str(x)+']', ws=True, q=True, bb=True)
                transX = (bBox[0] + bBox[3])/2
                transY = (bBox[1] + bBox[4])/2
                transZ = (bBox[2] + bBox[5])/2
                
                #Creates locators
                if (numGen <= num):
                    faceLocsNames = pm.spaceLocator(n="faceLoc{0}".format(1), p=(transX, transY, transZ))
                    duplicatedObject = pm.instance(selectedObject, leaf=True)
                    pm.setAttr(duplicatedObject[0] + '.translate', transX, transY + scaleOfItems, transZ)
                    randomScaleNumber = r.randrange(minRandomScale, maxRandomScale)
                    randomRotationNumber = r.randrange(minRandomRotation, maxRandomRotation)
                    _logger.debug("random rotaion number: {0}".format(randomRotationNumber))

                    if randomScale == True:
                        pm.setAttr(duplicatedObject[0] + '.scale', (scaleOfItems * randomScaleNumber), (scaleOfItems * randomScaleNumber), (scaleOfItems * randomScaleNumber))

                    elif randomRotation == True:      
                        pm.setAttr(duplicatedObject[0] + '.rotate', randomRotationNumber, randomRotationNumber, randomRotationNumber)

                    elif randomX == True:
                        pm.setAttr(duplicatedObject[0] + '.rotateX', randomRotationNumber)

                    elif randomY == True:
                        pm.setAttr(duplicatedObject[0] + '.rotateY', randomRotationNumber)

                    elif randomZ == True:
                        pm.setAttr(duplicatedObject[0] + '.rotateZ', randomRotationNumber)
                    else:
                        pm.setAttr(duplicatedObject[0] + '.scale', scaleOfItems, scaleOfItems, scaleOfItems)
                        pm.setAttr(duplicatedObject[0] + '.rotate', 0,0,0)
                    
                    
                    faceLocCount += 1

            # pm.group(faceLocsNames,duplicatedObject)

            totalFace = round(float(faceLocCount)/fc*100.0, 2)
            _logger.debug("Generated " + str(faceLocCount) + " locators at faces for " + str(fc) + " possible surfaces.(" + str(totalFace) + "%) ")
                    
                    
        if (num < 0 or num > 1):
            _logger.error("Error. Please input a number between 1 and 100")
        elif (pm.objExists(nameOfSurface) == False):
            _logger.error("Error. Enter a name of a plane that exists in your project.")
        else:
            vertLocators()
            faceLocators()
        
            
            
    


    