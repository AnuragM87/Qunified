import numpy as np
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, 
    QVBoxLayout, QTextEdit, QGridLayout
)

class DensityMatrixChecker(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.matrix_inputs = []  # Store matrix input fields
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Check Density Matrix")
        self.setGeometry(100, 100, 400, 400)

        self.label_dim = QLabel("Enter matrix dimension (n x n):")
        self.input_dim = QLineEdit()
        self.submit_dim_button = QPushButton("Enter Elements")
        self.submit_dim_button.clicked.connect(self.create_matrix_inputs)

        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)

        # Reset Button
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_inputs)

        self.back_button = QPushButton("Back to Main Menu")
        self.back_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_dim)
        self.layout.addWidget(self.input_dim)
        self.layout.addWidget(self.submit_dim_button)
        self.layout.addWidget(self.output_field)
        self.layout.addWidget(self.reset_button)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def create_matrix_inputs(self):
        try:
            self.n = int(self.input_dim.text())
            if self.n <= 0:
                self.output_field.setText("Dimension must be positive!")
                return

            # Remove any existing matrix input fields before creating new ones
            self.clear_matrix_inputs()

            self.matrix_inputs = []
            self.grid_layout = QGridLayout()  # Store grid layout so we can remove it later

            for i in range(self.n):
                row_inputs = []
                for j in range(self.n):
                    input_field = QLineEdit()
                    self.grid_layout.addWidget(input_field, i, j)
                    row_inputs.append(input_field)
                self.matrix_inputs.append(row_inputs)

            self.layout.addLayout(self.grid_layout)

            self.validate_button = QPushButton("Check Matrix")
            self.validate_button.clicked.connect(self.check_matrix)
            self.layout.addWidget(self.validate_button)

        except ValueError:
            self.output_field.setText("Please enter a valid integer for dimension.")

    def check_matrix(self):
        try:
            rho = np.zeros((self.n, self.n), dtype=complex)

            for i in range(self.n):
                for j in range(self.n):
                    text = self.matrix_inputs[i][j].text()
                    real_imag = text.split()
                    if len(real_imag) != 2:
                        self.output_field.setText("Enter elements as 'real imaginary' (space-separated).")
                        return
                    real_part = float(real_imag[0])
                    imag_part = float(real_imag[1])
                    rho[i, j] = complex(real_part, imag_part)

            # Check Density Matrix Properties
            is_valid, message = self.is_density_matrix(rho)
            self.output_field.setText(f"Matrix:\n{rho}\n\nCheck Result: {message}")

        except ValueError:
            self.output_field.setText("Invalid matrix elements!")

    def is_density_matrix(self, rho):
        if rho.shape[0] != rho.shape[1]:
            return False, "Matrix is not square"
        if not np.allclose(rho, rho.conj().T):
            return False, "Matrix is not Hermitian"
        if np.any(np.linalg.eigvalsh(rho) < 0):
            return False, "Matrix is not positive semi-definite"
        if not np.isclose(np.trace(rho), 1):
            return False, "Trace is not 1"
        return True, "Valid density matrix"

    def reset_inputs(self):
        """Resets all input fields, matrix elements, and output."""
        self.input_dim.clear()
        self.output_field.clear()
        self.clear_matrix_inputs()

    def clear_matrix_inputs(self):
        """Removes matrix input fields and validation button if present."""
        if hasattr(self, "grid_layout"):  # Check if matrix inputs exist
            while self.grid_layout.count():
                item = self.grid_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.layout.removeItem(self.grid_layout)  # Remove grid layout

        # Remove the validate button if it exists
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QPushButton) and widget.text() == "Check Matrix":
                widget.deleteLater()
