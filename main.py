import sys

from PyQt6.QtWidgets import QApplication

from scroll_widget import ScrollableWindow

app = QApplication(sys.argv)
window = ScrollableWindow()
window.show()
sys.exit(app.exec())
