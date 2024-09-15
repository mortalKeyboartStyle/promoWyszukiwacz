import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ustawienia rozmiaru okna
        self.setWindowTitle("Okno 1920x1080")
        self.setGeometry(100, 100, 1920, 1080)  # (x, y, width, height)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    # Wyświetlenie okna
    window.show()

    # Uruchomienie głównej pętli aplikacji
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
