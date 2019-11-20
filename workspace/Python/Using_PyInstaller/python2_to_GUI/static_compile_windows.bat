@echo off
SET countdown=5
Set "RootDir=%~d0"
SET cwd=%cd%
rem SET out_name=
rem SET src_name=main.py
SET icon_name=res/prog_icon.ico
SET src_name=%~1
SET /p out_name=Out File Name: 

SET p2=%RootDir%\CODING\Python\Python_2\
SET p2_scripts=%p2%\Scripts\
SET PATH=%p2%;%p2_scripts%;%PATH%

PATH

echo Command Run : 
echo [ 
echo	pyinstaller --name %out_name% --icon %cwd%\%icon_name% --distpath exe --workpath tmp --specpath spec --onefile %src_name%
echo ]
echo.
echo.

python_2 -m PyInstaller --name %out_name% --icon %cwd%\%icon_name% --distpath exe --workpath tmp --specpath spec --onefile %src_name% && (
	echo Success!
	rem for /L %%[variable_name] in (starting_value, increment_value, stop_value) Do [commands]
	for /L %%a in (1,1,%countdown%) Do SLEEP 1 && echo %%a
) || (
	echo Error detected.
	pause
)