# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# import os
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(952, 468)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(430, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(480, 110, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(480, 250, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_plain_text = QtWidgets.QTextEdit(Dialog)
        self.txt_plain_text.setGeometry(QtCore.QRect(100, 110, 311, 101))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_cipher_text = QtWidgets.QTextEdit(Dialog)
        self.txt_cipher_text.setGeometry(QtCore.QRect(100, 250, 311, 101))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.txt_info_text = QtWidgets.QTextEdit(Dialog)
        self.txt_info_text.setGeometry(QtCore.QRect(550, 110, 311, 101))
        self.txt_info_text.setObjectName("txt_info_text")
        self.txt_sign_text = QtWidgets.QTextEdit(Dialog)
        self.txt_sign_text.setGeometry(QtCore.QRect(550, 250, 311, 101))
        self.txt_sign_text.setObjectName("txt_sign_text")
        self.btn_encrypt = QtWidgets.QPushButton(Dialog)
        self.btn_encrypt.setGeometry(QtCore.QRect(100, 390, 75, 23))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(Dialog)
        self.btn_decrypt.setGeometry(QtCore.QRect(340, 390, 75, 23))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_sign = QtWidgets.QPushButton(Dialog)
        self.btn_sign.setGeometry(QtCore.QRect(550, 390, 75, 23))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(Dialog)
        self.btn_verify.setGeometry(QtCore.QRect(790, 390, 75, 23))
        self.btn_verify.setObjectName("btn_verify")
        self.btn_genkeys = QtWidgets.QPushButton(Dialog)
        self.btn_genkeys.setGeometry(QtCore.QRect(440, 60, 91, 31))
        self.btn_genkeys.setObjectName("btn_genkeys")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "RSA Cipher"))
        self.label_2.setText(_translate("Dialog", "Plain_text"))
        self.label_3.setText(_translate("Dialog", "Cipher_text"))
        self.label_4.setText(_translate("Dialog", "Infomation"))
        self.label_5.setText(_translate("Dialog", "Signature"))
        self.btn_encrypt.setText(_translate("Dialog", "Encrypt"))
        self.btn_decrypt.setText(_translate("Dialog", "Decrypt"))
        self.btn_sign.setText(_translate("Dialog", "Sign"))
        self.btn_verify.setText(_translate("Dialog", "Verify"))
        self.btn_genkeys.setText(_translate("Dialog", "Generate Keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
