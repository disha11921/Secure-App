from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QFileDialog, QLineEdit, QTextEdit, QListWidget
from models.security import SecurityManager
import os

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecureApp - Home")
        self.setGeometry(100, 100, 400, 400)

        self.security_manager = SecurityManager()
        self.layout = QVBoxLayout()

        self.label = QLabel("Welcome to SecureApp", self)
        self.layout.addWidget(self.label)

        self.encrypt_button = QPushButton("Encrypt File", self)
        self.encrypt_button.clicked.connect(self.encrypt_file)
        self.layout.addWidget(self.encrypt_button)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter password to save")
        self.layout.addWidget(self.password_input)

        self.save_password_button = QPushButton("Save Password", self)
        self.save_password_button.clicked.connect(self.save_password)
        self.layout.addWidget(self.save_password_button)

        self.retrieve_passwords_button = QPushButton("Retrieve Passwords", self)
        self.retrieve_passwords_button.clicked.connect(self.retrieve_passwords)
        self.layout.addWidget(self.retrieve_passwords_button)

        self.password_display = QTextEdit(self)
        self.password_display.setReadOnly(True)
        self.layout.addWidget(self.password_display)

        # قائمة لعرض الملفات المشفرة
        self.encrypted_files_list = QListWidget(self)
        self.layout.addWidget(self.encrypted_files_list)

        self.show_files_button = QPushButton("Show Encrypted Files", self)
        self.show_files_button.clicked.connect(self.show_encrypted_files)
        self.layout.addWidget(self.show_files_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def encrypt_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Encrypt", "", "All Files (*)", options=options)
        if file_path:
            encrypted_data = self.security_manager.encrypt_file(file_path)
            self.security_manager.save_encrypted_file(encrypted_data, os.path.basename(file_path))
            self.label.setText(f"Encrypted: {os.path.basename(file_path)}")

    def save_password(self):
        password = self.password_input.text()
        if password:
            self.security_manager.save_password(password)
            self.label.setText("Password saved successfully.")
            self.password_input.clear()

    def retrieve_passwords(self):
        passwords = self.security_manager.retrieve_passwords()
        self.password_display.setPlainText("\n".join(passwords) if passwords else "No passwords saved.")

    def show_encrypted_files(self):
        self.encrypted_files_list.clear()  # مسح القائمة الحالية
        encrypted_files_dir = "encrypted_data/images"
        if os.path.exists(encrypted_files_dir):
            for filename in os.listdir(encrypted_files_dir):
                self.encrypted_files_list.addItem(filename)
        else:
            self.encrypted_files_list.addItem("No encrypted files found.")