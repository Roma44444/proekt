import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QSettings
from diary1 import Ui_MainWindow_1  # Переконайтеся, що ім'я імпортованого модуля правильне
from main_2 import MainDialog

# Підключення до бази даних
db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT,
    password TEXT
)''')
db.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS numbers1(
    id TEXT
)''')
db.commit()

# Створюємо таблиці 'records3' та 'records2' (якщо вони не існують)
cursor.execute('''CREATE TABLE IF NOT EXISTS records3(
    user_id,
    year,
    month,
    day,
    weekday,
    r_1,
    mood
)''')
db.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS records2(
    user_id TEXT,
    year TEXT,
    month TEXT,
    day TEXT,
    weekday TEXT,
    r_1 TEXT,
    mood TEXT
)''')
db.commit()


# Визначення класів для реєстрації та входу
class Registration(QMainWindow, Ui_MainWindow_1):
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.lb_11.setText('')
        self.pb_12.setText('Назад')
        self.pb_11.setText('Додати акаунт')
        self.pb_13.hide()

        self.pb_14.clicked.connect(self.togglePassword)
        self.le_12.setEchoMode(QLineEdit.Password)  # Початково приховувати пароль

        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_11.setIcon(icon2)
        self.pb_11.setIconSize(QSize(24, 24))

        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow_back_ios_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_12.setIcon(icon1)
        self.pb_12.setIconSize(QSize(24, 24))

        self.pb_11.pressed.connect(self.reg)
        self.pb_12.pressed.connect(self.login)

    def togglePassword(self):
        # Зміна режиму відображення пароля
        if self.le_12.echoMode() == QLineEdit.Password:
            self.le_12.setEchoMode(QLineEdit.Normal)
        else:
            self.le_12.setEchoMode(QLineEdit.Password)

    def login(self):
        self.login_window = Login()
        self.login_window.show()
        self.hide()

    def reg(self):
        user_login = self.le_11.text()
        user_password = self.le_12.text()

        if len(user_login) == 0:
            return

        if len(user_password) == 0:
            return

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users (login, password) VALUES ("{user_login}", "{user_password}")')
            cursor.execute('SELECT last_insert_rowid()')
            last_inserted_id = cursor.fetchone()[0]
            new_id = last_inserted_id + 1
            cursor.execute(f'UPDATE users SET id = {new_id} WHERE login = "{user_login}"')
            self.lb_11.setText(f'Акаунт {user_login} зареєстрований!')
            db.commit()
        else:
            self.lb_11.setText('Цей логін уже не доступний!')


class Login(QMainWindow, Ui_MainWindow_1):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.lb_11.setText('')
        self.pb_11.setText('Увійти')
        self.pb_12.setText('Зареєструватися')

        self.settings = QSettings("MyCompany", "MyApp")

        self.pb_14.clicked.connect(self.togglePassword)


        # Завантаження стану кнопки та введених даних
        self.loadSettings()


        self.pb_11.pressed.connect(self.login)
        self.pb_12.pressed.connect(self.reg)
        self.pb_13.toggled.connect(self.onToggle)
        self.le_12.setEchoMode(QLineEdit.Password)


    def loadSettings(self):
        # Завантаження налаштувань
        self.pb_13.setChecked(self.settings.value("toggleState", False, type=bool))
        if self.pb_13.isChecked():
            self.le_11.setText(self.settings.value("login", ""))
            self.le_12.setText(self.settings.value("password", ""))
            self.le_11.setReadOnly(True)
            self.le_12.setReadOnly(True)
        else:
            self.le_11.setReadOnly(False)
            self.le_12.setReadOnly(False)

    def saveSettings(self):
        # Збереження налаштувань
        if self.pb_13.isChecked():
            self.settings.setValue("login", self.le_11.text())
            self.settings.setValue("password", self.le_12.text())
        else:
            self.settings.setValue("login", "")
            self.settings.setValue("password", "")
        self.settings.setValue("toggleState", self.pb_13.isChecked())

    def onToggle(self):
        # Дії при зміні стану кнопки-перемикача
        if not self.pb_13.isChecked():
            self.settings.setValue("login", "")
            self.settings.setValue("password", "")
            self.le_11.setReadOnly(False)
            self.le_12.setReadOnly(False)
            self.settings.setValue("toggleState", self.pb_13.isChecked())
        else:
            self.le_11.setReadOnly(True)
            self.le_12.setReadOnly(True)

    def togglePassword(self):
        # Зміна режиму відображення пароля
        if self.le_12.echoMode() == QLineEdit.Password:
            self.le_12.setEchoMode(QLineEdit.Normal)
        else:
            self.le_12.setEchoMode(QLineEdit.Password)

    def reg(self):
        self.reg_window = Registration()
        self.reg_window.show()
        self.hide()

    def login(self):
        user_login = self.le_11.text()
        user_password = self.le_12.text()

        if len(user_login) == 0 or len(user_password) == 0:
            self.lb_11.setText('Помилка авторизації!')
            return

        cursor.execute(f'SELECT id, password FROM users WHERE login="{user_login}"')
        result = cursor.fetchone()

        if result and result[1] == user_password:
            self.lb_11.setText('Успішна авторизація!')
            self.user_id = result[0]  # Зберегти ID користувача

            db.commit()
            self.saveSettings()
            self.openMainWindow()
        else:
            self.lb_11.setText('Помилка авторизації!')


    def openMainWindow(self):
        self.main_window = MainDialog(self.user_id)  # Передати ID користувача до нового вікна
        self.main_window.show()

        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = Login()
    login_window.show()

    sys.exit(app.exec())
