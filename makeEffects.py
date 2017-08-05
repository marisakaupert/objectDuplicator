


"""this is myModule where I put my code. """

import logging
from collections import Counter
import maya.cmds as mc
import random as r
import time


import os
import functools
from PySide import QtGui, QtCore, QtUiTools
from shiboken import wrapInstance
# import pyside_dynamic
import maya.cmds as mc 
import maya.OpenMayaUI as omui 


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


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
    win = MakeEffects(parent=getMayaWindow())
    win.show()

def stopwatch(func):

    def timed (*args, **kwargs):

        #start a timer
        timeStart = time.time()
        #run original function
        result = func(*args, **kwargs)

        #stop a timer
        timeEnd = time.time()
        elapsedTime = timeEnd - timeStart
        logger.debug("%2.2f sec" %(elapsedTime))
        #print the amount of time it took
        return result

    return timed




class MakeEffects(QtGui.QDialog):
    """ This is the main class of this module """

    def __init__(self, parent=None):
        super(MakeEffects,self).__init__(parent)


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

        self.numberGeneratedLabel = QtGui.QLabel("Percentage Generated (must be between 1 and 10): ")

        self.horizontalLayout_2.addWidget(self.numberGeneratedLabel)
        self.numberGeneratedLCDNumber = QtGui.QLCDNumber()

        self.horizontalLayout_2.addWidget(self.numberGeneratedLCDNumber)
        self.numberGeneratedHorizontalSlider = QtGui.QSlider()
        self.numberGeneratedHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.numberGeneratedHorizontalSlider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)

        self.scaleLabel = QtGui.QLabel("Scale (must be between 1 and 10): ")

        self.horizontalLayout_4.addWidget(self.scaleLabel)
        self.scaleLCDNumber = QtGui.QLCDNumber()

        self.horizontalLayout_4.addWidget(self.scaleLCDNumber)
        self.scaleHorizontalSlider = QtGui.QSlider()
        self.scaleHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.scaleHorizontalSlider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)

        self.randomizeScaleCheckBox = QtGui.QCheckBox("Randomize Scale")

        self.horizontalLayout_5.addWidget(self.randomizeScaleCheckBox)
        self.activateSurfaceRotationCheckBox = QtGui.QCheckBox("Activate Surface Rotation")

        self.horizontalLayout_5.addWidget(self.activateSurfaceRotationCheckBox)
        self.turnOffRandomizedRotationCheckBox = QtGui.QCheckBox("Turn Off Randomized Rotation")

        self.horizontalLayout_5.addWidget(self.turnOffRandomizedRotationCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)

        self.minRandomizedScaleValueLabel = QtGui.QLabel("Minimum Scale: ")

        self.horizontalLayout_3.addWidget(self.minRandomizedScaleValueLabel)
        self.minRandomizedScaleValueLcdNumber = QtGui.QLCDNumber()

        self.horizontalLayout_3.addWidget(self.minRandomizedScaleValueLcdNumber)
        self.minRandomizedScaleValueHorizontalSlider = QtGui.QSlider()
        self.minRandomizedScaleValueHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.minRandomizedScaleValueHorizontalSlider)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)

        self.maxRandomizedScaleValueLabel = QtGui.QLabel("Maximum Scale: ")

        self.horizontalLayout_6.addWidget(self.maxRandomizedScaleValueLabel)
        self.maxRandomizedScaleValueLcdNumber = QtGui.QLCDNumber()

        self.horizontalLayout_6.addWidget(self.maxRandomizedScaleValueLcdNumber)
        self.maxRandomizedScaleValueHorizontalSlider = QtGui.QSlider()
        self.maxRandomizedScaleValueHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.maxRandomizedScaleValueHorizontalSlider)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.createGeometryPushButton = QtGui.QPushButton("Create Locators and Geometry")

        self.verticalLayout.addWidget(self.createGeometryPushButton)
        self.deleteLocatorsPushButton = QtGui.QPushButton("Delete Locators")

        self.verticalLayout.addWidget(self.deleteLocatorsPushButton)
        self.emptyScenePushButton = QtGui.QPushButton("Empty Scene")

        self.verticalLayout.addWidget(self.emptyScenePushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)

        self.itemsCreatedLabel = QtGui.QLabel("Items Created: ")

        self.verticalLayout_3.addWidget(self.itemsCreatedLabel)
        self.itemsCreatedTextEdit = QtGui.QTextEdit()

        self.verticalLayout_3.addWidget(self.itemsCreatedTextEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.makeConnections()
        self.initStateOfUI()
        self.setWindowTitle("Make Effects")
        self.setLayout(self.gridLayout)
        self.show()

    def makeConnections(self):

        #number Generated Slider
        self.numberGeneratedHorizontalSlider.valueChanged.connect(self.numberGeneratedLCDNumber.display)

        #scale slider
        self.scaleHorizontalSlider.valueChanged.connect(self.scaleLCDNumber.display)

        #create geometry button
        self.createGeometryPushButton.clicked.connect(
            functools.partial(self.createGeometry))

        self.emptyScenePushButton.clicked.connect(
            functools.partial(self.emptyScene))

    def createGeometry(self):
        numberGenerated = self.numberGeneratedLCDNumber.value()

        name = self.nameOfSurfaceLineEdit.text()

        randomizedScale = False

        scaleValue = self.scaleLCDNumber.value()

        randomizedRotation = True
        

        if self.randomizeScaleCheckBox.isChecked():
            randomizedScale = True
        else:
            randomizedScale = False

        if self.turnOffRandomizedRotationCheckBox.isChecked():
            randomizedRotation = False
        else:
            randomizedRotation = True
        
        self.makeLocators(numberGenerated,name,scaleValue,randomizedScale, randomizedRotation)



    def emptyScene(self):
        # mc.delete(all=True)
        self.itemsCreatedTextEdit.clear()

        # self.itemsCreatedTextEdit.append(listOfItemsMade)



    def initStateOfUI(self):
        self.nameOfSurfaceLineEdit.setPlaceholderText("Name of Geometry Here")

        self.numberGeneratedLCDNumber.display(1)

        self.scaleLCDNumber.display(1)
        self.minRandomizedScaleValueLcdNumber.display(1)
        self.maxRandomizedScaleValueLcdNumber.display(1)







    @stopwatch
    def makeLocators(self, num, nameOfSurface, scaleOfItems, randomScale, randomRotation):
        
        """ Function to place random locators on a given name
        
        makeLocators() takes 2 arguments- 
            num = a percentage between 0.0 and 1 for relative density of locators
            nameOfSurface = name of surface in the open Project, input as a String 
        Example Usage: makeLocators(0.1, "geo") <-- places locator over 
            surface "geo", with a 10% density
        
        """
        
        #Puts all geometry in the scene into a list
        selectedObject = mc.ls(sl=True)
        sizeOfSelectedObject = int(mc.getAttr(selectedObject[0] + '.scaleY'))
        boundingBox = mc.exactWorldBoundingBox(selectedObject)
        bottom = [(boundingBox[0] + boundingBox[3])/2, boundingBox[1], (boundingBox[2] + boundingBox[5])/2]
        mc.xform(selectedObject, piv=bottom, ws=True)
        mc.select(nameOfSurface)
        mc.select(selectedObject, add=True)
        mc.parentConstraint(nameOfSurface, selectedObject, mo=False)
        mc.delete(selectedObject, cn=True)

        


        def vertLocators():
            """ Iterates through vertices on surface, attaches Locators """
            
            #Selects all vertices, puts all vertice coordinates in a list
            mc.select(nameOfSurface)
            vs = mc.polyEvaluate(v=True)
            verts = [] 
            vertLocCount = 0 
            for i in range(0,vs):
                verts += (mc.pointPosition(nameOfSurface + '.vtx['+ str(i) + ']'), )
            
            #Creates locators
            for v in verts: 
                numGen = r.random() * 10
                if (numGen <= num):
                    vertsLocsNames = mc.spaceLocator(n="vertexLoc{0}".format(1), p=(v[0],v[1],v[2]))
                    self.itemsCreatedTextEdit.append(vertsLocsNames[0])
                    duplicatedObject = mc.instance(selectedObject, leaf = True)
                    self.itemsCreatedTextEdit.append(duplicatedObject[0])
                    self.itemsCreatedTextEdit.setReadOnly(True)


                    mc.setAttr(duplicatedObject[0] + '.translate', v[0], v[1] + scaleOfItems, v[2])

                    if (randomScale == True):
                        mc.setAttr(duplicatedObject[0] + '.scale', (scaleOfItems * numGen), (scaleOfItems * numGen), (scaleOfItems * numGen))
                    else:
                        mc.setAttr(duplicatedObject[0] + '.scale', scaleOfItems, scaleOfItems, scaleOfItems)

                    if randomRotation == False:
                        mc.setAttr(duplicatedObject[0] + '.rotateY', 0)
                    else:
                        mc.setAttr(duplicatedObject[0] + '.rotateY', (numGen * 100))


                    vertLocCount += 1

            # mc.group(vertsLocsNames,duplicatedObject)

            totalVerts = round(float(vertLocCount)/vs*100.0, 2)
            print("Generated " + str(vertLocCount) + " locators at vertices for " + str(vs) + " possible vertices. (" + str(totalVerts) + "%) ")
        
        
        def faceLocators():
            """ Iterates through faces on surface, attaches Locators """
            
            #Selects all faces, puts average center coordinates in a list
            mc.select(nameOfSurface)
            fc = mc.polyEvaluate(face=True)
            faces = [] 
            faceLocCount=0
            for x in range(0, fc):
                numGen = r.random() * 10
                bBox = mc.xform(nameOfSurface + '.f['+str(x)+']', ws=True, q=True, bb=True)
                transX = (bBox[0] + bBox[3])/2
                transY = (bBox[1] + bBox[4])/2
                transZ = (bBox[2] + bBox[5])/2
                
                #Creates locators
                if (numGen <= num):
                    faceLocsNames = mc.spaceLocator(n="faceLoc{0}".format(1), p=(transX, transY, transZ))
                    self.itemsCreatedTextEdit.append(faceLocsNames[0])
                    duplicatedObject = mc.instance(selectedObject, leaf=True)
                    self.itemsCreatedTextEdit.append(duplicatedObject[0])
                    self.itemsCreatedTextEdit.setReadOnly(True)

                    mc.setAttr(duplicatedObject[0] + '.translate', transX, transY + scaleOfItems, transZ)

                    if (randomScale == True):
                        mc.setAttr(duplicatedObject[0] + '.scale', (scaleOfItems * numGen), (scaleOfItems * numGen), (scaleOfItems * numGen))
                    else:
                        mc.setAttr(duplicatedObject[0] + '.scale', scaleOfItems, scaleOfItems, scaleOfItems)

                    if randomRotation == False:
                        mc.setAttr(duplicatedObject[0] + '.rotateY', 0)
                    else:
                        mc.setAttr(duplicatedObject[0] + '.rotateY', (numGen * 100))

                    
                    faceLocCount += 1

            # mc.group(faceLocsNames,duplicatedObject)

            totalFace = round(float(faceLocCount)/fc*100.0, 2)
            print("Generated " + str(faceLocCount) + " locators at faces for " + str(fc) + " possible surfaces.(" + str(totalFace) + "%) ")
                    
                    
        if (num < 1 or num > 10):
            print("Error. Please input a number between 1 and 10")
        elif (mc.objExists(nameOfSurface) == False):
            print("Error. Enter a name of a plane that exists in your project.")
        else:
            vertLocators()
            faceLocators()
        
            
            
    


    