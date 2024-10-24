from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QMessageBox

from widgets import SimpleForm


class ScrollableWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.records_layout = QVBoxLayout(self)
        self.records_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.content_widget = QWidget()

        self.content_widget.setLayout(self.records_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidget(self.content_widget)
        scroll_area.setWidgetResizable(True)

        self.form = SimpleForm()
        self.form.form_submitted.connect(self.update_records_list)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.form)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)
        self.setWindowTitle("Scroll qilsa bo'ladigan oyna")

    def update_records_list(self, name: str, surname: str, age: int, gender: str, bio: str):
        if self.records_layout.count() + 1 <= 20:
            count = self.records_layout.count() + 1
            new_record = QLabel(f"{count}. Name: {name}, Surname: {surname}, Age: {age}, Gender: {gender}, Bio: {bio}")
            new_record.setStyleSheet(f"background-color: {"gray" if count % 2 == 0 else "black"}; padding: 10px;")
            self.records_layout.addWidget(new_record, alignment=Qt.AlignmentFlag.AlignTop)
        else:
            QMessageBox.warning(self, "Limit reached", "20tadan ortiq kiritish mumkin emas!")
