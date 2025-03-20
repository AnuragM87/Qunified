import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from mainMenu import MainMenu
from tomography import SingleQubitTomography
from checker import DensityMatrixChecker
if __name__ == "__main__":
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()

    main_menu = MainMenu(stacked_widget)
    tomography = SingleQubitTomography(stacked_widget)
    density_checker = DensityMatrixChecker(stacked_widget)

    stacked_widget.addWidget(main_menu)
    stacked_widget.addWidget(tomography)
    stacked_widget.addWidget(density_checker)

    stacked_widget.setCurrentIndex(0)
    stacked_widget.show()

    sys.exit(app.exec())