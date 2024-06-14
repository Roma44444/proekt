import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from PySide6.QtCore import QTimer
from diary2 import Ui_Dialog_1
from datetime import datetime
from maint3 import MyDialog1  # Імпортуємо клас MyDialog1 з файлу, де ви його описали

# Підключаємося до бази даних і створюємо курсор
db = sqlite3.connect('database.db')
cursor = db.cursor()


class MainDialog(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_1()
        self.ui.setupUi(self)
        self.user_id = user_id

#        cursor.execute("SELECT * FROM numbers LIMIT 1")
#        user = cursor.fetchone()
#        print(user)

        self.ui.pb_21.clicked.connect(self.openNewWindow)  # Прикріплюємо обробник натискання кнопки для відкриття нового вікна
        self.ui.pb_22.clicked.connect(self.clearTextAndConfirm)  # Прикріплюємо обробник натискання кнопки для очищення тексту з підтвердженням


        now = datetime.now()
        # Присвоюємо значення змінним
        self.year_value = now.year
        self.month_value = now.month
        self.day_value = now.day
        self.weekday_value = now.weekday()

        # Запускаємо таймер для збереження даних кожну секунду
        self.save_timer = QTimer(self)
        self.save_timer.timeout.connect(self.save_data)
        self.save_timer.start(1000)  # Запускаємо таймер з інтервалом 1 секунда

        # Запускаємо таймер для перевірки появи рядка в records2
        self.check_timer = QTimer(self)
        self.check_timer.timeout.connect(self.check_records2)
        self.check_timer.start(1000)  # Запускаємо таймер з інтервалом 1 секунда

        self.one_time_check_and_insert()

    def one_time_check_and_insert(self):
        # Перевіряємо наявність запису для поточного користувача, дати і дня тижня
        cursor.execute('''
                    SELECT * FROM records3
                    WHERE user_id = ? AND year = ? AND month = ? AND day = ? AND weekday = ?
                ''', (self.user_id, self.year_value, self.month_value, self.day_value, self.weekday_value))

        record = cursor.fetchone()


        if record is not None:  # Якщо запис знайдено
            self.ui.te_21.setText(record[5])  # Присвоюємо значення текстового поля
            self.ui.comboBox.setCurrentText(record[6])  # Присвоюємо значення комбобокса
        else:
            # Якщо запису немає, створюємо новий з початковими значеннями
            self.ui.te_21.setText("")
            self.ui.comboBox.setCurrentText("")
            cursor.execute('''
                INSERT INTO records3 (user_id, year, month, day, weekday, r_1, mood)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (self.user_id, self.year_value, self.month_value, self.day_value, self.weekday_value, "", ""))
            db.commit()

    def save_data(self):
        # Отримуємо значення з текстового поля і комбобокса
        text_value = self.ui.te_21.toPlainText()
        mood_value = self.ui.comboBox.currentText()

#        cursor.execute("SELECT * FROM numbers LIMIT 1")
#        user = cursor.fetchone()


         #Оновлюємо запис в таблиці 'records3'
        cursor.execute('''
            UPDATE records3
            SET r_1 = ?, mood = ?
            WHERE user_id = ? AND year = ? AND month = ? AND day = ? AND weekday = ?
        ''', (
        text_value, mood_value, self.user_id, self.year_value, self.month_value, self.day_value, self.weekday_value))
        db.commit()


    def check_records2(self):
        # Перевіряємо наявність запису в таблиці 'records2'
        cursor.execute("SELECT * FROM records2 LIMIT 1")
        row = cursor.fetchone()

        if row:
            # Якщо запис знайдено, оновлюємо відповідні змінні і поля інтерфейсу
            self.user_id = row[0]
            self.year_value = row[1]
            self.month_value = row[2]
            self.day_value = row[3]
            self.weekday_value = row[4]
            self.ui.te_21.setText(row[5])
            self.ui.comboBox.setCurrentText(row[6])
            # Видаляємо запис з таблиці 'records2'
            cursor.execute("DELETE FROM records2")
            db.commit()

    def openNewWindow(self):
        new_window = MyDialog1(self.user_id)  # Створюємо нове вікно
        new_window.exec()


    def clearTextAndConfirm(self):
        # Відображаємо діалогове вікно підтвердження для очищення тексту
        confirm_dialog = QMessageBox(self)
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Підтвердження")
        confirm_dialog.setText("Ви впевнені, що хочете видалити текст?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)

        yes_button = confirm_dialog.button(QMessageBox.Yes)
        yes_button.setText('Видалити')
        no_button = confirm_dialog.button(QMessageBox.No)
        no_button.setText('Скасувати')

        confirm_dialog.exec()

        if confirm_dialog.clickedButton() == yes_button:
            self.ui.te_21.clear()

    def closeEvent(self, event):
        # Відображаємо діалогове вікно підтвердження перед закриттям
        reply = QMessageBox.question(self, 'Повідомлення', 'Ви впевнені, що хочете закрити вікно?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                #cursor.execute("DELETE FROM numbers")  # Видаляємо записи з таблиці 'numbers'
                #db.commit()
                cursor.execute('''
                           DELETE FROM records3
                            WHERE r_1 = '' AND mood = ''
                        ''')
                db.commit()
            except Exception as e:
                print("Error:", e)
            db.close()  # Закриваємо базу даних
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog(1)
    main_dialog.show()
    sys.exit(app.exec())
