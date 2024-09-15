import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QWidget, QTextEdit, QFrame
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PromoWyszukiwacz")
        self.setGeometry(100, 100, 1920, 1080)  # Rozdzielczość okna 1920x1080

        # Layouty główne
        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QVBoxLayout()

        # Panel przycisków (lewa strona)
        button_panel = QVBoxLayout()
        button_label = QLabel("Tutaj przyciski do włączania wszystkich opcji w programie")
        button_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_panel.addWidget(button_label)

        # Dodaj przycisk (można dodać więcej w podobny sposób)
        button1 = QPushButton("Przycisk 1")
        button_panel.addWidget(button1)

        # GUI opcji (prawa strona)
        gui_panel = QVBoxLayout()
        gui_label = QLabel("Tutaj GUI opcji, programu uruchomionego po wybraniu przez naciśnięcie przycisku")
        gui_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        gui_panel.addWidget(gui_label)

        # Konsola na dole
        console_label = QLabel("Tutaj konsola, na przykład co znalazł, czy są promocje nowe po odświeżeniu, logi uruchomionego programu.")
        console_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        console_text = QTextEdit()
        console_text.setPlaceholderText("Wpisz komendy, np. /pomoc...")
        bottom_layout.addWidget(console_label)
        bottom_layout.addWidget(console_text)

        # Dodanie linii podziału (QFrame)
        line_vertical = QFrame()
        line_vertical.setFrameShape(QFrame.Shape.VLine)
        line_vertical.setFrameShadow(QFrame.Shadow.Sunken)

        line_horizontal = QFrame()
        line_horizontal.setFrameShape(QFrame.Shape.HLine)
        line_horizontal.setFrameShadow(QFrame.Shadow.Sunken)

        # Połączenie layoutów
        top_layout.addLayout(button_panel, 1)  # Panel przycisków (lewa strona)
        top_layout.addWidget(line_vertical)    # Pionowa linia
        top_layout.addLayout(gui_panel, 3)    # GUI opcji (prawa strona)
        
        main_layout.addLayout(top_layout)     # Górna część (przyciski + GUI)
        main_layout.addWidget(line_horizontal)  # Pozioma linia
        main_layout.addLayout(bottom_layout)  # Dolna część (konsola)

        # Centralny widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
