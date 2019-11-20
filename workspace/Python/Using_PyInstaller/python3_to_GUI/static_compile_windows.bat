@echo off
SET countdown=5
SET cwd=%cd%
SET out_name=py2Tk
SET icon_name=res/prog_icon.ico
SET src_name=py2Tk.py

echo Command Run : 
echo [ 
echo	pyinstaller --name %out_name% --icon %cwd%\%icon_name% --distpath exe --workpath tmp --specpath spec --onefile %src_name%


echo ]
echo.
echo.

pyinstaller --name %out_name% --icon %cwd%\%icon_name% --distpath exe --workpath tmp --specpath spec --onefile %src_name% && (
	echo Success!
	rem for /L %%[variable_name] in (starting_value, increment_value, stop_value) Do [commands]
	for /L %%a in (1,1,%countdown%) Do SLEEP 1 && echo %%a
) || (
	echo Error detected.
	pause
)