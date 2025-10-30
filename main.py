import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
import utils.logger as logger

if __name__ == '__main__':
    logger.setup_logging()
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
