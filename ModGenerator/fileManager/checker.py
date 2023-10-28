import os
import json

from .path import *


def getElementCnt(absPath):
    cnt = 0

    for element in os.listdir(absPath):
        elementAbsPath = os.path.join(absPath, element)
        if os.path.isdir(elementAbsPath):
            cnt += getElementCnt(elementAbsPath)
        else:
            cnt += 1

    return cnt


def GetTemplateTargetCnt():
    absPath = os.path.join(os.getcwd(), TEMPLATE_DIR + "targets/")
    return getElementCnt(absPath)


def GetResultsCnt():
    absPath = os.path.join(os.getcwd(), RESULT_DIR)
    return getElementCnt(absPath)


def CheckResultJson():
    absPath = os.path.join(os.getcwd(), RESULT_DIR)
    valid, filePath = checkJsonValidation(absPath)

    return valid, filePath


def checkJsonValidation(absPath):
    for element in os.listdir(absPath):
        elementAbsPath = os.path.join(absPath, element)
        if os.path.isdir(elementAbsPath):
            valid, filePath = checkJsonValidation(elementAbsPath)
            if not valid:
                return False, filePath
            else:
                continue

        # json 파일만 검사
        _, extension = os.path.splitext(element)
        if extension != ".json":
            continue

        with open(elementAbsPath, 'r') as file:
            try:
                json.loads(file.read())
            except ValueError:
                return False, element

    return True, ""
