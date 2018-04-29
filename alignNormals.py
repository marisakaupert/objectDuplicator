import logging
import random as r
import math
import os
import maya.cmds as mc
import pymel.core as pm
from pymel.all import *
from pymel.core.datatypes import Vector, Matrix, Point
import maya.OpenMaya as om


def makeLocators(self, num=None, nameOfSurface=None):

    """ Populates a given surface with objects.
        @param num: fl, percentage of geometry to be covered
        @param nameOfsurface: str, name given by user to determine the surface
    """

    selectedObject = pm.ls(sl=True)
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

                print(v)
                rotOrder = mc.getAttr(nameOfSurface + '.rotateOrder')
                pointOrigin = 0
                originalPosition = om.MVector(v)
                print(originalPosition)
                # poly = PyNode(nameOfSurface)
                # pos = [v[0], v[1], v[2]]
                # count = 0
                # for point in poly.getPoints('world'):
                #     if dt.Vector(point) == dt.Vector(pos):
                #         poly = PyNode(nameOfSurface + '.vtx[' + str(count) + ']')
                #         normalVector = poly.getNormal()
                #         print("normals: {0}".format(normalVector))
                #     count += 1

                vertLocCount += 1

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
            bBox = pm.xform(nameOfSurface + '.f['+str(x)+']', ws=True, q=True, bb=True)
            transX = (bBox[0] + bBox[3])/2
            transY = (bBox[1] + bBox[4])/2
            transZ = (bBox[2] + bBox[5])/2

            # Creates locators
            if (numGen <= num):
                pm.spaceLocator(n="faceLoc{0}".format(1), p=(transX, transY, transZ))
                duplicatedObject = pm.instance(selectedObject, leaf=True)
                pm.setAttr(duplicatedObject[0] + '.translate', transX, transY, transZ)

                poly = PyNode(nameOfSurface + '.f[' + str(x) + ']')
                normalVector = poly.getNormal()

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
