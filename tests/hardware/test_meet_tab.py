import pytest
from PyQt6.QtWidgets import QApplication
from meet_tab import MeetTab
import sys

@pytest.fixture(scope="session")
def app():
    return QApplication(sys.argv)

def test_required_fields_inline_warning(qtbot, app):
    tab = MeetTab()
    qtbot.addWidget(tab)
    tab.name.setText("")
    tab.date.setText("bad-date")
    qtbot.mouseClick(tab.save_btn, qtbot.MouseButton.LeftButton)
    assert tab.warn_name.isVisible()
    assert tab.warn_date.isVisible()
    tab.name.setText("Championship")
    tab.date.setText("2025-11-01")
    qtbot.keyClick(tab.save_btn, Qt.Key.Key_Enter)
    assert not tab.warn_name.isVisible()
    assert not tab.warn_date.isVisible()

def test_all_valid_and_save(qtbot, app):
    tab = MeetTab()
    qtbot.addWidget(tab)
    tab.name.setText("District Final")
    tab.date.setText("2025-11-01")
    triggered = []
    def on_save():
        triggered.append(True)
    tab.save_btn.clicked.connect(on_save)
    qtbot.mouseClick(tab.save_btn, qtbot.MouseButton.LeftButton)
    assert triggered  # Confirm save triggered after valid
