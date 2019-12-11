@echo off
SET countdown=5
Set "RootDir=%~d0"
SET cwd=%cd%
SET project_folder=%RootDir%\CODING\atom_workspace\Python\static_template\python2-7_to_GUI\
rem SET out_name=
rem SET src_name=main.py
SET icon_name=res/prog_icon.ico
SET src_name=%~1
SET /p out_name=Out File Name: 
SET modules=%~2

echo %cwd%

SET command=python27 -m
SET p27=%RootDir%\CODING\Python\Python_2\
SET p27_scripts=%p27%\Scripts\
SET PATH=%project_folder%;%cwd%;%p27%;%p27_scripts%;%PATH%

PATH

echo Command Run : 
echo [ 
echo	pyinstaller --name %out_name% --icon %cwd%\%icon_name% --distpath exe --workpath tmp --specpath spec --paths=%modules% --onefile %src_name%
echo ]
echo.
echo.

IF NOT EXIST "export" (
	mkdir "export" && (
		echo Directory [export] created successfully
	) || (
		echo Directory [export] creation failed
	)
)

IF NOT EXIST "export/res/" (
	mkdir "export/res/" && (
		echo Directory [res] created successfully
	) || (
		echo Directory [res] creation failed
	)
)

IF NOT EXIST "export/log/" (
	mkdir "export/log/" && (
		echo Directory [log] created successfully
	) || (
		echo Directory [log] creation failed
	)
)

xcopy "%project_folder%\res\prog_icon.ico" "%cwd%\export\res\prog_icon.ico" && (
	echo Copy of File : [prog_icon.ico] from [%project_folder%\%icon_name%] to [%cwd%\export\res\] complete.
) || (
	echo Copy of File : [prog_icon.ico] from [%project_folder%\%icon_name%] to [%cwd%\export\res\] failed.
)

SET module_paths=
SET temporary=
SET /a counter=0
SET /a post_counter=0
rem tokens=Start from 1, get all items
rem delimiter=Space
for /f "tokens=1,* delims= " %%a IN ("%*") do (
	call SET temporary=%%b
)

SET replacement=
SET paths=
FOR %%q IN (%temporary%) do (
	set /a counter+=1
	IF NOT EXIST %%q (
		echo Directory [%%q] doesn't exist
	) ELSE (
		echo Counter: %counter%
		echo Post Counter: %post_counter%
		IF NOT %counter% == %post_counter% (
			echo Error : Directory [%%q] exist
			call SET paths=%%paths%%;%%q;
			rem Append %%q to the end of the existing variable
			set /a post_counter+=1
		) ELSE (
			call SET paths=%%paths%%%%q;
		)
	)
)
SET module_paths="%paths%"

rem FOR %%q IN (%*) do (
rem	IF NOT EXIST %%q (
rem		echo Directory [%%q] doesn't exist
rem		call SET module_paths=%%module_paths%% "%%q"
rem		rem Append %%q to the end of the existing variable
rem	) ELSE (
rem		echo Error : Directory [%%q] exist
rem	)
rem )

SET master_command=python27 -m PyInstaller --name %out_name% --icon "%cwd%\export\%icon_name%" --distpath "%cwd%\export\exe" --workpath "%cwd%\export\tmp" --specpath "%cwd%\export\spec" --path=%module_paths% --onefile %src_name%
echo %master_command%
%master_command% && (
	echo Success!
	rem for /L %%[variable_name] in (starting_value, increment_value, stop_value) Do [commands]
	for /L %%a in (1,1,%countdown%) Do (
		rem SLEEP 1 
		echo %%a
	)
) || (
	echo Error detected.
	pause
)

rem Go to executable
cd %cwd%
cd export\exe

echo =====================
%out_name% && (
	echo %out_name% complete
) || (
	
	echo %out_name% run error.
)
echo =====================

rem Return back to original
cd %cwd%