import PyQt5.QtGui as G
import PyQt5.QtWidgets as W
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.ticker as ticker
from matplotlib.figure import Figure
import numpy as np
import sys

style_scheme = ["k-", "k--", "k-.", "k:", "ks-"]


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax2 = self.ax.twinx()
        self.ax2.set_axis_off()
        FigureCanvas.__init__(self, self.fig)
        self.setSizePolicy(W.QSizePolicy.Expanding,
                                    W.QSizePolicy.Expanding)
        self.updateGeometry()

    def clear(self):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.ax2 = self.ax.twinx()
        self.ax2.set_axis_off()


class MPLWidget(W.QWidget):
    def __init__(self, parent=None):
        super(MPLWidget, self).__init__(parent)
        self.canvas = MplCanvas()
        self.canvas.fig.subplots_adjust(left=0.07,right=0.95, top=0.92, bottom=0.10)
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.canvas)
        self.vbl = W.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.line_count = 0

    def clear(self):
        self.canvas.clear()
        self.line_count = 0

    def line_plot(self, data, title="", xlabel="", ylabel="", label=""):
        self.canvas.ax.clear()
        self.canvas.ax.set_xlabel(xlabel)
        self.canvas.ax.set_ylabel(ylabel)
        self.canvas.ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
        self.canvas.ax.set_title(title)
        self.add_line(data, label)
        self.canvas.draw()

    def add_line(self, data, label=""):
        print(self.line_count)
        self.canvas.ax.plot(data, style_scheme[self.line_count], label=label, lw=2)
        self.line_count += 1
        self.canvas.updateGeometry()
        if self.line_count > 1:
            handles, labels = self.canvas.ax.get_legend_handles_labels()
            self.canvas.ax.legend(handles, labels)
        self.canvas.draw()

    def second_axis(self, data, ylabel="", label=""):
        self.canvas.ax2 = self.canvas.ax.twinx()
        newline =  self.canvas.ax2.plot(data, style_scheme[self.line_count], lw=2, label=label)
        self.line_count += 1
        lines, labels = self.canvas.ax.get_legend_handles_labels()
        lines2, labels2 = self.canvas.ax2.get_legend_handles_labels()
        self.canvas.ax2.set_ylabel(ylabel)
        print(lines, labels)
        print(lines2, labels2)
        self.canvas.ax2.legend(lines + lines2, labels + labels2)
        self.canvas.ax2.set_axis_on()
        self.canvas.draw()

    def apc_route(self, data):
        self.canvas.ax.clear()
        self.canvas.ax.set_xlabel("Stop Sequence")
        self.canvas.ax.set_ylabel("People")
        line = self.canvas.ax.plot(data, lw=2)
        # self.canvas.ax.legend([line[0], line[1]], ['On', 'Off'])
        self.canvas.updateGeometry()
        self.canvas.draw()
