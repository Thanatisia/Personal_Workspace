@echo off

rem Build Python 3.7

SET command=python37
SET module_name="%~1"
rem SET parameters="%~2"

SET run_command=%command% -m

rem Concatenate all parameters
FOR %%q IN (%*) do call SET run_command=%%run_command%% %%q

rem Original Command: %command% -m %module_name% %parameters% && (
%run_command% && (
  echo Build Success
) || (
  echo Build error
)