@echo off
cd %~dp0

:: master �ֽ�ȭ
git checkout master
echo.
git pull
echo.

echo ��ũ��Ʈ ����
python .\ModGenerator\main.py
echo.

echo ���� �̵��ؼ� ��ġ
python .\ModInstaller\main.py
echo.

:: ����� �ϴ��� ������
pause
