from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecureApp - Settings")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("Change Password", self)
        self.layout.addWidget(self.label)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter new password")
        self.layout.addWidget(self.password_input)

        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_password)
        self.layout.addWidget(self.save_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def save_password(self):
        new_password = self.password_input.text()
        print(f"Password changed to: {new_password}")