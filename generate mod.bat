@echo off
cd %~dp0

:: ���� ������ ������ ���ʿ� ������ �� ��
IF NOT EXIST config.ini (
	echo "config.ini" ������ �־�� �� [README.md ����]
	pause
	exit
)

:: master �ֽ�ȭ
git checkout master
echo.
git pull
echo.

:: ��ũ��Ʈ ����
python .\ModGenerator\main.py

:: ���� ���� �б�
for /f "tokens=1,2 delims==" %%a in (config.ini) do (
    if %%a==diabloPath set %%a=%%b
    if %%a==modName set %%a=%%b
)

:: ������ ��ũ��Ʈ �̵�
echo %diabloPath%/mods/%modName%/%modName%.mpq/data ������ ��� ��ġ
move .\data %diabloPath%/mods/%modName%/%modName%.mpq/

:: ����� �ϴ��� ������
echo.
pause
