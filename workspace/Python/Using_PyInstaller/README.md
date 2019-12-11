# PyInstaller Conversion
  Pre-Requisites:

	1. Install PyInstaller Library
		
		In your Python, please use your appropriate pip modules to install PyInstaller via the following command:
			python3 -m pip install pyinstaller #For python 3
		or
			python2 -m pip install pyinstaller #For python 2


  Changes:
	     row_id - DateTime_of_update - Change_Type  - Changelog
		1   -   2019_11_20_2357  -   Update     - Updated PyInstaller batch file for Python2 - User to indicate path to Python2
		2   -   2019_11_20_2357  -   Update     - Updated PyInstaller batch file for Python3 - User to indicate path to Python3
		3   -	2019_12_11_1542	 - Modification - Modified folder, seperated to versions 01,02,03...


  Version Changelog Summary:
	v01 - Original - requires the use of template folder and the main in the same working directory as the batch file
	v02 - Modified - Put this folder into your path via either Environmental or via Programatically ( SET PATH=./path/to/batch/file.bat;%PATH%; ) and go to your project, 
				type [static_compile_windows_py37 <source_file_name> [ all external module paths if you used any - just leave empty if nothing ]


  Latest version: v02