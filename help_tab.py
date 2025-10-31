from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextBrowser, QPushButton, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QUrl
import webbrowser

FONT_FAMILY = "Arial Rounded MT Bold, Arial, Helvetica, sans-serif"

class HelpTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        title = QLabel("\U0001F4D6 Swim Meet Manager: Help & Onboarding")
        title.setFont(QFont(FONT_FAMILY, 16, QFont.Weight.Bold))

        doc = QTextBrowser()
        doc.setOpenExternalLinks(True)
        doc.setFont(QFont(FONT_FAMILY, 12))
        doc.setHtml('''
        <h3>Features</h3>
        <ul>
          <li>✔ Manage meet, athlete, and result data</li>
          <li>✔ Connect with Time Machine, Colorado, Daktronics</li>
          <li>✔ Export to CSV, PDF, Hytek formats</li>
          <li>✔ Live results webserver (see <b>Settings</b> tab)</li>
          <li>✔ Context menus & keyboard shortcuts everywhere</li>
        </ul>
        <h3>Keyboard navigation</h3>
        <ul>
          <li><b>Tab / Shift+Tab</b>: Move between fields/buttons</li>
          <li><b>Ctrl+S</b>: Save (on all tabs)</li>
          <li><b>F1</b>: Open this help tab</li>
        </ul>
        <h3>Getting Help</h3>
        <p>Check tooltips by hovering over fields and buttons.  

           For in-depth docs, see:
           <a href="https://github.com/Alex1-stack-dev/tm2">Project Wiki</a>
        </p>
        <h4>Contact & Support</h4>
        <p>Email: <a href="mailto:support@example.com">support@example.com</a></p>
        '''
        )
        btns = QHBoxLayout()
        contact_btn = QPushButton(QIcon(), "Contact Support")
        contact_btn.setToolTip("Opens your email client to contact support.")
        contact_btn.clicked.connect(self.contact_support)
        wiki_btn = QPushButton(QIcon(), "Open Wiki")
        wiki_btn.setToolTip("Opens the project documentation/wiki.")
        wiki_btn.clicked.connect(self.open_wiki)
        btns.addWidget(contact_btn)
        btns.addWidget(wiki_btn)
        btns.addStretch()
        layout.addWidget(title)
        layout.addWidget(doc)
        layout.addLayout(btns)
        self.setLayout(layout)
    def contact_support(self):
        webbrowser.open('mailto:support@example.com')
    def open_wiki(self):
        webbrowser.open('https://github.com/Alex1-stack-dev/tm2')
