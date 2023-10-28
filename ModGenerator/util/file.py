import os


TEMPLATE_DIR = "ModGenerator/template/"


# 특정 엔티티 내용을 전부 읽고 한줄로 반환
def ReadEntityTemplate(entityName):
    relativePath = TEMPLATE_DIR + "entity/" + entityName + ".txt"
    absPath = os.path.join(os.getcwd(), relativePath)

    with open(absPath, "r") as file:
        fileLines = file.readlines()

    return ''.join(fileLines)


# 목표가 되는 템플릿 파일 각각에 대해 스크립트를 삽입해서 새로운 폴더에 생성
def CreateModFiles(scriptStr):
    baseAbsPath = os.path.join(os.getcwd(), TEMPLATE_DIR + "targets/")
    resultAbsPath = os.path.join(os.getcwd(), "results/")

    createAllModFile(baseAbsPath, "", scriptStr, resultAbsPath)


# dirPath 폴더의 모든 json에 대하여 스크립트를 끼워넣기
def createAllModFile(baseAbsPath, relativePath, scriptStr, resultAbsPath):
    dirAbsPath = os.path.join(baseAbsPath, relativePath)
    for element in os.listdir(dirAbsPath):
        elementRelativePath = os.path.join(relativePath, element)

        # 폴더면 재귀적으로 계속 진행
        elementAbsPath = os.path.join(dirAbsPath, element)
        if os.path.isdir(elementAbsPath):
            createAllModFile(baseAbsPath, elementRelativePath, scriptStr, resultAbsPath)
            continue
            
        # json 파일만 스크립트 진행
        _, extension = os.path.splitext(element)
        if extension != ".json":
            continue

        createOneModFile(baseAbsPath, elementRelativePath, scriptStr, resultAbsPath)


# 해당 파일의 내용에 스크립트 끼워서 새롭게 파일 생성
def createOneModFile(baseAbsPath, relativePath, scriptStr, resultAbsPath):
    absPath = os.path.join(baseAbsPath, relativePath)

    # 기본 디아 모드 파일은 모두 1줄 짜리임
    with open(absPath, "r") as file:
        fileLine = file.readline()

    # 마지막 "]}" 이거 앞에 스크립트 넣으면 됨
    modFileLine = fileLine[:-2] + scriptStr + fileLine[-2:]

    # 폴더 상대경로가 유지 되도록 알맞게 생성
    resultFileAbsPath = os.path.join(resultAbsPath, relativePath)
    dirName = os.path.dirname(resultFileAbsPath)
    os.makedirs(dirName, exist_ok=True)

    with open(resultFileAbsPath, "w") as file:
        file.write(modFileLine)
