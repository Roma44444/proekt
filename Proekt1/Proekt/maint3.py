from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from diary3 import Ui_Dialog  # Імпортуємо користувацький інтерфейс
import sqlite3
from datetime import datetime

# Підключення до бази даних
db = sqlite3.connect('database.db')
cursor = db.cursor()

# Словник для назв місяців
MONTH_NAMES = {
    1: "Січень", 2: "Лютий", 3: "Березень", 4: "Квітень",
    5: "Травень", 6: "Червень", 7: "Липень", 8: "Серпень",
    9: "Вересень", 10: "Жовтень", 11: "Листопад", 12: "Грудень"
}

class MyDialog1(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.user_id = user_id

        self.ui.lb_31.setText("")

        # Поточна дата
        now = datetime.now()
        self.year_value = now.year
        self.month_value = now.month
        self.day_value = now.day
        self.weekday_value = now.weekday()
        self.month_1 = self.month_value

        # Ініціалізація мінімальних та максимальних років та місяців
        self.init_min_max_dates()

        # Встановлення початкової назви місяця
        self.update_month_label()

        # Завантаження записів з бази даних
        self.load_records()

        # Підключення кнопок до функцій
        self.ui.pb_33.clicked.connect(self.check_previous_month)
        self.ui.pb_34.clicked.connect(self.check_next_month)
        self.ui.pb_32.clicked.connect(self.close)
        self.ui.pb_35.clicked.connect(self.load_records)
        self.ui.de_31.dateChanged.connect(self.check_date)
        self.ui.pb_31.clicked.connect(self.move_record)
        self.ui.cb_31.currentTextChanged.connect(self.on_combobox_changed)

        # Підключення кнопок таблиці (pb_t1 - pb_t42) до функції
        for i in range(1, 43):
            button = getattr(self.ui, f"pb_t{i}")
            button.clicked.connect(self.select_date_button)

        self.update_navigation_buttons()  # Оновлення кнопок навігації при ініціалізації

        self.init_min_max_dates()

    def on_combobox_changed(self):
        if self.ui.pb_35.isChecked() and self.ui.pb_35.isChecked():
            self.load_records()


    def init_min_max_dates(self):
        """
        Ініціалізація мінімальних та максимальних років і місяців для навігації.
        """
        # Знайти мінімальний і максимальний рік
        cursor.execute("SELECT MIN(year), MAX(year) FROM records3 WHERE user_id=?", (self.user_id,))
        min_year_result, max_year_result = cursor.fetchone()

        if min_year_result is not None and max_year_result is not None:
            self.min_year = min_year_result
            self.max_year = max_year_result

            # Ініціалізація мінімального місяця для мінімального року
            self.min_month = None
            for month in range(1, 13):
                cursor.execute("SELECT 1 FROM records3 WHERE user_id=? AND year=? AND month=? LIMIT 1",
                               (self.user_id, self.min_year, month))
                if cursor.fetchone():
                    self.min_month = month
                    break

            # Ініціалізація максимального місяця для максимального року
            self.max_month = None
            for month in range(12, 0, -1):
                cursor.execute("SELECT 1 FROM records3 WHERE user_id=? AND year=? AND month=? LIMIT 1",
                               (self.user_id, self.max_year, month))
                if cursor.fetchone():
                    self.max_month = month
                    break

    def load_records(self):
        """
        Завантаження записів з таблиці records3 для поточного користувача, року та місяця.
        Якщо активовано фільтр за настроєм, додати його до запиту.
        """
        query = "SELECT * FROM records3 WHERE user_id=? AND year=? AND month=?"
        params = [self.user_id, self.year_value, self.month_value]

        if self.ui.pb_35.isChecked():
            mood = self.ui.cb_31.currentText()
            if mood.isdigit():
                params.append(int(mood))  # Перетворюємо рядок на ціле число
                query += " AND mood=?"

        cursor.execute(query, params)
        records = cursor.fetchall()


        # Оновлення таблиці кнопок на основі отриманих записів
        self.update_button_table(records)

    def update_button_table(self, records):
        """
        Оновлення таблиці кнопок на основі записів.
        Кнопки встановлюються неактивними та без тексту, якщо немає відповідного запису.
        """
        # Зробити всі кнопки неактивними та без тексту
        for i in range(1, 43):
            button = getattr(self.ui, f"pb_t{i}")
            button.setEnabled(False)
            button.setText("")
            button.mood = None  # Скидання атрибута настрою

        # Знаходимо день тижня для 1-го числа поточного місяця
        first_day_of_month = datetime(self.year_value, self.month_value, 1).weekday()
        start_index = first_day_of_month + 1  # Оскільки в нашій таблиці кнопок нумерація починається з 1

        # Відображення записів у кнопках
        for record in records:
            year = int(record[1])
            month = int(record[2])
            day = int(record[3])
            mood = record[6]
            mood = int(mood or 0)
            index = start_index + day - 1  # Зміщуємо індекс відповідно до дня місяця
            number = int(self.ui.cb_31.currentText() or 0)


            if not self.ui.pb_35.isChecked() or (self.ui.pb_35.isChecked() and mood == number):
                button = getattr(self.ui, f"pb_t{index}")
                button.setVisible(True)
                if year == self.year_value and month == self.month_1 and day == self.day_value:
                    button.setText(f"({day})")
                else:
                    button.setText(str(day))
                button.record = record
                button.mood = mood  # Додавання атрибута настрою
                button.setEnabled(True)  # Зробити кнопку активною

        # Відображення сьогоднішньої дати в дужках
        today = datetime.now()
        if self.year_value == today.year and self.month_value == today.month:
            day = today.day
            index = start_index + day - 1
            button = getattr(self.ui, f"pb_t{index}")
            button.setText(f"({day})")

    def update_month_label(self):
        """
        Оновлення текстової назви місяця в лейблі.
        """
        self.ui.lb_32.setText(f"{MONTH_NAMES[self.month_value]}")
        self.ui.lb_33.setText(f"{self.year_value}")

    def update_navigation_buttons(self):
        """
        Оновлює стан кнопок навігації (`pb_33` та `pb_34`) залежно від поточного року та місяця.
        """

        # Перевірка, чи поточна сторінка показує найстаріший запис
        if self.min_year is not None and self.min_month is not None:
            if self.year_value == int(self.min_year) and self.month_value == self.min_month:
                self.ui.pb_33.setEnabled(False)
            else:
                self.ui.pb_33.setEnabled(True)

        # Перевірка, чи поточна сторінка показує найновіший запис
        if self.max_year is not None and self.max_month is not None:
            if self.year_value == int(self.max_year) and self.month_value == self.max_month:
                self.ui.pb_34.setEnabled(False)
            else:
                self.ui.pb_34.setEnabled(True)

    def check_previous_month(self):
        """
        Перевіряє, чи поточний місяць не є найстарішим. Якщо так, переходить до попереднього місяця.
        """
        if self.ui.pb_33.isEnabled():
            self.previous_month()

    def check_next_month(self):
        """
        Перевіряє, чи поточний місяць не є найновішим. Якщо так, переходить до наступного місяця.
        """
        if self.ui.pb_34.isEnabled():
            self.next_month()

    def previous_month(self):
        """
        Перехід до попереднього місяця.
        Якщо поточний місяць - січень, перейти до грудня попереднього року.
        Перевірити, чи є записи в попередньому місяці.
        """
        new_year, new_month = self.find_nearest_month_with_records(self.year_value, self.month_value, -1)
        if new_year is not None and new_month is not None:
            self.year_value, self.month_value = new_year, new_month
            self.update_month_label()
            self.load_records()

    def next_month(self):
        """
        Перехід до наступного місяця.
        Якщо поточний місяць - грудень, перейти до січня наступного року.
        Перевірити, чи є записи в наступному місяці.
        """
        new_year, new_month = self.find_nearest_month_with_records(self.year_value, self.month_value, 1)
        if new_year is not None and new_month is not None:
            self.year_value, self.month_value = new_year, new_month
            self.update_month_label()
            self.load_records()

    def find_nearest_month_with_records(self, year, month, step):
        """
        Знаходить найближчий місяць з записами.
        """

        # Якщо поточний місяць і рік співпадають з мінімальними і ми рухаємося назад, повернути None, None
        if step < 0 and year == self.min_year and month == self.min_month:
            return None, None

        # Якщо поточний місяць і рік співпадають з максимальними і ми рухаємося вперед, повернути None, None
        if step > 0 and year == self.max_year and month == self.max_month:
            return None, None

        original_year0, original_month0 = self.max_year, self.max_month
        original_year1, original_month1 = self.min_year, self.min_month

        original_year1 = int(original_year1)
        original_month1 = int(original_month1)
        original_year0 = int(original_year0)
        original_month0 = int(original_month0)

        while True:
            # Крок вперед або назад
            month += step
            if month < 1:
                month = 12
                year -= 1
            elif month > 12:
                month = 1
                year += 1

            if (month == original_month0 and year == original_year0):
                self.ui.pb_34.setEnabled(False)
            else:
                self.ui.pb_34.setEnabled(True)

            if (month == original_month1 and year == original_year1):
                self.ui.pb_33.setEnabled(False)
            else:
                self.ui.pb_33.setEnabled(True)

            if self.has_records(year, month):
                return year, month


        return None, None

    def has_records(self, year, month):
        """
        Перевірка, чи є записи для даного року та місяця.
        """
        query = "SELECT 1 FROM records3 WHERE user_id=? AND year=? AND month=? LIMIT 1"
        cursor.execute(query, (self.user_id, year, month))
        result = cursor.fetchone()
        return result is not None

    def check_date(self):
        """
        Перевірка наявності запису для обраної дати.
        Якщо запис знайдено, оновити мітку lb_31 та встановити запис у pb_31.
        Якщо запис не знайдено, оновити мітку відповідним повідомленням.
        """
        date = self.ui.de_31.date().toString("yyyy-MM-dd")
        year, month, day = map(int, date.split('-'))
        query = "SELECT * FROM records3 WHERE user_id=? AND year=? AND month=? AND day=?"
        cursor.execute(query, (self.user_id, year, month, day))
        record = cursor.fetchone()
        if record:
            self.ui.lb_31.setText("За введеною вами датою є збіги")
            self.ui.pb_31.record = record
        else:
            self.ui.lb_31.setText("За введеною вами датою збігів немає")

    def select_date_button(self):
        """
        Обробка натискання кнопок у таблиці кнопок.
        Запис, що відповідає обраній кнопці, встановлюється у pb_31.
        """
        sender = self.sender()
        if hasattr(sender, 'record'):
            self.ui.pb_31.record = sender.record
        else:
            self.ui.pb_31.record = None

    def close(self):
        """
        Закриття вікна.
        """
        self.accept()

    def move_record(self):
        """
        Переміщення запису з таблиці records3 до records2.
        """
        record = getattr(self.ui.pb_31, 'record', None)
        if record is not None:
            cursor.execute("INSERT INTO records2 VALUES (?, ?, ?, ?, ?, ?, ?)", record)
            db.commit()
            self.accept()
        else:
            QMessageBox.warning(self, "Помилка", "Не вибрано жодного запису для переміщення.")

if __name__ == "__main__":
    app = QApplication([])
    dialog = MyDialog1(user_id=1)  # Передати ID користувача
    dialog.show()
    app.exec()
