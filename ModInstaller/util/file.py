import os
import sys
import json
import shutil


def InstallMod(configFileName, resultDir):
    destPath = getInstallPath(configFileName)
    srcPath = os.path.join(os.getcwd(), resultDir)
    if not os.path.exists(srcPath):
        sys.exit("mod result not exist")

    shutil.move(srcPath, destPath)


def getInstallPath(configFileName):
    absPath = os.path.join(os.getcwd(), configFileName)
    if not os.path.exists(absPath):
        sys.exit("config file does not exist")

    with open(absPath, "r") as file:
        try:
            jsonData = json.loads(file.read())
        except json.JSONDecodeError as err:
            errMsg = "invalid config json file - {0}".format(err.__str__())
            sys.exit(errMsg)

    basePath = jsonData["diabloPath"]
    modName = jsonData["modName"]

    return os.path.join(basePath, "mods", modName, modName + ".mpq")
