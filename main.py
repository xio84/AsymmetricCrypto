from backend.diffHell import DiffHell
from backend.elgamal import Elgamal
from backend import diffHell, elgamal, RSA
from backend.util import file, num
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import time
import os
import sys
import subprocess

class Ui_MainWindow(object):
    def __init__(self):
        self.plaintext_file_name = ''
        self.ciphertext_file_name = ''
        self.publickey_file_name = ''
        self.privatekey_file_name = ''
        self.rsa_result_file_path = ''
        self.elgamal_result_file_path = ''
        self.save_key_result_file_path = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 792)
        self.verticalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 841, 791))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(25, 15, 25, 15)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filename_plaintext = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filename_plaintext.setObjectName("filename_plaintext")
        self.horizontalLayout_2.addWidget(self.filename_plaintext)
        self.browse_plaintext = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_plaintext.setObjectName("browse_plaintext")
        self.horizontalLayout_2.addWidget(self.browse_plaintext)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filename_ciphertext = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filename_ciphertext.setObjectName("filename_ciphertext")
        self.horizontalLayout_3.addWidget(self.filename_ciphertext)
        self.browse_ciphertext = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_ciphertext.setObjectName("browse_ciphertext")
        self.horizontalLayout_3.addWidget(self.browse_ciphertext)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.filename_privatekey = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filename_privatekey.setObjectName("filename_privatekey")
        self.horizontalLayout_18.addWidget(self.filename_privatekey)
        self.browse_privatekey = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_privatekey.setObjectName("browse_privatekey")
        self.horizontalLayout_18.addWidget(self.browse_privatekey)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.filename_publickey = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filename_publickey.setObjectName("filename_publickey")
        self.horizontalLayout_12.addWidget(self.filename_publickey)
        self.browse_publickey = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_publickey.setObjectName("browse_publickey")
        self.horizontalLayout_12.addWidget(self.browse_publickey)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.ciphertext = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.ciphertext.setObjectName("ciphertext")
        self.verticalLayout_5.addWidget(self.ciphertext)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.rsa_decrypt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rsa_decrypt.setObjectName("rsa_decrypt")
        self.horizontalLayout_14.addWidget(self.rsa_decrypt)
        self.elgamal_decrypt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.elgamal_decrypt.setObjectName("elgamal_decrypt")
        self.horizontalLayout_14.addWidget(self.elgamal_decrypt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.plaintext = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.plaintext.setObjectName("plaintext")
        self.verticalLayout_3.addWidget(self.plaintext)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.rsa_encrypt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rsa_encrypt.setObjectName("rsa_encrypt")
        self.horizontalLayout_15.addWidget(self.rsa_encrypt)
        self.elgamal_encrypt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.elgamal_encrypt.setObjectName("elgamal_encrypt")
        self.horizontalLayout_15.addWidget(self.elgamal_encrypt)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.filename_key_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filename_key_2.setObjectName("filename_key_2")
        self.verticalLayout_6.addWidget(self.filename_key_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        self.rsa_p = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.rsa_p.setObjectName("rsa_p")
        self.verticalLayout_12.addWidget(self.rsa_p)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_12.addWidget(self.label_15)
        self.rsa_q = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.rsa_q.setObjectName("rsa_q")
        self.verticalLayout_12.addWidget(self.rsa_q)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_12.addWidget(self.label_16)
        self.rsa_e = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.rsa_e.setObjectName("rsa_e")
        self.verticalLayout_12.addWidget(self.rsa_e)
        self.rsa_generate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rsa_generate.setObjectName("rsa_generate")
        self.verticalLayout_12.addWidget(self.rsa_generate)
        self.horizontalLayout_8.addLayout(self.verticalLayout_12)
        spacerItem5 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_14.addWidget(self.label_12)
        self.elgamal_p = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.elgamal_p.setObjectName("elgamal_p")
        self.verticalLayout_14.addWidget(self.elgamal_p)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_14.addWidget(self.label_13)
        self.elgamal_g = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.elgamal_g.setObjectName("elgamal_g")
        self.verticalLayout_14.addWidget(self.elgamal_g)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_14.addWidget(self.label_14)
        self.elgamal_x = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.elgamal_x.setObjectName("elgamal_x")
        self.verticalLayout_14.addWidget(self.elgamal_x)
        self.elgamal_generate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.elgamal_generate.setObjectName("elgamal_generate")
        self.verticalLayout_14.addWidget(self.elgamal_generate)
        self.horizontalLayout_8.addLayout(self.verticalLayout_14)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_15.addWidget(self.label_17)
        self.diffie_helman_x = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.diffie_helman_x.setObjectName("diffie_helman_x")
        self.verticalLayout_15.addWidget(self.diffie_helman_x)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_15.addWidget(self.label_19)
        self.diffie_helman_n = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.diffie_helman_n.setObjectName("diffie_helman_n")
        self.verticalLayout_15.addWidget(self.diffie_helman_n)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_15.addWidget(self.label_20)
        self.diffie_helman_g = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.diffie_helman_g.setObjectName("diffie_helman_g")
        self.verticalLayout_15.addWidget(self.diffie_helman_g)
        self.diffie_helman_generate_X = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.diffie_helman_generate_X.setObjectName("diffie_helman_generate_X")
        self.verticalLayout_15.addWidget(self.diffie_helman_generate_X)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem8)
        self.horizontalLayout_9.addLayout(self.verticalLayout_15)
        spacerItem9 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_17.addWidget(self.label_18)
        self.diffie_helman_X = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.diffie_helman_X.setObjectName("diffie_helman_X")
        self.verticalLayout_17.addWidget(self.diffie_helman_X)
        self.horizontalLayout_9.addLayout(self.verticalLayout_17)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_18.addWidget(self.label_21)
        self.diffie_helman_Y = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.diffie_helman_Y.setObjectName("diffie_helman_Y")
        self.verticalLayout_18.addWidget(self.diffie_helman_Y)
        self.diffie_helman_generate_agreed_key = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.diffie_helman_generate_agreed_key.setObjectName("diffie_helman_generate_agreed_key")
        self.verticalLayout_18.addWidget(self.diffie_helman_generate_agreed_key)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem11)
        self.horizontalLayout_11.addLayout(self.verticalLayout_18)
        spacerItem12 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_20.addWidget(self.label_22)
        self.diffie_helman_agreed_key = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.diffie_helman_agreed_key.setObjectName("diffie_helman_agreed_key")
        self.verticalLayout_20.addWidget(self.diffie_helman_agreed_key)
        self.horizontalLayout_11.addLayout(self.verticalLayout_20)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_7.addLayout(self.verticalLayout_11)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browse_publickey.clicked.connect(lambda x: self.browse("filename_publickey"))
        self.browse_privatekey.clicked.connect(lambda x: self.browse("filename_privatekey"))
        self.browse_ciphertext.clicked.connect(lambda x: self.browse("filename_ciphertext"))
        self.browse_plaintext.clicked.connect(lambda x: self.browse("filename_plaintext"))
        self.rsa_encrypt.clicked.connect(self.RSAEncrypt)
        self.rsa_decrypt.clicked.connect(self.RSADecrypt)
        self.elgamal_encrypt.clicked.connect(self.ElgamalEncrypt)
        self.elgamal_decrypt.clicked.connect(self.ElgamalDecrypt)
        self.rsa_generate.clicked.connect(self.GenerateRSA)
        self.elgamal_generate.clicked.connect(self.GenerateElgamal)
        self.diffie_helman_generate_X.clicked.connect(self.DiffHellmanX)
        self.diffie_helman_generate_agreed_key.clicked.connect(self.DiffHellmanKey)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Asymmetric Crypto"))
        self.label.setText(_translate("MainWindow", "Plaintext File"))
        self.browse_plaintext.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Ciphertext File"))
        self.browse_ciphertext.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindow", "*.pri File"))
        self.browse_privatekey.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "*.pub File"))
        self.browse_publickey.setText(_translate("MainWindow", "Browse"))
        self.label_6.setText(_translate("MainWindow", "Ciphertext"))
        self.rsa_decrypt.setText(_translate("MainWindow", "Decrypt with RSA"))
        self.elgamal_decrypt.setText(_translate("MainWindow", "Decrypt with Elgamal"))
        self.label_7.setText(_translate("MainWindow", "Plaintext"))
        self.rsa_encrypt.setText(_translate("MainWindow", "Encrypt with RSA"))
        self.elgamal_encrypt.setText(_translate("MainWindow", "Encrypt with Elgamal"))
        self.label_8.setText(_translate("MainWindow", "Key-Generator"))
        self.label_9.setText(_translate("MainWindow", "Key Filename"))
        self.label_11.setText(_translate("MainWindow", "p (default = 0, must be <= 256)"))
        self.label_15.setText(_translate("MainWindow", "q (default = 0, must be <= 256)"))
        self.label_16.setText(_translate("MainWindow", "e (default = 0)"))
        self.rsa_generate.setText(_translate("MainWindow", "Generate RSA Key"))
        self.label_12.setText(_translate("MainWindow", "p (must be >= 256 and <= 65536)"))
        self.label_13.setText(_translate("MainWindow", "g (must be < p)"))
        self.label_14.setText(_translate("MainWindow", "x (must be >= 1 and <= p - 2)"))
        self.elgamal_generate.setText(_translate("MainWindow", "Generate Elgamal Key"))
        self.label_10.setText(_translate("MainWindow", "Diffie-Helman Key Exchange"))
        self.label_17.setText(_translate("MainWindow", "x"))
        self.label_19.setText(_translate("MainWindow", "n"))
        self.label_20.setText(_translate("MainWindow", "g"))
        self.diffie_helman_generate_X.setText(_translate("MainWindow", "Generate X"))
        self.label_18.setText(_translate("MainWindow", "X (to create agreed key)"))
        self.label_21.setText(_translate("MainWindow", "Y"))
        self.diffie_helman_generate_agreed_key.setText(_translate("MainWindow", "Generate Agreed Key"))
        self.label_22.setText(_translate("MainWindow", "Agreed Key"))

    def createErrorMsg(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def createTimeMsg(self, message, size):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("elapsed time: " + message + " seconds")
        if (size != ''):
            msg.setInformativeText("   file size: " + size + "bytes")
        msg.setWindowTitle("Information")
        msg.exec_()

    def browse(self, target):
        if (target == "filename_publickey"):
            inputFileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                None,
                "Select Input File",
                "",
                "Public Key File (*.pub)",
            )
        elif (target == "filename_privatekey"):
            inputFileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                None,
                "Select Input File",
                "",
                "Private Key File (*.pri)",
            )
        else:
            inputFileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                None,
                "Select Input File",
                "",
                "All Files (*)",
            )
        if inputFileName:
            if (target == "filename_publickey"):
                self.filename_publickey.insert(inputFileName)
            elif (target == "filename_privatekey"):
                self.filename_privatekey.insert(inputFileName)
            elif (target == "filename_ciphertext"):
                self.filename_ciphertext.insert(inputFileName)
            elif (target == "filename_plaintext"):
                self.filename_plaintext.insert(inputFileName)
            else:
                print("Error when writing input file")
                self.createErrorMsg("Error when writing input file!")
                return -1
        else:
            print("Cancelled / Error when reading input file")
            return -1

    def RSAEncrypt(self):
        then = time.time()
        pubKeyPath = self.filename_publickey.text()
        if (pubKeyPath != ""):
            pubKey = file.readFromJson(pubKeyPath)
            plainFile = self.filename_plaintext.text()
            plainText = self.plaintext.toPlainText()
            cipherText = self.ciphertext
            if (plainFile != ""):
                array = file.readFile(plainFile)
                encrypted = RSA.encrypt(array, pubKey["e"], pubKey["n"])

                now = time.time()
                self.createTimeMsg(str(now-then), str(len(encrypted)))

                # Set Path
                path, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None,
                    "Select Input File",
                    plainFile,
                    "All Files (*)",
                )
                file.writeFile(path=path, arr=encrypted)
            elif (plainText != ""):
                # array = bytearray(plainText.encode("ascii"))
                # array = list(array)
                cText = RSA.encryptText(plainText, pubKey["e"], pubKey["n"])
                # encrypted = bytearray(encrypted)
                # cText = encrypted.decode("ascii")
                cipherText.setPlainText(cText)
                now = time.time()
                self.createTimeMsg(str(now-then), '')
            else:
                self.createErrorMsg("Plaintext Empty!")
                return -1
        else:
            self.createErrorMsg("Public Key empty!")
            return -1

    def RSADecrypt(self):
        then = time.time()
        priKeyPath = self.filename_privatekey.text()
        if (priKeyPath != ""):
            priKey = file.readFromJson(priKeyPath)
            cipherFile = self.filename_ciphertext.text()
            plainText = self.plaintext
            cipherText = self.ciphertext.toPlainText()
            if (cipherFile != ""):
                array = file.readFile(cipherFile)
                decrypted = RSA.decrypt(array, priKey["d"], priKey["n"])

                now = time.time()
                self.createTimeMsg(str(now-then), str(len(decrypted)))

                # Set Path
                path, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None,
                    "Select Input File",
                    cipherFile,
                    "All Files (*)",
                )
                file.writeFile(path=path, arr=decrypted)
            elif (cipherText != ""):
                # array = bytearray(cipherText.encode("ascii"))
                # array = list(array)
                pText = RSA.decryptText(cipherText, priKey["d"], priKey["n"])
                # decrypted = bytearray(decrypted)
                # pText = decrypted.decode("ascii")
                plainText.setPlainText(pText)
                now = time.time()
                self.createTimeMsg(str(now-then), '')
            else:
                self.createErrorMsg("Ciphertext Empty!")
                return -1
        else:
            self.createErrorMsg("Private Key empty!")
            return -1

    def ElgamalEncrypt(self):
        then = time.time()
        pubKeyPath = self.filename_publickey.text()

        if (pubKeyPath != ""):
            pubKey = file.readFromJson(pubKeyPath)
            plainFile = self.filename_plaintext.text()
            plainText = self.plaintext.toPlainText()
            cipherText = self.ciphertext

            if (plainFile != ""):
                array = file.readFile(plainFile)
                el = Elgamal(pubKey["p"], pubKey["g"], (pubKey["p"] - 2))
                el.setPublicKey(pubKey["y"], pubKey["g"], pubKey["p"])
                encrypted = el.encrypt(array)

                now = time.time()
                self.createTimeMsg(str(now-then), str(len(encrypted)))

                # Set Path
                path, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None,
                    "Select Input File",
                    plainFile,
                    "All Files (*)",
                )
                file.writeFile(path=path, arr=encrypted)
            elif (plainText != ""):
                # array = bytearray(plainText.encode("ascii"))
                # array = list(array)
                el = Elgamal(pubKey["p"], pubKey["g"], (pubKey["p"] - 2))
                el.setPublicKey(pubKey["y"], pubKey["g"], pubKey["p"])
                cText = el.encryptText(plainText)
                # encrypted = bytearray(encrypted)
                # cText = encrypted.decode("ascii")
                cipherText.setPlainText(cText)

                now = time.time()
                self.createTimeMsg(str(now-then), '')
            else:
                self.createErrorMsg("Plaintext Empty!")
                return -1
        else:
            self.createErrorMsg("Public Key empty!")
            return -1

    def ElgamalDecrypt(self):
        then = time.time()
        priKeyPath = self.filename_privatekey.text()
        if (priKeyPath != ""):
            priKey = file.readFromJson(priKeyPath)
            cipherFile = self.filename_ciphertext.text()
            plainText = self.plaintext
            cipherText = self.ciphertext.toPlainText()
            if (cipherFile != ""):
                array = file.readFile(cipherFile)
                el = Elgamal(priKey["p"], (priKey["p"] - 1), priKey["x"])
                el.setPrivateKey(priKey["x"], priKey["p"])
                decrypted = el.decrypt(array)

                now = time.time()
                self.createTimeMsg(str(now-then), str(len(decrypted)))

                # Set Path
                path, _ = QtWidgets.QFileDialog.getSaveFileName(
                    None,
                    "Select Input File",
                    cipherFile,
                    "All Files (*)",
                )
                file.writeFile(path=path, arr=decrypted)
            elif (cipherText != ""):
                # array = bytearray(cipherText.encode("ascii"))
                # array = list(array)
                el = Elgamal(priKey["p"], (priKey["p"] - 1), priKey["x"])
                el.setPrivateKey(priKey["x"], priKey["p"])
                pText = el.decryptText(cipherText)
                # decrypted = bytearray(decrypted)
                # pText = decrypted.decode("ascii")
                plainText.setPlainText(pText)

                now = time.time()
                self.createTimeMsg(str(now-then), '')
            else:
                self.createErrorMsg("Plaintext Empty!")
                return -1
        else:
            self.createErrorMsg("Public Key empty!")
            return -1

    def GenerateRSA(self):
        then = time.time()
        self.save_key_result_file_path = self.filename_key_2.text()
        if (self.save_key_result_file_path != ""):
            p = int(self.rsa_p.text())
            e = int(self.rsa_e.text())
            q = int(self.rsa_q.text())

            key = RSA.RSAKeygen(p = p, q = q, e = e)
            key.writeToFile(self.save_key_result_file_path)
        else:
            self.createErrorMsg("Target save filename is empty!")
            return -1
        now = time.time()
        self.createTimeMsg(str(now-then), '')

    def GenerateElgamal(self):
        then = time.time()
        self.save_key_result_file_path = self.filename_key_2.text()
        if (self.save_key_result_file_path != ""):
            p = int(self.elgamal_p.text())
            g = int(self.elgamal_g.text())
            x = int(self.elgamal_x.text())

            key = Elgamal(p, g, x)
            key.writeToFile(self.save_key_result_file_path)
        else:
            self.createErrorMsg("Target save filename is empty!")
            return -1
        now = time.time()
        self.createTimeMsg(str(now-then), '')

    def DiffHellmanX(self):
        then = time.time()
        x = int(self.diffie_helman_x.text())
        n = int(self.diffie_helman_n.text())
        g = int(self.diffie_helman_g.text())
        if (x != ""):
            if (n != ""):
                if (g != ""):
                    res = DiffHell(x, n, g)
                    self.diffie_helman_X.setPlainText(str(res.send()))
                else:
                    self.createErrorMsg("g empty!")
                    return -1
            else:
                self.createErrorMsg("n empty!")
                return -1
        else:
            self.createErrorMsg("x empty!")
            return -1
        now = time.time()
        self.createTimeMsg(str(now-then), '')

    def DiffHellmanKey(self):
        then = time.time()
        x = int(self.diffie_helman_x.text())
        n = int(self.diffie_helman_n.text())
        g = int(self.diffie_helman_g.text())
        y = int(self.diffie_helman_Y.text())
        if (x != ""):
            if (n != ""):
                if (g != ""):
                    if (y != ""):
                        res = DiffHell(x, n, g)
                        res.exchange(y)
                        self.diffie_helman_agreed_key.setPlainText(str(res.agreedKey()))
                    else:
                        self.createErrorMsg("Y empty!")
                        return -1
                else:
                    self.createErrorMsg("g empty!")
                    return -1
            else:
                self.createErrorMsg("n empty!")
                return -1
        else:
            self.createErrorMsg("x empty!")
            return -1
        now = time.time()
        self.createTimeMsg(str(now-then), '')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())