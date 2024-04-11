from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
import sys
from random import randint
import sqlite3
from mainwindow import Ui_MainWindow
from prestart import Ui_Prestart
from dialogwid import Ui_Lang
from anagramma import Ui_GameOne
from result import Ui_Result
from tableshulte import Ui_Shulte
from findletters import Ui_findletters, table_let
from qqqqqqqq import Ui_Stat
from passwordcheck import Ui_Pass
import time

language = 'Русский язык'

table = ['рецензия',
         'рубить',
         'салат',
         'терпеливо',
         'экономия',
         'эстрада',
         'аппетит',
         'банда',
         'борец',
         'вылезать',
         'интуиция',
         'контур',
         'маневр',
         'мрачно',
         'мучиться',
         'наткнуться',
         'обрыв',
         'огненный',
         'отделить',
         'отметка',
         'привыкать',
         'проживание',
         'разрушать',
         'скакать',
         'сотрудничать',
         'фуражка',
         'хохот',
         'шелковый',
         'шина',
         'больничный',
         'бронзовый',
         'валенок',
         'ввиду',
         'вертеться',
         'всяческий',
         'выкинуть',
         'выходной',
         'диагностика',
         'заблуждение',
         'заводской',
         'заповедь',
         'излишний',
         'каникулы',
         'комар',
         'контейнер',
         'координата',
         'лопнуть',
         'люк',
         'майка',
         'небось',
         'неправильно',
         'отработать',
         'парус',
         'перец',
         'пират',
         'пластиковый',
         'прибежать',
         'расположиться',
         'родительский',
         'сбегать',
         'сегмент',
         'скромно',
         'смущать',
         'снизиться',
         'стенд',
         'тигр',
         'убедительный',
         'удивлять',
         'упоминаться',
         'устранение',
         'аптека',
         'бак',
         'безумие',
         'будить',
         'вздрагивать',
         'дежурство',
         'залезть',
         'кирпичный',
         'кустарник',
         'мониторинг',
         'ограничивать',
         'отводить',
         'откровение',
         'оцениваться',
         'павильон',
         'подчиненный',
         'помещаться',
         'поплыть',
         'проводник',
         'пространственный',
         'проявиться',
         'ранение',
         'санкция',
         'серебро',
         'составляющая',
         'спустить',
         'схватиться',
         'табличка',
         'тоненький',
         'уделять',
         'валить',
         'взлететь',
         'внушать',
         'глупо',
         'грядущий',
         'ежели',
         'закуска',
         'календарь',
         'командный',
         'кулиса',
         'мирно',
         'неторопливо',
         'опомниться',
         'орбита',
         'очистка',
         'подмосковный',
         'просвещение',
         'публиковать',
         'расписание',
         'свитер',
         'сотворить',
         'сравнительный',
         'сходный',
         'терраса',
         'укол',
         'упрек',
         'холдинг',
         'цепляться',
         'эхо',
         'грамотный',
         'грусть',
         'достоверный',
         'злиться',
         'количественный',
         'конструктивный',
         'лебедь',
         'наводить',
         'оправдываться',
         'отделять',
         'первое',
         'поставлять',
         'пошутить',
         'прекратиться',
         'призрак',
         'лицей',
         'Уфа',
         'семья',
         'друзья',
         'гений',
         'лучший',
         'питон',
         'окно',
         'брат',
         'дружба']


class FirstPage(Ui_MainWindow, QMainWindow):
    def __init__(self):
        global language
        super().__init__()
        self.setupUi(self)
        self.settingsbtn.clicked.connect(self.settings)
        self.startbtn.clicked.connect(self.prestart)
        self.staticbtn.clicked.connect(self.st)

        self.window_set = None
        self.window_prest = None
        self.window_stat = None

    def settings(self):
        self.window_set = Settings()

        self.show()
        self.window_set.show()

    def prestart(self):
        self.window_prest = Prest()
        self.window_prest.show()
        self.close()

    def st(self):
        self.window_set = Statistic()
        self.window_set.update()
        self.window_set.show()




