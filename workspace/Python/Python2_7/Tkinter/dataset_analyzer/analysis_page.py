"""
Documentation: ICT1002 Python Project - Analysis.py
Contains the analysis page and all related functions.
"""

import os
import sys
import Tkinter as tk
import main
import settings
import ttk
from Tkinter import TOP
from Tkinter import BOTTOM
from Tkinter import LEFT
from Tkinter import RIGHT
from Tkinter import X
from Tkinter import Y
from Tkinter import BOTH
from Tkinter import INSIDE
from Tkinter import OUTSIDE
from Tkinter import Frame
from Tkinter import Label
from Tkinter import Canvas
import tkMessageBox
from ttk import Entry
import datetime
from datetime import datetime
from datetime import date


class AnalysisPage(tk.Frame):

    def sort_col(self, col_name, list1, order=False, tree_list=None):
        """ Sorts a column in the treeview in ascending/descending order."""

        # Sort the given list
        list1.sort(key=lambda x: float(x.get(col_name)), reverse=order)

        # Insert sorted data into the treeview
        tree_list[0].delete(*tree_list[0].get_children())
        counter = 0
        for i in list1:
            test2 = []
            for x in i:
                test2.append(i.get(x))
                test2[-1] = test2[-1].decode('utf8', 'ignore')
            tree_list[0].insert("", 0, text=counter, values=test2, tags=['blue_fg'])
            counter += 1

    def get_award_year(self, tree_list=None, _year=2015):
        """ Displays all the procurements in a specified year """

        tree_list[0].delete(*tree_list[0].get_children())
        counter = 0

        # Sort the list by award_date before looping through it
        for i in sorted(settings.data_set[0], key=lambda x: datetime.strptime(x['award_date'], '%Y-%m-%d'),
                        reverse=True):
            award_date = i.get('award_date')
            award_year = datetime.strptime(award_date, '%Y-%m-%d').year

            test2 = []
            for x in i:
                test2.append(i.get(x))
                test2[-1] = test2[-1].decode('utf8', 'ignore')

            # Check if award_date matches with the input year
            if award_year == _year:
                tree_list[0].insert("", 0, text=counter, values=test2, tags=['blue_fg'])
                counter += 1

    def list_company_from_keyword(self, tree_list=None, keyword=None):
        """ Display a list of companies with names that matches the search term """
        tree_list[1].delete(*tree_list[1].get_children())
        given_word = keyword
        counter = 0
        for a in settings.data_set[1]:
            test2 = []
            company_check = a.get('company_name')

            for x in a:
                test2.append(a.get(x))
                test2[-1] = test2[-1].decode('utf8', 'ignore')
            try:
                # Check if search term is in company_name
                if given_word.lower() in company_check.lower():
                    tree_list[1].insert("", 0, text=counter, values=test2, tags=['blue_fg'])
                    counter += 1
            except Exception as e:
                print e

    def get_company_by_uen(self, tree_list=None, uen_number=None):
        """ Display a list of companies with UEN that matches the search term """
        given_number = uen_number
        tree_list[1].delete(*tree_list[1].get_children())
        counter = 0
        for a in settings.data_set[1]:
            test2 = []
            uen_check = a.get('uen_no')
            for x in a:
                test2.append(a.get(x))
                test2[-1] = test2[-1].decode('utf8', 'ignore')
            try:
                # Check if user input matches with the UEN
                if given_number == uen_check:
                    tree_list[1].insert("", 0, text=counter, values=test2, tags=['blue_fg'])
                    counter += 1
            except Exception as e:
                print e

    def get_procurement_by_cat(self, mainframe):
        """ Categorise the procurements and list along with the procurement amount """
        agency_list = {}
        # declare the key before hand
        educationkey = ['School', 'Education', 'Polytechnic', 'College', 'University', 'SCHOOL', 'Examinations',
                        'Institute']
        financekey = ['Finance', 'Accounting', 'Monetary']
        defencekey = ['Defence']
        # to store the data later on
        education = {}
        finance = {}
        defence = {}
        others = {}
        catmain = {'Education': 0, 'Finance': 0, 'Defence': 0, 'Others': 0}
        # the 4 main cateogry that it is being sort in to
        # the first for loop get the agency name and the awarded amt
        for d in settings.data_set[0]:
            if d.get('awarded_amt').isdigit():
                if d.get('agency') in agency_list:
                    agency_list[d.get('agency')] += float(d.get('awarded_amt'))
                else:
                    agency_list[d.get('agency')] = float(d.get('awarded_amt'))

        # the 2nd for loop search the agency name if the matches the key
        for k, v in agency_list.items():
            if any(a in k for a in educationkey):
                education[k] = v
            elif any(a in k for a in financekey):
                finance[k] = v
            elif any(a in k for a in defencekey):
                defence[k] = v
            else:
                others[k] = v
        # combining them into 1 dictonary and adding the awarded amt tgt
        catmain['Education'] = sum(education.values())
        catmain['Finance'] = sum(finance.values())
        catmain['Defence'] = sum(defence.values())
        catmain['Others'] = sum(others.values())

        # This will make sure that user has to close this window before user can interact with the main frame
        display_category_and_procurement_amount_root = tk.Toplevel(mainframe)
        display_category_and_procurement_amount_root.grab_set()

        display_category_and_procurement_amount_root.minsize(width=settings.WIDTH / 2, height=settings.HEIGHT / 2)
        canvas = Canvas(display_category_and_procurement_amount_root, width=settings.WIDTH, height=settings.HEIGHT)
        canvas.pack(fill=BOTH, expand=True)

        frame = Frame(canvas, bd=5, bg="#282C34")
        frame.pack(fill=BOTH, expand=True)
        display_category_and_procurement_amount_root.title("Category and Procurement Amount")
        tree_display_category_and_procurement = ttk.Treeview(frame)

        # Set Vertical Scrollbar to the Trees
        tree_scrollbar_vertical = ttk.Scrollbar(tree_display_category_and_procurement, orient='vertical',
                                                command=tree_display_category_and_procurement.yview)
        tree_scrollbar_horizontal = ttk.Scrollbar(tree_display_category_and_procurement, orient='horizontal',
                                                  command=tree_display_category_and_procurement.xview)
        # tree_scrollbar_vertical.pack(side=RIGHT, fill=Y)
        tree_scrollbar_vertical.pack(side=RIGHT, fill=Y)
        tree_scrollbar_horizontal.pack(side=BOTTOM, fill=X)
        tree_display_category_and_procurement.configure(xscrollcommand=tree_scrollbar_horizontal.set,
                                                        yscrollcommand=tree_scrollbar_vertical.set)

        heading_list = ['Category', 'Total Procurement Amount']
        tree_display_category_and_procurement["columns"] = heading_list
        tree_display_category_and_procurement['show'] = 'headings'
        for x in range(0, len(heading_list)):
            tree_display_category_and_procurement.heading(heading_list[x], text=heading_list[x])
        for x in catmain:
            value_list = [x, catmain.get(x)]
            tree_display_category_and_procurement.insert("", 0, values=value_list)
        tree_display_category_and_procurement.pack(fill=BOTH, expand=True)

        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))

        for col in heading_list:
            tree_display_category_and_procurement.heading(col, text=col,command=lambda _col=col: treeview_sort_column(tree_display_category_and_procurement, _col, False))


    def get_agency(self, mainframe):
        """ Display the list of all agencies along with the procurement amount"""

        # This will make sure that user has to close this window before user can interact with the main frame
        display_category_and_procurement_amount_root = tk.Toplevel(mainframe)
        display_category_and_procurement_amount_root.grab_set()

        display_category_and_procurement_amount_root.minsize(width=settings.WIDTH / 2, height=settings.HEIGHT / 2)
        canvas = Canvas(display_category_and_procurement_amount_root, width=settings.WIDTH, height=settings.HEIGHT)
        canvas.pack(fill=BOTH, expand=True)

        frame = Frame(canvas, bd=5, bg="#282C34")
        frame.pack(fill=BOTH, expand=True)
        display_category_and_procurement_amount_root.title("Agency's Total Awarded Amount")
        tree_display_category_and_procurement = ttk.Treeview(frame)

        # Set Vertical Scrollbar to the Trees
        tree_scrollbar_vertical = ttk.Scrollbar(tree_display_category_and_procurement, orient='vertical',
                                                command=tree_display_category_and_procurement.yview)

        tree_scrollbar_vertical.pack(side=RIGHT, fill=Y)
        tree_display_category_and_procurement.configure(
            yscrollcommand=tree_scrollbar_vertical.set)

        heading_list = ['Agency', 'Total Procurement Amount']
        tree_display_category_and_procurement["columns"] = heading_list
        tree_display_category_and_procurement['show'] = 'headings'

        agency_list = {}
        for d in settings.data_set[0]:
            if d.get('agency') in agency_list:
                agency_list[d.get('agency')] += float(d.get('awarded_amt'))
            else:
                agency_list[d.get('agency')] = float(d.get('awarded_amt'))

        for x in range(0, len(heading_list)):
            tree_display_category_and_procurement.heading(heading_list[x], text=heading_list[x])
        for x in agency_list:
            value_list = [x, agency_list.get(x)]
            tree_display_category_and_procurement.insert("", 0, values=value_list)
        tree_display_category_and_procurement.pack(fill=BOTH, expand=True)

        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))

        for col in heading_list:
            tree_display_category_and_procurement.heading(col, text=col,command=lambda _col=col: treeview_sort_column(tree_display_category_and_procurement, _col, False))

    def get_awarded_contractors(self, tree_list=None):
        """Display the list of supplies that are also registered contractors"""
        tree_list[1].delete(*tree_list[1].get_children())
        supplier_list = []
        contractor_list = []
        counter = 1
        for i in settings.data_set[0]:
            supplier_list.append(i.get('supplier_name'))
        for i in settings.data_set[1]:
            contractor_list.append(i.get('company_name'))

        # Get the intersection of supplier_list and contractor_list
        output = list(set(supplier_list).intersection(contractor_list))

        for i in settings.data_set[1]:
            test2 = []
            for x in i:
                test2.append(i.get(x))
                test2[-1] = test2[-1].decode('utf8', 'ignore')
            for x in output:
                if x == i.get('company_name'):
                    tree_list[1].insert("", 0, text=counter, values=test2, tags=['blue_fg'])
                    counter += 1

    def get_top_contractors(self, mainframe, n=0):
        """
        List the top contractors based on procurement amount.
        n is the number of contractors that will be listed.
        """
        contractor_dict = {}

        for i in settings.data_set[0]:
            contractor = i.get('supplier_name')

            try:
                awarded_amt = float(i.get('awarded_amt'))
            except ValueError:
                awarded_amt = 0.0

            # Add the contractor to the dict if an entry doesn't exist. If not increment the awarded_amt
            if contractor not in contractor_dict:
                contractor_dict[contractor] = awarded_amt
            else:
                contractor_dict[contractor] += awarded_amt

        # This will make sure that user has to close this window before user can interact with the main frame
        display_supplier_name_to_awarded_amount_root = tk.Toplevel(mainframe)
        display_supplier_name_to_awarded_amount_root.grab_set()

        display_supplier_name_to_awarded_amount_root.minsize(width=settings.WIDTH / 2, height=settings.HEIGHT / 2)
        canvas = Canvas(display_supplier_name_to_awarded_amount_root, width=settings.WIDTH, height=settings.HEIGHT)
        canvas.pack(fill=BOTH, expand=True)

        frame = Frame(canvas, bd=5, bg="#282C34")
        frame.pack(fill=BOTH, expand=True)
        display_supplier_name_to_awarded_amount_root.title("Top Contractors List")
        tree_supplier_name_to_awarded_amount = ttk.Treeview(frame)

        # Set Vertical Scrollbar to the Trees
        tree_scrollbar_vertical = ttk.Scrollbar(tree_supplier_name_to_awarded_amount, orient='vertical',
                                                command=tree_supplier_name_to_awarded_amount.yview)
        tree_scrollbar_vertical.pack(side=RIGHT, fill=Y)
        tree_supplier_name_to_awarded_amount.configure(yscrollcommand=tree_scrollbar_vertical.set)

        heading_list = ['Contractor', 'Total Awarded Amount']
        tree_supplier_name_to_awarded_amount["columns"] = heading_list
        tree_supplier_name_to_awarded_amount['show'] = 'headings'
        for x in range(0, len(heading_list)):
            tree_supplier_name_to_awarded_amount.heading(heading_list[x], text=heading_list[x])
        sorted_list = sorted(contractor_dict, key=contractor_dict.get,
                             reverse=True)  # list of key according to most awarded amount
        topNlist = sorted_list[:n]  # Get the top N number contractor's key
        for key in reversed(topNlist):  # reversed because tree insert in reversed order
            value_list = []
            value_list.append(key)
            value_list.append(contractor_dict[key])
            tree_supplier_name_to_awarded_amount.insert("", 0, values=value_list)
        tree_supplier_name_to_awarded_amount.pack(fill=BOTH, expand=True)

    def get_qualified_contractors(self, _procurement, tree_list=None):
        """List the contractors that can bid for a tender with a specified procurement amount"""
        tree_list[1].delete(*tree_list[1].get_children())
        counter = 1
        try:
            _procurement = float(_procurement)
        except ValueError:
            tkMessageBox.showwarning("Wrong data type", "Please enter either a float or an integer value")
            return
        contractors_list = []
        for i in settings.data_set[1]:
            test2 = []
            tender_limit = settings.grade_dict[i.get('grade')]  # Get the tendering limit of the contractor based on its grade
            for x in i:
                test2.append(i.get(x))
                test2[-1] = test2[-1].decode('utf8', 'ignore')
            # Check if tendering limit is within the procurement amount.
            if tender_limit >= (_procurement / 1000000.0):
                tree_list[1].insert("", 0, text=counter, values=test2, tags=['blue_fg'])
                counter += 1

    def export_file(self):
        """ Export the data set into multiple txt files. Each agency will be stored in an individual txt file."""
        save_path = settings.cd + "\\" + "agency_procurement" + "\\"

        agency_list = []
        for d in settings.data_set[0]:
            if not d.get('agency') in agency_list:
                agency_list.append(d.get('agency'))


        if not os.path.exists(save_path):
            os.makedirs(save_path)
        for i in agency_list:
            headers = []
            full_path = os.path.join(save_path, i + ".txt")
            file1 = open(full_path, "w")
            for header in settings.data_set[0][0].keys():
                headers.append(header + "\t")
            file1.writelines(headers)
            file1.writelines("\n")
            for x in settings.data_set[0]:
                if i == x.get('agency'):
                    for k in x:
                        file1.writelines(x.get(k) + "\t")
                    file1.writelines("\n")
            file1.close()
        tkMessageBox.showinfo("Successfully Exported",
                              "You have successfully export the agency data into %s" % save_path)


    def get_expiry_date(self, tree=None):
        """ List all contractors that have expired contracts """
        expired_list = []
        counter = 0
        today = (date.today().strftime("%d/%m/%Y")).split("/")  # Store current date

        tree.delete(*tree.get_children())

        for a in settings.data_set[1]:
            test2 = []
            datecheck = a.get('expiry_date').split("/")
            for x in a:
                test2.append(a.get(x))
                test2[-1] = test2[-1].decode('utf8', 'ignore')
            if int(datecheck[2]) < int(today[2]):
                expired_list.append(a.get("uen_no"))
                counter += 1
                tree.insert("", 0, text=counter, values=test2, tags=['blue_fg'])
            elif datecheck[2] == today[2] and int(datecheck[1]) < int(today[1]):
                expired_list.append(a.get("uen_no"))
                counter += 1
                tree.insert("", 0, text=counter, values=test2, tags=['blue_fg'])
            elif datecheck[2] == today[2] and datecheck[1] == today[1] and int(datecheck[0]) < int(today[0]):
                expired_list.append(a.get("uen_no"))
                counter += 1
                tree.insert("", 0, text=counter, values=test2, tags=['blue_fg'])

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        canvas = tk.Canvas(self, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())
        canvas.pack()

        frame = tk.Frame(canvas, bg="#282C34")
        frame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        instruction_label = tk.Label(frame, text="What would you like to do?", font=50)
        instruction_label.pack()

        tree_list = []
        # Create the treeview to display the data sets
        for data_set in settings.data_set:
            tree = ttk.Treeview(frame)

            # Set Vertical Scrollbar to the Trees
            tree_scrollbar_vertical = ttk.Scrollbar(tree, orient='vertical', command=tree.yview)
            tree_scrollbar_horizontal = ttk.Scrollbar(tree, orient='horizontal', command=tree.xview)
            tree_scrollbar_vertical.pack(side=RIGHT, fill=Y)
            tree_scrollbar_horizontal.pack(side=BOTTOM, fill=X)
            tree.configure(xscrollcommand=tree_scrollbar_horizontal.set, yscrollcommand=tree_scrollbar_vertical.set)

            for i in range(0, len(data_set)):
                heading_list = []
                value_list = []

                for x in data_set[i]:
                    heading_list.append(x)
                    value_list.append(data_set[i].get(x))
                    value_list[-1] = value_list[-1].decode('utf-8', 'ignore')

                tree["columns"] = heading_list
                tree['show'] = 'headings'

                for x in range(0, len(heading_list)):
                    tree.heading(heading_list[x], text=heading_list[x])

                tree.insert("", 0, values=value_list)

            tree.pack(fill=BOTH, expand=True)

            # Fill the trees with data
            tree_list.append(tree)

            def treeview_sort_column(tv, col, reverse):
                l = [(tv.set(k, col), k) for k in tv.get_children('')]
                l.sort(reverse=reverse)

                # rearrange items in sorted positions
                for index, (val, k) in enumerate(l):
                    tv.move(k, '', index)

                # reverse sort next time
                tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))

            for col in heading_list:
                tree.heading(col, text=col,command=lambda _col=col: treeview_sort_column(tree, _col, False))

        """
        Bottom Frame - Seperator for Input Widgets
        """
        bottom_frame = Frame(frame, bg="#282C34")
        bottom_frame.pack(fill=BOTH, expand=True)

        ## Sub-Frame [1] for Input ##
        frame_Input_1 = Frame(bottom_frame, bg="#282C34")
        frame_Input_1.pack(expand=True)

        input_label_UEN = Label(frame_Input_1, text="UEN:", bg='gray65')
        input_label_UEN.pack(side=LEFT)

        input_Entry_1 = Entry(frame_Input_1)
        input_Entry_1.pack(side=LEFT)

        btn_get_company_by_uen = tk.Button(frame_Input_1, text="Search Company By UEN",
                                           command=lambda: self.get_company_by_uen(tree_list=tree_list,
                                                                                   uen_number=input_Entry_1.get()))
        btn_get_company_by_uen.pack(side=LEFT, padx="10")

        input_label_keyword = Label(frame_Input_1, text="Keyword:", bg='gray65')
        input_label_keyword.pack(side=LEFT, padx="1")

        input_Entry_2 = Entry(frame_Input_1)
        input_Entry_2.pack(side=LEFT)

        btn_list_company_from_keyword = tk.Button(frame_Input_1, text="Search Company by Name",
                                                  command=lambda: self.list_company_from_keyword(tree_list=tree_list,
                                                                                                 keyword=input_Entry_2.get()))
        btn_list_company_from_keyword.pack(side=LEFT, padx="10")

        input_label_filter_top = Label(frame_Input_1, text="No. of Contractors:", bg='gray65')
        input_label_filter_top.pack(side=LEFT, padx="1")

        input_Entry_4 = Entry(frame_Input_1)
        input_Entry_4.pack(side=LEFT, padx="1")

        btn_get_top_contractors = tk.Button(frame_Input_1, text="Get Top Contractors",
                                            command=lambda: self.get_top_contractors(frame, n=int(input_Entry_4.get())))
        btn_get_top_contractors.pack(side=LEFT, padx="10")

        ## Sub-Frame [2] for Input ##
        frame_Input_2 = Frame(bottom_frame, bg="#282C34")
        frame_Input_2.pack(expand=True)

        input_label_filter_qual = Label(frame_Input_2, text="Tender Amt:", bg='gray65')
        input_label_filter_qual.pack(side=LEFT, padx="1")

        input_Entry_5 = Entry(frame_Input_2)
        input_Entry_5.pack(side=LEFT, padx="1")

        btn_get_qualified_contractors = tk.Button(frame_Input_2, text="Get Qualified Contractors",
                                                  command=lambda: self.get_qualified_contractors(input_Entry_5.get(),
                                                                                                 tree_list=tree_list))

        btn_get_qualified_contractors.pack(side=LEFT, padx="10")

        input_label_award_year = Label(frame_Input_2, text="Award Year:", bg='gray65')
        input_label_award_year.pack(side=LEFT, padx="1")

        input_Entry_6 = Entry(frame_Input_2)
        input_Entry_6.pack(side=LEFT, padx="1")

        btn_get_award_year = tk.Button(frame_Input_2, text="List Procurements during Award Year",
                                       command=lambda: self.get_award_year(tree_list=tree_list,
                                                                           _year=int(input_Entry_6.get())))

        btn_get_award_year.pack(side=LEFT, padx="10")

        ## Sub-Frame [1] for Buttons ##
        frame_button_1 = Frame(bottom_frame, bg="#282C34")
        frame_button_1.pack(side=TOP, expand=True)

        btn_get_procurement_by_category = tk.Button(frame_button_1, text="List Procurements by Category",
                                                    command=lambda: self.get_procurement_by_cat(frame))

        btn_get_procurement_by_category.pack(side=LEFT, padx="10")

        btn_get_agency = tk.Button(frame_button_1, text="List of Agencies", command=lambda: self.get_agency(frame))
        btn_get_agency.pack(side=LEFT, padx="10")

        btn_get_awarded_contractors = tk.Button(frame_button_1, text="List of Awarded Contractors",
                                                command=lambda: self.get_awarded_contractors(tree_list=tree_list))

        btn_get_awarded_contractors.pack(side=LEFT, padx="10")

        btn_get_expired_contracts = tk.Button(frame_button_1, text="Get Expired Contracts",
                                              command=lambda tree_variable=tree: self.get_expiry_date(
                                                  tree=tree_variable))

        btn_get_expired_contracts.pack(side=LEFT, padx="10")

        btn_sort_procure = tk.Button(frame_button_1, text="Sort by Procurement Amt",
                                     command=lambda: self.sort_col("awarded_amt", settings.data_set[0], False,
                                                                   tree_list=tree_list))

        btn_sort_procure.pack(side=LEFT, padx="10")

        ## Sub-Frame [2] for Buttons ##
        frame_button_2 = Frame(bottom_frame, bg="#282C34")
        frame_button_2.pack(expand=True)

        function4_button = tk.Button(frame_button_2, text="Export Agency Procurement to Text File",
                                     command=lambda: self.export_file())
        function4_button.pack(side=LEFT, expand=True, padx="10")

        back_button = tk.Button(frame_button_2, text="Return to start page",
                                command=lambda: master.switch_frame(main.StartPage))
        back_button.pack(side=LEFT, expand=True, padx="1")
