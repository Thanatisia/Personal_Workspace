"""
Project Idea,Topic, Description

Name:
Version:
Language to Use: 
Idea:
Description:
Tags:
Features:

========
Design |
========
> Unified Modelling Language
> Use-Case Diagram
> Use-Case Description
> Use-Case Design
[Database]
> Database Design
  Database Name:
  Table Name:
  =======================================================================
  | column_Name | column_Type | Null_Type | Key_Type    | AUTOINCREMENT |
  =======================================================================
  | rowID       | INTEGER     | NOT NULL  | PRIMARY KEY | AUTOINCREMENT |
  |
  =======================================================================
"""
import sys
import os
import argparse
import time as t
import socket # for socket programming
import platform

## Global Variables ##
#[Compilation Mode]
# d : Debugging Mode 
# r : Release Mode
compile_mode = "d"
#[Permissions]
PERMISSION_USER_READ_OWNER_WRITE = 0o755 # Readable and Accessible by all users, write access only by owners
PERMISSION_READ_WRITE = 0o777 # Read and Write Permission to all users
#[global use]
gl_dir_seperator = "/"

# Environment Variables
cwd = os.getcwd()
ENV_VARIABLE_HOME = os.getenv("HOME")
OS_NAME = os.name

# Test import module variables
TEST_HOSTNAME = platform.node()

# System Details
HOSTNAME = socket.gethostname()

# Python Details
PY_VERSION_MAJOR = sys.version_info[0]
PY_VERSION_MINOR = sys.version_info[1]
PY_VERSION_FULL = float(str(PY_VERSION_MAJOR) + "." + str(PY_VERSION_MINOR))

# Path Appending #
sys.path.append(cwd + gl_dir_seperator) 
if OS_NAME == 'nt':
  sys.path.append("." + gl_dir_seperator)
else:
  sys.path.append("~" + gl_dir_seperator)

# External Modules


# Command Line Arguments #
all_args = sys.argv
all_args_size = len(all_args)
py_file_path = all_args[0]
argc = (all_args_size - 1)
argv = "Empty"
if argc < 1:
	argv = "Empty"
else:
	argv = all_args[1:]
	
def main():
	if compile_mode is "d":
		print(f"Mode [{compile_mode}] : Debugging")
	elif compile_mode is "r":
		print(f"Mode [{compile_mode}] : Release")
	else:
		print(f"Invalid Mode")
	
	for i in range(1):
		print("\n")
		
	print("Template")
	
if __name__ == "__main__":
	main()