@echo off
cd %~dp0

:: 설정 파일이 없으면 애초에 시작을 안 함
IF NOT EXIST config.ini (
	echo "config.ini" 파일이 있어야 함 [README.md 참고]
	pause
	exit
)

:: master 최신화
git checkout master
echo.
git pull
echo.

:: 스크립트 생성
python .\ModGenerator\main.py

:: 설정 파일 읽기
for /f "tokens=1,2 delims==" %%a in (config.ini) do (
    if %%a==diabloPath set %%a=%%b
    if %%a==modName set %%a=%%b
)

:: 생성된 스크립트 이동
echo %diabloPath%/mods/%modName%/%modName%.mpq/data 폴더에 모드 설치
move .\data %diabloPath%/mods/%modName%/%modName%.mpq/

:: 뭐라고 하는지 봐야지
echo.
pause
