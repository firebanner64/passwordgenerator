# Modules PyQt5, sys, string, random, pyperclip not written by program author
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import PyQt5
import sys
import string
import random
import os
import pyperclip
import json
app = QApplication(sys.argv)
class Ui_mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hook_functions()
        self.load_save_file()
    def generate(self):
        self.passwordList.clear()
        capitals = self.capitalsCheck.isChecked()
        symbols = self.symbolsCheck.isChecked()
        numbers = self.numbersCheck.isChecked()
        number_of_passwords = self.numberOfPasswords.value()
        password_length = self.passwordLength.value()

        generated_passwords = list()
        char_pool = string.ascii_lowercase
        # random functions and string not created by program author
        if capitals:
            char_pool = char_pool + string.ascii_uppercase
        if numbers:
            char_pool = char_pool + string.digits + string.digits
        if symbols:
            symbol_pool = self.specialCharactersLine.text()
            number_of_symbols = random.randint(1, int(password_length / 2))
            length_minus_symbols = password_length - number_of_symbols
            for i in range(number_of_passwords):
                selected_symbols = self.n_random_char_from_pool(symbol_pool, number_of_symbols)
                selected_chars = self.n_random_char_from_pool(char_pool, length_minus_symbols)
                current = list(selected_chars + selected_symbols)
                random.shuffle(current)
                generated_passwords.append(''.join(current))
        else: 
            for i in range(number_of_passwords):
                generated_passwords.append(self.n_random_char_from_pool(char_pool, password_length))
        self.display_list(generated_passwords)
    def hook_functions(self) -> None:
        self.generateButton.clicked.connect(self.generate)
        self.copyTextButton.clicked.connect(self.copy_selected)
        self.saveButton.clicked.connect(self.save_save_file)
    def copy_selected(self) -> None:
        pyperclip.copy(self.passwordList.currentItem().text())
    def display_list(self, ls: list) -> None:
        for i in ls:
            self.passwordList.addItem(i)
    def load_save_file(self):
        # os code and json code not created by program author
        cwd = os.getcwd()
        try:
            with open(cwd + R"\settings.json", 'r+') as f:
                contents = f.read()
                if contents == '':
                    f.seek(0)
                    f.write(json.dumps({'npsdws':5,'lnpsdws':10,'caps':True,'symbols':False,'numbers':True,'spechars':"!#$%&()*+,-./:;<=>?@[\]^_`{|}~"}))
                    f.seek(0)
                    contents = f.read()
                loads = json.loads(contents)
                self.numberOfPasswords.setValue(loads['npsdws'])
                self.passwordLength.setValue(loads['lnpsdws'])
                self.capitalsCheck.setChecked(loads['caps'])
                self.symbolsCheck.setChecked(loads['symbols'])
                self.numbersCheck.setChecked(loads['numbers'])
                self.specialCharactersLine.setText(loads['spechars'])
        except Exception:
            print(Exception)
            open(cwd + R"\settings.json", 'x')
            self.load_save_file()
    def save_save_file(self):
        cwd = os.getcwd()
        capitals = self.capitalsCheck.isChecked()
        symbols = self.symbolsCheck.isChecked()
        numbers = self.numbersCheck.isChecked()
        number_of_passwords = self.numberOfPasswords.value()
        password_length = self.passwordLength.value()
        spechars = self.specialCharactersLine.text()
        with open(cwd + R"\settings.json", 'w') as f:
            f.write(json.dumps({'npsdws':number_of_passwords,'lnpsdws':password_length,'caps':capitals,'symbols':symbols,'numbers':numbers,'spechars':spechars}))
        
    def n_random_char_from_pool(self, pool: str, n: int) -> str:
        ret = str()
        for _ in range(n):
            ret += random.choice(pool)
        return ret
    # Ui library not created by program author
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(651, 412)
        self.numberOfPasswordsLabel = QtWidgets.QLabel(mainWindow)
        self.numberOfPasswordsLabel.setGeometry(QtCore.QRect(493, 20, 91, 20))
        self.numberOfPasswordsLabel.setObjectName("numberOfPasswordsLabel")
        self.numberOfPasswords = QtWidgets.QSpinBox(mainWindow)
        self.numberOfPasswords.setGeometry(QtCore.QRect(590, 20, 42, 20))
        self.numberOfPasswords.setObjectName("numberOfPasswords")
        self.passwordLengthLabel = QtWidgets.QLabel(mainWindow)
        self.passwordLengthLabel.setGeometry(QtCore.QRect(483, 50, 101, 20))
        self.passwordLengthLabel.setObjectName("passwordLengthLabel")
        self.passwordLength = QtWidgets.QSpinBox(mainWindow)
        self.passwordLength.setGeometry(QtCore.QRect(590, 50, 42, 20))
        self.passwordLength.setObjectName("passwordLength")
        self.generateButton = QtWidgets.QPushButton(mainWindow)
        self.generateButton.setGeometry(QtCore.QRect(20, 337, 93, 61))
        self.generateButton.setObjectName("generateButton")
        self.capitalsCheck = QtWidgets.QCheckBox(mainWindow)
        self.capitalsCheck.setGeometry(QtCore.QRect(530, 80, 81, 20))
        self.capitalsCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.capitalsCheck.setObjectName("capitalsCheck")
        self.symbolsCheck = QtWidgets.QCheckBox(mainWindow)
        self.symbolsCheck.setGeometry(QtCore.QRect(530, 110, 81, 20))
        self.symbolsCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.symbolsCheck.setObjectName("symbolsCheck")
        self.numbersCheck = QtWidgets.QCheckBox(mainWindow)
        self.numbersCheck.setGeometry(QtCore.QRect(530, 140, 81, 20))
        self.numbersCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.numbersCheck.setObjectName("numbersCheck")
        self.copyTextButton = QtWidgets.QPushButton(mainWindow)
        self.copyTextButton.setGeometry(QtCore.QRect(120, 337, 93, 61))
        self.copyTextButton.setObjectName("copyTextButton")
        self.passwordList = QtWidgets.QListWidget(mainWindow)
        self.passwordList.setGeometry(QtCore.QRect(20, 20, 431, 281))
        self.passwordList.setItemAlignment(QtCore.Qt.AlignLeading)
        self.passwordList.setObjectName("passwordList")
        self.specialCharactersLine = QtWidgets.QLineEdit(mainWindow)
        self.specialCharactersLine.setGeometry(QtCore.QRect(560, 170, 71, 22))
        self.specialCharactersLine.setObjectName("specialCharactersLine")
        self.label = QtWidgets.QLabel(mainWindow)
        self.label.setGeometry(QtCore.QRect(454, 170, 101, 16))
        self.label.setObjectName("label")
        self.saveButton = QtWidgets.QPushButton(mainWindow)
        self.saveButton.setGeometry(QtCore.QRect(220, 340, 93, 61))
        self.saveButton.setObjectName("saveButton")

        self.retranslateUi(mainWindow)
        self.passwordList.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Password Generator"))
        self.numberOfPasswordsLabel.setText(_translate("mainWindow", "# of Passwords"))
        self.passwordLengthLabel.setText(_translate("mainWindow", "Password Length"))
        self.generateButton.setText(_translate("mainWindow", "Generate"))
        self.capitalsCheck.setText(_translate("mainWindow", "Capitals"))
        self.symbolsCheck.setText(_translate("mainWindow", "Symbols"))
        self.numbersCheck.setText(_translate("mainWindow", "Numbers"))
        self.copyTextButton.setText(_translate("mainWindow", "Copy Text"))
        self.specialCharactersLine.setText(_translate("mainWindow", "\" !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\""))
        self.label.setText(_translate("mainWindow", "Special Characters"))
        self.saveButton.setText(_translate("mainWindow", "Save"))

window = Ui_mainWindow()
window.show()
app.exec()