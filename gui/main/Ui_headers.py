# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\enema\gui\main\headers.ui'
#
# Created: Tue Apr 10 23:39:58 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_HeadersWidget(object):
    def setupUi(self, HeadersWidget):
        HeadersWidget.setObjectName(_fromUtf8("HeadersWidget"))
        HeadersWidget.resize(572, 162)
        HeadersWidget.setMinimumSize(QtCore.QSize(572, 162))
        HeadersWidget.setMaximumSize(QtCore.QSize(572, 162))
        self.groupBox = QtGui.QGroupBox(HeadersWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 551, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineUserAgent = QtGui.QLineEdit(self.groupBox)
        self.lineUserAgent.setGeometry(QtCore.QRect(100, 20, 441, 21))
        self.lineUserAgent.setText(_fromUtf8(""))
        self.lineUserAgent.setObjectName(_fromUtf8("lineUserAgent"))
        self.RefererLabel = QtGui.QLabel(self.groupBox)
        self.RefererLabel.setEnabled(False)
        self.RefererLabel.setGeometry(QtCore.QRect(30, 80, 51, 21))
        self.RefererLabel.setObjectName(_fromUtf8("RefererLabel"))
        self.lineReferer = QtGui.QLineEdit(self.groupBox)
        self.lineReferer.setEnabled(False)
        self.lineReferer.setGeometry(QtCore.QRect(80, 80, 461, 21))
        self.lineReferer.setText(_fromUtf8(""))
        self.lineReferer.setObjectName(_fromUtf8("lineReferer"))
        self.lineXForwardedFor = QtGui.QLineEdit(self.groupBox)
        self.lineXForwardedFor.setEnabled(False)
        self.lineXForwardedFor.setGeometry(QtCore.QRect(130, 110, 411, 21))
        self.lineXForwardedFor.setText(_fromUtf8(""))
        self.lineXForwardedFor.setObjectName(_fromUtf8("lineXForwardedFor"))
        self.lineCookie = QtGui.QLineEdit(self.groupBox)
        self.lineCookie.setEnabled(False)
        self.lineCookie.setGeometry(QtCore.QRect(80, 50, 461, 21))
        self.lineCookie.setText(_fromUtf8(""))
        self.lineCookie.setObjectName(_fromUtf8("lineCookie"))
        self.UALabel = QtGui.QLabel(self.groupBox)
        self.UALabel.setGeometry(QtCore.QRect(30, 20, 71, 21))
        self.UALabel.setObjectName(_fromUtf8("UALabel"))
        self.CookieLabel = QtGui.QLabel(self.groupBox)
        self.CookieLabel.setEnabled(False)
        self.CookieLabel.setGeometry(QtCore.QRect(30, 50, 51, 21))
        self.CookieLabel.setObjectName(_fromUtf8("CookieLabel"))
        self.XForwardedLabel = QtGui.QLabel(self.groupBox)
        self.XForwardedLabel.setEnabled(False)
        self.XForwardedLabel.setGeometry(QtCore.QRect(30, 110, 91, 21))
        self.XForwardedLabel.setObjectName(_fromUtf8("XForwardedLabel"))
        self.UserAgent = QtGui.QCheckBox(self.groupBox)
        self.UserAgent.setGeometry(QtCore.QRect(10, 20, 16, 21))
        self.UserAgent.setText(_fromUtf8(""))
        self.UserAgent.setChecked(True)
        self.UserAgent.setObjectName(_fromUtf8("UserAgent"))
        self.Cookie = QtGui.QCheckBox(self.groupBox)
        self.Cookie.setGeometry(QtCore.QRect(10, 50, 16, 21))
        self.Cookie.setText(_fromUtf8(""))
        self.Cookie.setChecked(False)
        self.Cookie.setObjectName(_fromUtf8("Cookie"))
        self.Referer = QtGui.QCheckBox(self.groupBox)
        self.Referer.setGeometry(QtCore.QRect(10, 80, 16, 21))
        self.Referer.setText(_fromUtf8(""))
        self.Referer.setChecked(False)
        self.Referer.setObjectName(_fromUtf8("Referer"))
        self.XForwardedFor = QtGui.QCheckBox(self.groupBox)
        self.XForwardedFor.setGeometry(QtCore.QRect(10, 110, 16, 21))
        self.XForwardedFor.setText(_fromUtf8(""))
        self.XForwardedFor.setChecked(False)
        self.XForwardedFor.setObjectName(_fromUtf8("XForwardedFor"))

        self.retranslateUi(HeadersWidget)
        QtCore.QMetaObject.connectSlotsByName(HeadersWidget)

    def retranslateUi(self, HeadersWidget):
        HeadersWidget.setWindowTitle(QtGui.QApplication.translate("HeadersWidget", "HTTP Headers", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("HeadersWidget", "Headers", None, QtGui.QApplication.UnicodeUTF8))
        self.RefererLabel.setText(QtGui.QApplication.translate("HeadersWidget", "Referer:", None, QtGui.QApplication.UnicodeUTF8))
        self.UALabel.setText(QtGui.QApplication.translate("HeadersWidget", "User-Agent:", None, QtGui.QApplication.UnicodeUTF8))
        self.CookieLabel.setText(QtGui.QApplication.translate("HeadersWidget", "Cookie:", None, QtGui.QApplication.UnicodeUTF8))
        self.XForwardedLabel.setText(QtGui.QApplication.translate("HeadersWidget", "X-Forwarded-For:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HeadersWidget = QtGui.QWidget()
    ui = Ui_HeadersWidget()
    ui.setupUi(HeadersWidget)
    HeadersWidget.show()
    sys.exit(app.exec_())