class Statistic(Ui_Stat, QMainWindow):
    def __init__(self):
        global language
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("stat.db")
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM stat").fetchall()
        self.tableWidget.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        if language == 'Башкорт тель':
            self.tableWidget.setHorizontalHeaderLabels(['Тестлау тибы', 'Тест датаһы', 'Үтеү ваҡыты', 'Һөҙөмтә'])
        else:
            self.tableWidget.setHorizontalHeaderLabels(
                ['Тип тестирования', 'Дата тестирования', 'Время прохождения', 'Результат'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}
        self.pushButton.clicked.connect(self.push)

    def push(self):
        self.close()


class Settings(Ui_Lang, QWidget):
    def __init__(self):
        global language
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.res)
        self.radioButton.toggled.connect(self.ru)
        self.radioButton_2.toggled.connect(self.ba)

    def res(self):
        self.close()

    def ru(self):
        global language
        language = 'Русский язык'
        self.lang()

    def ba(self):
        global language
        language = 'Башкорт тель'
        self.lang()

    def lang(self):
        global language, ex
        if language == 'Башкорт тель':
            self.label.setText('Тель')
            ex.label.setText("Иғтибар күнекмәһе")
            ex.startbtn.setText("Башлау")
            ex.staticbtn.setText("Статистикаһы")
            ex.settingsbtn.setText("Көйләүҙәр")
        else:
            self.label.setText('Язык')
            ex.staticbtn.setText('Статистика')
            ex.label.setText("Тренировка внимания")
            ex.startbtn.setText("Начать")
            ex.staticbtn.setText("Статистика")
            ex.settingsbtn.setText("Настройки")
        self.update()
        ex.update()


class Prest(Ui_Prestart, QMainWindow):
    def __init__(self):
        global language
        super().__init__()
        self.setupUi(self)
        self.game = None
        if language == 'Башкорт тель':
            self.label.setText('Сайларга режим')
            self.label_2.setText('Языгыз сүз киресенчә, уен берерга кадәр бара хата')
            self.label_3.setText('Арту тәртибендә 1 дән 25 саннарны сайлагыз')
            self.label_7.setText('Виртуаль клавиатура кулланып сүз языгыз')
            self.backbtn.setText("Кирегә")
            self.label_8.setText('Һеҙгә бөтә паролдәрегеҙҙе төҙөргә кәрәк (бөтә паролдәрҙе алдан файлға яҙырға кәрәк)')
        else:

            self.label.setText("Выберите режим")
            self.label_2.setText("Вам нужно будет записать слово в обратном порядке Игра идёт до 1 ошибки")
            self.backbtn.setText("Назад")
            self.label_3.setText("Вам нужно нажать на числа от 1 до 25 по порядку")
            self.label_7.setText("Записать слово, используя виртуальную клавиатуру")
            self.label_8.setText("Вам нужно повтроить все свои пароли (все пароли нужно заранее записать в файл)")
        self.backbtn.clicked.connect(self.back)
        self.findletter.clicked.connect(self.let)
        self.findnumber.clicked.connect(self.numb)
        self.findanargamma.clicked.connect(self.anag)
        self.findletter_2.clicked.connect(self.password)

    def back(self):
        self.hide()
        ex.show()

    def anag(self):
        self.game = One()
        self.game.show()
        self.close()

    def numb(self):
        self.game = Two()
        self.game.show()
        self.close()

    def let(self):
        self.game = Three()
        self.game.show()
        self.close()

    def password(self):
        self.game = Four()
        self.game.show()
        self.close()


