"""
Use your Graphic Class or module defined in previous assignments to draw a MatPlotLib XYPlot.

"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import json


class GraphLayer:
    def __init__(self, root):
        self.years = []
        self.values = []

        self.fig = Figure((10, 8), dpi=80)  # drawing board
        self.plotCanvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvasAddPlot = self.fig.add_subplot(111)

    def setDataAndPlot(self, data, message):
        self.convertJsonToDict(data)
        self.xyPlot(message)

    def canvasSetting(self):  # matplotlib figure setting
        self.plotCanvas.get_tk_widget().grid(row="10", column="2", columnspan="3", sticky="news")
        canvasA = self.canvasAddPlot

        canvasA.set_xlabel('Years', fontsize=14)
        canvasA.set_ylabel('Value', fontsize=14)

        canvasA.tick_params(axis='both', which='major', labelsize=14)

        canvasA.grid(axis='y', linewidth=1, linestyle='--')

        return canvasA

    def xyPlot(self, message):
        self.canvasAddPlot.clear()
        canvasA = self.canvasSetting()
        canvasA.set_title(message, fontsize=20)
        canvasA.plot(self.years, self.values, 'r-', label='Data relative to 1990-2017')
        canvasA.legend()
        self.plotCanvas.draw()

    def convertJsonToDict(self, obj):
        # Clear data
        self.years = []
        self.values = []

        d = json.loads(obj)

        # sorting the dictionary
        for key in dict(sorted(d.items())):
            self.years.append(int(key))
            self.values.append(int(d[key]))
