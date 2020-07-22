from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import *
from tkinter.ttk import *
import shutil
import os.path
import math
import calc
import xml_ge_formater as XML
import pandas as pd
import tables_validation as validation

data_path = ''
ept_path = ''

def get_ept_template():
    save_dir = askdirectory()
    src = os.path.abspath(os.getcwd()) + '/ept_template.csv'
    shutil.copy(src, save_dir)
    open("ept_template.csv", 'r')


def get_data_template():
    save_dir = askdirectory()
    src = os.path.abspath(os.getcwd()) + '/data_template.csv'
    shutil.copy(src, save_dir)
    open("data_template.csv", 'r')

''' This function executes all calculation and generates the final XML '''
def submit_button():
    if data_path != '' and ept_path != '':
        full_df = validation.validate(data_path, ept_path)                #Validate tables
        kml_data = calc.generateKMLData(full_df)                          #Generate a dataframe with all data required for XML generation
        kml_data.to_excel("output.xlsx")                                  #Save the dataframe in an excel file
        XML.generateXML(kml_data)                                         #Generate the XML (KML) from the Dataframe

''' This function is to browse the data got it from U2000 '''
def browse_data():
    global data
    data_path = askopenfilename()

''' This function is to browse the engineering parameter table '''
def browse_ept():
    global ept
    ept_path = askopenfilename()

''' Following code is the configuration of the GUI '''
root = Tk()
root.title("3G TP Propagation Delay Tool for GE")
root.geometry('410x200')

style = Style()
style.configure('Send.TButton', font=('calibri', 10, 'bold', 'underline'), background = 'blue')

button1 = Button(text="Select data file", command=browse_data)
button1.grid(row = 0, column = 2, padx = 5) 

button2 = Button(text="Select ept file", command=browse_ept)
button2.grid(row = 0, column = 4, pady = 10, padx = 5)

button3 = Button(root, text="Send", style='Send.TButton', command=submit_button)
button3.grid(row = 2, column = 3, pady = 10, padx = 5)

button4 = Button(root, text="Download EPT Template", style='Send.TButton', command=get_ept_template)
button4.grid(row = 5, column = 2, pady = 10, padx = 5)

button5 = Button(root, text="Download Data Template", style='Send.TButton', command=get_data_template)
button5.grid(row = 5, column = 4, pady = 10, padx = 5)

''' This function keeps the program running'''
mainloop()