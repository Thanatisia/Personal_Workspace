"""
Documentation: ICT1002 Python Project - Main.py
Contains the Application master class with the Start Page and runs the main app loop
"""
import Tkinter as tk
import analysis_page
import csv
import settings
import pprint
import tkFileDialog
from Tkinter import X
from Tkinter import Y
from Tkinter import BOTH

class Application (tk.Tk):
    """ The master Application class. All pages of the application will be based on this class. """
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """ Switches to a new page. Destroys current frame and replaces it with a new one. """
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def read_csv(self, _file_path):
        """ Reads a csv file and stores it in a dictionary list """
        settings.data_set = []
        for path in _file_path:
            with open(path) as f:
                reader = csv.reader(f, skipinitialspace=True)
                header = next(reader)
                settings.data_set.append([dict(zip(header, map(str, row))) for row in reader])

    def openfiledialog(self, _path_entry):
        """ Opens the file browser and insert the file path of the chosen file into the entry box. """
        _path_entry.delete(0, 'end')
        _path_entry.insert(0, tkFileDialog.askopenfilename(initialdir="/", title="Select csv file",
                                                           filetypes=(("csv files", "*.csv"), ("all files", "*.*"))))

    def set_dataset_path(self, mode, value):
        """ Sets a default file path if the file path is empty """
        if str(value) is not "":
            settings.path[mode-1] = value

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Sets the window size according to the screen resolution
        canvas = tk.Canvas(self, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())
        canvas.pack()

        frame = tk.Frame(canvas, bd=5, bg="#282C34")
        frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        instruction_label = tk.Label(frame, text="Enter the file path of data sets", font=50)
        instruction_label.place(relx=0, rely=0)

        path1_label = tk.Label(frame, text="Procurement Dataset:", font=40)
        path1_label.place(relx=0, rely=0.05)

        path1_entry = tk.Entry(frame)
        path1_entry.place(relx=0.2, rely=0.06, relwidth=0.5)

        file_dialog_button = tk.Button(frame, text="...", command=lambda: self.openfiledialog(path1_entry))
        file_dialog_button.place(relx=0.75, rely=0.06, relwidth=0.05)

        path2_label = tk.Label(frame, text="Contractors Dataset:", font=40)
        path2_label.place(relx=0, rely=0.1)

        path2_entry = tk.Entry(frame)
        path2_entry.place(relx=0.2, rely=0.11, relwidth=0.5)

        file_dialog_button = tk.Button(frame, text="...", command=lambda: self.openfiledialog(path2_entry))
        file_dialog_button.place(relx=0.75, rely=0.11, relwidth=0.05)

        confirm_button = tk.Button(frame, text="Confirm", command=lambda: [self.set_dataset_path(1, path1_entry.get()),
                                                                           self.set_dataset_path(2, path2_entry.get()),
                                                                           self.read_csv(settings.path),
                                                                           master.switch_frame(analysis_page.
                                                                                               AnalysisPage)])
        confirm_button.place(relx=0, rely=0.175, relwidth=0.2)


if __name__ == "__main__":
    settings.init()
    app = Application()
    app.title("Python Data Analyzer")
    app.state('zoomed')
    app.mainloop()
