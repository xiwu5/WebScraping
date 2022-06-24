# Import required library
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk
from Client import Client
from GraphLayer import GraphLayer

"""
 The user selects a country,
 and passes the country name to the Business Layer.
 Use TKinter to produce a pull-down for the user to select a country.
 Send the selected country to the Business Layer.
"""


class UserLayer:
    def __init__(self):
        self.fileName = "/Users/xiwu/PycharmProjects/Python/41B/Practice/LabFour/UNData.xml"
        # Create an empty set
        self.countryName = set()
        self.readFile()
        self.choice = None
        self.tkwindow = None
        self.client = Client(5000)
        self.graphLayer = None
        self.window()

    """ 
    read xml file as a set, 
    read the countries name, 
    add the countries name into the set
    """

    def readFile(self):
        tree = ET.ElementTree(file=self.fileName)
        root = tree.getroot()

        for country in root.iter('Country'):
            name = country.text
            self.countryName.add(name)

    def window(self):
        # Create tkinter window
        self.tkwindow = tk.Tk()
        self.tkwindow.title('Country')
        self.tkwindow.geometry("1500x1500")

        # Label text for title
        ttk.Label(self.tkwindow, text="Choose the Country and Plot it!",
                  background='cyan', foreground="black",
                  font=("Times New Roman", 15)).grid(row=0, column=1)

        # Label
        ttk.Label(self.tkwindow, text="Select the Country : ",
                  font=("Times New Roman", 12)).grid(column=0,
                                                     row=5, padx=10, pady=25)
        # Combobox creation
        n = tk.StringVar()
        countryChoosen = ttk.Combobox(self.tkwindow, width=27, textvariable=n)

        # Adding combobox drop down list
        countryChoosen['values'] = list(self.countryName)
        countryChoosen.grid(column=1, row=5)

        countryChoosen.bind("<<ComboboxSelected>>", self.selection)
        countryChoosen.current()

        self.graphLayer = GraphLayer(self.tkwindow)

        self.tkwindow.mainloop()

    # This function stores user's choice and send it to client socket
    def selection(self, event):
        widget = event.widget
        self.choice = widget.get()
        self.client.Connect(self.choice, self.graphLayer)


T = UserLayer()
