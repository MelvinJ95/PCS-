# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import store_item
from PyQt5 import QtCore, QtGui, QtWidgets
from report_view import Ui_report_view
import functions as FT

class Ui_MainWindow(object):

    #GLOBAL VARIABLES
    total_cost = 0;

    def add_toCart(self,item):
        item_to_send = item
        FT.function().addtoCart(self, item_to_send)

    def report(self):
        FT.function().report()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(643, 445)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 641, 421))
        self.main_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_frame.setObjectName("main_frame")

        self.shop_name_label = QtWidgets.QLabel(self.main_frame)
        self.shop_name_label.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.shop_name_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shop_name_label.setFrameShape(QtWidgets.QFrame.Box)
        self.shop_name_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.shop_name_label.setLineWidth(1)
        self.shop_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shop_name_label.setObjectName("shop_name_label")

        self.elements_grid = QtWidgets.QListWidget(self.main_frame)
        self.elements_grid.setGeometry(QtCore.QRect(0, 20, 421, 401))
        self.elements_grid.setMovement(QtWidgets.QListView.Free)
        self.elements_grid.setFlow(QtWidgets.QListView.LeftToRight)
        self.elements_grid.setProperty("isWrapping", False)
        self.elements_grid.setResizeMode(QtWidgets.QListView.Fixed)
        self.elements_grid.setLayoutMode(QtWidgets.QListView.Batched)
        self.elements_grid.setGridSize(QtCore.QSize(75, 75))
        self.elements_grid.setViewMode(QtWidgets.QListView.IconMode)
        self.elements_grid.setModelColumn(0)
        self.elements_grid.setUniformItemSizes(True)
        self.elements_grid.setWordWrap(False)
        self.elements_grid.setObjectName("elements_grid")

        item = QtWidgets.QListWidgetItem()

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)

        item.setBackground(brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)

        item.setForeground(brush)

        self.elements_grid.addItem(item)
        item = QtWidgets.QListWidgetItem()

        self.elements_grid.addItem(item)

        self.cart_table = QtWidgets.QTableWidget(self.main_frame)
        self.cart_table.setGeometry(QtCore.QRect(430, 20, 201, 251))
        self.cart_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cart_table.setAlternatingRowColors(False)
        self.cart_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.cart_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cart_table.setGridStyle(QtCore.Qt.NoPen)
        self.cart_table.setObjectName("cart_table")
        self.cart_table.setColumnCount(2)
        self.cart_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cart_table.setHorizontalHeaderItem(1, item)
        self.cart_table.verticalHeader().setVisible(False)
        self.check_out_button = QtWidgets.QPushButton(self.main_frame)
        self.check_out_button.setGeometry(QtCore.QRect(430, 320, 201, 41))
        self.check_out_button.setObjectName("check_out_button")
        self.total_table = QtWidgets.QTableWidget(self.main_frame)
        self.total_table.setGeometry(QtCore.QRect(430, 280, 201, 31))
        self.total_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.total_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.total_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.total_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.total_table.setShowGrid(False)
        self.total_table.setGridStyle(QtCore.Qt.SolidLine)
        self.total_table.setCornerButtonEnabled(True)
        self.total_table.setObjectName("total_table")
        self.total_table.setColumnCount(2)
        self.total_table.setRowCount(1)

        item = QtWidgets.QTableWidgetItem()
        self.total_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_table.setItem(0, 0, item)
        self.total_table.horizontalHeader().setVisible(False)
        self.total_table.horizontalHeader().setHighlightSections(True)
        self.total_table.verticalHeader().setVisible(False)
        self.check_out_button_2 = QtWidgets.QPushButton(self.main_frame)
        self.check_out_button_2.setGeometry(QtCore.QRect(430, 370, 201, 41))
        self.check_out_button_2.setObjectName("check_out_button_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.shop_name_label.setText(_translate("MainWindow", "shop_name"))
        self.elements_grid.setSortingEnabled(True)
        __sortingEnabled = self.elements_grid.isSortingEnabled()
        self.elements_grid.setSortingEnabled(False)
        item = self.elements_grid.item(0)
        item.setText(_translate("MainWindow", "hola1"))
        item = self.elements_grid.item(1)
        item.setText(_translate("MainWindow", "hola2"))
        self.elements_grid.setSortingEnabled(__sortingEnabled)
        item = self.cart_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.cart_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "item"))
        item = self.cart_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "cost"))
        self.check_out_button.setText(_translate("MainWindow", "Check out"))
        item = self.total_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.total_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "total_text"))
        item = self.total_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "total_value"))
        __sortingEnabled = self.total_table.isSortingEnabled()
        self.total_table.setSortingEnabled(False)
        item = self.total_table.item(0, 0)
        item.setText(_translate("MainWindow", "Total:"))
        self.total_table.setSortingEnabled(__sortingEnabled)
        self.check_out_button_2.setText(_translate("MainWindow", "Report"))


        #ITEM EVENT ACTION
        self.elements_grid.itemClicked.connect(self.add_toCart)
        #USER CANT EDIT ITEM/COST HEADERS
        self.cart_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        #BUTTON EVENTS
        self.check_out_button_2.clicked.connect(self.report)

        #Give function an Instance of Main Window to have access to UI Elements 
        FT.function().returnObj(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
