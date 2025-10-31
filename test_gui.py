import pytest
from PyQt6.QtWidgets import QApplication, QMessageBox
from meet_tab import MeetTab
import sys

@pytest.fixture(scope="session")
def app():
    return QApplication(sys.argv)

def test_meet_tab_required_fields(qtbot, app):
    tab = MeetTab()
    qtbot.addWidget(tab)
    tab.name.setText("")
    tab.date.setText("bad-date")
    qtbot.mouseClick(tab.findChild(QPushButton), qtbot.MouseButton.LeftButton)
    # Simulate testing that warning pops up, etc.
