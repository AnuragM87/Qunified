# from PyQt6.QtWidgets import QWidget,QPushButton, QVBoxLayout
# class MainMenu(QWidget):
#     """Main menu with navigation buttons."""
#     def __init__(self, stacked_widget):
#         super().__init__()
#         self.stacked_widget = stacked_widget
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("Quantum Toolkit")
#         self.setGeometry(100, 100, 400, 200)

#         # Buttons
#         self.tomography_button = QPushButton("Single Tomography")
#         self.density_matrix_button = QPushButton("Check Density Matrix")

#         # Connect buttons
#         self.tomography_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
#         self.density_matrix_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

#         # Layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.tomography_button)
#         layout.addWidget(self.density_matrix_button)
#         self.setLayout(layout)

from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class MainMenu(QWidget):
    """Main menu with navigation buttons."""
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Quantum Toolkit")
        self.setGeometry(100, 100, 400, 250)

        # Title Label
        title = QLabel("Quantum Toolkit", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")

        # Buttons
        self.tomography_button = QPushButton("Single Qubit Tomography")
        self.density_matrix_button = QPushButton("Check Density Matrix")

        # Button Styling
        button_style = """
            QPushButton {
                font-size: 14px;
                padding: 8px;
                border-radius: 6px;
                background-color: #007BFF;
                color: white;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """
        self.tomography_button.setStyleSheet(button_style)
        self.density_matrix_button.setStyleSheet(button_style)

        # Connect buttons
        self.tomography_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.density_matrix_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))

        # Layout
        layout = QVBoxLayout()
        layout.setSpacing(15)  # Add space between elements
        layout.addWidget(title)
        layout.addWidget(self.tomography_button)
        layout.addWidget(self.density_matrix_button)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
