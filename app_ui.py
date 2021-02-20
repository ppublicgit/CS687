# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 847)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_user_select = QtWidgets.QWidget()
        self.tab_user_select.setObjectName("tab_user_select")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_user_select)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_select_user = QtWidgets.QLabel(self.tab_user_select)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_select_user.setFont(font)
        self.label_select_user.setObjectName("label_select_user")
        self.gridLayout_16.addWidget(self.label_select_user, 2, 0, 1, 1)
        self.le_user_company = QtWidgets.QLineEdit(self.tab_user_select)
        self.le_user_company.setObjectName("le_user_company")
        self.gridLayout_16.addWidget(self.le_user_company, 7, 0, 1, 1)
        self.rb_user_company = QtWidgets.QRadioButton(self.tab_user_select)
        self.rb_user_company.setObjectName("rb_user_company")
        self.gridLayout_16.addWidget(self.rb_user_company, 4, 0, 1, 1)
        self.le_user_user = QtWidgets.QLineEdit(self.tab_user_select)
        self.le_user_user.setObjectName("le_user_user")
        self.gridLayout_16.addWidget(self.le_user_user, 7, 2, 1, 1)
        self.rb_user_user = QtWidgets.QRadioButton(self.tab_user_select)
        self.rb_user_user.setObjectName("rb_user_user")
        self.gridLayout_16.addWidget(self.rb_user_user, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem, 11, 0, 1, 1)
        self.label_user_company = QtWidgets.QLabel(self.tab_user_select)
        self.label_user_company.setObjectName("label_user_company")
        self.gridLayout_16.addWidget(self.label_user_company, 6, 0, 1, 1)
        self.label_user_user = QtWidgets.QLabel(self.tab_user_select)
        self.label_user_user.setObjectName("label_user_user")
        self.gridLayout_16.addWidget(self.label_user_user, 6, 2, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_8, 10, 0, 1, 1)
        self.pb_user_select = QtWidgets.QPushButton(self.tab_user_select)
        self.pb_user_select.setObjectName("pb_user_select")
        self.gridLayout_16.addWidget(self.pb_user_select, 10, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem2, 11, 2, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_user_select, "")
        self.tab_account = QtWidgets.QWidget()
        self.tab_account.setObjectName("tab_account")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_account)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem3, 8, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.le_act_company = QtWidgets.QLineEdit(self.tab_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_act_company.sizePolicy().hasHeightForWidth())
        self.le_act_company.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.le_act_company.setFont(font)
        self.le_act_company.setObjectName("le_act_company")
        self.gridLayout_9.addWidget(self.le_act_company, 8, 0, 1, 1)
        self.label_user_id = QtWidgets.QLabel(self.tab_account)
        self.label_user_id.setObjectName("label_user_id")
        self.gridLayout_9.addWidget(self.label_user_id, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_account)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 9, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_account)
        self.label.setObjectName("label")
        self.gridLayout_9.addWidget(self.label, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_account)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 9, 0, 1, 1)
        self.le_last_name = QtWidgets.QLineEdit(self.tab_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_last_name.sizePolicy().hasHeightForWidth())
        self.le_last_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.le_last_name.setFont(font)
        self.le_last_name.setObjectName("le_last_name")
        self.gridLayout_9.addWidget(self.le_last_name, 10, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_account)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 7, 2, 1, 1)
        self.label_address_user = QtWidgets.QLabel(self.tab_account)
        self.label_address_user.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_address_user.setFont(font)
        self.label_address_user.setObjectName("label_address_user")
        self.gridLayout_9.addWidget(self.label_address_user, 11, 2, 1, 1)
        self.le_address_company = QtWidgets.QLineEdit(self.tab_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_address_company.sizePolicy().hasHeightForWidth())
        self.le_address_company.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.le_address_company.setFont(font)
        self.le_address_company.setObjectName("le_address_company")
        self.gridLayout_9.addWidget(self.le_address_company, 12, 0, 1, 1)
        self.le_first_name = QtWidgets.QLineEdit(self.tab_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_first_name.sizePolicy().hasHeightForWidth())
        self.le_first_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.le_first_name.setFont(font)
        self.le_first_name.setObjectName("le_first_name")
        self.gridLayout_9.addWidget(self.le_first_name, 8, 2, 1, 1)
        self.label_address_company = QtWidgets.QLabel(self.tab_account)
        self.label_address_company.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_address_company.setFont(font)
        self.label_address_company.setObjectName("label_address_company")
        self.gridLayout_9.addWidget(self.label_address_company, 11, 0, 1, 1)
        self.le_address_user = QtWidgets.QLineEdit(self.tab_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_address_user.sizePolicy().hasHeightForWidth())
        self.le_address_user.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.le_address_user.setFont(font)
        self.le_address_user.setObjectName("le_address_user")
        self.gridLayout_9.addWidget(self.le_address_user, 12, 2, 1, 1)
        self.le_user_id = QtWidgets.QLineEdit(self.tab_account)
        self.le_user_id.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_user_id.sizePolicy().hasHeightForWidth())
        self.le_user_id.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.le_user_id.setFont(font)
        self.le_user_id.setObjectName("le_user_id")
        self.gridLayout_9.addWidget(self.le_user_id, 5, 2, 1, 1)
        self.label_user = QtWidgets.QLabel(self.tab_account)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")
        self.gridLayout_9.addWidget(self.label_user, 2, 2, 1, 1)
        self.le_company_id = QtWidgets.QLineEdit(self.tab_account)
        self.le_company_id.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_company_id.sizePolicy().hasHeightForWidth())
        self.le_company_id.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.le_company_id.setFont(font)
        self.le_company_id.setObjectName("le_company_id")
        self.gridLayout_9.addWidget(self.le_company_id, 5, 0, 1, 1)
        self.le_country_of_origin = QtWidgets.QLineEdit(self.tab_account)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_country_of_origin.sizePolicy().hasHeightForWidth())
        self.le_country_of_origin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.le_country_of_origin.setFont(font)
        self.le_country_of_origin.setObjectName("le_country_of_origin")
        self.gridLayout_9.addWidget(self.le_country_of_origin, 10, 0, 1, 1)
        self.label_company = QtWidgets.QLabel(self.tab_account)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_company.setFont(font)
        self.label_company.setObjectName("label_company")
        self.gridLayout_9.addWidget(self.label_company, 2, 0, 1, 1)
        self.label_company_id = QtWidgets.QLabel(self.tab_account)
        self.label_company_id.setObjectName("label_company_id")
        self.gridLayout_9.addWidget(self.label_company_id, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_9, 1, 0, 1, 1)
        self.pb_edit_details = QtWidgets.QPushButton(self.tab_account)
        self.pb_edit_details.setObjectName("pb_edit_details")
        self.gridLayout_4.addWidget(self.pb_edit_details, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_account, "")
        self.tab_transact = QtWidgets.QWidget()
        self.tab_transact.setObjectName("tab_transact")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_transact)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_sort = QtWidgets.QLabel(self.tab_transact)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sort.sizePolicy().hasHeightForWidth())
        self.label_sort.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_sort.setFont(font)
        self.label_sort.setObjectName("label_sort")
        self.horizontalLayout_5.addWidget(self.label_sort)
        self.rb_sort_order_num = QtWidgets.QRadioButton(self.tab_transact)
        self.rb_sort_order_num.setChecked(True)
        self.rb_sort_order_num.setObjectName("rb_sort_order_num")
        self.horizontalLayout_5.addWidget(self.rb_sort_order_num)
        self.rb_sort_date = QtWidgets.QRadioButton(self.tab_transact)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_sort_date.sizePolicy().hasHeightForWidth())
        self.rb_sort_date.setSizePolicy(sizePolicy)
        self.rb_sort_date.setChecked(False)
        self.rb_sort_date.setObjectName("rb_sort_date")
        self.horizontalLayout_5.addWidget(self.rb_sort_date)
        self.rb_sort_price = QtWidgets.QRadioButton(self.tab_transact)
        self.rb_sort_price.setObjectName("rb_sort_price")
        self.horizontalLayout_5.addWidget(self.rb_sort_price)
        self.rb_sort_quantity = QtWidgets.QRadioButton(self.tab_transact)
        self.rb_sort_quantity.setObjectName("rb_sort_quantity")
        self.horizontalLayout_5.addWidget(self.rb_sort_quantity)
        self.pb_sort = QtWidgets.QPushButton(self.tab_transact)
        self.pb_sort.setObjectName("pb_sort")
        self.horizontalLayout_5.addWidget(self.pb_sort)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.frame_sort = QtWidgets.QFrame(self.tab_transact)
        self.frame_sort.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sort.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sort.setObjectName("frame_sort")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_sort)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.table_transactions = QtWidgets.QTableWidget(self.frame_sort)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_transactions.sizePolicy().hasHeightForWidth())
        self.table_transactions.setSizePolicy(sizePolicy)
        self.table_transactions.setObjectName("table_transactions")
        self.table_transactions.setColumnCount(0)
        self.table_transactions.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.table_transactions)
        self.verticalLayout_3.addWidget(self.frame_sort)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_transact, "")
        self.tab_product = QtWidgets.QWidget()
        self.tab_product.setObjectName("tab_product")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_product)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.le_buy_id = QtWidgets.QLineEdit(self.tab_product)
        self.le_buy_id.setObjectName("le_buy_id")
        self.gridLayout_10.addWidget(self.le_buy_id, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_product)
        self.label_8.setObjectName("label_8")
        self.gridLayout_10.addWidget(self.label_8, 0, 0, 1, 1)
        self.pb_buy = QtWidgets.QPushButton(self.tab_product)
        self.pb_buy.setObjectName("pb_buy")
        self.gridLayout_10.addWidget(self.pb_buy, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_product)
        self.label_9.setObjectName("label_9")
        self.gridLayout_10.addWidget(self.label_9, 1, 0, 1, 1)
        self.le_buy_quantity = QtWidgets.QLineEdit(self.tab_product)
        self.le_buy_quantity.setObjectName("le_buy_quantity")
        self.gridLayout_10.addWidget(self.le_buy_quantity, 1, 2, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_product, "")
        self.tab_companies = QtWidgets.QWidget()
        self.tab_companies.setObjectName("tab_companies")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_companies)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cb_new_item_category = QtWidgets.QComboBox(self.tab_companies)
        self.cb_new_item_category.setObjectName("cb_new_item_category")
        self.gridLayout_5.addWidget(self.cb_new_item_category, 2, 2, 1, 1)
        self.le_new_item_price = QtWidgets.QLineEdit(self.tab_companies)
        self.le_new_item_price.setObjectName("le_new_item_price")
        self.gridLayout_5.addWidget(self.le_new_item_price, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_companies)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_companies)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_companies)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 5, 0, 1, 1)
        self.label_search_options = QtWidgets.QLabel(self.tab_companies)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_search_options.setFont(font)
        self.label_search_options.setObjectName("label_search_options")
        self.gridLayout_5.addWidget(self.label_search_options, 0, 0, 1, 1)
        self.le_new_item_name = QtWidgets.QLineEdit(self.tab_companies)
        self.le_new_item_name.setObjectName("le_new_item_name")
        self.gridLayout_5.addWidget(self.le_new_item_name, 1, 2, 1, 1)
        self.pb_new_item = QtWidgets.QPushButton(self.tab_companies)
        self.pb_new_item.setObjectName("pb_new_item")
        self.gridLayout_5.addWidget(self.pb_new_item, 4, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_5)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_4.addLayout(self.verticalLayout_18)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_companies, "")
        self.tab_items = QtWidgets.QWidget()
        self.tab_items.setObjectName("tab_items")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_items)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.table_items = QtWidgets.QTableWidget(self.tab_items)
        self.table_items.setObjectName("table_items")
        self.table_items.setColumnCount(0)
        self.table_items.setRowCount(0)
        self.verticalLayout_32.addWidget(self.table_items)
        self.horizontalLayout_7.addLayout(self.verticalLayout_32)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_products_search_options = QtWidgets.QLabel(self.tab_items)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_products_search_options.setFont(font)
        self.label_products_search_options.setObjectName("label_products_search_options")
        self.verticalLayout.addWidget(self.label_products_search_options)
        self.frame_product_category = QtWidgets.QFrame(self.tab_items)
        self.frame_product_category.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_product_category.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_product_category.setObjectName("frame_product_category")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_product_category)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_product_name_2 = QtWidgets.QLabel(self.frame_product_category)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_product_name_2.setFont(font)
        self.label_product_name_2.setObjectName("label_product_name_2")
        self.verticalLayout_25.addWidget(self.label_product_name_2)
        self.cb_search_category = QtWidgets.QComboBox(self.frame_product_category)
        self.cb_search_category.setObjectName("cb_search_category")
        self.verticalLayout_25.addWidget(self.cb_search_category)
        self.pb_add_product_category = QtWidgets.QPushButton(self.frame_product_category)
        self.pb_add_product_category.setObjectName("pb_add_product_category")
        self.verticalLayout_25.addWidget(self.pb_add_product_category)
        self.verticalLayout.addWidget(self.frame_product_category)
        self.frame_product_price = QtWidgets.QFrame(self.tab_items)
        self.frame_product_price.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_product_price.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_product_price.setObjectName("frame_product_price")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_product_price)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.hs_product_price_2 = QtWidgets.QLabel(self.frame_product_price)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.hs_product_price_2.setFont(font)
        self.hs_product_price_2.setObjectName("hs_product_price_2")
        self.verticalLayout_31.addWidget(self.hs_product_price_2)
        self.label_product_price_min = QtWidgets.QLabel(self.frame_product_price)
        self.label_product_price_min.setObjectName("label_product_price_min")
        self.verticalLayout_31.addWidget(self.label_product_price_min)
        self.sb_min_price = QtWidgets.QDoubleSpinBox(self.frame_product_price)
        self.sb_min_price.setObjectName("sb_min_price")
        self.verticalLayout_31.addWidget(self.sb_min_price)
        self.label_product_price_max = QtWidgets.QLabel(self.frame_product_price)
        self.label_product_price_max.setObjectName("label_product_price_max")
        self.verticalLayout_31.addWidget(self.label_product_price_max)
        self.sb_max_price = QtWidgets.QDoubleSpinBox(self.frame_product_price)
        self.sb_max_price.setObjectName("sb_max_price")
        self.verticalLayout_31.addWidget(self.sb_max_price)
        self.verticalLayout.addWidget(self.frame_product_price)
        self.pb_product_search = QtWidgets.QPushButton(self.tab_items)
        self.pb_product_search.setObjectName("pb_product_search")
        self.verticalLayout.addWidget(self.pb_product_search)
        self.pb_product_search_reset = QtWidgets.QPushButton(self.tab_items)
        self.pb_product_search_reset.setObjectName("pb_product_search_reset")
        self.verticalLayout.addWidget(self.pb_product_search_reset)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_items, "")
        self.tab_all_companies = QtWidgets.QWidget()
        self.tab_all_companies.setObjectName("tab_all_companies")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_all_companies)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.table_companies = QtWidgets.QTableWidget(self.tab_all_companies)
        self.table_companies.setObjectName("table_companies")
        self.table_companies.setColumnCount(0)
        self.table_companies.setRowCount(0)
        self.gridLayout_12.addWidget(self.table_companies, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_all_companies, "")
        self.tab_support = QtWidgets.QWidget()
        self.tab_support.setObjectName("tab_support")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_support)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.table_support = QtWidgets.QTableWidget(self.tab_support)
        self.table_support.setObjectName("table_support")
        self.table_support.setColumnCount(0)
        self.table_support.setRowCount(0)
        self.gridLayout_6.addWidget(self.table_support, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_support, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_select_user.setText(_translate("MainWindow", "Select User"))
        self.rb_user_company.setText(_translate("MainWindow", "Company"))
        self.rb_user_user.setText(_translate("MainWindow", "Customer"))
        self.label_user_company.setText(_translate("MainWindow", "Company ID"))
        self.label_user_user.setText(_translate("MainWindow", "Customer ID"))
        self.pb_user_select.setText(_translate("MainWindow", "Select User"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_user_select), _translate("MainWindow", "Select User"))
        self.label_user_id.setText(_translate("MainWindow", "User ID"))
        self.label_3.setText(_translate("MainWindow", "Last Name"))
        self.label.setText(_translate("MainWindow", "Company Name"))
        self.label_4.setText(_translate("MainWindow", "Country of Origin"))
        self.label_2.setText(_translate("MainWindow", "First Name"))
        self.label_address_user.setText(_translate("MainWindow", "Address"))
        self.label_address_company.setText(_translate("MainWindow", "Address"))
        self.label_user.setText(_translate("MainWindow", "User"))
        self.label_company.setText(_translate("MainWindow", "Company"))
        self.label_company_id.setText(_translate("MainWindow", "Company ID"))
        self.pb_edit_details.setText(_translate("MainWindow", "Edit Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_account), _translate("MainWindow", "My Account"))
        self.label_sort.setText(_translate("MainWindow", "Sort"))
        self.rb_sort_order_num.setText(_translate("MainWindow", "Order #"))
        self.rb_sort_date.setText(_translate("MainWindow", "Date"))
        self.rb_sort_price.setText(_translate("MainWindow", "Price"))
        self.rb_sort_quantity.setText(_translate("MainWindow", "Quantity"))
        self.pb_sort.setText(_translate("MainWindow", "Sort"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_transact), _translate("MainWindow", "My Transactions"))
        self.label_8.setText(_translate("MainWindow", "Product Id"))
        self.pb_buy.setText(_translate("MainWindow", "Buy"))
        self.label_9.setText(_translate("MainWindow", "Quantity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_product), _translate("MainWindow", "Buy Product"))
        self.label_6.setText(_translate("MainWindow", "Category"))
        self.label_7.setText(_translate("MainWindow", "Price"))
        self.label_5.setText(_translate("MainWindow", "Product Name"))
        self.label_search_options.setText(_translate("MainWindow", "New Product"))
        self.pb_new_item.setText(_translate("MainWindow", "Add Item"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_companies), _translate("MainWindow", "Add Item"))
        self.label_products_search_options.setText(_translate("MainWindow", "Search Options"))
        self.label_product_name_2.setText(_translate("MainWindow", "Category"))
        self.pb_add_product_category.setText(_translate("MainWindow", "Add Category"))
        self.hs_product_price_2.setText(_translate("MainWindow", "Price"))
        self.label_product_price_min.setText(_translate("MainWindow", "Minimum Price"))
        self.label_product_price_max.setText(_translate("MainWindow", "Maximum Price"))
        self.pb_product_search.setText(_translate("MainWindow", "Search"))
        self.pb_product_search_reset.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_items), _translate("MainWindow", "All Items"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_all_companies), _translate("MainWindow", "All Companies"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_support), _translate("MainWindow", "Support"))
