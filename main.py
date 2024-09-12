from PyQt5.QtWidgets import * #Віджети та сам QT
from PyQt5.QtGui import QFont #Шрифти
from PyQt5 import uic #для підключення файлу, зробленого в Qt Designer



class MyGui(QMainWindow): #Супер Клас для Імпорту та логіки кнопок в файлі
    def __init__(self):
        super(MyGui,self).__init__()
        uic.loadUi("mygui.ui",self)
        self.show()

        self.pushButton.clicked.connect(self.convert)
    def convert(self):
        try: #Команда для помилок(коли є помилка то воно направляє в ValueError)
            celsius = float(self.lineEdit.text())
            fahrenheit = (celsius * 9 / 5) + 32
            self.show_message(f"Температура у Фаренгейтах: {fahrenheit:.2f}")
        except ValueError:
            self.show_message("Будь ласка, введіть правильне число.")

    def show_message(self, msg): #Для виводу нового вікна з відповіддю
        message_box = QMessageBox()
        message_box.setText(msg)
        message_box.setWindowTitle("Result")
        message_box.exec_()

def main(): #Для створення програми та відображення вікна
    app = QApplication([])
    window = MyGui()
    window.setWindowTitle("Conventer")
    window.setFixedSize(605,250)
    app.exec_()

if __name__ == '__main__': #для перевірки модуля, чи воно працює
    main()


'''
i=1
while i:
    celsius = int(input("Set the temperature to degrees Celsius to convert this to Fahrenheit:"))
    fahrenheit = (celsius * 9 / 5) + 32
    print(fahrenheit)
    i=i+i
'''
#Программу на Pyqt5 я дивився на Ютубі:https://www.youtube.com/watch?v=MOItX2aKTGc&ab_channel=NeuralNine