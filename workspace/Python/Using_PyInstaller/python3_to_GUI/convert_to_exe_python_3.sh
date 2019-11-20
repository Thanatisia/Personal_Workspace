shell_path=$0
target_file=$1

./pyinstaller_python3 --distpath exe --workpath tmp --specpath spec --onefile $target_file

