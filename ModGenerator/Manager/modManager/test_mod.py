import pytest

from .mod import *


# 딱히 테스트 없이 일단 똑같이 실행
@pytest.mark.order(1)
def test_generateMod():
    GenerateMod()


# 당연히 템플릿의 파일 수와 결과 파일 수가 똑같아야 함
def test_checkFileCnt():
    templateCnt = GetTemplateTargetCnt()
    resultsCnt = GetResultsCnt()
    errMsg = "templateCnt: {0}, resultsCnt: {1}".format(templateCnt, resultsCnt)

    assert templateCnt == resultsCnt, errMsg


# 결과로 나온 모든 json 파일에 문제가 없어야 함
def test_checkJsonValidation():
    valid, filePath = CheckResultJson()
    errMsg = "invalid json detected: {0}".format(filePath)

    assert valid, errMsg
