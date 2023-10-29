@echo off
cd %~dp0

:: master 최신화
git checkout master
echo.
git pull
echo.

echo 스크립트 생성
python .\ModGenerator\main.py
echo.

echo 폴더 이동해서 설치
python .\ModInstaller\main.py
echo.

:: 뭐라고 하는지 봐야지
pause
