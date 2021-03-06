import turtle
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class TurtleControl(QWidget):
    def __init__(self, turtle):
        super(TurtleControl, self).__init__()
        self.turtle = turtle

        self.left_btn = QPushButton("Left", self)
        self.right_btn = QPushButton("Right", self)
        self.move_btn = QPushButton("Move", self)
        self.distance_spin = QSpinBox()

        self.controlsLayout = QGridLayout()
        self.controlsLayout.addWidget(self.left_btn, 0, 0)
        self.controlsLayout.addWidget(self.right_btn, 0, 1)
        self.controlsLayout.addWidget(self.distance_spin, 1, 0)
        self.controlsLayout.addWidget(self.move_btn, 1, 1)
        self.setLayout(self.controlsLayout)

        self.distance_spin.setRange(0, 100)
        self.distance_spin.setSingleStep(5)
        self.distance_spin.setValue(20)

        self.move_btn.clicked.connect(self.move_turtle)
        self.right_btn.clicked.connect(self.turn_turtle_right)
        self.left_btn.clicked.connect(self.turn_turtle_left)

    def turn_turtle_left(self):
        self.turtle.left(45)

    def turn_turtle_right(self):
        self.turtle.right(45)

    def move_turtle(self):
        self.turtle.forward(self.distance_spin.value())

# set up turtle
window = turtle.Screen()
babbage = turtle.Turtle()

# Create a Qt application
app = QApplication(sys.argv)
control_window = TurtleControl(babbage)
control_window.show()

# Enter Qt application main loop
app.exec_()
sys.exit()

                            
