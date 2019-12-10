@echo off

rem Build Python 2

SET command=python27
SET source_file="%~1"
SET parameters="%*"

SET run_command=%command%

rem Concatenate all parameters
FOR %%q IN (%*) do call SET run_command=%%run_command%% %%q

rem Original Command: %command% %source_file% %parameters% && (
%run_command% && (
  echo Build Success
) || (
  echo Build error
)
