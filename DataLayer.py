import sqlite3
from sqlite3 import Error
import json
import xml.etree.ElementTree as ET

"""
Construct a SQL Database based on the data from the DataFile.
Processes the queries from the Business Layer.   
Sends back a JSON string for the requested query.  
"""


class DataLayer:
    def __init__(self):
        # Construct a SQL Database based on the data from the DataFile.
        self.fileName = "/Users/xiwu/PycharmProjects/Python/41B/Practice/LabFour/UNData.xml"

        self.conn = self.sqConnect()
        self.cur = self.conn.cursor()
        self.createTable()
        self.insertRow()

        self.cur.close()

    def sqConnect(self):
        try:
            conn = sqlite3.connect('lab4.database')
            return conn
        except Error as e:
            print(e)
        return None

    def createTable(self):
        new = """CREATE TABLE IF NOT EXISTS countryData (
                                                country TEXT NOT NULL,
                                                year INTEGER,
                                                value REAL
                                                );"""
        self.conn.execute(new)

    def insertRow(self):
        self.cur.execute('DELETE FROM countryData')
        tree = ET.ElementTree(file=self.fileName)
        root = tree.getroot()
        for element in root.iter('record'):
            country = element.find('Country').text
            year = element.find('Year').text
            value = element.find('Value').text
            self.cur.execute("INSERT INTO countryData (country, year, value) VALUES (?, ?, ?)", (country, year, value))
            self.conn.commit()

    def readDb(self, countryName):
        conn = self.sqConnect()
        cur = conn.cursor()
        sqData = {}
        cur.execute("SELECT country, year, value FROM countryData WHERE country=?", (countryName,))
        while True:
            oneRow = cur.fetchone()
            if oneRow is not None:
                sqData[oneRow[1]] = oneRow[2]
            else:
                break
            # convert into JSON
            jData = json.dumps(sqData)
        return jData
