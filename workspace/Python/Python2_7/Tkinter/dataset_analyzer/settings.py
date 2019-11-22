"""
Documentation: ICT1002 Python Project - Settings.py
Module to contain all global variables that are used throughout the program
"""

import os
import sys

# Change which library to import depending on the Python version
if float(str(sys.version_info.major) + "." + str(sys.version_info.minor)) < 3.7:
    import Tkinter as tk
else:
    import tkinter as tk


def init():
    """ Initialize all global variables. Function will be called once before running the main app."""
    global data_set, HEIGHT, WIDTH, file_name1, file_name2, path, data_folder, color_set, grade_dict, cd

    # Set the window size here
    HEIGHT = 800
    WIDTH = 1400

    color_set = {
        "grey": "#56B6C2",
        "darkblue": "#282C34"
    }

    # List to contain the data from the data sets
    data_set = []

    # Dictionary to assign each grade to the tendering limit (SGD million)
    grade_dict = {"A1": float('inf'), "A2": 85, 'B1': 40, 'B2': 13.0, 'C1': 4.0, 'C2': 1.3, 'C3': 0.65,
                  "Single Grade": float('inf'), "L6": float('inf'), 'L5': 13.0, 'L4': 6.5, 'L3': 4.0,
                  'L2': 1.3, 'L1': 0.65}

    # Set the default file path if no file is specified

    cd = os.path.dirname(os.path.abspath(__file__))

    data_folder = cd + "\\" + "data" + "\\"

    file_name1 = "government-procurement-sample.csv"
    file_name2 = "registered-contractors-sample.csv"

    path = []
    path.append(data_folder + file_name1)
    path.append(data_folder + file_name2)
