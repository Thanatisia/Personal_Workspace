
chmod +x "convert_to_exe.sh"

./pyinstaller --distpath exe --workpath tmp --specpath spec --onefile proj_Manager.py

