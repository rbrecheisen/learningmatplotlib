@echo off
setlocal enabledelayedexpansion

REM === CONFIG ===
set APP_NAME=matplotlib
set ENTRYPOINT=src\projects\pyside6\main.py
set DIST_DIR=dist
set BUILD_DIR=build

REM Clean previous builds
if exist "%DIST_DIR%" rmdir /s /q "%DIST_DIR%"
if exist "%BUILD_DIR%" rmdir /s /q "%BUILD_DIR%"
if exist "%APP_NAME%.spec" del /q "%APP_NAME%.spec"

REM Build one-file exe
pyinstaller ^
  --name "%APP_NAME%" ^
  --onefile ^
  --windowed ^
  --clean ^
  --noconfirm ^
  --distpath "%DIST_DIR%" ^
  --workpath "%BUILD_DIR%" ^
  "%ENTRYPOINT%"

echo.
echo === Done. Output: %DIST_DIR%\%APP_NAME%.exe ===
endlocal
