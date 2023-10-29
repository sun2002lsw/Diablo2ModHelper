import os
import shutil

from util import InstallMod

configFile = "config.json"
resultDir = "data"

# resultDir 폴더의 내용물을 configFile에 정의된 목적지로 옮기기
InstallMod(configFile, resultDir)

# 깡통 폴더만 남은거 삭제
shutil.rmtree(os.path.join(os.getcwd(), resultDir))