class One(Ui_GameOne, QMainWindow):
    def __init__(self):
        global language
        super().__init__()
        self.setupUi(self)
        if language == 'Башкорт тель':
            self.corrword.setText('Дөрес')
            self.timeword.setText('Ваҡыт ҡалды')
        else:
            self.corrword.setText('Верно')
            self.timeword.setText('Осталось времени')
        self.res = 0
        self.timer = time.time()
        self.sec = QTimer(self)
        self.sec.setInterval(1000)
        self.sec.timeout.connect(self.showtime)
        self.sec.start()
        self.time = 50
        self.prerv = 0
        self.r = None
        self.slovo = table[randint(0, 153)]
        self.corrnum.display(str(self.res))
        self.word.setText(self.slovo)
        self.ansbtn.clicked.connect(self.check)

    def check(self):
        if self.slovo[::-1] == self.answord.text():
            self.res += 1
            self.time = 30
            self.upd()
        else:
            self.data()

    def upd(self):
        self.slovo = table[randint(0, 153)]
        self.corrnum.display(str(self.res))
        self.word.setText(self.slovo)
        self.answord.clear()

    def data(self):
        t = int(time.time() - self.timer)
        m = str((t % 3600) // 60)
        s = str(t % 3600 % 60)
        if len(s) < 2:
            s = '0' + s
        self.r = TempWind(self.res, 1, m + ':' + s)
        self.r.show()
        self.close()

    def showtime(self):
        self.timenum.display(self.time)
        self.time -= 1
        if self.time < 0 and self.prerv == 0:
            self.sec.stop()
            self.time = 0
            self.data()

    def timerStart(self):
        self.sec.start()


class Two(QWidget, Ui_Shulte):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.matrix = list(range(1, 25))
        self.res = 0
        self.timer = time.time()
        self.r = None
        self.pushButton.clicked.connect(self.right)
        self.pushButton_2.clicked.connect(self.right)
        self.pushButton_3.clicked.connect(self.right)
        self.pushButton_4.clicked.connect(self.right)
        self.pushButton_5.clicked.connect(self.right)
        self.pushButton_6.clicked.connect(self.right)
        self.pushButton_7.clicked.connect(self.right)
        self.pushButton_8.clicked.connect(self.right)
        self.pushButton_9.clicked.connect(self.right)
        self.pushButton_10.clicked.connect(self.right)
        self.pushButton_11.clicked.connect(self.right)
        self.pushButton_12.clicked.connect(self.right)
        self.pushButton_13.clicked.connect(self.right)
        self.pushButton_14.clicked.connect(self.right)
        self.pushButton_15.clicked.connect(self.right)
        self.pushButton_16.clicked.connect(self.right)
        self.pushButton_17.clicked.connect(self.right)
        self.pushButton_18.clicked.connect(self.right)
        self.pushButton_19.clicked.connect(self.right)
        self.pushButton_20.clicked.connect(self.right)
        self.pushButton_21.clicked.connect(self.right)
        self.pushButton_22.clicked.connect(self.right)
        self.pushButton_23.clicked.connect(self.right)
        self.pushButton_24.clicked.connect(self.right)
        self.pushButton_25.clicked.connect(self.right)

    def right(self):
        n = self.sender().text()

        if self.matrix:
            if int(n) == self.matrix[0]:
                del self.matrix[0]
                self.res += 1
            else:
                self.data()
        else:
            self.res += 1
            self.data()

    def data(self):
        t = int(time.time() - self.timer)
        m = str((t % 3600) // 60)
        s = str(t % 3600 % 60)
        if len(s) < 2:
            s = '0' + s
        self.r = TempWind(self.res, 2, m + ':' + s)
        self.r.show()
        self.close()


class Three(QWidget, Ui_findletters):
    def __init__(self):
        global language
        super().__init__()
        self.setupUi(self)
        self.sec = QTimer(self)
        self.sec.setInterval(1000)
        self.sec.timeout.connect(self.showtime)
        self.sec.start()
        self.time = 50
        self.res = 0
        self.timer = time.time()
        self.r = None
        self.table = table_let
        if language == 'Башкорт тель':
            self.resword.setText('Дөрес')
            self.timeword.setText('Вакыт калды')
        else:
            self.resword.setText('Верно')
            self.timeword.setText('Осталось времени')
        self.word = [self.table[randint(0, 35)] for _ in range(8)]
        f = open('generated_password.txt', mode='a', encoding='utf8')


        f.write(''.join(self.word))
        f.write('\n')
        f.close()
        self.word = ''.join(self.word)
        self.outputword.setText(self.word)
        self.prerv = 0
        self.pushButton.clicked.connect(self.right)
        self.pushButton_2.clicked.connect(self.right)
        self.pushButton_3.clicked.connect(self.right)
        self.pushButton_4.clicked.connect(self.right)
        self.pushButton_5.clicked.connect(self.right)
        self.pushButton_6.clicked.connect(self.right)
        self.pushButton_7.clicked.connect(self.right)
        self.pushButton_8.clicked.connect(self.right)
        self.pushButton_9.clicked.connect(self.right)
        self.pushButton_10.clicked.connect(self.right)
        self.pushButton_11.clicked.connect(self.right)
        self.pushButton_12.clicked.connect(self.right)
        self.pushButton_13.clicked.connect(self.right)
        self.pushButton_14.clicked.connect(self.right)
        self.pushButton_15.clicked.connect(self.right)
        self.pushButton_16.clicked.connect(self.right)
        self.pushButton_17.clicked.connect(self.right)
        self.pushButton_18.clicked.connect(self.right)
        self.pushButton_19.clicked.connect(self.right)
        self.pushButton_20.clicked.connect(self.right)
        self.pushButton_21.clicked.connect(self.right)
        self.pushButton_22.clicked.connect(self.right)
        self.pushButton_23.clicked.connect(self.right)
        self.pushButton_24.clicked.connect(self.right)
        self.pushButton_25.clicked.connect(self.right)
        self.pushButton_26.clicked.connect(self.right)
        self.pushButton_27.clicked.connect(self.right)
        self.pushButton_28.clicked.connect(self.right)
        self.pushButton_29.clicked.connect(self.right)
        self.pushButton_30.clicked.connect(self.right)
        self.pushButton_31.clicked.connect(self.right)
        self.pushButton_32.clicked.connect(self.right)
        self.pushButton_33.clicked.connect(self.right)
        self.pushButton_34.clicked.connect(self.right)
        self.pushButton_35.clicked.connect(self.right)
        self.pushButton_36.clicked.connect(self.right)

    def showtime(self):
        self.timenum.display(self.time)
        self.time -= 1
        if self.time < 0 and self.prerv == 0:
            self.sec.stop()
            self.time = 0
            self.data()

    def timerStart(self):
        self.sec.start()

    def data(self):
        t = int(time.time() - self.timer)
        m = str((t % 3600) // 60)
        s = str(t % 3600 % 60)
        if len(s) < 2:
            s = '0' + s
        self.r = TempWind(self.res, 3, m + ':' + s)
        self.r.show()
        self.close()

    def right(self):
        n = self.sender().text()
        if n == self.word[0]:
            self.word = self.word[1:]
            if len(self.word) == 0:
                self.time = 30
                self.res += 1
                self.word = [self.table[randint(0, 35)] for _ in range(8)]
                self.word = ''.join(self.word)
                self.outputword.setText(self.word)
                self.resnum.display(str(self.res))
        else:
            self.prerv = 1
            self.data()


class Four(QMainWindow, Ui_Pass):
    def __init__(self):
        global language
        super().__init__()
        self.setupUi(self)
        if language == 'Башкорт тель':
            self.corrword.setText('Дөрес')
            self.timeword.setText('Ваҡыт ҡалды')
        else:
            self.corrword.setText('Верно')
            self.timeword.setText('Осталось времени')
        self.res = 0
        self.timer = time.time()
        self.sec = QTimer(self)
        self.sec.setInterval(1000)
        self.sec.timeout.connect(self.showtime)
        self.sec.start()
        self.time = 50
        self.prerv = 0
        self.r = None
        f = open('pass.txt', mode='r', encoding='utf8')
        f = [line.rstrip() for line in f.readlines()]
        self.pass_table = f
        self.slovo = self.pass_table[randint(0, len(self.pass_table) - 1)]
        self.corrnum.display(str(self.res))
        self.password.setText(self.slovo)
        self.ansbtn.clicked.connect(self.check)

    def check(self):
        if self.password.text() == self.answord.text():
            self.res += 1
            self.time = 30
            self.upd()
        else:
            self.data()

    def upd(self):
        self.slovo = self.pass_table[randint(0, len(self.pass_table) - 1)]
        self.corrnum.display(str(self.res))
        self.password.setText(self.slovo)
        self.answord.clear()

    def data(self):
        t = int(time.time() - self.timer)
        m = str((t % 3600) // 60)
        s = str(t % 3600 % 60)
        if len(s) < 2:
            s = '0' + s
        self.r = TempWind(self.res, 4, m + ':' + s)
        self.r.show()
        self.close()

    def showtime(self):
        self.timenum.display(self.time)
        self.time -= 1
        if self.time < 0 and self.prerv == 0:
            self.sec.stop()
            self.time = 0
            self.data()

    def timerStart(self):
        self.sec.start()


class TempWind(Ui_Result, QMainWindow):
    def __init__(self, res, mode, vremya):
        global language
        super().__init__()
        self.setupUi(self)
        self.mode = mode
        self.res = res
        self.vremya = vremya
        self.resnum.display(str(self.res))
        self.timenum.display(self.vremya)
        self.backbtn.clicked.connect(self.back)
        self.replybtn.clicked.connect(self.rep)
        self.game = None
        self.m = {
            1: 'Анаграмма',
            2: "Таблица Шульте",
            3: "Поиск буквы",
            4: "Набор пароля"
        }
        self.base()
        if language == 'Башкорт тель':
            self.restword.setText('Сезнең нәтиҗә')
            self.timeword.setText('Сезнең вакыт')
            self.replybtn.setText('Ейгә кайту')
            self.backbtn.setText('Тагын бер тапкыр')
        else:
            self.restword.setText('Ваш результат')
            self.timeword.setText('Ваше время')
            self.replybtn.setText('Ещё раз')
            self.backbtn.setText('Домой')

    def back(self):
        ex.show()
        self.close()

    def rep(self):
        if self.mode == 1:
            self.game = One()
            self.game.show()
            self.close()
        elif self.mode == 2:
            self.game = Two()
            self.game.show()
            self.close()
        elif self.mode == 3:
            self.game = Three()
            self.game.show()
            self.close()
        elif self.mode == 4:
            self.game = Four()
            self.game.show()
            self.close()

    def base(self):
        result = time.localtime()
        self.con = sqlite3.connect("stat.db")
        cur = self.con.cursor()
        data = [
            (self.m[self.mode], f'{result.tm_mday}.{result.tm_mon}.{result.tm_year}', self.vremya, self.res),
        ]
        cur.executemany("INSERT INTO stat VALUES(?, ?, ?, ?)", data)
        self.con.commit()


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("logo.png")
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(100, 200)
        self.setWindowTitle('Зубаеров Радмир')
        self.resize(500, 500)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstPage()
    ex.show()

    sys.excepthook = except_hook
    sys.exit(app.exec())
