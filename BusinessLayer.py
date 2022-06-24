"""
Receives the information from the User Layer and constructs a SQL query to send to the Data Layer.
The query extracts the yearly data (1990,2017) for the requested country.
The data may be queried either country year-by-year or in one query for year range.
After receiving the JSON string back from the Data Layer, send the data to the Graphic Layer for plotting.
"""
from DataLayer import DataLayer


class Process:
    def __init__(self):
        self.D = DataLayer()

    # Receives the information from the client socket
    def getJsonStr(self, query):
        # Constructs a SQL query to send to the Data Layer.
        return self.D.readDb(query)
