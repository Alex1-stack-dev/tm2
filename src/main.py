import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import pyqtSignal, QObject
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
from database.meet_manager import MeetManager
from timing.g2_controller import G2Controller
from gui.main_window import MainWindow

class ErrorSignal(QObject):
    error_signal = pyqtSignal(str)

def main():
    # Persistent DB setup
    engine = create_engine('sqlite:///timemachine.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    meet_manager = MeetManager(session)
    # Shared session data
    heats = []
    # Hardware controller
    timing_controller = G2Controller()
    # Error signal connector
    class _ErrorSignal(QObject): error_signal = pyqtSignal(str)
    error_signal_obj = _ErrorSignal()
    app = QApplication(sys.argv)
    window = MainWindow(session, meet_manager, timing_controller, heats, error_signal_obj.error_signal)
    def show_error(msg):
        QMessageBox.critical(window, "Error", msg)
    error_signal_obj.error_signal.connect(show_error)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
