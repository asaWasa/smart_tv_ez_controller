from PyQt5.QtWidgets import QApplication, QMainWindow
from web.controller import Ui_MainWindow
import samsungctl
import sys
import time


class WindowManager:

    def __init__(self):
        self.app = QApplication(sys.argv)

        self.MainWindow = QMainWindow()

        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self.MainWindow)

    def main(self):
        self.__init_main_window()
        self.exit()

    def __init_main_window(self):
        self.MainWindow.show()
        self.__func_in_main()

    def __func_in_main(self):
        self.ui_main.btn1.clicked.connect(lambda: self.__call('1'))
        self.ui_main.btn2.clicked.connect(lambda: self.__call('2'))
        self.ui_main.btn3.clicked.connect(lambda: self.__call('3'))
        self.ui_main.btn4.clicked.connect(lambda: self.__call('4'))
        self.ui_main.btn5.clicked.connect(lambda: self.__call('5'))
        self.ui_main.btn6.clicked.connect(lambda: self.__call('6'))
        self.ui_main.btn7.clicked.connect(lambda: self.__call('7'))
        self.ui_main.btn8.clicked.connect(lambda: self.__call('8'))
        self.ui_main.btn9.clicked.connect(lambda: self.__call('9'))
        self.ui_main.btn0.clicked.connect(lambda: self.__call('0'))
        self.ui_main.btn_smart_hub.clicked.connect(lambda: self.__call('CONTENTS'))
        self.ui_main.btn_off.clicked.connect(lambda: self.__call('POWEROFF'))
        self.ui_main.btn_html.clicked.connect(lambda: self.__call('HDMI'))
        self.ui_main.btn_up.clicked.connect(lambda: self.__call('UP'))
        self.ui_main.btn_down.clicked.connect(lambda: self.__call('DOWN'))
        self.ui_main.btn_left.clicked.connect(lambda: self.__call('LEFT'))
        self.ui_main.btn_right.clicked.connect(lambda: self.__call('RIGHT'))
        self.ui_main.btn_enter.clicked.connect(lambda: self.__call('ENTER'))
        self.ui_main.btn_tools.clicked.connect(lambda: self.__call('TOOLS'))
        self.ui_main.btn_return.clicked.connect(lambda: self.__call('RETURN'))
        self.ui_main.btn_menu.clicked.connect(lambda: self.__call('MENU'))
        self.ui_main.btn_pls.clicked.connect(lambda: self.__call('VOLUP'))
        self.ui_main.btn_mns.clicked.connect(lambda: self.__call('VOLDOWN'))

    def __call(self, cmd):
        self.config = {
            "name": "samsungctl",
            "description": "PC",
            "id": "controller",
            "host": "{}".format(self.ui_main.lineEdit.text()),
            "port": 55000,
            "method": "legacy",
            "timeout": 0,
        }
        try:
            samsungctl.Remote(self.config).remote.control("KEY_"+cmd)
            self.ui_main.label_2.setText(cmd)
            samsungctl.Remote(self.config).remote.close()
        except:
            self.ui_main.label_2.setText('ERROR')

    def __click_btn1(self):
        pass

    def exit(self):
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    windows = WindowManager()
    windows.main()
