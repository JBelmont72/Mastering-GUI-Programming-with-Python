'''
MyPyqtGraph/Lissagous_1.py
import pyqtgraph.examples
pyqtgraph.examples.run()
 this site does live plotting with multiple options to vary parameters
 chat help https://chatgpt.com/c/6880e009-ba3c-800f-b031-2907ed0fdbea
'''
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSlider, QLabel, QComboBox, QStackedWidget, QSpinBox
)
from PyQt5.QtCore import Qt
import pyqtgraph as pg


class LissajousWidget(QWidget):
    def __init__(self, plot_callback):
        super().__init__()
        self.plot_callback = plot_callback

        layout = QVBoxLayout()

        self.freq_a = QSlider(Qt.Horizontal)
        self.freq_b = QSlider(Qt.Horizontal)
        self.phase = QSlider(Qt.Horizontal)

        self.freq_a.setRange(1, 10)
        self.freq_b.setRange(1, 10)
        self.phase.setRange(0, 628)  # 0 to 2π * 100

        self.freq_a.valueChanged.connect(self.update_plot)
        self.freq_b.valueChanged.connect(self.update_plot)
        self.phase.valueChanged.connect(self.update_plot)

        layout.addWidget(QLabel("Frequency a"))
        layout.addWidget(self.freq_a)
        layout.addWidget(QLabel("Frequency b"))
        layout.addWidget(self.freq_b)
        layout.addWidget(QLabel("Phase shift (0 – 2π)"))
        layout.addWidget(self.phase)

        self.setLayout(layout)

    def update_plot(self):
        a = self.freq_a.value()
        b = self.freq_b.value()
        delta = self.phase.value() / 100  # Convert to float

        t = np.linspace(0, 2 * np.pi, 1000)
        x = np.sin(a * t + delta)
        y = np.sin(b * t)

        self.plot_callback(x, y)


class ButterflyWidget(QWidget):
    def __init__(self, plot_callback):
        super().__init__()
        self.plot_callback = plot_callback

        layout = QVBoxLayout()

        self.tmin = QSpinBox()
        self.tmax = QSpinBox()
        self.tmin.setRange(-100, 0)
        self.tmax.setRange(0, 100)
        self.tmin.setValue(-50)
        self.tmax.setValue(50)

        self.tmin.valueChanged.connect(self.update_plot)
        self.tmax.valueChanged.connect(self.update_plot)

        layout.addWidget(QLabel("t min"))
        layout.addWidget(self.tmin)
        layout.addWidget(QLabel("t max"))
        layout.addWidget(self.tmax)

        self.setLayout(layout)

    def update_plot(self):
        t_min = self.tmin.value()
        t_max = self.tmax.value()

        t = np.linspace(t_min, t_max, 5000)
        r = np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12))**5
        x = np.sin(t) * r
        y = np.cos(t) * r

        self.plot_callback(x, y)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Parametric Plot Explorer")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Lissajous", "Butterfly"])
        self.mode_selector.currentIndexChanged.connect(self.switch_mode)

        self.stack = QStackedWidget()
        self.plot_widget = pg.PlotWidget()
        self.plot_curve = self.plot_widget.plot([], [], pen=pg.mkPen('c', width=1))

        self.lissajous_panel = LissajousWidget(self.plot)
        self.butterfly_panel = ButterflyWidget(self.plot)

        self.stack.addWidget(self.lissajous_panel)
        self.stack.addWidget(self.butterfly_panel)

        main_layout.addWidget(QLabel("Select Plot Type"))
        main_layout.addWidget(self.mode_selector)
        main_layout.addWidget(self.stack)
        main_layout.addWidget(self.plot_widget)

        central_widget.setLayout(main_layout)

        self.lissajous_panel.update_plot()

    def switch_mode(self, index):
        self.stack.setCurrentIndex(index)
        # Trigger plot refresh
        if index == 0:
            self.lissajous_panel.update_plot()
        else:
            self.butterfly_panel.update_plot()

    def plot(self, x, y):
        self.plot_curve.setData(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(800, 600)
    win.show()
    sys.exit(app.exec_())
