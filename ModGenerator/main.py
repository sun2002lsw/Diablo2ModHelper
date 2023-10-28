from ModGenerator.fileManager import *
from ModGenerator.scriptManager import *


# 이전에 만들었던 모드는 지우고, 새롭게 모드를 생성
def GenerateMod():
    CleanResults()

    pathGuideScript = GeneratePathGuideScript()
    CreateModFiles(pathGuideScript)


# main
GenerateMod()
