@echo off
cd %~dp0

IF EXIST config.ini (
) ELSE (
	echo "config.ini" 파일이 있어야 함 (README.md 참고)
	pause
	exist
)

# 변경 사항 다 버리고 master 최신화
git checkout master
echo.
git pull
echo.
git reset --hard origin/master
echo.

# 스크립트 생성
python .\ModGenerator\main.py

# 설정 파일 읽기
for /f "tokens=1,2 delims==" %%a in (config.ini) do (
    if %%a==diabloPath set %%a=%%b
    if %%a==modName set %%a=%%b
)

# 생성된 스크립트 이동
move .\data %diabloPath%/mods/%modName%/%modName%.mpq/
