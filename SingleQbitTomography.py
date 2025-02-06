import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit

class SingleQubitTomography(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Single-Qubit Quantum Tomography")
        self.setGeometry(100, 100, 400, 400)

        # Labels and Inputs
        self.label_Nh = QLabel("No. of H-polarized Photons:")
        self.input_Nh = QLineEdit()

        self.label_Nv = QLabel("No. of V-polarized Photons:")
        self.input_Nv = QLineEdit()

        self.label_Nl = QLabel("No. of L-polarized Photons:")
        self.input_Nl = QLineEdit()

        self.label_Nd = QLabel("No. of D-polarized Photons:")
        self.input_Nd = QLineEdit()

        # Compute Button
        self.compute_button = QPushButton("Compute")
        self.compute_button.clicked.connect(self.compute_results)

        # Output Text Field
        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_Nh)
        layout.addWidget(self.input_Nh)
        layout.addWidget(self.label_Nv)
        layout.addWidget(self.input_Nv)
        layout.addWidget(self.label_Nl)
        layout.addWidget(self.input_Nl)
        layout.addWidget(self.label_Nd)
        layout.addWidget(self.input_Nd)
        layout.addWidget(self.compute_button)
        layout.addWidget(self.output_field)

        self.setLayout(layout)

    def compute_results(self):
        try:
            Nh = int(self.input_Nh.text())
            Nv = int(self.input_Nv.text())
            Nl = int(self.input_Nl.text())
            Nd = int(self.input_Nd.text())

            # Compute probabilities
            N_total = Nh + Nv
            Ph = Nh / N_total if N_total > 0 else 0
            Pl = Nl / N_total if N_total > 0 else 0
            Pd = Nd / N_total if N_total > 0 else 0
            Pv = Nv / N_total if N_total > 0 else 0

            # Compute Stokes Vector
            S0 = 1
            S1 = 2 * Ph - 1
            S2 = 2 * Pl - 1
            S3 = 2 * Pd - 1

            # Compute Density Matrix
            rho = 0.5 * np.array([
                [S0 + S3, S1 - 1j * S2],
                [S1 + 1j * S2, S0 - S3]
            ])

            # Compute Expectation Values
            sigma_x = np.array([[0, 1], [1, 0]])
            sigma_y = np.array([[0, -1j], [1j, 0]])
            sigma_z = np.array([[1, 0], [0, -1]])

            exp_S1 = np.real(np.trace(np.dot(rho, sigma_x)))
            exp_S2 = np.real(np.trace(np.dot(rho, sigma_y)))
            exp_S3 = np.real(np.trace(np.dot(rho, sigma_z)))

            # Display Results
            output_text = f"Probabilities:\nPh={Ph:.3f}, Pl={Pl:.3f}, Pd={Pd:.3f}, Pv={Pv:.3f}\n\n"
            output_text += f"Stokes Vector:\n[S0={S0:.3f}, S1={S1:.3f}, S2={S2:.3f}, S3={S3:.3f}]\n\n"
            output_text += f"Density Matrix:\n{rho}\n\n"
            output_text += f"Expectation Values:\nS1={exp_S1:.3f}, S2={exp_S2:.3f}, S3={exp_S3:.3f}"

            self.output_field.setText(output_text)

        except ValueError:
            self.output_field.setText("Please enter valid integers for Nh, Nv, Nl, and Nd.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingleQubitTomography()
    window.show()
    sys.exit(app.exec())
