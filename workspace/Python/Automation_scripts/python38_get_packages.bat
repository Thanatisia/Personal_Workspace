@echo off

rem Build Python 3.8

SET command=python38
SET module_name="%~1"
rem SET parameters="%~2"

SET run_command=%command% -m pip list

echo ===========================
%run_command% && (
	echo List complete
) || (
	echo %command% is not installed
)
echo ===========================