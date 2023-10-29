import os
import sys
import json
import shutil


# 모드 설치하기
def InstallMod(configFileName, resultDir):
    dstPath = getInstallPath(configFileName)
    srcPath = os.path.join(os.getcwd(), resultDir)
    if not os.path.exists(srcPath):
        sys.exit("mod result not exist")

    moveAndOverwrite(srcPath, dstPath)


# 설치할 폴더 위치를 확인
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


# https://stackoverflow.com/questions/7419665/python-move-and-overwrite-files-and-folders
def moveAndOverwrite(srcPath, dstPath):
    firDirName = os.path.basename(srcPath)
    dstPath = os.path.join(dstPath, firDirName)

    for src_dir, dirs, files in os.walk(srcPath):
        dst_dir = src_dir.replace(srcPath, dstPath)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                # in case of the src and dst are the same file
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)
