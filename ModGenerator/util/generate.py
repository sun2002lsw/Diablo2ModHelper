import math

from .file import ReadEntityTemplate


# 뭔가 엄청난 방법으로 길찾기 가이드를 그려줌
def GeneratePathGuideScript():
    circle1 = drawEntityCircle("quest_alert", 200)
    circle2 = drawEntityCircle("quest_alert", 125)
    circle3 = drawEntityCircle("quest_alert", 50)

    # alert 엔티티로 3개의 원을 그려서 가이드
    return circle1 + circle2 + circle3


# circleSize 크기에 해당하는 원형으로 entity를 찍어냄
def drawEntityCircle(entityName, circleSize):
    circleSizeSquare = circleSize * circleSize
    entityTemplate = ReadEntityTemplate(entityName)
    circle = ""

    # 엔티티 간격이 너무 조밀해서, step을 3으로 지정
    for xPos in range(-circleSize, circleSize + 1, 3):
        zPos = math.sqrt(circleSizeSquare - xPos * xPos)

        circle += drawEntityPoint(entityTemplate, xPos, zPos)
        if zPos != 0:
            circle += drawEntityPoint(entityTemplate, xPos, -zPos)

    return circle


# 해당 포인트에 entity 하나를 찍어냄
def drawEntityPoint(entityTemplate, xPos, zPos):
    xPos = round(xPos, 1)
    zPos = round(zPos, 1)

    entityTemplate = entityTemplate.replace("xPos", str(xPos))
    entityTemplate = entityTemplate.replace("zPos", str(zPos))
    entityTemplate = entityTemplate.replace("yPos", "5")  # 높이는 5로 고정

    return entityTemplate
