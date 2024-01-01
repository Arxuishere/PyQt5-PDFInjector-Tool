import sys
import os
import PyPDF4
from PyPDF4.generic import DictionaryObject, NameObject, TextStringObject, EncodedStreamObject, ArrayObject

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QFileDialog, QWidget, QPlainTextEdit, QButtonGroup, QMessageBox, QGroupBox, QInputDialog
from PyQt5.QtCore import Qt

js_payloads = {
    # ... (unchanged)
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # ... (unchanged)

    def inject(self):
        input_pdf = self.input_line_edit.text()
        output_pdf = self.output_line_edit.text()

        if not input_pdf or not os.path.isfile(input_pdf):
            self.show_error_message("Error: Invalid input file")
            return

        if not output_pdf:
            self.show_error_message("Error: No output file selected")
            return

        injection_method = self.get_selected_injection_method()
        if not injection_method:
            self.show_error_message("Error: No injection method selected")
            return

        try:
            self.perform_injection(input_pdf, output_pdf, injection_method)
            self.show_success_message("Injection successful")

        except Exception as e:
            self.show_error_message(f"Error: {str(e)}")

    def get_selected_injection_method(self):
        if self.url_radio_button.isChecked():
            return "url"
        elif self.file_radio_button.isChecked():
            return "file"
        elif self.js_radio_button.isChecked():
            return "js"
        else:
            return None

    def perform_injection(self, input_pdf, output_pdf, injection_method):
        # Handle injection based on the selected method
        if injection_method == "url":
            malicious_url = self.url_line_edit.text()
            self.validate_input(malicious_url, "Malicious URL")
            inject_url(input_pdf, output_pdf, malicious_url)

        elif injection_method == "file":
            file_to_inject = self.file_line_edit.text()
            self.validate_input(file_to_inject, "File to inject")
            inject_file(input_pdf, output_pdf, file_to_inject)

        elif injection_method == "js":
            js_code = self.js_plain_text_edit.toPlainText()
            self.validate_input(js_code, "JavaScript code")
            if js_code.endswith('.js'):
                with open(js_code, 'r') as js_file:
                    js_code = js_file.read()
            inject_js(input_pdf, output_pdf, js_code)

    def validate_input(self, value, field_name):
        if not value:
            self.show_error_message(f"Error: {field_name} cannot be empty")

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("PDF Injector")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def show_success_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("PDF Injector")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    # ... (unchanged)

# ... (unchanged)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
