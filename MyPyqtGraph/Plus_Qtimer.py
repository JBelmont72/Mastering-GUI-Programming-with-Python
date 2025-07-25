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
    QSlider, QLabel, QComboBox, QStackedWidget, QSpinBox, QPushButton
)
from PyQt5.QtCore import Qt, QTimer
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

        for slider in (self.freq_a, self.freq_b, self.phase):
            slider.valueChanged.connect(self.update_plot)

        layout.addWidget(QLabel("Frequency a"))
        layout.addWidget(self.freq_a)
        layout.addWidget(QLabel("Frequency b"))
        layout.addWidget(self.freq_b)
        layout.addWidget(QLabel("Phase shift (0 – 2π)"))
        layout.addWidget(self.phase)

        self.setLayout(layout)

    def get_params(self):
        a = self.freq_a.value()
        b = self.freq_b.value()
        delta = self.phase.value() / 100
        return a, b, delta

    def update_plot(self):
        self.plot_callback()


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

    def get_params(self):
        return self.tmin.value(), self.tmax.value()

    def update_plot(self):
        self.plot_callback()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parametric Plot Explorer")

        # Central layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()

        # Mode selection
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Lissajous", "Butterfly"])
        self.mode_selector.currentIndexChanged.connect(self.switch_mode)

        # Color selection
        self.color_selector = QComboBox()
        self.color_selector.addItems(["Cyan", "Yellow", "Magenta", "Red", "Green", "White"])
        self.color_selector.currentIndexChanged.connect(self.update_color)

        # Start/stop animation
        self.start_btn = QPushButton("Start Animation")
        self.start_btn.clicked.connect(self.toggle_animation)

        control_row = QHBoxLayout()
        control_row.addWidget(QLabel("Plot Type"))
        control_row.addWidget(self.mode_selector)
        control_row.addWidget(QLabel("Color"))
        control_row.addWidget(self.color_selector)
        control_row.addWidget(self.start_btn)

        # Stacked widgets for mode-specific controls
        self.stack = QStackedWidget()
        self.lissajous_panel = LissajousWidget(self.update_plot)
        self.butterfly_panel = ButterflyWidget(self.update_plot)
        self.stack.addWidget(self.lissajous_panel)
        self.stack.addWidget(self.butterfly_panel)

        # Plot area
        pg.setConfigOption('background', 'k')  # black background
        self.plot_widget = pg.PlotWidget()
        self.plot_curve = self.plot_widget.plot([], [], pen=pg.mkPen('c', width=1))

        # Timer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.t_anim = 0

        main_layout.addLayout(control_row)
        main_layout.addWidget(self.stack)
        main_layout.addWidget(self.plot_widget)
        central_widget.setLayout(main_layout)

        self.update_plot()  # initial plot

    def switch_mode(self, index):
        self.stack.setCurrentIndex(index)
        self.update_plot()

    def update_color(self):
        color = self.color_selector.currentText().lower()
        self.plot_curve.setPen(pg.mkPen(color=color, width=1))

    def toggle_animation(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_btn.setText("Start Animation")
        else:
            self.t_anim = 0
            self.timer.start(30)  # ~30 FPS
            self.start_btn.setText("Stop Animation")

    def update_plot(self):
        mode = self.mode_selector.currentText()
        if mode == "Lissajous":
            a, b, delta = self.lissajous_panel.get_params()
            t = np.linspace(0, 2 * np.pi, 1000) + self.t_anim
            x = np.sin(a * t + delta)
            y = np.sin(b * t)
        else:
            tmin, tmax = self.butterfly_panel.get_params()
            t = np.linspace(tmin, tmax, 4000) + self.t_anim
            r = np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12))**5
            x = np.sin(t) * r
            y = np.cos(t) * r

        self.plot_curve.setData(x, y)
        if self.timer.isActive():
            self.t_anim += 0.02


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(1000, 700)
    win.show()
    sys.exit(app.exec_())
