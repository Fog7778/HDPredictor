import sys
import time
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QComboBox, QLabel, QFrame, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont

class HDPredictor(QMainWindow):
    def __init__(self):
        super().__init__()
        #Window setup
        self.setWindowTitle("HDPredictor")
        self.setGeometry(100, 100, 700, 550)
        self.setStyleSheet("background-color: #2c3e50; color: #ecf0f1;")

        #days
        self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        #UI
        self.setup_ui()
        
    def setup_ui(self):
        #Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(25)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter) 


        #Title
        title_label = QLabel("Whats the day??")
        title_label.setFont(QFont("SF Pro", 12))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        #Dropdown 
        dropdown_container = QWidget()
        dropdown_layout = QVBoxLayout(dropdown_container)
        dropdown_layout.setContentsMargins(0, 0, 0, 0)
        dropdown_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day_selector = QComboBox()
        self.day_selector.addItems(self.days)
        self.day_selector.setCurrentIndex(-1) #Staart with nun selected
        self.day_selector.setFont(QFont("SF Pro", 10))
        self.day_selector.setMinimumHeight(25)
        self.day_selector.setMaximumWidth(200)

        #Coloring / styling
        self.day_selector.setStyleSheet(
            """
            QComboBox {
                border: 1px solid #3498db;
                border-radius: 6px;
                padding: 2px 6px;
                background-color: #34495e;
                color: #ecf0f1;
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QComboBox QAbstractItemView {
                border: 1px solid #3498db;
                background-color: #34495e;
                color: #ecf0f1;
                selection-background-color: #2980b9;
            }
            """
        )
        # acctual fix for the jumping T-T
        dropdown_layout.addWidget(self.day_selector)
        layout.addWidget(dropdown_container)

        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

        #when selcted stat computing ehheheheeh
        self.day_selector.currentIndexChanged.connect(self.start_computation)

        #Figuring out what day
        self.result_label = QLabel("Whats the day??")
        self.result_label.setFont(QFont("SF Pro", 11, QFont.Weight.Bold))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("color: #34495e; padding: 2px; min-height: 30px;")
        
        #Loading screen
        result_frame = QFrame()
        result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        result_frame.setFrameShadow(QFrame.Shadow.Raised)
        result_frame.setStyleSheet("""
            QFrame {
                border: 1px solid #4e6a87;
                border-radius: 10px;
                background-color: #34495e;
            }
        """)
        frame_layout = QVBoxLayout(result_frame)
        frame_layout.setContentsMargins(5, 5, 5, 5)
        frame_layout.addWidget(self.result_label)
        layout.addWidget(result_frame)
        self.set_label_style(initial=True)
        bottom_spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        layout.addItem(bottom_spacer)

        #fix for issue of the drop down moving with the buffer box
    def set_label_style(self, state='default', initial=False):         
        min_height_value = "min-height: 50px;"
        base_style = f"padding: 2px; {min_height_value}"
        if initial or state == 'default':
            self.result_label.setText("Whats the day??")
            self.result_label.setStyleSheet(f"color: #4b5563; {base_style}")
        elif state == 'buffer':
            self.result_label.setStyleSheet(f"color: #bdc3c7; {base_style}")
        elif state == 'result':
            self.result_label.setStyleSheet(f"color: #10b981; {base_style}")


    def start_computation(self, index):
        if index == -1:
            self.result_label.setText("Whats the day??")
            self.result_label.setStyleSheet("color: #4b5563; padding: 2px; min-height: 50px;")
            return
            
        current_day = self.days[index]
        
        self.result_label.setText(f"uhhhhhhhhhhhhhhhhhhhhhh... {current_day}??")
        self.result_label.setStyleSheet("color: #bdc3c7; padding: 2px; min-height: 30px;")

        #Timer
        QTimer.singleShot(3000, lambda: self.show_next_day(index))

        #Next day calc
    def show_next_day(self, index):
        next_day_index = (index + 1) % len(self.days)
        
        next_day = self.days[next_day_index]
        
        #Display the final result
        self.result_label.setText(f"gonna be {next_day} Twi")
        self.result_label.setStyleSheet("color: #10b981; padding: 2px; min-height: 30px;")


if __name__ == '__main__':
    #Int app
    app = QApplication(sys.argv)
    window = HDPredictor()
    window.show()
    sys.exit(app.exec())
